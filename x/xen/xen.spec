%def_with efi
%def_disable vtpm
%def_without xsm
%def_enable ocamltools
%def_enable monitors
%def_enable xenapi

%ifndef x86_64
%define x86_64 x86_64
%endif
%define set_without() %{expand:%%force_without %{1}} %{expand:%%undefine _with_%{1}}

Summary: Xen is a virtual machine monitor
Name: xen
Version: 4.7.0
%define pre %nil
# Hypervisor ABI
%define hv_abi 4.7
Release: alt1
Group: Emulators
License: GPLv2+, LGPLv2+, BSD
%define qemu_ver %version%pre
URL: http://www.xenproject.org/
Packager: Dmitriy D. Shadrinov <shadrinov@altlinux.ru>

Source0: %name-%version%pre.tar.bz2
Source1: qemu-xen-%version%pre.tar.bz2
Source2: qemu-xen-traditional-%qemu_ver.tar.bz2
Source3: mini-os-%qemu_ver.tar.bz2
Source4: %name.logrotate
# used by stubdoms
Source10: newlib-1.16.0.tar.gz
Source11: zlib-1.2.3.tar.gz
Source12: polarssl-1.1.4-gpl.tgz
Source13: lwip-1.3.0.tar.gz
Source14: grub-0.97.tar.gz
Source15: pciutils-2.2.9.tar.bz2
%if_enabled vtpm
Source16: tpm_emulator-0.7.4.tar.gz
Source17: gmp-4.3.2.tar.bz2
%endif
# systemd bits
Source49: tmpfiles.d.xen.conf

Patch0: %name-%version-%release.patch

# Fedora
Patch5: %name-net-disable-iptables-on-bridge.patch

Patch10: pygrubfix.patch
Patch15: %name.use.fedora.ipxe.patch
Patch17: %name.fedora.efi.build.patch
Patch19: %name.pygrubtitlefix.patch
Patch20: %name.xsm.enable.patch
Patch21: %name.64.bit.hyp.on.ix86.patch

# ALT
Patch50: %name-4.0.0-libfsimage-soname-alt.patch

ExclusiveArch: %ix86 %x86_64 armh aarch64

Requires: bridge-utils
Requires: python-module-lxml
Requires: udev >= 059
Requires: chkconfig

%ifarch %ix86
%def_without hypervisor
%else
%def_with hypervisor
%endif

# xen only supports efi boot images on x86_64
%ifnarch %x86_64
%set_without efi
%endif

%if_without hypervisor
# no point in trying to build xsm on ix86 without a hypervisor
%set_without xsm
%endif

%ifarch %ix86 %x86_64
%def_enable stubdom
%else
%def_disable stubdom
%endif

%{?_with_hypervisor:Requires: %name-runtime = %version-%release}

%{?_with_efi:BuildPreReq: rpm-macros-uefi}
BuildRequires: zlib-devel libncurses-devel libaio-devel
BuildRequires: python-devel ghostscript %_bindir/texi2html transfig
BuildRequires: pkgconfig(glib-2.0) >= 2.12
# for the docs
BuildRequires: perl(Pod/Man.pm) perl(Pod/Text.pm) texinfo graphviz
BuildRequires: discount perl-devel
# so that the makefile knows to install udev rules
BuildRequires: udev
BuildRequires: gettext libgnutls-devel libssl-devel
# For ioemu PCI passthrough
BuildRequires: libpci-devel
# Several tools now use uuid
BuildRequires: libuuid-devel
# iasl needed to build hvmloader
BuildRequires: iasl
# build using Fedora seabios and ipxe packages for roms
BuildRequires: seabios ipxe-roms-qemu
# modern compressed kernels
BuildRequires: bzlib-devel liblzma-devel
# libfsimage
BuildRequires: libe2fs-devel
# tools now require yajl
BuildRequires: libyajl-devel
%{?_enable_ocamltools:BuildRequires: ocaml ocamlbuild ocamldoc findlib}
%{?_enable_xenapi:BuildRequires: libxml2-devel}
%if 0
BuildRequires: %_includedir/gnu/stubs-32.h
# for the VMX "bios"
BuildRequires: dev86
# xsm policy file needs needs checkpolicy and m4
%{?_with_xsm:BuildRequires: checkpolicy m4}
# efi image needs an ld that has -mi386pep option
%{?_with_efi:BuildRequires: mingw64-binutils}
%{?_enable_stubdom:BuildRequires: makeinfo}
%{?_with_hypervisor:BuildRequires: flex discount libfdt-devel libgcrypt-devel liblzo2-devel libvde-devel perl-HTML-Parser perl-devel}
%else
BuildRequires: rpm-build-xen >= 4.3.1
%endif
# from 4.7.0
BuildRequires: libnl-devel >= 3.2.8 libnl3 >= 3.2.8 libnl3-utils >= 3.2.8
BuildRequires: libpixman-devel >= 0.21.8 libpixman >= 0.21.8
BuildRequires: libnettle-devel nettle
BuildRequires: gcc5-c++
BuildRequires: libsystemd-devel >= 209

