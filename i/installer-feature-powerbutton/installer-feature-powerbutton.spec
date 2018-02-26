Name: installer-feature-powerbutton
Version: 0.1
Release: alt1

Summary: Arrange for power button to work as expected
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

%description
This package sets up APM or ACPI power button actions
so that pressing it would result in system shutdown

%package stage2
Summary: Arrange for power button to work as expected
License: GPL
Group: System/Configuration/Other
Requires: installer-stage2

%description stage2
This package sets up APM or ACPI power button actions
so that pressing it would result in system shutdown

%prep
%setup -q

%install
%makeinstall

%files stage2
%_datadir/install2/postinstall.d/*

%changelog
* Tue Aug 12 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- init with installer-sdk

