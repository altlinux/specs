%define  themename Clearlooks-Phenix

Name:    gtk3-theme-clearlooks-phenix
Version: 3.0.16
Release: alt1

Summary: GTK3 port of the Clearlooks theme

License: GPLv3+
Group:   Graphical desktop/GNOME
Url:     http://www.jpfleury.net/en/software/clearlooks-phenix.php

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch

Requires: libgtk-engine-clearlooks

%description
The Clearlooks-Phenix project (formerly known as Clearwaita) aims at
creating a GTK3 port of Clearlooks, the default theme for Gnome 2. Style
is also included for GTK2, Unity and for Metacity, Openbox and Xfwm4
window managers.

%install
mkdir -p %buildroot%_datadir/themes
tar xf %SOURCE0 -C %buildroot%_datadir/themes

%files
%_datadir/themes/%themename

%changelog
* Thu Sep 18 2014 Andrey Cherepanov <cas@altlinux.org> 3.0.16-alt1
- New version

* Fri Mar 22 2013 Andrey Cherepanov <cas@altlinux.org> 3.0.15-alt1
- Initial build in Sisyphus
