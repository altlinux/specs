Name: installer-feature-powerbutton-stage3
Version: 0.2
Release: alt1

Summary: Arrange for power button to work as expected
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch
Source: %name-%version.tar
Requires: installer-common-stage3

%description
This package sets up APM or ACPI power button actions
so that pressing it would result in system shutdown.

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 08-powerbutton %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Fri Apr 10 2009 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- Ported from stage2 to stage3.

* Tue Aug 12 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- init with installer-sdk
