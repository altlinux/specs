Name: dhcp_probe
Version: 1.3.1
Release: alt1
Summary: Tool for discover DHCP and BootP servers
License: %bsdstyle
Group: Networking/Other
URL: https://www.net.princeton.edu/software/dhcp_probe/

Source0: %name-%version.tar
Patch0: dhcp_probe-1.3.1-alt-fix-strerror-declaration.patch
Source999: watch

AutoReqProv: yes
BuildRequires(pre): rpm-build-licenses

BuildRequires: libnet2-devel libpcap-devel

%description
dchp_probe attempts to discover DHCP and BootP servers on a directly-attached Ethernet network.
A network administrator can use this tool to locate unauthorized DHCP and BootP servers. 

%prep
%setup
%patch0 -p2

%build
%configure
%ifarch x86_64
%make_build CFLAGS="%optflags -D__ARCH__=64"
%else
%make_build CFLAGS="%optflags -D__ARCH__=32"
%endif

%install
%makeinstall
install -m 644 -D extras/dhcp_probe.cf.sample %buildroot%_sysconfdir/dhcp_probe.cf

%files
%doc INSTALL.dhcp_probe README COPYING
%_sbindir/%name
%config(noreplace) %_sysconfdir/dhcp_probe.cf
%_man8dir/*
%_man5dir/*

%changelog
* Thu Apr 23 2026 Anton Farygin <rider@altlinux.org> 1.3.1-alt1
- 1.3.0 -> 1.3.1

* Tue Aug  2 2016 Terechkov Evgenii <evg@altlinux.org> 1.3.0-alt2
- Sync with Debian patches to make it work on x86_64

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.3.0-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Apr 12 2009 Anton Farygin <rider@altlinux.ru> 1.3.0-alt1
- first build for Sisyphus
