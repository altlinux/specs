Name: dnswl-sync
Version: 0.1
Release: alt2

Summary: dnswl.org synchronization utilities
License: GPL
Group: System/Configuration/Networking

BuildArch: noarch

Source: %name-%version.tar

Requires: libshell

%description
%summary

%package common
Summary: dnswl.org synchronization utilities - common files
Group: System/Configuration/Networking

%description common
%summary

%package postfix
Summary: dnswl.org synchronization utilities - postfix version
Group: System/Configuration/Networking
Requires: %name-common = %version-%release

%description postfix
%summary

%prep
%setup

%install
install -d %buildroot%_bindir
install -d %buildroot%_sysconfdir/{cron.d,dnswl}
install -d %buildroot%_localstatedir/%name/tmp

install -pm755 dnswl-sync-postfix %buildroot%_bindir/
install -pm644 dnswl-postfix.conf %buildroot%_sysconfdir/dnswl/
install -pDm644 dnswl-postfix.cron %buildroot%_sysconfdir/cron.d/dnswl-postfix

%files common
%_localstatedir/%name
%dir %_sysconfdir/dnswl

%files postfix
%_bindir/dnswl-sync-postfix
%config(noreplace) %_sysconfdir/cron.d/dnswl-postfix
%config(noreplace) %_sysconfdir/dnswl/dnswl-postfix.conf
%doc README.ALT

%changelog
* Tue Nov 24 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.1-alt2
- Update README.ALT.

* Wed Nov 12 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 0.1-alt1
- Initial build for ALT Linux.

