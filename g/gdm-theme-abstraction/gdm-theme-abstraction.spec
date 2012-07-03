%define base gdm-theme
%define _name abstraction

Name: %base-%_name
Version: 0.1
Release: alt1

Summary: A GDM2 theme - Abstraction
Summary(ru_RU.UTF-8): Тема менеджера входа в систему GDM - Abstraction
License: GPL
Group: Graphical desktop/GNOME
Url: http://gnome-look.org/content/show.php/Serenity+GDM?content=106425
Source: %base-%_name-%version.tar.bz2
Packager: Radik Usupov <radik@altlinux.org>
BuildArch: noarch
Requires: gdm2.20

%description
Simple theme based on Gnome Serenity GDM theme

%description -l ru_RU.UTF-8
Тема для менеджера входа в систему GDM - Abstraction. Разрабатывается
в рамках проекта ALTLinux LXDE Remix и основана на теме GDM = Serenity.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/gdm/themes/%_name
cp -r * %buildroot%_datadir/gdm/themes/%_name

%files
%_datadir/gdm/themes/*

%changelog
* Thu Jan 06 2011 Radik Usupov <radik@altlinux.org> 0.1-alt1
- Initial build

