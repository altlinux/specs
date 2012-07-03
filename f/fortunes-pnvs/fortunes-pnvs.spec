# vim: set ft=spec: -*- rpm-spec -*-
%define _name PNVS

Name: fortunes-pnvs
Version: 1.0
Release: alt1

Summary: Quotes from Strugatsky brothers' "Monday begins on Saturday"
Summary(ru_RU.UTF-8): Цитаты из книги братьев Стругацких "Понедельник начинается в субботу"
Group: Games/Other
License: Freely distributable
Url: http://rusf.ru/abs/books/pnvs00.htm

BuildArch: noarch

Source: %_name.tar.bz2

PreReq: fortune-mod

BuildRequires: fortune-mod

%description
This is a collection of quotes from a well-known book of Strugatsky
brothers, "Monday begins on Saturday".

%description -l ru_RU.UTF-8
Собрание цитат из знаменитой книги братьев Стругацких "Понедельник
начинается в субботу".

%prep
%setup -q -n %_name
strfile %_name

%install
%__mkdir_p %buildroot%_gamesdatadir/fortune
%__install -p -m 644 %_name %_name.dat %buildroot%_gamesdatadir/fortune

%files
%_gamesdatadir/fortune/*

%changelog
* Tue Aug 23 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.0-alt1
- Initial Sisyphus package.


