Name:    installer-feature-set-gtk-theme
Version: 1.2
Release: alt1

Summary: Set default GTK 2.x and 3.x theme
License: GPLv3+
Group:   System/Configuration/Other
Url:     http://www.altlinux.org/Installer/beans
BuildArch: noarch
Packager: Andrey Cherepanov <cas@altlinux.org>
Source:  %name-%version.tar

Requires: libshell
Requires: gtk3-theme-clearlooks-phenix
Requires: gnome-icon-theme

%description
Set default GTK 2.x and 3.x theme.

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Tue Feb 11 2014 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1
- Fix autodetect requires
- Run in chroot

* Mon Feb 10 2014 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Test of existence of gtkrc files
- Set icon theme too

* Mon Feb 10 2014 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus
