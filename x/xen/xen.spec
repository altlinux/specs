# Hypervisor ABI
%define hv_abi  4.1

Summary: Xen is a virtual machine monitor
Name: xen
Version: 4.1.2
Release: alt3
Group: Development/Kernel
License: GPLv2+ and LGPLv2+ and BSD
Url: http://xen.org/
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: xen-%version.tar.gz
Source1: %name.modules
Source2: %name.logrotate
# used by stubdoms
Source10: lwip-1.3.0.tar.gz
Source11: newlib-1.16.0.tar.gz
Source12: zlib-1.2.3.tar.gz
Source13: pciutils-2.2.9.tar.bz2
Source14: grub-0.97.tar.gz

Patch4: xen-dumpdir.patch

Patch10: xen-no-werror.patch

Patch100: xen-configure-xend.patch
Patch104: xen-4.1.0-alt-various-underlink.patch
Patch105: xen-4.0.0-remove-rcstatus-alt.patch
Patch106: xen-4.0.0-libfsimage-soname-alt.patch
Patch107: xen-4.0.0-i586-fpic.patch
Patch108: xen-4.0.1-stubdom-secure-tmp-alt.patch
Patch109: xen-4.0.1-linux-fs-includes-fix-alt.patch
Patch110: xen-4.1-xsa7-xsa8.patch
Patch111: xen-4.1-xsa9.patch

# Automatically added by buildreq on Mon Jan 18 2010
%set_gcc_version 4.4

BuildRequires: bzlib-devel dev86 ghostscript-utils latex2html libGL-devel libSDL-devel libX11-devel libe2fs-devel libgnutls-devel liblzma-devel libncurses-devel libpci-devel libssl-devel python-devel python-modules-compiler python-modules-logging texi2html texlive-fonts-recommended texlive-generic-recommended transfig zlib-devel libuuid-devel iasl

Requires: xen-runtime = %version-%release
ExclusiveArch: %ix86 x86_64

%description
This package contains the XenD daemon and xm command line
tools, needed to manage virtual machines running under the
Xen hypervisor

%package -n libxen
Summary: Libraries for Xen tools
Group: Development/Kernel
Provides: xen-libs = %version-%release
Obsoletes: xen-libs < %version-%release

%description -n libxen
This package contains the libraries needed to run applications
which manage Xen virtual machines.

%package runtime
Summary: Core Xen runtime environment
Group: Development/Kernel
Requires: xen-libs = %version-%release
Requires: %_bindir/qemu-img %_bindir/qemu-nbd
# Ensure we at least have a suitable kernel installed, though we can't
# force user to actually boot it.
Requires: xen-hypervisor-abi = %hv_abi

%description runtime
This package contains the runtime programs and daemons which
form the core Xen userspace environment.

%package hypervisor
Summary: Libraries for Xen tools
Group: Development/Kernel
Provides: xen-hypervisor-abi = %hv_abi

%description hypervisor
This package contains the Xen hypervisor

%package doc
Summary: Xen documentation
Group: Documentation
BuildArch: noarch

%description doc
This package contains the Xen documentation.

%package devel
Summary: Development libraries for Xen tools
Group: Development/Kernel
Requires: xen-libs = %version-%release

%description devel
This package contains what's needed to develop applications
which manage Xen virtual machines.

%package devel-static
Summary: Development libraries for Xen tools
Group: Development/Kernel
Requires: xen-libs = %version-%release
Requires: xen-devel = %version-%release

%description devel-static
This package static libraries to develop applications
which manage Xen virtual machines.

%prep
%setup -q

%patch4 -p1

%patch10 -p1

%patch100 -p1

%patch104 -p2
%patch105 -p2
%patch106 -p2
%patch107 -p2
%patch108 -p2
%patch109 -p2
%patch110 -p1
%patch111 -p1

# stubdom sources
cp -v %SOURCE10 %SOURCE11 %SOURCE12 %SOURCE13 %SOURCE14 stubdom

%build
export XEN_VENDORVERSION="-%release"
export CFLAGS="$RPM_OPT_FLAGS"
%make_build prefix=/usr dist-xen
%make_build prefix=/usr dist-tools
make                 prefix=/usr dist-docs
unset CFLAGS
make dist-stubdom

%install

make DESTDIR=%buildroot prefix=/usr install-xen
make DESTDIR=%buildroot prefix=/usr install-tools
make DESTDIR=%buildroot prefix=/usr install-docs
make DESTDIR=%buildroot prefix=/usr install-stubdom

############ debug packaging: list files ############

