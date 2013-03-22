Name: remove-obsoleted-packages
Version: 0.2
Release: alt1

Summary: Remove obsoleted packages

Group: System/Servers
License: GPL

#Source: %name-%version.tar

BuildArch: noarch

Obsoletes: hald libhal hal-info hal-laptop hal-cups-utils DeviceKit
Obsoletes: arts libarts libarts-qtmcop libarts-devel
Obsoletes: xpdf xpdf-common xpdf-reader
Obsoletes: libmysqlclient15 libmysqlclient16

# there are 7colors, soundtracker, fvwm-gtk, xtetty using imlib
Obsoletes: imlib

Obsoletes:  gnome-libs

%description
This package will remove obsoleted packages from your system
during install.

%files

%changelog
* Fri Mar 22 2013 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- new build

* Thu Nov 29 2012 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
