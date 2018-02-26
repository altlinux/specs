Summary: IPsec-Tools package use the IPsec functionality in the linux-2.5+ kernels.
Name: ipsec-tools
Version: 0.8.0
Release: alt1
URL: http://ipsec-tools.sourceforge.net/
License: BSD
Group: Security/Networking
Requires: libipsec = %version-%release

Packager: Dmitry Lebkov <dlebkov@altlinux.ru>

Source0: ftp://ftp.netbsd.org/pub/NetBSD/misc/ipsec-tools/0.7/ipsec-tools-%{version}.tar.bz2
Source1: %name-racoon.init
Source2: %name-racoon.sysconfig
Source3: p1_up_down
Source4: racoon.conf
Source5: racoon.pam

# patches from ipsec-tools-0.8.0-2.fc16.src.rpm
# Ignore acquires that are sent by kernel for SAs that are already being
# negotiated (#234491)
Patch3: ipsec-tools-0.8.0-acquires.patch
# Support for labeled IPSec on loopback
Patch4: ipsec-tools-0.8.0-loopback.patch
# Create racoon as PIE
Patch11: ipsec-tools-0.7.1-pie.patch
# Fix leak in certification handling
Patch14: ipsec-tools-0.7.2-moreleaks.patch
# Do not install development files
Patch16: ipsec-tools-0.8.0-nodevel.patch
# Use krb5 gssapi mechanism
Patch18: ipsec-tools-0.7.3-gssapi-mech.patch
# Drop -R from linker
Patch19: ipsec-tools-0.7.3-build.patch
# Silence strict aliasing warnings
Patch20: ipsec-tools-0.8.0-aliasing.patch

Patch100: ipsec-tools-0.7.2-alt-werror.patch
Patch101: ipsec-tools-0.8.0-alt-makefile.patch
Patch102: ipsec-tools-0.7.2-alt-config.patch
Patch103: ipsec-tools-0.7.2-alt-unres.patch
Patch104: ipsec-tools-0.7.2-alt-gcc44-warns.patch
Patch105: ipsec-tools-0.8.0-alt-wildcard-psk.patch

#optimized out: libcom_err-devel libkrb5-devel
BuildRequires: flex libaudit-devel libpam-devel libreadline-devel libselinux-devel libssl-devel

%description
This is the IPsec-Tools package.  You need this package in order to
really use the IPsec functionality in the linux-2.5+ kernels.  This
package builds:

- setkey, a program to directly manipulate policies and SAs
- racoon, an IKEv1 keying daemon

%package -n libipsec
Summary: IPSec-Tools shared libraries
Group: System/Libraries

%description -n libipsec
IPSec-Tools shared libraries package.


%package -n libipsec-devel
Summary: IPSec-Tools development files
Group: Development/C
Requires: %name = %version-%release
Provides: %name-devel = %version
Obsoletes: %name-devel

%description -n libipsec-devel
IPSec-Tools development files package.


%prep
%setup -q

%patch3 -p1 -b .acquires
%patch4 -p1 -b .loopback

%patch11 -p1 -b .pie
%patch14 -p1 -b .moreleaks
#%patch16 -p1 -b .nodevel
%patch18 -p1 -b .gssapi-mech
%patch19 -p1 -b .build
%patch20 -p1 -b .aliasing

#%patch100 -p1 -b .werror
%patch101 -p1 -b .altmake
%patch102 -p1 -b .syscfg
%patch103 -p1 -b .unres
%patch104 -p1 -b .gcc4warn
%patch105 -p1 -b .wildcard

sed -i 's|-Werror||g' configure*

%build
./bootstrap
%configure \
	--disable-static \
	--with-kernel-headers=/usr/include \
	--enable-shared \
	--sysconfdir=/etc/racoon \
	--enable-hybrid \
	--enable-frag \
	--enable-stats \
	--enable-dpd \
	--enable-natt=kernel \
	--enable-natt \
	--enable-security-context \
	--enable-audit \
	--enable-gssapi \
	--with-libpam

%make

