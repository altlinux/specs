Name: avahi-sh-functions
Version: 0.1
Release: alt3

Packager: Stanislav Ievlev <inger@altlinux.org>

BuildArch: noarch

Source0: %name
Source1: avahi-sh

Summary: helper functions to publish services in avahi
License: GPL
Group: System/Base

%description
helper functions to publish services in avahi

%install
install -Dpm 644 %SOURCE0 %buildroot/%_bindir/%name
install -Dp -m0755 %SOURCE1 %buildroot/%_bindir/avahi-sh

%files
%_bindir/*

%changelog
* Mon Dec 10 2012 Paul Wolneykien <manowar@altlinux.ru> 0.1-alt3
- Add the dispatcher to call functions externally.

* Fri Mar 13 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- don't reload avahi-daemon

* Thu Feb 12 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
