from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password, check_password
from balance.models import Transaction
from user.models import MyUser, UserGroup
from user.forms import RegistrationForm, LoginForm, GroupRegistrationForm
from datetime import date
import calendar

# Create your views here.


month_str = str(date.today().month)
year_str = str(date.today().year)
month_year_int = int(month_str + year_str)


class WelcomeView(LoginRequiredMixin, ListView):

    @property
    def show_month(self):
        try:
            month_year = self.kwargs["monthyear"]

            if len(str(month_year)) == 6:
                show_month = int(str(month_year)[:2])
            else:
                show_month = int(str(month_year)[:1])

        except KeyError:
            show_month = int(month_str)

        self._show_month = show_month
        return self._show_month

    @show_month.setter
    def show_month(self, value):
        self._show_month = value

    @property
    def show_year(self):
        try:
            month_year = self.kwargs["monthyear"]
            self._show_year = int(str(month_year)[-4:])
        except KeyError:
            self._show_year = int(year_str)

        return self._show_year

    @show_year.setter
    def show_year(self, value):
        self._show_year = value

    @property
    def prev_month_year(self):
        if self._show_month != 1:
            self._prev_month_year = (self._show_month - 1, self._show_year)
        else:
            self._prev_month_year = (12, self._show_year - 1)

        return self._prev_month_year

    @prev_month_year.setter
    def prev_month_year(self, value):
        self._prev_month_year = value

    @property
    def next_month_year(self):
        if self._show_month != 12:
            self._next_month_year = (self._show_month + 1, self._show_year)
        else:
            self._next_month_year = (1, self._show_year + 1)

        return self._next_month_year

    @next_month_year.setter
    def next_month_year(self, value):
        self._next_month_year = value

    def get_queryset(self):
        active_user = MyUser.objects.get(id=self.request.user.id)
        if active_user.as_group == "True":
            queryset = Transaction.objects.filter(
                group=active_user.get_active_group()).exclude(group__isnull=True)
        else:
            queryset = Transaction.objects.filter(
                user=active_user, group__isnull=True)
        return queryset

    def dayly_transactions(self):
        dayly_transactions_dict = dict()
        for transaction in self.get_queryset():
            for key, value in transaction.day_balance(self.show_month, self.show_year).items():
                if key not in dayly_transactions_dict:
                    dayly_transactions_dict[key] = [value]
                else:
                    dayly_transactions_dict[key].append(value)

        transaction_tuples = [
            (i, None)
            if i not in dayly_transactions_dict
            else (i, dayly_transactions_dict.get(i))
            for i in range(1, calendar.monthrange(self.show_year, self.show_month)[1] + 1)
        ]
        return transaction_tuples

    def weeks(self):
        transaction_tuples = self.dayly_transactions()
        prev_month_num_days = calendar.monthrange(
            self.prev_month_year[1], self.prev_month_year[0])[1]
        curr_month_weekday, curr_month_num_days = calendar.monthrange(
            self.show_year, self.show_month)
        last_days = [prev_month_num_days -
                     i for i in range(curr_month_weekday - 1, -1, -1)]

        first_week = [transaction_tuples[i] for i in range(7 - len(last_days))]

        second_week = [
            transaction_tuples[i] for i in range(first_week[-1][0], 14 - len(last_days))
        ]
        third_week = [
            transaction_tuples[i] for i in range(second_week[-1][0], 21 - len(last_days))
        ]
        fourth_week = [
            transaction_tuples[i] for i in range(third_week[-1][0], 28 - len(last_days))
        ]
        weeks = [first_week, second_week, third_week, fourth_week]
        if fourth_week[-1][0] == curr_month_num_days:
            fifth_week = None
            sixth_week = None
        else:
            fifth_week = [
                transaction_tuples[i]
                for i in range(fourth_week[-1][0], len(transaction_tuples))
            ]
            weeks.append(fifth_week)

        if len(fifth_week) < 7:
            first_days = [i for i in range(1, 7) if len(fifth_week) + i <= 7]
            sixth_week = None
        elif fifth_week[-1][0] == curr_month_num_days:
            sixth_week = None
            first_days = None
        else:
            sixth_week = [
                transaction_tuples[i] for i in range(fifth_week[-1][0], 35 - len(last_days))
            ]
            weeks.append(sixth_week)
            first_days = [i for i in range(1, 7) if len(sixth_week) + i <= 7]
        return (last_days, weeks, first_days)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        last_days, weeks, first_days = self.weeks()
        context["last_days"] = last_days
        context["weeks"] = weeks
        context["first_days"] = first_days
        show_date = date(year=self.show_year, month=self.show_month, day=1)
        context["month"] = show_date.strftime("%B")
        context["year"] = show_date.year
        prev_month = int(
            str(self.prev_month_year[0]) + str(self.prev_month_year[1]))
        next_month = int(
            str(self.next_month_year[0]) + str(self.next_month_year[1]))
        context["prev_month"] = prev_month
        context["next_month"] = next_month
        return context


def registration(request):

    if request.method == "GET":
        form = RegistrationForm()
        return render(request, "registration/register.html", {"form": form})
    elif request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("welcome")
        else:
            return render(request, "registration/register.html", {"form": form})


def sign_in(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "home/login.html", {"form": form})


def logout(request):
    if request.method == "GET":
        pass


def registration_group(request):
    if request.method == "GET":
        form = GroupRegistrationForm()
        return render(request, "registration/register_group.html", {"form": form})
    elif request.method == "POST":
        form = GroupRegistrationForm(request.POST)
        if form.is_valid():
            password = make_password(request.POST["password"])
            name = request.POST["name"]
            group = (UserGroup(name=name, password=password))
            group.save()
            group.members.add(MyUser.objects.get(id=request.user.id))

            return redirect("welcome")
        else:
            return render(request, "registration/register_group.html", {"form": form})


def login_group(request):
    if request.method == "GET":

        return render(request, "registration/login_group.html")
    elif request.method == "POST":

        try:
            group = UserGroup.objects.get(
                name=request.POST.get("Group Name"))
        except:
            return render(request, "registration/login_group.html", {"group_exists": True,
                                                                     "name": request.POST.get("Group Name")})
        if check_password(request.POST.get("Password"), group.password):
            try:
                group.members.get(id=request.user.id)
                return render(request, "registration/login_group.html",
                              {"member": True, "name": request.POST.get("Group Name")})
            except:
                group.members.add(MyUser.objects.get(id=request.user.id))
                group.nr_of_members += 1
                group.save()
                return render(request, "registration/success_group.html", {"name": group.name})

        else:
            return render(request, "registration/login_group.html",
                          {"wrong_password": True})


def show_group_members(request):
    if request.method == "GET":
        group_names = dict()
        groups = UserGroup.objects.all()
        for i in groups:
            group_names[i.name] = i.get_member_names()

        items = group_names.items()
        return render(request, "registration/show_groups.html", {"items": items})


class MemberView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        queryset = UserGroup.objects.filter(members=self.request.user.id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["groups"] = [x.name for x in self.get_queryset()]
        return context
