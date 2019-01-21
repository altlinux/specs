Name: installer-feature-disable-ipv6
Version: 0.1
Release: alt1

Summary: ipv6.disable=1
License: public domain
Group: System/Kernel and hardware

Url: http://altlinux.org/installer/beans
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

%description
Setup %summary.

%package stage3
Summary: ipv6.disable=1
Group: System/Kernel and hardware

%description stage3
Setup "%summary" when IPv6 is prohibited.

%prep
%setup

%install
%makeinstall

%files stage3
%_datadir/install2/postinstall.d/*

%changelog
* Mon Jan 21 2019 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

