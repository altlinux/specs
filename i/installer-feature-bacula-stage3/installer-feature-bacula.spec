Name: installer-feature-bacula-stage3
Version: 0.2
Release: alt1

Summary:Installer hook for alterator-bacula setup
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

Requires: alterator-bacula >= 1.3.0-alt1

%description
This package contains installer stage3 hook for
alterator-bacula module.

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Mon Jul 21 2014 Mikhail Efremov <sem@altlinux.org> 0.2-alt1
- Use full path for bacula-reset-settings script.
- Don't require install2-init-functions.

* Mon Jul 14 2014 Mikhail Efremov <sem@altlinux.org> 0.1-alt1
- Initial build.

