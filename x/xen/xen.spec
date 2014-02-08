%def_with efi
%def_disable vtpm
%def_without xsm
# findlib for arm missed
%def_disable ocaml

%define _localstatedir %_var
%define _libexecdir %_prefix/libexec

%ifndef x86_64
%define x86_64 x86_64
%endif
%define set_without() %{expand:%%force_without %{1}} %{expand:%%undefine _with_%{1}}

Summary: Xen is a virtual machine monitor
Name: xen
Version: 4.3.1
# Hypervisor ABI
%define hv_abi 4.3
Release: alt1
Group: Emulators
License: GPLv2+, LGPLv2+, BSD
URL: http://www.xenproject.org/
Source0: http://bits.%{name}source.com/oss-%name/release/%version/%name-%version.tar
Source1: qemu-upstream-%version.tar
Source2: qemu-%name-%version.tar
Source3: %name.modules
#Source3: %name.modules.alt
Source4: %name.logrotate
# used by stubdoms
Source10: lwip-1.3.0.tar.gz
Source11: newlib-1.16.0.tar.gz
Source12: zlib-1.2.3.tar.gz
Source13: pciutils-2.2.9.tar.bz2
Source14: grub-0.97.tar.gz
Source15: polarssl-1.1.4-gpl.tgz
%if_enabled vtpm
Source16: tpm_emulator-0.7.4.tar.gz
Source17: gmp-4.3.2.tar.bz2
%endif
# init.d bits
#Source20: init.xenstored
#Source21: init.xenconsoled
#Source22: init.blktapctrl
#Source23: init.xend
Source20: xenstored.init
Source21: xenconsoled.init
Source22: blktapctrl.init
Source23: xend.init
Source24: xendomains.init
# sysconfig bits
Source30: sysconfig.xenstored
Source31: sysconfig.xenconsoled
Source32: sysconfig.blktapctrl
# systemd bits
Source40: proc-xen.mount
Source41: var-lib-xenstored.mount
Source42: xenstored.service
Source43: blktapctrl.service
Source44: xend.service
Source45: xenconsoled.service
Source46: %name-watchdog.service
Source47: xendomains.service
Source48: libexec.xendomains
Source49: tmpfiles.d.xen.conf
Source50: oxenstored.service

Patch1: %name-initscript.patch
Patch4: %name-dumpdir.patch
Patch5: %name-net-disable-iptables-on-bridge.patch

Patch10: pygrubfix.patch
Patch11: xend.catchbt.patch
Patch12: xend-pci-loop.patch
Patch13: xend.selinux.fixes.patch
Patch14: %name.use.fedora.seabios.patch
Patch15: %name.use.fedora.ipxe.patch
Patch16: qemu-%name.tradonly.patch
Patch17: %name.fedora.efi.build.patch
Patch18: %name.fedora19.buildfix.patch
Patch19: %name.pygrubtitlefix.patch
Patch20: %name.xsm.enable.patch
Patch21: %name.64.bit.hyp.on.ix86.patch
Patch22: xsa73-4.3-unstable.patch
Patch23: xsa75-4.3-unstable.patch
Patch24: xsa78.patch
Patch25: xsa74-4.3-unstable.patch
Patch26: xsa76.patch
Patch27: xsa82.patch
Patch28: xsa77-unstable.patch
Patch29: xsa80.patch

# ALT
Patch50: %name-4.0.0-libfsimage-soname-alt.patch
Patch51: %name-4.3.1-alt-libfsimage-link.patch
Patch52: %name-4.3.1-alt-libxl-link.patch

Patch100: %name-configure-xend.patch

ExclusiveArch: %ix86 %x86_64 armh aarch64

Requires: bridge-utils
Requires: python-module-lxml
Requires: udev >= 059
# Not strictly a dependency, but kpartx is by far the most useful tool right
# now for accessing domU data from within a dom0 so bring it in when the user
# installs xen.
Requires: kpartx
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

BuildRequires: libidn-devel zlib-devel libSDL-devel libcurl-devel libX11-devel
BuildRequires: libncurses-devel libgtk+2-devel libaio-devel
BuildRequires: python-devel ghostscript texi2html transfig
# for the docs
BuildRequires: perl(Pod/Man.pm) perl(Pod/Text.pm) texinfo graphviz
# so that the makefile knows to install udev rules
BuildRequires: udev
BuildRequires: %_includedir/gnu/stubs-32.h
# for the VMX "bios"
BuildRequires: dev86
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
# xsm policy file needs needs checkpolicy and m4
%{?_with_xsm:BuildRequires: checkpolicy m4}
%{?_with_hypervisor:Requires: %name-runtime = %version-%release}
%{?_enable_ocaml:BuildRequires: ocaml findlib}
# efi image needs an ld that has -mi386pep option
%{?_with_efi:BuildRequires: rpm-macros-uefi mingw64-binutils}