%install
%make install DESTDIR=%buildroot

mkdir -p %buildroot/%_sysconfdir/racoon/certs
mkdir -p %buildroot/%_sysconfdir/racoon/scripts
mkdir -p %buildroot/%_initdir
mkdir -p %buildroot/%_sysconfdir/sysconfig
mkdir -p %buildroot/%_sysconfdir/pam.d
install -p -m0600 src/racoon/samples/psk.txt %buildroot%_sysconfdir/racoon/
install -p -m0644 %SOURCE4 %buildroot%_sysconfdir/racoon/
install -p -m0700 %SOURCE3 %buildroot%_sysconfdir/racoon/scripts/
install -m 0755 %SOURCE1 %buildroot%_initdir/racoon
install -m 0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/racoon
install -p -m0644 %SOURCE5 %buildroot%_sysconfdir/pam.d/racoon

%preun
%preun_service racoon

%post
%post_service racoon

%files
%_initdir/racoon
%config(noreplace) %_sysconfdir/racoon/racoon.conf
%config(noreplace) %_sysconfdir/racoon/psk.txt
%config(noreplace) %_sysconfdir/sysconfig/racoon
%config(noreplace) %_sysconfdir/pam.d/racoon
%_sysconfdir/racoon/scripts/p1_up_down
%dir %_sysconfdir/racoon/certs
%dir %_sysconfdir/racoon/scripts
%dir %_sysconfdir/racoon/
%_sbindir/plainrsa-gen
%_sbindir/racoon
%_sbindir/racoonctl
%_sbindir/setkey
%_man3dir/*
%_man5dir/racoon.conf.5*
%_man8dir/plainrsa-gen.8.gz
%_man8dir/racoon.8.gz
%_man8dir/racoonctl.8.gz
%_man8dir/setkey.8.gz
%doc ChangeLog NEWS README src/racoon/doc/* src/racoon/samples/roadwarrior src/racoon/samples/*sample*
%dir %_localstatedir/racoon

%files -n libipsec
%_libdir/libipsec.so.*
%_libdir/libracoon.so.*

%files -n libipsec-devel
%_libdir/libipsec.so
%_libdir/libracoon.so
%_includedir/libipsec/*
%dir %_includedir/libipsec
%_includedir/racoon/*
%dir %_includedir/racoon


%changelog
* Thu Dec 29 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0
- enable ipv6
- build with pam support
- add support wildcard in psk.txt (patch105)

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 0.7.2-alt1.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sun May 24 2009 Dmitry Lebkov <dlebkov@altlinux.ru> 0.7.2-alt1.1
- fix package build

* Sun May 24 2009 Dmitry Lebkov <dlebkov@altlinux.ru> 0.7.2-alt1
- 0.7.2 (closes: #19917)
- move shared libraries to 'libipsec' package
- add libipsec-devel package

* Sun Dec 14 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 0.7.1-alt1
- 0.7.1 with patches from ipsec-tools-0.7.1-6.fc11

* Wed Aug 27 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 0.6.7-alt2
- CVE-2008-3651 and CVE-2008-3652 patches from RedHat package
  ipsec-tools-0.6.5-9.3:
  + for DoS through various memory leaks (rh#456660, rh#458846)
- other patches from RH

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.6.7-alt1.1
- Automated rebuild due to libcrypto.so.6 -> libcrypto.so.7 soname change.

* Sun May 13 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 0.6.7-alt1
- 0.6.7
- CVE-2007-1841
- ALT bug #11604 fixed
- add init-script for racoon daemon

* Wed Dec 20 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 0.6.6-alt1
- fix build requires

* Fri Oct 27 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 0.6.6-alt0
- 0.6.6

* Wed Mar 2 2005 Maxim Tyurin <mrkooll@altlinux.ru> 0.5-alt1
- New version (fixed CAN-2004-0155) and fixed potencial buffer ovefflow.

* Thu Jun 10 2004 Maxim Tyurin <mrkooll@altlinux.ru> 0.2.3-alt1
- Initial build.