%description
This package contains the command line tools, needed to manage virtual
machines running under the Xen hypervisor.


%package -n lib%name
Summary: Shared libraries for Xen tools
Group: System/Libraries
Provides: %name-libs = %version-%release
Obsoletes: %name-libs
Requires: xen-licenses

%description -n lib%name
This package contains the libraries needed to run applications
which manage Xen virtual machines.


%package runtime
Summary: Core Xen runtime environment
Group: Emulators
Requires: lib%name = %version-%release
Requires: %_bindir/qemu-img
# Ensure we at least have a suitable kernel installed, though we can't
# force user to actually boot it.
%{?_with_hypervisor:Requires: %name-hypervisor-abi = %hv_abi}

%description runtime
This package contains the runtime programs and daemons which form the
core Xen userspace environment.


%if_with hypervisor
%package hypervisor
Summary: Xen hypervisor
Group: System/Kernel and hardware
Provides: xen-hypervisor-abi = %hv_abi
Requires: xen-licenses

%description hypervisor
This package contains the Xen hypervisor.
%endif


%package doc
Summary: Xen documentation
Group: Documentation
BuildArch: noarch
Requires: xen-licenses

%description doc
This package contains the Xen documentation.


%package devel
Summary: Development libraries for Xen tools
Group: Development/C
BuildArch: noarch
Requires: lib%name = %version-%release
Requires: libuuid-devel

%description devel
This package contains what's needed to develop applications
which manage Xen virtual machines.


%package licenses
Summary: License files from Xen source
Group: Documentation
BuildArch: noarch

%description licenses
This package contains the license files from the source used
to build the xen packages.


%if_enabled ocamltools
%package ocaml
Summary: Ocaml libraries for Xen tools
Group: Development/Other
Requires: ocaml-runtime, lib%name = %version-%release

%description ocaml
This package contains libraries for ocaml tools to manage Xen
virtual machines.


%package ocaml-devel
Summary: Ocaml development libraries for Xen tools
Group: Development/Other
Requires: %name-ocaml = %version-%release

%description ocaml-devel
This package contains libraries for developing ocaml tools to
manage Xen virtual machines.
%endif


%prep
%setup -q -n %name-%version%pre -a1 -a2 -a3
mkdir extras
ln -s ../qemu-xen-%version tools/qemu-xen
ln -s ../qemu-xen-traditional-%version tools/qemu-xen-traditional
ln -s ../mini-os-%version extras/mini-os
%patch0 -p1

%patch5 -p1

%patch10 -p1
%patch15 -p1
%patch17 -p1
#-%-patch18 -p1
%patch19 -p1
%{?_with_xsm:%patch20 -p1}
%{?_with_hypervisor:%patch21 -p1}

%patch50 -p2

sed -i '/^[[:blank:]]*\. \/etc\/rc\.status[[:blank:]]*$/s/\. /: # &/' tools/hotplug/Linux/xendomains.in

# stubdom sources
cd stubdom

ln -s %SOURCE10
ln -s %SOURCE11
ln -s %SOURCE12
ln -s %SOURCE13
ln -s %SOURCE14
ln -s %SOURCE15

cd ..

