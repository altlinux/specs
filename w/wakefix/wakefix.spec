Name: wakefix
Version: 1.0.4
Release: alt2

Summary: An ACPI wakeup event table control tool and service
License: GPLv3
Group: System/Configuration/Hardware
Packager: Paul Wolneykien <manowar@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

BuildPreReq: help2man

%description
wakefix is a tool to read and modify (fix) the ACPI wakeup event table
(/proc/acpi/wakeup). It is intended to be installed as a system startup
service to make such modifications at boot.

%package -n fanfix
Summary: Show and configure smart fan controller on boot and resume
Group: System/Configuration/Hardware
License: GPLv3

%description -n fanfix
wakefix is a tool to read and modify (fix) the smart fan controller
settings (nct6775 and possibly others) via hwmon /sys interface.
The package provides systemd services to fix fan configuration
on boot and resume.

%prep
%setup

%build
%make_build

%install
%make_install install DESTDIR=%buildroot unitdir=%_unitdir

%files
%_sbindir/%name
%_mandir/man8/%name.8*
%_unitdir/%name.service
%config(noreplace) %_sysconfdir/sysconfig/%name.conf

%files -n fanfix
%_bindir/fanfix
#%_mandir/man8/fanfix.1*
%_mandir/man8/fanfix.8*
%_unitdir/fanfix.service
%_unitdir/fanfix-resume.service
%config(noreplace) %_sysconfdir/sysconfig/fanfix.conf

%changelog
* Wed Aug 07 2024 Paul Wolneykien <manowar@altlinux.org> 1.0.4-alt2
- Fixed build: Pass unitdir to make.

* Sat Feb 20 2021 Paul Wolneykien <manowar@altlinux.org> 1.0.4-alt1
- Fix: Always show the fan speed.
- Added fanfix(8) manual page.

* Mon Oct 26 2020 Paul Wolneykien <manowar@altlinux.org> 1.0.3-alt1
- Fanfix: Allow to set temperature offsets.

* Sat Oct 24 2020 Paul Wolneykien <manowar@altlinux.org> 1.0.2-alt1
- Change RPM group to System/Configuration/Hardware.
- Added fanfix package.

* Sat Oct 19 2019 Paul Wolneykien <manowar@altlinux.org> 1.0.1-alt2
- Fix: Do not replace the modified configuration files.

* Sat Oct 19 2019 Paul Wolneykien <manowar@altlinux.org> 1.0.1-alt1
- Output the verbose messages to stderr.
- Fix: List the event table by default.

* Sat Oct 19 2019 Paul Wolneykien <manowar@altlinux.org> 1.0.0-alt1
- Initial version.
