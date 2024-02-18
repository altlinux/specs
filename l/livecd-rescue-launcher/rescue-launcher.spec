Name: livecd-rescue-launcher
Version: 0.1.3
Release: alt1

Summary: Optional autorun feature for ALT Rescue
License: GPL-2.0-or-later
Group: System/Base
BuildArch: noarch

Url: https://www.altlinux.org/Rescue/Launcher
Source: rescue-launcher-%version.tar
Packager: Leonid Krivoshein <klark@altlinux.org>

Provides: rescue-launcher = %EVR

%description
This package contains additional scripts, used for auto-run
pre-defined programm or external script (by default, on the
/dev/tty1 only) at the boot-time system from the ALT rescue.
Commonly used for mass-deployment and total automatization.

%prep
%setup -n rescue-launcher-%version

%install
mkdir -pm755 -- %buildroot/{etc/rescue-launcher,%_sbindir,usr/libexec/rescue-launcher/methods,var/log}
install -pm644 methods/* %buildroot/usr/libexec/rescue-launcher/methods/
install -pm644 net-functions %buildroot/usr/libexec/rescue-launcher/
install -pm644 rescue-launcher.conf *.list %buildroot/etc/rescue-launcher/
install -pm755 rescue-launcher %buildroot/%_sbindir/
> %buildroot/var/log/rescue-launcher.log
chmod 644 %buildroot/var/log/rescue-launcher.log

%files
%dir /etc/rescue-launcher
%dir /usr/libexec/rescue-launcher
%dir /usr/libexec/rescue-launcher/methods
%config(noreplace) /etc/rescue-launcher/*
%_sbindir/rescue-launcher
/usr/libexec/rescue-launcher/net-functions
/usr/libexec/rescue-launcher/methods/*
%ghost /var/log/rescue-launcher.log

%changelog
* Mon Feb 05 2024 Anton Midyukov <antohami@altlinux.org> 0.1.3-alt1
- rename package to livecd-rescue-launcher
- replace /sbin to %%_sbindir

* Wed Jan 16 2019 Leonid Krivoshein <klark@altlinux.org> 0.1.2-alt1
- spec file: project documentation URI updated.
- plan9 method: small bug in condition fixed.
- vbox method: small code improvement.

* Thu Dec 27 2018 Leonid Krivoshein <klark@altlinux.org> 0.1.1-alt1
- vbox method: mounting error fixed.

* Thu Dec 13 2018 Leonid Krivoshein <klark@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus.