%build
%{?_with_efi:install -d -m 0755 dist/install/boot/efi/efi/altlinux}
#export QEMU_REMOTE=$PWD/qemu-%name-%qemu_ver
#export CONFIG_QEMU=$PWD/qemu-%name-%qemu_ver
#export QEMU_UPSTREAM_URL=$PWD/qemu-upstream-%version%pre
#	--with-system-qemu \
#	--enable-qemu \
%if "%pre" == "%nil"
export XEN_VENDORVERSION="-%release"
%else
v="%version"
export XEN_EXTRAVERSION="${v#${v%%.*}}-%release"
%endif
export EXTRA_CFLAGS_XEN_TOOLS="%optflags"
export EXTRA_CFLAGS_QEMU_TRADITIONAL="%optflags"
export EXTRA_CFLAGS_QEMU_XEN="%optflags"
%{?_enable_xenapi:export XML=$(which xml2-config)}
export WGET=$(which true)
export GIT=$(which true)
./configure \
	--prefix=%_prefix \
	--libdir=%_libdir \
	--enable-xen \
	--with-system-seabios=%_datadir/seabios/bios-256k.bin \
	--with-systemd=%_unitdir \
	--with-xenstored=xenstored \
	--without-systemd-modules-load \
	%{subst_enable xenapi} \
	%{subst_enable monitors} \
	%{subst_enable stubdom} \
%if_enabled vtpm
	--enable-vtpm-stubdom \
	--enable-vtpmmgr-stubdom \
%else
	--disable-vtpm-stubdom \
	--disable-vtpmmgr-stubdom \
%endif
	%{subst_enable ocamltools} \
	--enable-tools \
	--disable-kernels \
	--enable-docs
%make_build %{?_with_efi:LD_EFI=x86_64-pc-mingw32-ld}


%install
#export QEMU_REMOTE=$PWD/qemu-%name-%qemu_ver
#export CONFIG_QEMU=$PWD/qemu-%name-%qemu_ver
#export QEMU_UPSTREAM_URL=$PWD/qemu-upstream-%version%pre
%if "%pre" == "%nil"
export XEN_VENDORVERSION="-%release"
%else
v="%version"
export XEN_EXTRAVERSION="${v#${v%%.*}}-%release"
%endif
export EXTRA_CFLAGS_XEN_TOOLS="%optflags"
export EXTRA_CFLAGS_QEMU_TRADITIONAL="%optflags"
export EXTRA_CFLAGS_QEMU_XEN="%optflags"
%{?_enable_xenapi:export XML=$(which xml2-config)}
export WGET=$(which true)
export GIT=$(which true)
%{?_enable_ocamltools:install -d -m 0755 %buildroot%_libdir/ocaml/stublibs}
%{?_with_efi:install -d -m 0755 %buildroot/boot/efi/efi/altlinux}
%make_install DESTDIR=%buildroot %{?_with_efi:LD_EFI=x86_64-pc-mingw32-ld}

%{?_with_efi:mv %buildroot/boot/efi/efi %buildroot/boot/efi/EFI}

%if_with xsm
# policy file should be in /boot/flask
install -d -m 0755 %buildroot/boot/flask
mv %buildroot/boot/xenpolicy.* %buildroot/boot/flask
%else
rm -f %buildroot/boot/xenpolicy.*
%endif

############ kill unwanted stuff ############

