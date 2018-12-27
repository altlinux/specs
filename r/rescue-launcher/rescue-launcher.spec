Name: rescue-launcher
Version: 0.1.1
Release: alt1

Summary: Optional autorun feature for ALT Rescue
License: GPLv2+
Group: System/Base
BuildArch: noarch

Url: http://en.altlinux.org/rescue
Source: %name-%version.tar
Packager: Leonid Krivoshein <klark@altlinux.org>

%description
This package contains additional scripts, used for auto-run
pre-defined programm or external script (by default, on the
/dev/tty1 only) at the boot-time system from the ALT rescue.
Commonly used for mass-deployment and total automatization.

%prep
%setup

%install
mkdir -pm755 -- %buildroot/{etc/%name,sbin,usr/libexec/%name/methods,var/log}
install -pm644 methods/* %buildroot/usr/libexec/%name/methods/
install -pm644 net-functions %buildroot/usr/libexec/%name/
install -pm644 %name.conf *.list %buildroot/etc/%name/
install -pm755 %name %buildroot/sbin/
> %buildroot/var/log/%name.log
chmod 644 %buildroot/var/log/%name.log

%files
%dir /etc/%name
%dir /usr/libexec/%name
%dir /usr/libexec/%name/methods
%config(noreplace) /etc/%name/*
/sbin/%name
/usr/libexec/%name/net-functions
/usr/libexec/%name/methods/*
%ghost /var/log/%name.log

%changelog
* Thu Dec 27 2018 Leonid Krivoshein <klark@altlinux.org> 0.1.1-alt1
- vbox method: mounting error fixed.

* Thu Dec 13 2018 Leonid Krivoshein <klark@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus.
