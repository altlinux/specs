%define base gdm-theme
%define _name education

Name: %base-%_name
Version: 0.1
Release: alt2

Summary: A GDM2 theme - Education
Summary(ru_RU.UTF-8): Тема менеджера входа в систему GDM - Education
License: GPL
Group: Graphical desktop/GNOME
Url: http://gnome-look.org/content/show.php/Blue+ambience?content=120449
Source: %base-%_name-%version.tar.bz2
Packager: Radik Usupov <radik@altlinux.org>
BuildArch: noarch
Requires: gdm2.20

%description
Simple theme based on Gnome Blueambience GDM theme

%description -l ru_RU.UTF-8
Тема для менеджера входа в систему GDM - Education. Разрабатывается
в рамках проекта ALTLinux LXDE Remix from School и основана на теме GDM - blueambience.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/gdm/themes/%_name
cp -r * %buildroot%_datadir/gdm/themes/%_name

%files
%_datadir/gdm/themes/*

%changelog
* Tue Jan 11 2011 Radik Usupov <radik@altlinux.org> 0.1-alt2
- Change color theme

* Thu Jan 06 2011 Radik Usupov <radik@altlinux.org> 0.1-alt1
- Initial build