find %buildroot -print | xargs ls -ld | sed -e 's|.*%buildroot||' > f1.list

############ kill unwanted stuff ############

# stubdom: newlib
rm -rf %buildroot/usr/*-xen-elf

# hypervisor symlinks
rm -rf %buildroot/boot/xen-3.4.gz
rm -rf %buildroot/boot/xen-3.gz

# silly doc dir fun
rm -fr %buildroot%_docdir/xen
rm -rf %buildroot%_docdir/qemu

# Pointless helper
rm -f %buildroot%_sbindir/xen-python-path

# qemu stuff (unused or available from upstream)
rm -rf %buildroot%_datadir/xen/man
rm -rf %buildroot%_bindir/qemu-*-xen
ln -s qemu-img %buildroot/%_bindir/qemu-img-xen
ln -s qemu-img %buildroot/%_bindir/qemu-nbd-xen
for file in bios.bin openbios-sparc32 openbios-sparc64 ppc_rom.bin \
         pxe-e1000.bin pxe-ne2k_pci.bin pxe-pcnet.bin pxe-rtl8139.bin \
         vgabios.bin vgabios-cirrus.bin video.x openbios-ppc bamboo.dtb
do
	rm -f %buildroot/%_datadir/xen/qemu/$file
done

# README's not intended for end users
rm -f %buildroot/%_sysconfdir/xen/README*

# standard gnu info files
rm -rf %buildroot/usr/info

# remove python tests
rm -rf %buildroot/%python_sitelibdir/%name/xend/tests
rm -rf %buildroot/%python_sitelibdir/%name/xend/server/tests
rm -rf %buildroot/%python_sitelibdir/%name/xend/xenstore/tests
rm -rf %buildroot/%python_sitelibdir/%name/xm/tests

############ fixup files in /etc ############

# udev
mkdir -p %buildroot%_sysconfdir/udev/rules.d
cp -a dist/install/etc/udev/rules.d/*.rules %buildroot%_sysconfdir/udev/rules.d/

# modules
mkdir -p %buildroot%_sysconfdir/sysconfig/modules
install -m 644 %SOURCE1 %buildroot%_sysconfdir/sysconfig/modules/%name.modules

# logrotate
mkdir -p %buildroot%_sysconfdir/logrotate.d/
install -m 644 %SOURCE2 %buildroot%_sysconfdir/logrotate.d/%name

# init scripts
mkdir -p %buildroot%_initdir/

# sysconfig
mkdir -p %buildroot%_sysconfdir/sysconfig

############ create dirs in /var ############

mkdir -p %buildroot%_localstatedir/xen/xend-db/domain
mkdir -p %buildroot%_localstatedir/xen/xend-db/vnet
mkdir -p %buildroot%_localstatedir/xen/xend-db/migrate
mkdir -p %buildroot%_localstatedir/xen/images
mkdir -p %buildroot%_logdir/xen/console

############ debug packaging: list files ############

find %buildroot -print | xargs ls -ld | sed -e 's|.*%buildroot||' > f2.list
diff -u f1.list f2.list || true

# Base package only contains XenD/xm python stuff
#files -f xen-xm.lang
%files
%doc COPYING README
%_bindir/xencons
%_sbindir/xend
%_sbindir/xm
%python_sitelibdir/%name
%python_sitelibdir/xen-*.egg-info
%_man1dir/xm.1*
%_man5dir/xend-config.sxp.5*
%_man5dir/xmdomain.cfg.5*

# Startup script
%_initdir/xend
%_initdir/xencommons
%_initdir/xendomains
%_initdir/xen-watchdog
# Guest config files
%config(noreplace) %_sysconfdir/%name/xmexample*
# Daemon config
%config(noreplace) %_sysconfdir/%name/xend-*
# xm config
%config(noreplace) %_sysconfdir/%name/xm-*

%config(noreplace) %_sysconfdir/%name/xl.conf
%config(noreplace) %_sysconfdir/%name/cpupool

# Guest autostart links
%dir %attr(0700,root,root) %_sysconfdir/%name/auto
# Autostart of guests
%config(noreplace) %attr(0644,root,root) %_sysconfdir/sysconfig/xendomains

# Persistent state for XenD
%dir %_localstatedir/%name/xend-db/
%dir %_localstatedir/%name/xend-db/domain
%dir %_localstatedir/%name/xend-db/migrate
%dir %_localstatedir/%name/xend-db/vnet

%files -n libxen
%_libdir/*.so.*
%_libdir/fs

# All runtime stuff except for XenD/xm python stuff
%files runtime
# Hotplug rules
%config(noreplace) %_sysconfdir/udev/rules.d/*

%dir %attr(0700,root,root) %_sysconfdir/%name
%dir %attr(0700,root,root) %_sysconfdir/%name/scripts/
%config %attr(0700,root,root) %_sysconfdir/%name/scripts/*

# Auto-load xen backend drivers
%attr(0755,root,root) %_sysconfdir/sysconfig/modules/%name.modules

# Rotate console log files
%config(noreplace) %_sysconfdir/logrotate.d/xen

# sysconfig
%config(noreplace) %attr(0644,root,root) %_sysconfdir/sysconfig/xencommons

# Programs run by other programs
%dir %_libdir/%name
%dir %_libdir/%name/bin
%attr(0700,root,root) %_libdir/%name/bin/*
# QEMU runtime files
%dir %_datadir/%name/qemu
%dir %_datadir/%name/qemu/keymaps
%_datadir/%name/qemu/keymaps/*
%_datadir/%name/create.dtd

# man pages
%_man1dir/xentop.1*
%_man1dir/xentrace_format.1*
%_man8dir/xentrace.8*

%python_sitelibdir/fsimage.so
%python_sitelibdir/grub
%python_sitelibdir/pygrub-*.egg-info

# The firmware
%ifnarch ia64
# Avoid owning /usr/lib twice on i386
%if "%_libdir" != "/usr/lib"
%dir /usr/lib/%name
%dir /usr/lib/%name/bin
/usr/lib/%name/bin/qemu-dm
/usr/lib/%name/bin/stubdom-dm
/usr/lib/%name/bin/stubdompath.sh
%endif
%dir /usr/lib/%name/boot
# HVM loader is always in /usr/lib regardless of multilib
/usr/lib/xen/boot/hvmloader
/usr/lib/xen/boot/ioemu-stubdom.gz
/usr/lib/xen/boot/pv-grub*.gz
%endif
# General Xen state
%dir %_localstatedir/%name
%dir %_localstatedir/%name/dump
%dir %_localstatedir/%name/images
# Xenstore persistent state
%dir %_localstatedir/xenstored
# Xenstore runtime state
%dir %_runtimedir/xenstored
# XenD runtime state
%dir %attr(0700,root,root) %_runtimedir/xend
%dir %attr(0700,root,root) %_runtimedir/xend/boot

# All xenstore CLI tools
%_bindir/qemu-*-xen
%_bindir/xenstore
%_bindir/xenstore-*
%_bindir/pygrub
%_bindir/xentrace*
%_bindir/remus

# blktap daemon
%_sbindir/blktapctrl
%_sbindir/tapdisk
# XSM
%_sbindir/flask-loadpolicy
# Disk utils
%_sbindir/qcow-create
%_sbindir/qcow2raw
%_sbindir/img2qcow
# Misc stuff
%_bindir/xen-detect
%_sbindir/xen-bugtool
%_sbindir/xenconsoled
%_sbindir/xenmon.py*
%_sbindir/xentop
%_sbindir/xentrace_setmask
%_sbindir/xenbaked
%_sbindir/xenstored
%_sbindir/xenpm
%_sbindir/xenpmd
%_sbindir/xenperf
%_sbindir/xsview

%_sbindir/flask-getenforce
%_sbindir/flask-setenforce
%_sbindir/gtracestat
%_sbindir/gtraceview
%_sbindir/lock-util
%_sbindir/tapdisk-client
%_sbindir/tapdisk-diff
%_sbindir/tapdisk-stream
%_sbindir/tapdisk2
%_sbindir/td-util
%_sbindir/vhd-update
%_sbindir/vhd-util
%_sbindir/xen-hvmctx
%_sbindir/xen-tmem-list-parse
%_sbindir/xenlockprof
%_sbindir/xenpaging
%_sbindir/xl
%_sbindir/kdd
%_sbindir/tap-ctl
%_sbindir/xen-hptool
%_sbindir/xen-hvmcrash
%_sbindir/xenwatchdogd

# Xen logfiles
%dir %attr(0700,root,root) %_logdir/xen
# Guest/HV console logs
%dir %attr(0700,root,root) %_logdir/xen/console

%files hypervisor
/boot/xen-syms-*
/boot/xen-*.gz
/boot/xen.gz

%files doc
%doc docs/misc/
%doc dist/install%_docdir/xen/html
%doc dist/install%_docdir/xen/pdf/*.pdf

%files devel
%_sbindir/gdbsx
%_includedir/*.h
%dir %_includedir/xen
%_includedir/xen/*
%_libdir/*.so

%files devel-static
%_libdir/*.a

%changelog
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
