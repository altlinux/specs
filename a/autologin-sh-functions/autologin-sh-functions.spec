Name: autologin-sh-functions
Version: 0.2.1
Release: alt1

Summary: helper functions for autologin setup
License: GPLv2+
Group: System/Base

Url: http://altlinux.org/autologin
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

%description
%summary

%prep
%setup

%install
install -pDm644 %name %buildroot%_bindir/%name

%files
%doc README
%_bindir/*

%changelog
* Mon Jan 25 2016 Andrey Cherepanov <cas@altlinux.org> 0.2.1-alt1
- extend API with al_possible()

* Thu Dec 03 2015 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- update for installed system case as well (see #30037)

* Wed Oct 07 2015 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (based on mkimage-profiles 1.1.75)

