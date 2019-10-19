Name: wakefix
Version: 1.0.1
Release: alt2

Summary: An ACPI wakeup event table control tool and service
License: GPL
Group: Development/Other
Packager: Paul Wolneykien <manowar@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

BuildPreReq: help2man

%description
wakefix is a tool to read and modify (fix) the ACPI wakeup event table
(/proc/acpi/wakeup). It is intended to be installed as a system startup
service to make such modifications at boot.

%prep
%setup

%build
%make_build

%install
%make_install install DESTDIR=%buildroot

%files
%_sbindir/%name
%_mandir/man8/%name.8*
%_unitdir/%name.service
%config(noreplace) %_sysconfdir/sysconfig/%name.conf

%changelog
* Sat Oct 19 2019 Paul Wolneykien <manowar@altlinux.org> 1.0.1-alt2
- Fix: Do not replace the modified configuration files.

* Sat Oct 19 2019 Paul Wolneykien <manowar@altlinux.org> 1.0.1-alt1
- Output the verbose messages to stderr.
- Fix: List the event table by default.

* Sat Oct 19 2019 Paul Wolneykien <manowar@altlinux.org> 1.0.0-alt1
- Initial version.
