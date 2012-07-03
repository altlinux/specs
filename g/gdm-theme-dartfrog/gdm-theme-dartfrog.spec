%define base gdm-theme
%define _name dartfrog

Name: %base-%_name
Version: 0.0
Release: alt1

Summary: A GDM2 theme - Dart Frog
Summary(ru_RU.UTF-8): Тема для GDM2 - Лягушка
License: GPL
Group: Graphical desktop/GNOME
Url: ftp://ftp.gnome.org/pub/gnome/teams/art.gnome.org/themes/gdm/
Source: %_name.tar.gz
BuildArch: noarch
Requires: gdm

%description
Does anyone know whether the frog is a Tinc or a Leucomelas? The image came from x.themes.org.

%description -l ru_RU.UTF-8
К какому роду: Tinc или Leucomelas, относится эта лягушка? Картинка получена с сервера x.themes.org.

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

