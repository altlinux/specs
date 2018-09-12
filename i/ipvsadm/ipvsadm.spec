Summary: Utility to administer the Linux Virtual Server
Name: ipvsadm
Version: 1.29
Release: alt1
License: GPL
Url: http://www.LinuxVirtualServer.org/
Group: System/Kernel and hardware

Provides: %name-%version

Source0: %name-%version.tar
Source1: %name.init.alt
Source2: %name.service

# Automatically added by buildreq on Sat May 16 2009
BuildRequires: libnl-devel libpopt-devel

%description
ipvsadm is a utility to administer the IP Virtual Server services
offered by the Linux kernel.

%prep
%setup -n %name-%version

%build
%make POPT_LIB="-lpopt"

%install
mkdir -p %buildroot/{sbin,%_man8dir,%_initrddir,%_sysconfdir/sysconfig}
%makeinstall BUILD_ROOT=%buildroot MANDIR=%_mandir
install -pD -m755 %SOURCE1 %buildroot%_initrddir/%name
install -pD -m644 %SOURCE2 %buildroot%_unitdir/%name.service
install -pD -m644 /dev/null %buildroot%_sysconfdir/sysconfig/%name

%files
%doc README
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/sysconfig/%name
%config %_initrddir/ipvsadm
/sbin/ipvsadm*
%_man8dir/ipvsadm*
%_unitdir/%name.service

%post
%post_service ipvsadm

%preun
%preun_service ipvsadm

%changelog
* Wed Sep 12 2018 Terechkov Evgenii <evg@altlinux.org> 1.29-alt1
- 1.29 (ALT #35385)
- Spec cleanup

* Tue Jan 12 2016 Mikhail Efremov <sem@altlinux.org> 1.28-alt1
- Updated to 1.28.

* Tue Mar 26 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.26-alt2
- Fix build

* Wed Apr 27 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.26-alt1
- New version
- Add LSB Init header

* Tue Dec 01 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.25-alt2
- Change priority to start after network

* Sat May 16 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.25-alt1
- New version
- Update BuildRequires
- Update spec
- Remove patch
- Fix init script

* Sun Apr 23 2006 LAKostis <lakostis@altlinux.org> 1.24-alt1
- First build for ALTLinux.
- .spec based on 1.24-7.2.1 FC package.

