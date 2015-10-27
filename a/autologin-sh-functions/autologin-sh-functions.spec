Name: autologin-sh-functions
Version: 0.1
Release: alt1

Summary: helper functions for autologin setup
License: GPLv2+
Group: System/Base

Url: http://altlinux.org/m-p
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
* Wed Oct 07 2015 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (based on mkimage-profiles 1.1.75)