# stubdom: newlib
rm -rf %buildroot/usr/*-xen-elf

# hypervisor symlinks
%{!?_with_hypervisor:rm -rf %buildroot/boot}

# silly doc dir fun
mv %buildroot%_docdir/%name{,-%version}
install -p -m 0644 COPYING README %buildroot%_docdir/%name-%version/
mv %buildroot%_docdir/%name-%version/{html/,}misc

# Pointless helper
rm -f %buildroot%_sbindir/xen-python-path

# qemu stuff (unused or available from upstream)
rm -rf %buildroot{%_datadir/%name/man,%_bindir/qemu-*-%name}
for i in img nbd; do
	ln -s qemu-img %buildroot/%_bindir/qemu-$i-xen
done
for f in \
	{bios,ppc_rom}.bin \
	openbios-{ppc,sparc{32,64}} \
	pxe-{e1000,ne2k_pci,pcnet,rtl8139}.bin \
	vgabios{,-cirrus}.bin \
	video.x \
	bamboo.dtb
do
	rm -f %buildroot/%_datadir/%name/qemu/$f
done

# README's not intended for end users
rm -f %buildroot/%_sysconfdir/%name/README*

# standard gnu info files
rm -rf %buildroot%_prefix/info

# adhere to Static Library Packaging Guidelines
rm -f %buildroot%_libdir/*.a

# clean up extra efi files
%{?_with_efi:#rm -rf %buildroot%_libdir/efi}

############ fixup files in /etc ############

# logrotate
install -pD -m 0644 %SOURCE4 %buildroot%_logrotatedir/%name
install -pD -m 0644 %SOURCE49 %buildroot/lib/tmpfiles.d/xen.conf

############ create dirs in /var ############
install -d -m 0755 %buildroot%_localstatedir/%name/{xend-db/{domain,vnet,migrate},images}
install -d -m 0755 %buildroot%_logdir/%name/console

############ assemble license files ############
# avoid licensedir to avoid recursion, also stubdom/ioemu and dist
# which are copies of files elsewhere
find . \
	-path %buildroot%_docdir/%name-%version/licenses -prune -o \
	-path stubdom/ioemu -prune -o \
	-path dist -prune -o \
	-name COPYING -o \
	-name LICENSE |
while read f; do
	install -pD -m 0644 {,%buildroot%_docdir/%name-%version/licenses/}$f
done

%ifarch %x86_64
rm -fr %buildroot%_docdir/%name-%version/licenses/stubdom/lwip-x86_64
rm -fr %buildroot%_docdir/%name-%version/licenses/stubdom/polarssl-x86_64
%endif

mv %buildroot%_docdir/%name-%version/licenses/stubdom/lwip-x86_32 %buildroot%_docdir/%name-%version/licenses/stubdom/lwip
mv %buildroot%_docdir/%name-%version/licenses/stubdom/polarssl-x86_32 %buildroot%_docdir/%name-%version/licenses/stubdom/polarssl

############ all done now ############

%ifdef brp_strip_none
%brp_strip_none %_datadir/xen/qemu/* %_datadir/qemu-xen/qemu/*
%else
%add_strip_skiplist %_datadir/xen/qemu/* %_datadir/qemu-xen/qemu/*
%endif
%add_verify_elf_skiplist %_datadir/xen/qemu/openbios-* %_datadir/qemu-xen/qemu/* /boot/*


%post runtime
%post_service xen-watchdog
%post_service xencommons
%post_service xendomains
%post_service xendriverdomain


%preun runtime
%preun_service xendriverdomain
%preun_service xendomains
%preun_service xencommons
%preun_service xen-watchdog


%files
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/COPYING
%doc %_docdir/%name-%version/README
%_bindir/xencons
%python_sitelibdir/%name
%python_sitelibdir/xen-*.egg-info

%dir %_localstatedir/%name

%dir %attr(0700,root,root) %_sysconfdir/%name
# Guest autostart links
%dir %attr(0700,root,root) %_sysconfdir/%name/auto


%files -n lib%name
%_libdir/*.so
%_libdir/*.so.*
%_libdir/fs


# All runtime stuff
%files runtime
%dir %attr(0700,root,root) %_sysconfdir/%name
%dir %attr(0700,root,root) %_sysconfdir/%name/auto
%dir %attr(0700,root,root) %_sysconfdir/%name/scripts

%_sysconfdir/%name/scripts/*

%config(noreplace) %_sysconfdir/%name/cpupool
%config(noreplace) %_sysconfdir/%name/xl.conf
%config(noreplace) %_sysconfdir/%name/xlexample*

%config(noreplace) %_sysconfdir/sysconfig/xencommons
%config(noreplace) %_sysconfdir/sysconfig/xendomains

%_initddir/xen-watchdog
%_initddir/xencommons
%_initddir/xendomains
%_initddir/xendriverdomain

%_sysconfdir/bash_completion.d/*

# Rotate console log files
%config(noreplace) %_sysconfdir/logrotate.d/%name

%_unitdir/proc-xen.mount
%_unitdir/var-lib-xenstored.mount

%_unitdir/xen-init-dom0.service
%_unitdir/xen-qemu-dom0-disk-backend.service
%_unitdir/xen-watchdog.service
%_unitdir/xenconsoled.service
%_unitdir/xendomains.service
%_unitdir/xenstored.service

%_tmpfilesdir/xen.conf

%{?_with_efi:/boot/efi/EFI/altlinux}

# Programs run by other programs
%if_enabled stubdom
%dir %_datadir/%name
# QEMU runtime files
%dir %_datadir/%name/qemu
%_datadir/%name/qemu/keymaps
%endif

# man pages
%_man1dir/xenstore*
%_man1dir/xentop.*
%_man1dir/xentrace_format.*
%_man8dir/xentrace.*
%_man1dir/xl.*
%_man5dir/xl.cfg.*
%_man5dir/xl.conf.*
%_man5dir/xlcpupool.cfg.*

%python_sitelibdir/fsimage.so
%python_sitelibdir/grub
%python_sitelibdir/pygrub-*.egg-info

# The firmware
%ifarch %ix86 %x86_64
%dir %_libexecdir/%name
%_libexecdir/%name/boot
%{?_enable_vtpm:%_libexecdir/%name/boot/vtpm*.gz}
%endif

%_datadir/qemu-xen/qemu
%_libexecdir/%name/bin
%_libexecdir/%name/libexec

# General Xen state
%dir %_localstatedir/%name
%dir %_localstatedir/%name/dump
%dir %_localstatedir/%name/images

%_sbindir/*

%{?_enable_ocamltools:%exclude %_sbindir/oxenstored}
%_bindir/*

%exclude %_bindir/xencons
%exclude %_datadir/qemu-xen/qemu/s390-ccw.img

# Xen logfiles
%dir %attr(0700,root,root) %_logdir/xen
# Guest/HV console logs
%dir %attr(0700,root,root) %_logdir/xen/console

%exclude %_datadir/pkgconfig/xenlight.pc
%exclude %_datadir/pkgconfig/xlutil.pc

%if_with hypervisor
%files hypervisor
/boot/xen*
%{?_with_xsm:/boot/flask}
%{?_with_efi:%_efi_bindir/*}
%endif


%files doc
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/misc/
%doc %_docdir/%name-%version/html


%files devel
%_includedir/*.h
%_includedir/%name
%_includedir/%{name}store-compat


%files licenses
%dir %_docdir/%name-%version
%_docdir/%name-%version/licenses


%if_enabled ocamltools
%files ocaml
%_libdir/ocaml/site-lib/%{name}*
%exclude %_libdir/ocaml/site-lib/%{name}*/*.a
%exclude %_libdir/ocaml/site-lib/%{name}*/*.cmxa
%exclude %_libdir/ocaml/site-lib/%{name}*/*.cmx
%_sbindir/oxenstored
%config(noreplace) %_sysconfdir/%name/oxenstored.conf


