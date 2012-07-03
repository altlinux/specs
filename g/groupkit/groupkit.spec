Name: groupkit
Version: 0.3
Release: alt1

Summary: Supplementary group membership management utilities
Summary(ru_RU.KOI8-R): Утилиты управления членством пользователя в дополнительных группах

License: GPL
Group: System/Base

Requires: shadow-utils coreutils grep

Source0: http://www.avalon.ru/~dketov/%{name}-%{version}.tar.bz2

%description
These utilities provides a way to manage user`s group membership
in supplementary groups in a simple and convinient manner,
by adding and removing user from appropriate groups.

%description -l ru_RU.KOI8-R
Набор утилит, позволяющий управлять членством полльзователей
в дополнительных группах простым и удобным образом, добавляя и удаляя
пользоваетля из соответствующих групп.

%prep
%setup -q

%build

%install
%__install -d %{buildroot}/%{_sbindir}
%__install -pD -m755 addusertogroup deluserfromgroup %{buildroot}/%{_sbindir}

%files
%{_sbindir}/*

%changelog
* Wed Mar 10 2004 Dimitry V. Ketov <dketov@altlinux.ru> 0.3-alt1
- Initial build for Sisyphus

