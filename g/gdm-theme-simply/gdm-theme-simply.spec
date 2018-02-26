%define base gdm-theme
%define _name simply

Name: %base-%_name
Version: 1.0
Release: alt3

Summary: A GDM2 theme - Simply
Summary(ru_RU.UTF-8): Тема менеджера входа в систему GDM - Simply
License: GPL
Group: Graphical desktop/GNOME
Url: http://code.google.com/p/simplicity-desktop-theme
Source: %base-%_name-%version.tar.bz2
Packager: Alexandra Panyukova <mex3@altlinux.ru>
BuildArch: noarch
Requires: gdm

%description
Simply theme based on Gnome Arc Colors Brave GDM theme

%description -l ru_RU.UTF-8
Тема для менеджера входа в систему GDM - Simply. Разрабатывается
в рамках проекта Simplicity и основана на теме GDM - Arc Colors Brave.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/gdm/themes/%_name
cp -r * %buildroot%_datadir/gdm/themes/%_name

%files
%_datadir/gdm/themes/*

%changelog
* Mon Aug 08 2011 Alexandra Panyukova <mex3@altlinux.ru> 1.0-alt3
- First build for Sisyphus based on gdm-theme-pingwin.

