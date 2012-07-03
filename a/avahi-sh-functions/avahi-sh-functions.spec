Name: avahi-sh-functions
Version: 0.1
Release: alt2

Packager: Stanislav Ievlev <inger@altlinux.org>

BuildArch: noarch

Source0: %name

Summary: helper functions to publish services in avahi
License: GPL
Group: System/Base

%description
helper functions to publish services in avahi

%install
install -Dpm 644 %SOURCE0 %buildroot/%_bindir/%name

%files
%_bindir/*

%changelog
* Fri Mar 13 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- don't reload avahi-daemon

* Thu Feb 12 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
