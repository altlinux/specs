%define  themename Clearlooks-Phenix

Name:    gtk3-theme-clearlooks-phenix
Version: 7.0.1
Release: alt1.gite1bb5fe
Epoch:   1

Summary: GTK3 port of the Clearlooks theme

License: GPLv3+
Group:   Graphical desktop/GNOME
Url:     https://github.com/jpfleury/clearlooks-phenix
# VCS:   https://github.com/jpfleury/clearlooks-phenix

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch

Requires: libgtk-engine-clearlooks
Provides: clearlooks-phenix-gtk3-theme = %version-%release
Obsoletes: clearlooks-phenix-gtk3-theme < %version-%release

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
* Thu Oct 27 2016 Andrey Cherepanov <cas@altlinux.org> 1:7.0.1-alt1.gite1bb5fe
- New version
- Fix background color of hovered menu item in Chromium 54.x
- Fix transparent app-notifications

* Mon May 23 2016 Andrey Cherepanov <cas@altlinux.org> 1:6.0.3-alt4.git299f91c
- Base adapt theme to GTK 3.20

* Mon Apr 18 2016 Andrey Cherepanov <cas@altlinux.org> 1:6.0.3-alt3
- Obsoletes clearlooks-phenix-gtk3-theme

* Wed Apr 13 2016 Andrey Cherepanov <cas@altlinux.org> 1:6.0.3-alt2
- Increase Epoch for downgrade package version in stable branch

* Fri Apr 08 2016 Andrey Cherepanov <cas@altlinux.org> 6.0.3-alt1
- New version

* Thu Sep 18 2014 Andrey Cherepanov <cas@altlinux.org> 3.0.16-alt1
- New version

* Fri Mar 22 2013 Andrey Cherepanov <cas@altlinux.org> 3.0.15-alt1
- Initial build in Sisyphus
