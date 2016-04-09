%define  themename Clearlooks-Phenix

Name:    gtk3-theme-clearlooks-phenix
Version: 6.0.3
Release: alt1

Summary: GTK3 port of the Clearlooks theme

License: GPLv3+
Group:   Graphical desktop/GNOME
Url:     https://github.com/jpfleury/clearlooks-phenix
# VCS:   https://github.com/jpfleury/clearlooks-phenix

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
* Fri Apr 08 2016 Andrey Cherepanov <cas@altlinux.org> 6.0.3-alt1
- New version

* Thu Sep 18 2014 Andrey Cherepanov <cas@altlinux.org> 3.0.16-alt1
- New version

* Fri Mar 22 2013 Andrey Cherepanov <cas@altlinux.org> 3.0.15-alt1
- Initial build in Sisyphus
