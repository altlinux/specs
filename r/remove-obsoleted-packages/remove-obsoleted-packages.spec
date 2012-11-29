Name: remove-obsoleted-packages
Version: 0.1
Release: alt1

Summary: Remove obsoleted packages

Group: System/Servers
License: GPL

#Source: %name-%version.tar

BuildArch: noarch

Obsoletes: hald libhal hal-info

%description
This package will remove obsoleted packages from your system
during install.

%files

%changelog
* Thu Nov 29 2012 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
