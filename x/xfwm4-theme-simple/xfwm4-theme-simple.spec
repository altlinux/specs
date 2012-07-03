Name: xfwm4-theme-simple
Version: 0.1
Release: alt1

Summary: Simple theme for xfwm4
License: GPL
Group: Graphical desktop/XFce
Packager: Eugene Prokopiev <enp@altlinux.ru>

Source: %name-%version.tar

Requires: xfwm4
BuildArch: noarch

%description
Simple theme for the xfwm4 window manager.

%prep
%setup

%install
mkdir -p %buildroot/%_datadir/themes/simple
cp -a xfwm4 %buildroot/%_datadir/themes/simple/

%files
%_datadir/themes/*

%changelog
* Sun Oct 19 2008 Eugene Prokopiev <enp@altlinux.ru> 0.1-alt1
- first build for Sisyphus

