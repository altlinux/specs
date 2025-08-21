Name: livecd-auto-hostname
Version: 0.1.2
Release: alt1

Summary: Try to autoconfigure hostname
License: GPL-3.0-or-later
Group: System/Configuration/Networking

Url: https://www.altlinux.org
Source: %name-%version.tar

BuildArch: noarch

Conflicts: livecd-hostname

%description
This package might be useful for livecd images when it's required
to autoconfigure hostname.

%prep
%setup

%install
install -pDm755 %name.init %buildroot%_initdir/%name
install -pDm755 %name.sh %buildroot%_prefix/libexec/%name
install -pDm644 %name.service %buildroot%_unitdir/%name.service

%preun
%preun_service %name

%files
%_initdir/%name
%_prefix/libexec/%name
%_unitdir/%name.service

%changelog
* Fri Aug 15 2025 Anton Midyukov <antohami@altlinux.org> 0.1.2-alt1
- livecd-net-eth: add RemainAfterExit=yes

* Thu May 29 2025 Anton Midyukov <antohami@altlinux.org> 0.1.1-alt1
- decrease length of generate hostname, when unavailable network

* Wed May 28 2025 Anton Midyukov <antohami@altlinux.org> 0.1.0-alt1
- initial build
