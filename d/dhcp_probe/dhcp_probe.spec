Name: dhcp_probe
Version: 1.3.0
Release: alt2
Summary: Tool for discover DHCP and BootP servers
License: %bsdstyle
Group: Networking/Other
URL: http://www.net.princeton.edu/software/dhcp_probe/

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

AutoReqProv: yes
BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun Apr 12 2009
BuildRequires: libnet2-devel libpcap-devel

%description
dchp_probe attempts to discover DHCP and BootP servers on a directly-attached Ethernet network.
A network administrator can use this tool to locate unauthorized DHCP and BootP servers. 

%prep
%setup
%patch0 -p1

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
* Tue Aug  2 2016 Terechkov Evgenii <evg@altlinux.org> 1.3.0-alt2
- Sync with Debian patches to make it work on x86_64

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.3.0-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Apr 12 2009 Anton Farygin <rider@altlinux.ru> 1.3.0-alt1
- first build for Sisyphus
