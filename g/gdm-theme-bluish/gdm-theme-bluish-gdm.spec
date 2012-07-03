%define base gdm-theme
%define _name bluish

Name: %base-%_name
Version: 0.0
Release: alt1

Summary: A GDM2 theme - Bluish
Summary(ru_RU.UTF-8): Тема для GDM2 - Bluish
License: GPL
Group: Graphical desktop/GNOME
Url: ftp://ftp.gnome.org/pub/gnome/teams/art.gnome.org/themes/gdm/
Source: %_name-gdm.tar.gz
BuildArch: noarch
Requires: gdm

%description
Based on the "Bluish" background.

%description -l ru_RU.UTF-8
Основана на рисунке "Bluish" для рабочего стола.

%prep
%setup -q -n %_name-gdm

%install
%__mkdir_p %buildroot%_datadir/gdm/themes/%_name
%__cp -r * %buildroot%_datadir/gdm/themes/%_name

%files
%_datadir/gdm/themes/*

%changelog
* Thu Oct 31 2002 Vyacheslav Dikonov <slava@altlinux.ru> 0.0-alt1
- 1st build, translation

