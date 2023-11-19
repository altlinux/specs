Name: ubridge
Version: 0.9.18
Release: alt2

Summary: Bridge for UDP tunnels, Ethernet, TAP and VMnet interfaces
License: GPL-3.0-or-later
Group: Networking/Other
Url: https://github.com/GNS3/ubridge

Source: %name-%version.tar

BuildRequires: libpcap-devel
BuildRequires: libiniparser-devel
BuildRequires: libnl-devel

Requires(pre): libcap-utils

%description
uBridge is a simple application to create user-land bridges between various
technologies. Currently bridging between UDP tunnels, Ethernet and TAP
interfaces is supported. Packet capture is also supported.

%prep
%setup

%build
%make_build SYSTEM_INIPARSER=1 CFLAGS="-DLINUX_RAW $RPM_OPT_FLAGS -lnl-3"

%install
mkdir -p %buildroot%_bindir
install -p -m4755 %name %buildroot%_bindir

%post
setcap cap_net_admin,cap_net_raw=ep %_bindir/%name

%files
%doc LICENSE README.rst
%attr(0755,root,root) %_bindir/%name

%changelog
* Sat Nov 18 2023 Anton Midyukov <antohami@altlinux.org> 0.9.18-alt2
- unboundle libiniparser, liblnl
- fix setcap with first install
- clean Packager
- fix License

* Wed May 20 2020 Anton Midyukov <antohami@altlinux.org> 0.9.18-alt1
- new version 0.9.18

* Wed Jul 31 2019 Anton Midyukov <antohami@altlinux.org> 0.9.16-alt1
- new version 0.9.16

* Fri Jun 29 2018 Anton Midyukov <antohami@altlinux.org> 0.9.14-alt1.1
- Rebuilt for aarch64

* Wed Apr 11 2018 Anton Midyukov <antohami@altlinux.org> 0.9.14-alt1
- new version 0.9.14

* Thu Oct 26 2017 Anton Midyukov <antohami@altlinux.org> 0.9.13-alt1
- new version 0.9.13

* Thu Feb 23 2017 Anton Midyukov <antohami@altlinux.org> 0.9.11-alt1
- new version 0.9.11

* Sun Dec 11 2016 Anton Midyukov <antohami@altlinux.org> 0.9.8-alt1
- New version 0.9.8

* Mon Aug 08 2016 Anton Midyukov <antohami@altlinux.org> 0.9.4-alt1
- Initial build for ALT Linux Sisyphus.
