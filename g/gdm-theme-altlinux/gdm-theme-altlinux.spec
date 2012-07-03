%define base gdm-theme
%define _name altlinux

Name: %base-%_name
Version: 0.0
Release: alt1

Summary: A GDM2 theme - ALT Linux
License: GPL
Group: Graphical desktop/GNOME
Source: %base-%_name-%version.tar
Packager: Eugene Prokopiev <enp@altlinux.ru>
BuildArch: noarch
Requires: gdm

%description
ALT Linux simple theme based on Gnome Hardy-Simple Brave GDM theme

%prep
%setup

%install
%__mkdir_p %buildroot%_datadir/gdm/themes/%_name
%__cp -r * %buildroot%_datadir/gdm/themes/%_name

%files
%_datadir/gdm/themes/*

%changelog
* Fri Oct 10 2008 Eugene Prokopiev <enp@altlinux.ru> 0.0-alt1
- first build for Sisyphus
