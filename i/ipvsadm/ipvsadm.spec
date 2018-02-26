Summary: Utility to administer the Linux Virtual Server
Name: ipvsadm
Version: 1.26
Release: alt1
License: GPL
Url: http://www.LinuxVirtualServer.org/
Group: System/Kernel and hardware
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Provides: %name-%version

Source0: http://www.LinuxVirtualServer.org/software/ipvsadm-%version.tar.gz
Source1: %name.init.alt
#Patch0: ipvsadm-1.25-kernhdr-1.2.0.patch

# Automatically added by buildreq on Sat May 16 2009
BuildRequires: libnl-devel libpopt-devel

%description
ipvsadm is a utility to administer the IP Virtual Server services
offered by the Linux kernel.

%prep
%setup -n %name-%version
#%patch0 -p1

%build
#make INCLUDE="-Ikernheaders -I.. -I." CFLAGS="%optflags" POPT_LIB="-lpopt"
%make_build POPT_LIB="-lpopt"

%install
%__mkdir_p $RPM_BUILD_ROOT/{sbin,%_man8dir,%_initrddir,%_sysconfdir/sysconfig}
%makeinstall BUILD_ROOT=%buildroot MANDIR=%_mandir
%__install -pD -m755 %SOURCE1 %buildroot%_initrddir/%name
%__install -pD -m644 /dev/null %buildroot%_sysconfdir/sysconfig/%name

%files
%doc README
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/sysconfig/%name
%config %_initrddir/ipvsadm
/sbin/ipvsadm*
%_man8dir/ipvsadm*

%post
%post_service ipvsadm

%preun
%preun_service ipvsadm

%changelog
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