%description
This package contains the XenD daemon and xm command line tools, needed to manage
virtual machines running under the Xen hypervisor.


%package -n lib%name
Summary: Shared libraries for Xen tools
Group: System/Libraries
Provides: %name-libs = %version-%release
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
This package contains the runtime programs and daemons which form the core Xen
userspace environment.


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
Requires: lib%name = %version-%release
Requires: libuuid-devel

%description devel
This package contains what's needed to develop applications
which manage Xen virtual machines.


%package licenses
Summary: License files from Xen source
Group: Documentation
#BuildArch: noarch

%description licenses
This package contains the license files from the source used
to build the xen packages.


%if_enabled ocaml
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
%setup -q -a1 -a2
#ln -s ../qemu-upstream-%version tools/qemu-xen
#ln -s ../qemu-%name-%version tools/qemu-xen-traditional
%patch1 -p1
%patch4 -p1
%patch5 -p1

%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%{?_with_xsm:%patch20 -p1}
%{?_with_hypervisor:%patch21 -p1}
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1

%patch50 -p2
%patch51 -p1
%patch52 -p1

%patch100 -p1

sed -i '/^[[:blank:]]*\. \/etc\/rc\.status[[:blank:]]*$/s/\. /: # &/' tools/hotplug/Linux/init.d/xendomains

sed -i '/^EFI_VENDOR=/s/=.*$/=altlinux/' xen/Makefile

# stubdom sources
install -p -m 0644 %SOURCE10 %SOURCE11 %SOURCE12 %SOURCE13 %SOURCE14 %SOURCE15 %{?_enable_vtpm:%SOURCE16 %SOURCE17} stubdom/


%build
%{?_with_efi:install -d -m 0755 dist/install/boot/efi/efi/altlinux}
#export QEMU_REMOTE=$PWD/qemu-%name-%version
export CONFIG_QEMU=$PWD/qemu-%name-%version
export QEMU_UPSTREAM_URL=$PWD/qemu-upstream-%version
export XEN_VENDORVERSION="-%release"
export EXTRA_CFLAGS_XEN_TOOLS="%optflags"
export EXTRA_CFLAGS_QEMU_TRADITIONAL="%optflags"
export EXTRA_CFLAGS_QEMU_XEN="%optflags"
export WGET=$(which true)
export GIT=$(which true)
./configure \
	--prefix=%_prefix \
	--libdir=%_libdir \
	--enable-xen \
	%{subst_enable stubdom} \
%if_enabled vtpm
	--enable-vtpm-stubdom \
	--enable-vtpmmgr-stubdom \
%else
	--disable-vtpm-stubdom \
	--disable-vtpmmgr-stubdom \
%endif
%if_enabled ocaml
	--enable-ocamltools \
%else
	--disable-ocamltools \
%endif
	--enable-tools \
	--disable-kernels \
	--enable-docs
%make_build %{?_with_efi:LD_EFI=x86_64-pc-mingw32-ld}


%install
#export QEMU_REMOTE=$PWD/qemu-%name-%version
export CONFIG_QEMU=$PWD/qemu-%name-%version
export QEMU_UPSTREAM_URL=$PWD/qemu-upstream-%version
export XEN_VENDORVERSION="-%release"
export EXTRA_CFLAGS_XEN_TOOLS="%optflags"
export EXTRA_CFLAGS_QEMU_TRADITIONAL="%optflags"
export EXTRA_CFLAGS_QEMU_XEN="%optflags"
export WGET=$(which true)
export GIT=$(which true)
%{?_enable_ocaml:install -d -m 0755 %buildroot%_libdir/ocaml/stublibs}
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
rm -rf %buildroot/boot/xen-4.0.gz
rm -rf %buildroot/boot/xen-4.gz
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

# udev
#rm -rf %buildroot%_sysconfdir/udev/rules.d/%{name}*.rules
#mv %buildroot%_sysconfdir/udev/%{name}*.rules %buildroot%_sysconfdir/udev/rules.d/

# modules
install -pD -m 0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/modules/%name.modules

# logrotate
install -pD -m 0644 %SOURCE4 %buildroot%_logrotatedir/%name

# FIXME
install -pD -m 0755 %SOURCE48 %buildroot%_libexecdir/xendomains
sed -i '/^[[:blank:]]*\. \/etc\/rc\.status[[:blank:]]*$/s/\. /: # &/' %buildroot%_libexecdir/xendomains

