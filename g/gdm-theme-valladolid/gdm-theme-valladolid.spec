%define base gdm-theme
%define _name valladolid

Name: %base-%_name
Version: 0.0
Release: alt1

Summary: A GDM2 theme - Valladolid (Spain)
Summary(ru_RU.UTF-8): Тема для GDM2 - Вальядолид (Испания)
License: GPL
Group: Graphical desktop/GNOME
Url: ftp://ftp.gnome.org/pub/gnome/teams/art.gnome.org/themes/gdm/
Source: %_name.tar.gz
BuildArch: noarch
Requires: gdm

%description
Sights of Spain - Valladolid

%description -l ru_RU.UTF-8
Виды Испании - Вальядолид.

%prep
%setup -q -n %_name

%install
%__mkdir_p %buildroot%_datadir/gdm/themes/%_name
%__cp -r * %buildroot%_datadir/gdm/themes/%_name

%files
%_datadir/gdm/themes/*

%changelog
* Thu Oct 31 2002 Vyacheslav Dikonov <slava@altlinux.ru> 0.0-alt1
- 1st build, translation