%files ocaml-devel
%_libdir/ocaml/site-lib/%{name}*/*.a
%_libdir/ocaml/site-lib/%{name}*/*.cmxa
%_libdir/ocaml/site-lib/%{name}*/*.cmx
%endif


%changelog
* Mon Sep 26 2016 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.7.0-alt1
- 4.7.0 release

* Tue Sep 02 2014 Led <led@altlinux.ru> 4.4.1-alt1
- 4.4.1 release

* Thu Aug 28 2014 Led <led@altlinux.ru> 4.4.1-alt0.7
- upstream fixes:
  + CVE-2014-4611

* Sat Aug 16 2014 Led <led@altlinux.ru> 4.4.1-alt0.6
- upstream updates and fixes:
  + CVE-2014-5146
  + CVE-2014-5147
  + CVE-2014-5148

* Sun Aug 10 2014 Led <led@altlinux.ru> 4.4.1-alt0.5
- 4.4.1-rc2

* Sun Aug 03 2014 Led <led@altlinux.ru> 4.4.1-alt0.4
- upstream updates

* Thu Jul 24 2014 Led <led@altlinux.ru> 4.4.1-alt0.3
- upstream updates

* Thu Jul 10 2014 Led <led@altlinux.ru> 4.4.1-alt0.2
- upstream updates
- libxen obsoletes xen-libs (ALT#30173)

* Sat Jun 21 2014 Led <led@altlinux.ru> 4.4.1-alt0.1
- 4.4.1-rc1

* Sun May 25 2014 Led <led@altlinux.ru> 4.4.0-alt9
- disabled xend (obsolete xen management user interface)

* Fri May 23 2014 Led <led@altlinux.ru> 4.4.0-alt8
- upstream updates for fixing vulnerabilities:
  + CVE-2013-3495

* Mon May 12 2014 Led <led@altlinux.ru> 4.4.0-alt7
- upstream updates for fixing vulnerabilities:
  + CVE-2013-3495
  + CVE-2014-3125

* Fri Apr 25 2014 Led <led@altlinux.ru> 4.4.0-alt6
- upstream updates for fixing vulnerabilities on ARM
  (CVE-2014-2915, CVE-2014-2986)

* Wed Mar 26 2014 Led <led@altlinux.ru> 4.4.0-alt5
- x86: enforce preemption in HVM_set_mem_access / p2m_set_mem_access()
  (CVE-2014-2599)

* Sun Mar 16 2014 Led <led@altlinux.ru> 4.4.0-alt4
- upstream fixes

* Thu Mar 13 2014 Led <led@altlinux.ru> 4.4.0-alt3
- add missed ARM-specific headers

* Tue Mar 11 2014 Led <led@altlinux.ru> 4.4.0-alt2
- enabled xenapi

* Tue Mar 11 2014 Led <led@altlinux.ru> 4.4.0-alt1
- 4.4.0

* Sun Feb 16 2014 Led <led@altlinux.ru> 4.3.2-alt1
- 4.3.2

* Sat Feb 15 2014 Led <led@altlinux.ru> 4.3.1-alt3
- fixed BuildRequires

* Wed Feb 12 2014 Led <led@altlinux.ru> 4.3.1-alt2
- fixed build tools/ocaml for arm arches
- enabled ocaml

* Sat Feb 08 2014 Led <led@altlinux.ru> 4.3.1-alt1
- 4.3.1
- based on Fedora spec 4.3.1-6
- fixed URL

* Tue Apr 16 2013 Fr. Br. George <george@altlinux.ru> 4.1.3-alt3.1
- Fix build (DSO and underinclude)

* Mon Oct 29 2012 Lenar Shakirov <snejok@altlinux.ru> 4.1.3-alt3
- xen-4.1.3-qemu-revert-O_DIRECT.patch added:
  * fix loading from boot discs with phy:/dev/cdrom
  * http://xenbits.xen.org/gitweb/?p=qemu-xen-4.2-testing.git;
    a=commit;h=effd5676225761abdab90becac519716515c3be4
 
* Fri Oct 26 2012 Lenar Shakirov <snejok@altlinux.ru> 4.1.3-alt2
- build witch ipxe

* Wed Oct 03 2012 Lenar Shakirov <snejok@altlinux.ru> 4.1.3-alt1
- 4.1.3
- old patched dropped: applied in upstream

* Wed Jun 13 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1.2-alt3
- CVE-2012-0217, CVE-2012-0218, CVE-2012-2934

* Mon Feb 06 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1.2-alt2
- CVE-2012-0029

* Fri Jan 27 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1.2-alt1
- 4.1.2
- rename xen-libs to libxen (ALT #24693)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1.1-alt1.1
- Rebuild with Python-2.7

* Wed Jun 15 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1.1-alt1
- 4.1.1 including CVE-2011-1898 fix

* Tue May 10 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1.0-alt2
- CVE-2011-1583

* Tue Mar 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1.0-alt1
- 4.1.0

* Tue Mar 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.2-alt0.2
- 4.0.2-rc2

* Thu Nov 18 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.1-alt2
- rebuild with liblzma.so.5
- build with gcc-4.4 (errors while building with gcc-4.5)

* Thu Aug 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.1-alt1
- 4.0.1

* Thu Apr 08 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.0-alt1
- 4.0.0

* Mon Jan 18 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.2-alt1
- 3.4.2-alt1 based on fedora spec
