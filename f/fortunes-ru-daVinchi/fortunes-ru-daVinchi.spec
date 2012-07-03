# vim: set ft=spec: -*- rpm-spec -*-
%define _name fortunes-ru-daVinchi

Name: fortunes-ru-daVinchi
Version: 20050724
Release: alt1

Summary: Quotes from Leonardo da Vinchi's utterances.
Summary(ru_RU.KOI8-R): Цитаты из высказываний Леонардо да Винчи (взято с ru.wikiquote.org)
Group: Games/Other
License: LGPL
Url: http://ru.wikiquote.org/

BuildArch: noarch

Source: %_name.tar.gz

PreReq: fortune-mod

%description
This is a collection of quotes from Leonardo da Vinchi's utterances for use
with 'fortune' program.

%description -l ru_RU.KOI8-R
Это коллекция цитат из высказываний Ленардо да Винчи для использования
программой 'fortune'

%prep
%setup -q -n %_name

%install
%__mkdir_p %buildroot%_gamesdatadir/fortune
%__install -p -m 644 ru-daVinchi* %buildroot%_gamesdatadir/fortune

%files
%_gamesdatadir/fortune/*

%changelog
* Wed Aug 03 2005 Boldin Pavel <bp@altlinux.ru> 20050724-alt1
- First build for ALTLinux.