# init scripts
#install -d -m 0755 %buildroot%_initddir
#mv %buildroot%_sysconfdir/init.d/* %buildroot%_initddir
#rmdir %buildroot%_sysconfdir/init.d
install -m 0755 %SOURCE20 %buildroot%_initddir/xenstored
install -m 0755 %SOURCE21 %buildroot%_initddir/xenconsoled
install -m 0755 %SOURCE22 %buildroot%_initddir/blktapctrl
install -m 0755 %SOURCE23 %buildroot%_initddir/xend
install -m 0755 %SOURCE24 %buildroot%_initddir/xendomains

# sysconfig
install -d -m 0755 %buildroot%_sysconfdir/sysconfig
install -p -m 0644 %SOURCE30 %buildroot%_sysconfdir/sysconfig/xenstored
install -p -m 0644 %SOURCE31 %buildroot%_sysconfdir/sysconfig/xenconsoled
install -p -m 0644 %SOURCE32 %buildroot%_sysconfdir/sysconfig/blktapctrl

# systemd
install -d -m 0755 %buildroot%_unitdir
install -p -m 0644 %SOURCE40 %buildroot%_unitdir/proc-xen.mount
install -p -m 0644 %SOURCE41 %buildroot%_unitdir/var-lib-xenstored.mount
install -p -m 0644 %SOURCE42 %buildroot%_unitdir/xenstored.service
install -p -m 0644 %SOURCE43 %buildroot%_unitdir/blktapctrl.service
install -p -m 0644 %SOURCE44 %buildroot%_unitdir/xend.service
install -p -m 0644 %SOURCE45 %buildroot%_unitdir/xenconsoled.service
install -p -m 0644 %SOURCE46 %buildroot%_unitdir/xen-watchdog.service
install -p -m 0644 %SOURCE47 %buildroot%_unitdir/xendomains.service
%{?_enable_ocaml:install -p -m 0644 %SOURCE50 %buildroot%_unitdir/oxenstored.service}

install -pD -m 0644 %SOURCE49 %buildroot/lib/tmpfiles.d/xen.conf

# config file only used for hotplug, Fedora uses udev instead
rm -f %buildroot/%_sysconfdir/sysconfig/xend

############ create dirs in /var ############
install -d -m 0755 %buildroot%_localstatedir/lib/%name/{xend-db/{domain,vnet,migrate},images}
install -d -m 0755 %buildroot%_logdir/%name/console

############ create symlink for x86_64 for compatibility with 3.4 ############
%if "%_libdir" != "/usr/lib"
ln -s {/usr/lib,%buildroot%_libdir}/%name/bin/qemu-dm
%endif

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

############ all done now ############

%ifdef brp_strip_none
%brp_strip_none %_datadir/xen/qemu/* %_datadir/qemu-xen/qemu/*
%else
%add_strip_skiplist %_datadir/xen/qemu/* %_datadir/qemu-xen/qemu/*
%endif
%add_verify_elf_skiplist %_datadir/xen/qemu/openbios-* /boot/*
# FIXME
#add_findreq_skiplist %_initddir/*


%post
%post_service xend
%post_service xendomains

%preun
%preun_service xend
%preun_service xendomains


%post runtime
%post_service xenconsoled
%post_service xenstored


%preun runtime
%preun_service xenconsoled
%preun_service xenstored


%if_enabled ocaml
%post ocaml
%post_service oxenstored

%preun ocaml
%preun_service oxenstored
%endif


%files
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/COPYING
%doc %_docdir/%name-%version/README
%_bindir/xencons
%_sbindir/xend
%_sbindir/xm
%python_sitelibdir/%name
%python_sitelibdir/xen-*.egg-info
%_man1dir/xm.*
%_man5dir/xend-config.sxp.*
%_man5dir/xmdomain.cfg.*
%dir %_datadir/%name
%_datadir/%name/create.dtd

# Startup script
%_initddir/xend
%_initddir/xendomains
%dir %attr(0700,root,root) %_sysconfdir/%name
# Guest config files
%config(noreplace) %_sysconfdir/%name/xmexample*
# Daemon config
%config(noreplace) %_sysconfdir/%name/xend-*
# xm config
%config(noreplace) %_sysconfdir/%name/xm-*
# Guest autostart links
%dir %attr(0700,root,root) %_sysconfdir/%name/auto
# Autostart of guests
%config(noreplace) %_sysconfdir/sysconfig/xendomains

%_unitdir/xend.service
%_unitdir/xendomains.service
%_libexecdir/xendomains

%dir %_localstatedir/lib/%name
# Persistent state for XenD
%dir %_localstatedir/lib/%name/xend-db/
%dir %_localstatedir/lib/%name/xend-db/domain
%dir %_localstatedir/lib/%name/xend-db/migrate
%dir %_localstatedir/lib/%name/xend-db/vnet


%files -n lib%name
%_libdir/*.so.*
%_libdir/fs


# All runtime stuff except for XenD/xm python stuff
%files runtime
# Hotplug rules
%config(noreplace) %_sysconfdir/udev/rules.d/*

%dir %attr(0700,root,root) %_sysconfdir/%name
%dir %attr(0700,root,root) %_sysconfdir/%name/scripts/
%config %attr(0700,root,root) %_sysconfdir/%name/scripts/*

%_initddir/blktapctrl
%_initddir/xenstored
%_initddir/xenconsoled
%_initddir/xen-watchdog
%_initddir/xencommons

%_sysconfdir/bash_completion.d

%_unitdir/proc-xen.mount
%_unitdir/var-lib-xenstored.mount
%_unitdir/xenstored.service
%_unitdir/blktapctrl.service
%_unitdir/xenconsoled.service
%_unitdir/%name-watchdog.service
/lib/tmpfiles.d/%name.conf

%config(noreplace) %_sysconfdir/sysconfig/xenstored
%config(noreplace) %_sysconfdir/sysconfig/xenconsoled
%config(noreplace) %_sysconfdir/sysconfig/blktapctrl
%config(noreplace) %_sysconfdir/sysconfig/xencommons
%config(noreplace) %_sysconfdir/%name/xl.conf
%config(noreplace) %_sysconfdir/%name/cpupool
%config(noreplace) %_sysconfdir/%name/xlexample*

# Auto-load xen backend drivers
%attr(0755,root,root) %_sysconfdir/sysconfig/modules

# Rotate console log files
%config(noreplace) %_sysconfdir/logrotate.d/%name

# Programs run by other programs
%dir %_libdir/%name
%dir %_libdir/%name/bin
%attr(0700,root,root) %_libdir/%name/bin/*
%if_enabled stubdom
%dir %_datadir/%name
# QEMU runtime files
%dir %_datadir/%name/qemu
%_datadir/%name/qemu/keymaps
%endif

# man pages
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
# Avoid owning /usr/lib twice on x86
%if "%_libdir" != "/usr/lib"
%dir /usr/lib/%name
%dir /usr/lib/%name/bin
/usr/lib/%name/bin/stubdom-dm
/usr/lib/%name/bin/qemu-dm
/usr/lib/%name/bin/stubdompath.sh
/usr/lib/%name/bin/xenpaging
%endif
%dir /usr/lib/%name/boot
# HVM loader is always in /usr/lib regardless of multilib
/usr/lib/xen/boot/hvmloader
/usr/lib/xen/boot/ioemu-stubdom.gz
/usr/lib/xen/boot/xenstore-stubdom.gz
/usr/lib/xen/boot/pv-grub*.gz
%{?_enable_vtpm:/usr/lib/xen/boot/vtpm*.gz}
%endif
# General Xen state
%dir %_localstatedir/lib/%name
%dir %_localstatedir/lib/%name/dump
%dir %_localstatedir/lib/%name/images
# Xenstore persistent state
%dir %_localstatedir/lib/xenstored
# Xenstore runtime state
%ghost %_localstatedir/run/xenstored
# XenD runtime state
%ghost %attr(0700,root,root) %dir %_runtimedir/xend
%ghost %attr(0700,root,root) %_runtimedir/xend/boot

%_sbindir/*
%{?_enable_ocaml:%exclude %_sbindir/oxenstored}
%exclude %_sbindir/xend
%exclude %_sbindir/xm
%_bindir/*
%exclude %_bindir/xencons

# Xen logfiles
%dir %attr(0700,root,root) %_localstatedir/log/xen
# Guest/HV console logs
%dir %attr(0700,root,root) %_localstatedir/log/xen/console


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
%_libdir/*.so


%files licenses
%dir %_docdir/%name-%version
%_docdir/%name-%version/licenses


%if_enabled ocaml
%files ocaml
%_libdir/ocaml/site-lib/%{name}*
%exclude %_libdir/ocaml/site-lib/%{name}*/*.a
%exclude %_libdir/ocaml/site-lib/%{name}*/*.cmxa
%exclude %_libdir/ocaml/site-lib/%{name}*/*.cmx
%_sbindir/oxenstored
%config(noreplace) %_sysconfdir/%name/oxenstored.conf
%_unitdir/oxenstored.service


%files ocaml-devel
%_libdir/ocaml/site-lib/%{name}*/*.a
%_libdir/ocaml/site-lib/%{name}*/*.cmxa
%_libdir/ocaml/site-lib/%{name}*/*.cmx
%endif


%changelog
* Sat Feb 08 2014 Led <led@altlinux.ru> 4.3.1-alt1
- 4.3.1
- based on Fedora spec 4.3.1-6
- fixed URL
- enabled ocaml

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
