%def_with efi
%def_enable xsmpolicy
%def_enable vtpm
%def_enable ocamltools
%def_enable monitors
%def_enable xenapi

%ifndef x86_64
%define x86_64 x86_64
%endif

Summary: Xen is a virtual machine monitor (hypervisor)
Name: xen
Version: 4.10.0
Release: alt3%ubt
Group: Emulators
License: GPLv2+, LGPLv2+, BSD
URL: http://www.xenproject.org/

%define pre %nil
%define qemu_ver %version%pre

Source0: %name-%version%pre.tar
Source1: qemu-xen-%qemu_ver.tar
Source2: qemu-xen-traditional-%qemu_ver.tar
Source3: mini-os-%version%pre.tar
Source4: %name.logrotate
Source5: %name-qemu-dom0

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

Patch0: %name-%version-upstream.patch
Patch1: %name-%version-alt.patch

# Fedora
Patch5: %name-net-disable-iptables-on-bridge.patch

Patch10: pygrubfix.patch
Patch15: %name.use.fedora.ipxe.patch
Patch17: %name.fedora.efi.build.patch
Patch19: %name.pygrubtitlefix.patch
Patch21: %name.64.bit.hyp.on.ix86.patch

# ALT
Patch50: %name-4.0.0-libfsimage-soname-alt.patch
Patch55: qemu-traditional-lost-parenthesis.patch


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
%def_without efi
%endif

# no point in trying to build xsm on ix86 without a hypervisor
%if_without hypervisor
%def_disable xsmpolicy
%endif

%ifarch %ix86 %x86_64
%def_enable stubdom
%else
%def_disable stubdom
%endif

BuildRequires(pre): rpm-build-ubt

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
%{?_enable_ocamltools:BuildRequires: ocaml ocaml-ocamlbuild ocaml-ocamldoc ocaml-findlib}
%{?_enable_xenapi:BuildRequires: libxml2-devel}
BuildRequires: %_includedir/gnu/stubs-32.h
# for the VMX "bios"
BuildRequires: dev86
BuildRequires: libSDL-devel libXext-devel
# xsm policy file needs needs checkpolicy and m4
%{?_enable_xsmpolicy:BuildRequires: checkpolicy m4}
# efi image needs an ld that has -mi386pep option
%{?_with_efi:BuildRequires: mingw64-binutils >= 2.26}
%{?_enable_stubdom:BuildRequires: makeinfo}
# with hypervisor
BuildRequires: flex discount libfdt-devel libgcrypt-devel liblzo2-devel libvde-devel perl-HTML-Parser perl-devel
# from 4.7.0
BuildRequires: libnl-devel >= 3.2.8 libnl3 >= 3.2.8 libnl3-utils >= 3.2.8
BuildRequires: libpixman-devel >= 0.21.8 libpixman >= 0.21.8
BuildRequires: libnettle-devel nettle
BuildRequires: gcc-c++
BuildRequires: libsystemd-devel >= 209
# VirtFS support
BuildRequires: libcap-devel libattr-devel
# Qemu-Xen VNC-PNGm VNC-JPEG support
BuildRequires: libpng-devel libjpeg-devel
%{?_enable_vtpm:BuildRequires: cmake}

%description
The Xen Project hypervisor is an open-source type-1 or baremetal
hypervisor, which makes it possible to run many instances of an
operating system or indeed different operating systems in parallel on a
single machine (or host). The Xen Project hypervisor is the only type-1
hypervisor that is available as open source. It is used as the basis for
a number of different commercial and open source applications, such as:
server virtualization, Infrastructure as a Service (IaaS),
desktop virtualization, security applications, embedded and hardware
appliances. The Xen Project hypervisor is powering the largest clouds in
production today.

This package contains the command line tools, needed to manage virtual
machines running under the Xen hypervisor.

%filter_from_requires /^\s*\(open-iscsi\|nbd-client\|drbd-utils\)\s*$/d


%package -n lib%name
Summary: Shared libraries for Xen tools
Group: System/Libraries
Provides: %name-libs = %version-%release
Obsoletes: %name-libs
Requires: xen-licenses

%description -n lib%name
The Xen Project hypervisor is an open-source type-1 or baremetal
hypervisor, which makes it possible to run many instances of an
operating system or indeed different operating systems in parallel on a
single machine (or host).

This package contains the libraries needed to run applications
which manage Xen virtual machines.


%package -n lib%name-devel
Summary: Development libraries for Xen tools
Group: Development/C
Provides: %name-devel = %version-%release
Obsoletes: %name-devel
Requires: lib%name = %version-%release
Requires: libuuid-devel

%description -n lib%name-devel
The Xen Project hypervisor is an open-source type-1 or baremetal
hypervisor, which makes it possible to run many instances of an
operating system or indeed different operating systems in parallel on a
single machine (or host).

This package contains what's needed to develop applications
which manage Xen virtual machines.


%package runtime
Summary: Core Xen runtime environment
Group: Emulators
Requires: %name = %version-%release
Requires: %name-runtime-common = %version-%release
Requires: lib%name = %version-%release
Requires: seabios ipxe-roms-qemu

%description runtime
The Xen Project hypervisor is an open-source type-1 or baremetal
hypervisor, which makes it possible to run many instances of an
operating system or indeed different operating systems in parallel on a
single machine (or host).

This package contains the runtime programs which form the core Xen
userspace environment.


%package runtime-common
Summary: Core Xen runtime environment
Group: Emulators
BuildArch: noarch

%description runtime-common
The Xen Project hypervisor is an open-source type-1 or baremetal
hypervisor, which makes it possible to run many instances of an
operating system or indeed different operating systems in parallel on a
single machine (or host).

This package contains the runtime programs which form the core Xen
userspace environment.


%if_with hypervisor
%package hypervisor
Summary: Xen hypervisor
Group: System/Kernel and hardware
Requires: xen-licenses

%description hypervisor
The Xen Project hypervisor is an open-source type-1 or baremetal
hypervisor, which makes it possible to run many instances of an
operating system or indeed different operating systems in parallel on a
single machine (or host).

This package contains the Xen hypervisor.
%endif


%package doc
Summary: Xen documentation
Group: Documentation
BuildArch: noarch
Requires: xen-licenses

%description doc
The Xen Project hypervisor is an open-source type-1 or baremetal
hypervisor, which makes it possible to run many instances of an
operating system or indeed different operating systems in parallel on a
single machine (or host). The Xen Project hypervisor is the only type-1
hypervisor that is available as open source. It is used as the basis for
a number of different commercial and open source applications, such as:
server virtualization, Infrastructure as a Service (IaaS),
desktop virtualization, security applications, embedded and hardware
appliances. The Xen Project hypervisor is powering the largest clouds in
production today.

This package contains the Xen documentation.


%package licenses
Summary: License files from Xen source
Group: Documentation
BuildArch: noarch

%description licenses
The Xen Project hypervisor is an open-source type-1 or baremetal
hypervisor, which makes it possible to run many instances of an
operating system or indeed different operating systems in parallel on a
single machine (or host).

This package contains the license files from the source used
to build the xen packages.


%if_enabled ocamltools
%package ocaml
Summary: Ocaml libraries for Xen tools
Group: Emulators
Requires: ocaml-runtime, lib%name = %version-%release

%description ocaml
The Xen Project hypervisor is an open-source type-1 or baremetal
hypervisor, which makes it possible to run many instances of an
operating system or indeed different operating systems in parallel on a
single machine (or host).

This package contains libraries for ocaml tools to manage Xen
virtual machines.


%package ocaml-devel
Summary: Ocaml development libraries for Xen tools
Group: Development/Other
Requires: %name-ocaml = %version-%release

%description ocaml-devel
The Xen Project hypervisor is an open-source type-1 or baremetal
hypervisor, which makes it possible to run many instances of an
operating system or indeed different operating systems in parallel on a
single machine (or host).

This package contains libraries for developing ocaml tools to
manage Xen virtual machines.
%endif


%ifarch %ix86 %x86_64
%package stubdoms
Summary: Xen Hypervisor Stub Domains
Group: Emulators

%description stubdoms
The Xen Project hypervisor is an open-source type-1 or baremetal
hypervisor, which makes it possible to run many instances of an
operating system or indeed different operating systems in parallel on a
single machine (or host).

Stubdoms (or stub domains) are lightweight 'service' or 'driver' domain
to run device models and one technique to implement Dom0 Disaggregation.
The initial purpose of stub domains were to offload qemu workloads from
dom0 into a seperate domain.

So with stub domains, a separate unprivileged stub domain is created per
HVM guest. This boosts performance and makes your system more secure.
%endif


%prep
%setup -q -n %name-%version%pre -a1 -a2 -a3

mkdir extras
ln -s ../qemu-xen-%version tools/qemu-xen
ln -s ../qemu-xen-traditional-%version tools/qemu-xen-traditional
ln -s ../mini-os-%version extras/mini-os

%patch0 -p1
%patch1 -p1
%patch5 -p1
%patch10 -p1
%patch15 -p1
%patch17 -p1
#-%-patch18 -p1
%patch19 -p1
%{?_with_hypervisor:%patch21 -p1}
%patch50 -p2

pushd tools/qemu-xen-traditional
%patch55 -p1
popd

sed -i '/^[[:blank:]]*\. \/etc\/rc\.status[[:blank:]]*$/s/\. /: # &/' tools/hotplug/Linux/xendomains.in

# stubdoms sources
pushd stubdom
ln -s %SOURCE10
ln -s %SOURCE11
ln -s %SOURCE12
ln -s %SOURCE13
ln -s %SOURCE14
ln -s %SOURCE15

%if_enabled vtpm
ln -s %SOURCE16
ln -s %SOURCE17
%endif
popd

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
	%{subst_enable xsmpolicy} \
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
	--enable-kvm \
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

%if_enabled xsmpolicy
# policy file should be in /boot/flask
install -d -m 0755 %buildroot/boot/flask
mv %buildroot/boot/xenpolicy* %buildroot/boot/flask/
%endif

############ kill unwanted stuff ############

# hypervisor symlinks
%{!?_with_hypervisor:rm -rf %buildroot/boot}

# silly doc dir fun
mv %buildroot%_docdir/%name{,-%version}
install -p -m 0644 COPYING README %buildroot%_docdir/%name-%version/
mv %buildroot%_docdir/%name-%version/{html/,}misc

# README's not intended for end users
rm -f %buildroot/%_sysconfdir/%name/README*

# adhere to Static Library Packaging Guidelines
rm -f %buildroot%_libdir/*.a

############ fixup files in /etc ############

# logrotate
install -pD -m 0644 %SOURCE4 %buildroot%_logrotatedir/%name
install -pD -m 0644 %SOURCE49 %buildroot%_tmpfilesdir/%name.conf

############ create dirs in /var ############
#install -d -m 0700 %buildroot%_localstatedir/%name/save
install -d -m 0700 %buildroot%_localstatedir/xenstored
#install -d -m 0700 %buildroot%_logdir/%name/console

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
rm -fr %buildroot%_docdir/%name-%version/licenses/stubdom/lwip-x86_32
rm -fr %buildroot%_docdir/%name-%version/licenses/stubdom/polarssl-x86_32

mv %buildroot%_docdir/%name-%version/licenses/stubdom/lwip-x86_64 %buildroot%_docdir/%name-%version/licenses/stubdom/lwip
mv %buildroot%_docdir/%name-%version/licenses/stubdom/polarssl-x86_64 %buildroot%_docdir/%name-%version/licenses/stubdom/polarssl
mv %buildroot%_docdir/%name-%version/licenses/stubdom/gmp-x86_64 %buildroot%_docdir/%name-%version/licenses/stubdom/gmp
%endif

%ifarch %ix86
mv %buildroot%_docdir/%name-%version/licenses/stubdom/lwip-x86_32 %buildroot%_docdir/%name-%version/licenses/stubdom/lwip
mv %buildroot%_docdir/%name-%version/licenses/stubdom/polarssl-x86_32 %buildroot%_docdir/%name-%version/licenses/stubdom/polarssl
mv %buildroot%_docdir/%name-%version/licenses/stubdom/gmp-x86_32 %buildroot%_docdir/%name-%version/licenses/stubdom/gmp
%endif

install -pD -m 0755 %SOURCE5 %buildroot%_initddir/%name-qemu-dom0
mv %buildroot%_unitdir/%name-qemu-dom0-disk-backend.service %buildroot%_unitdir/%name-qemu-dom0.service

############ all done now ############

%ifdef brp_strip_none
%brp_strip_none %_datadir/%name/qemu/* %_datadir/qemu-%name/qemu/*
%else
%add_strip_skiplist %_datadir/%name/qemu/* %_datadir/qemu-%name/qemu/*
%endif

%add_verify_elf_skiplist %_datadir/%name/qemu/openbios-* %_datadir/qemu-%name/qemu/* /boot/*


%post
%post_service xen-watchdog
%post_service xencommons
%post_service xendomains
%post_service xendriverdomain


%preun
%preun_service xendriverdomain
%preun_service xendomains
%preun_service xencommons
%preun_service xen-watchdog


%files
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

%_sysconfdir/bash_completion.d

# Rotate console log files
%config(noreplace) %_sysconfdir/logrotate.d/%name

%dir /lib/systemd
%dir %_unitdir

%_unitdir/proc-xen.mount
%_unitdir/var-lib-xenstored.mount

%_unitdir/xen-init-dom0.service
%_unitdir/xen-watchdog.service
%_unitdir/xenconsoled.service
%_unitdir/xendomains.service
%_unitdir/xenstored.service
%_unitdir/xendriverdomain.service

%_tmpfilesdir/xen.conf

%dir %_libexecdir/%name
%dir %_libexecdir/%name/bin
%_libexecdir/%name/bin/init-xenstore-domain
%_libexecdir/%name/bin/libxl-save-helper
%_libexecdir/%name/bin/lsevtchn
%_libexecdir/%name/bin/readnotes

%_libexecdir/%name/bin/xen-init-dom0
%_libexecdir/%name/bin/xenconsole
%_libexecdir/%name/bin/xendomains
%_libexecdir/%name/bin/xenctx
%_libexecdir/%name/bin/xenpaging
%_libexecdir/%name/bin/xenpvnetboot

%_bindir/qemu-img-xen
%_bindir/qemu-nbd-xen
%_bindir/xen-cpuid
%_bindir/xen-detect
%_bindir/xenalyze
%_bindir/xencov_split
%_bindir/xenstore
%_bindir/xenstore-chmod
%_bindir/xenstore-control
%_bindir/xenstore-exists
%_bindir/xenstore-list
%_bindir/xenstore-ls
%_bindir/xenstore-read
%_bindir/xenstore-rm
%_bindir/xenstore-watch
%_bindir/xenstore-write
%_bindir/xentrace_format

%_sbindir/flask-get-bool
%_sbindir/flask-getenforce
%_sbindir/flask-label-pci
%_sbindir/flask-loadpolicy
%_sbindir/flask-set-bool
%_sbindir/flask-setenforce
%_sbindir/gdbsx
%_sbindir/kdd
%_sbindir/xen-diag
%_sbindir/xen-hptool
%_sbindir/xen-hvmcrash
%_sbindir/xen-hvmctx
%_sbindir/xen-livepatch
%_sbindir/xen-lowmemd
%_sbindir/xen-mfndump
%_sbindir/xen-ringwatch
%_sbindir/xen-tmem-list-parse
%_sbindir/xenbaked
%_sbindir/xenconsoled
%_sbindir/xencov
%_sbindir/xenlockprof
%_sbindir/xenmon.py
%_sbindir/xenperf
%_sbindir/xenpm
%_sbindir/xenpmd
%_sbindir/xenstored
%_sbindir/xentop
%_sbindir/xentrace
%_sbindir/xentrace_setmask
%_sbindir/xentrace_setsize
%_sbindir/xenwatchdogd
%_sbindir/xl

# man pages
%_man1dir/xenstore*
%_man1dir/xentop.*
%_man1dir/xentrace_format.*
%_man1dir/xl.*
%_man5dir/xl.cfg.*
%_man5dir/xl.conf.*
%_man5dir/xlcpupool.cfg.*
%_man5dir/xl-disk-configuration.*
%_man5dir/xl-network-configuration.5.xz
%_man7dir/xen-pci-device-reservations.*
%_man7dir/xen-pv-channel.7.xz
%_man7dir/xen-tscmode.*
%_man7dir/xen-vtpm.*
%_man7dir/xen-vtpmmgr.*
%_man8dir/xentrace.*
%_man7dir/xl-numa-placement.7.xz


# Xen logfiles
%dir %attr(0700,root,root) %_localstatedir/xen
%dir %attr(0700,root,root) %_localstatedir/xenstored
%dir %attr(0700,root,root) %_logdir/xen


%files -n lib%name
%_libdir/*.so.*
%_libdir/fs


%files -n lib%name-devel
%_libdir/*.so

%_includedir/*.h
%_includedir/%name
%_includedir/%{name}store-compat

%_datadir/pkgconfig/xen*.pc
%_datadir/pkgconfig/xlutil.pc


%post runtime
%post_service xen-qemu-dom0


%preun runtime
%preun_service xen-qemu-dom0


%files runtime
%_bindir/pygrub
%_bindir/xencons

%_initddir/%name-qemu-dom0

%dir /lib/systemd
%dir %_unitdir
%_unitdir/xen-qemu-dom0.service

%dir %_libexecdir/%name
%dir %_libexecdir/%name/bin
%dir %_libexecdir/%name/boot
%_libexecdir/%name/bin/ivshmem-client
%_libexecdir/%name/bin/ivshmem-server
%_libexecdir/%name/bin/qemu-dm
%_libexecdir/%name/bin/qemu-img
%_libexecdir/%name/bin/qemu-io
%_libexecdir/%name/bin/qemu-nbd
%_libexecdir/%name/bin/qemu-system-i386
%_libexecdir/%name/bin/virtfs-proxy-helper
%_libexecdir/%name/boot/hvmloader

%dir %_libexecdir/%name/libexec
%_libexecdir/%name/libexec/qemu-bridge-helper

%python_sitelibdir/%name
%python_sitelibdir/xen-*.egg-info
%python_sitelibdir/grub
%python_sitelibdir/pygrub-*.egg-info
%python_sitelibdir/fsimage.so

%attr(0700,root,root) %_logdir/%name


%files runtime-common
%_sbindir/xen-bugtool

%dir %_libexecdir/%name/bin
%_libexecdir/%name/bin/pygrub
%_libexecdir/%name/bin/convert-legacy-stream
%_libexecdir/%name/bin/verify-stream-v2

%_datadir/%name
%_datadir/qemu-%name

%exclude %_datadir/qemu-%name/qemu/s390-ccw.img
%exclude %_datadir/qemu-%name/qemu/s390-netboot.img

%if_with hypervisor
%files hypervisor
/boot/xen*
%{?_enable_xsmpolicy:/boot/flask}
%{?_with_efi:%_efi_bindir}
%{?_with_efi:%_efi_bootdir}
%endif


%files doc
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/misc
%doc %_docdir/%name-%version/html
%doc %_docdir/%name-%version/README


%files licenses
%dir %_docdir/%name-%version
%doc %_docdir/%name-%version/licenses
%doc %_docdir/%name-%version/COPYING


%if_enabled ocamltools
%files ocaml
%_libdir/ocaml/%{name}*
%_libdir/ocaml/stublibs/*
%exclude %_libdir/ocaml/%{name}*/*.cmxa
%exclude %_libdir/ocaml/%{name}*/*.cmx

%_sbindir/oxenstored

%dir %attr(0700,root,root) %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/oxenstored.conf


%files ocaml-devel
%_libdir/ocaml/%{name}*/*.cmxa
%_libdir/ocaml/%{name}*/*.cmx
%endif


%ifarch %ix86 %x86_64
%files stubdoms
%dir %_libexecdir/%name
%dir %_libexecdir/%name/bin
%dir %_libexecdir/%name/boot

%_libexecdir/%name/bin/stubdom-dm
%_libexecdir/%name/bin/stubdompath.sh

%_libexecdir/%name/boot/ioemu-stubdom.gz
%_libexecdir/%name/boot/pv-grub-x86_*.gz
%_libexecdir/%name/boot/xenstore-stubdom.gz

%{?_enable_vtpm:%_libexecdir/%name/boot/vtpm*.gz}
%endif


%changelog
* Thu Jan 11 2018 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.10.0-alt3%ubt
- upstream updates:
  + x86/msr: Free msr_vcpu_policy during vcpu destruction (thx Andrew Cooper).
  + x86/vmx: Don't use hvm_inject_hw_exception() in
    long_mode_do_msr_write() (thx Andrew Cooper).
  + xen/efi: Fix build with clang-5.0 (thx Andrew Cooper).
  + gnttab: improve GNTTABOP_cache_flush locking (thx Jan Beulich).
  + gnttab: correct GNTTABOP_cache_flush empty batch handling (thx Jan Beulich).
  + x86/microcode: Add support for fam17h microcode loading (thx Tom Lendacky).
  + x86/mm: drop bogus paging mode assertion (thx Jan Beulich).
  + x86/mb2: avoid Xen image when looking for module/crashkernel
    position (thx Daniel Kiper).
  + x86/vvmx: don't enable vmcs shadowing for nested guests (thx Sergey Dyasli).
  + xen/pv: Construct d0v0's GDT properly (thx Andrew Cooper).
  + update Xen version to 4.10.1-pre (thx Jan Beulich).
  + migration, xen: Fix block image lock issue on live migration (thx Anthony PERARD).

* Tue Jan 02 2018 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.10.0-alt2%ubt
- fix gear rules: previous (4.10.0-alt2.S1) build was actually 4.8.2-alt2.S1
- 4.10.0 release

* Sat Dec 30 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.10.0-alt1%ubt
- 4.10.0 release

* Sat Dec 09 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.8.2-alt2%ubt
- upstream updates:
  + p2m: Check return value of p2m_set_entry() when decreasing reservation (thx George Dunlap) (XSA-247).
  + p2m: Always check to see if removing a p2m entry actually worked (thx George Dunlap). (XSA-247)
  + x86/pod: prevent infinite loop when shattering large pages (thx Julien Grall). (XSA-246)
  + x86/shadow: correct SH_LINEAR mapping detection in sh_guess_wrmap() (thx Andrew Cooper). (XSA-243)
  + x86: don't wrongly trigger linear page table assertion (thx Jan Beulich). (XSA-240)
  + x86/mm: fix race condition in modify_xen_mappings() (thx Yu Zhang).
  + x86/mm: fix race conditions in map_pages_to_xen() (thx Min He).
  + x86/hvm: do not register hpet mmio during s3 cycle (thx Eric Chanudet).
  + x86/mm: Make PV linear pagetables optional (thx George Dunlap).
  + x86: fix asm() constraint for GS selector update (thx Jan Beulich).
  + x86: don't latch wrong (stale) GS base addresses (thx Jan Beulich).
  + x86: also show FS/GS base addresses when dumping registers (thx Jan Beulich).
  + x86: fix GS-base-dirty determination (thx Jan Beulich).
  + ui/gtk: Fix deprecation of vte_terminal_copy_clipboard (thx Anthony PERARD).
  + xen/pt: allow QEMU to request MSI unmasking at bind time (thx Roger Pau Monne).

* Sun Oct 29 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.8.2-alt1%ubt
- 4.8.2 release
- upstream updates:
  + x86emul: handle address wrapping (thx Jan Beulich).
  + VMX: PLATFORM_INFO MSR is r/o (thx Jan Beulich).
  + x86: avoid #GP for PV guest MSR accesses (thx Jan Beulich).
  + x86/vvmx: Fix WRMSR interception of VMX MSRs (thx Andrew Cooper).
  + x86: fix do_update_va_mapping_otherdomain() wrt translated
    domains (thx Jan Beulich).
  + x86: request page table page-in for the correct domain (thx Jan Beulich).
  + xen/domctl: Fix Xen heap leak via XEN_DOMCTL_getvcpucontext (thx Andrew Cooper).
  + x86/PV: fix/generalize guest nul selector handling (thx Jan Beulich).
  + x86/msr: Correct the definition of MSR_IA32_APICBASE_BASE (thx Andrew Cooper).
  + x86/svm: Fix a livelock when trying to run shadowed unpaged
    guests (thx Andrew Cooper).
  + gnttab: fix pin count / page reference race (thx Jan Beulich).
  + tools/libxc/xc_dom_arm: add missing variable initialization (thx Bernd Kuhls).
  + x86/cpu: Fix IST handling during PCPU bringup (thx Andrew Cooper).
  + x86/shadow: Don't create self-linear shadow mappings for 4-level
    translated guests (thx Andrew Cooper).
  + x86: don't allow page_unlock() to drop the last type reference (thx Jan Beulich).
  + x86: don't store possibly stale TLB flush time stamp (thx Jan Beulich).
  + x86: limit linear page table use to a single level (thx Jan Beulich).
  + x86/HVM: prefill partially used variable on emulation paths (thx Jan Beulich).
  + x86/ioreq server: correctly handle bogus
    XEN_DMOP_{,un}map_io_range_to_ioreq_server arguments (thx Vitaly Kuznetsov).
  + x86/FLASK: fix unmap-domain-IRQ XSM hook (thx Jan Beulich).
  + x86/IRQ: conditionally preserve irq <-> pirq mapping on map
    error paths (thx Jan Beulich).
  + x86/MSI: disallow redundant enabling (thx Jan Beulich).
  + x86: enforce proper privilege when (un)mapping pIRQ-s (thx Jan Beulich).
  + x86: don't allow MSI pIRQ mapping on unowned device (thx Jan Beulich).
  + xen/arm: p2m: Read *_mapped_gfn with the p2m lock taken (thx Julien Grall).
  + xen/arm: Fix the issue in cmp_mmio_handler used in
    find_mmio_handler (thx Bhupinder Thakur).
  + xen/arm: Correctly report the memory region in the dummy
    NUMA helpers (thx Julien Grall).
  + xen/page_alloc: Cover memory unreserved after boot in
    first_valid_mfn (thx Julien Grall).
  + x86: introduce and use setup_force_cpu_cap() (thx Jan Beulich).
  + x86/emul: Fix the handling of unimplemented Grp7 instructions (thx Andrew Cooper).
  + VT-d: use correct BDF for VF to search VT-d unit (thx Chao Gao).
  + hvmloader: use base instead of pci_mem_start for find_next_rmrr() (thx Xiong Zhang).
  + x86/efi: don't write relocations in efi_arch_relocate_image()
    first pass (thx David Woodhouse).
  + x86: check for allocation errors in modify_xen_mappings() (thx Jan Beulich).
  + vga: stop passing pointers to vga_draw_line* functions (thx Gerd Hoffmann).
  + gnttab: also validate PTE permissions upon destroy/replace (thx Jan Beulich).
  + tools/xenstore: dont unlink connection object twice (thx Juergen Gross).
  + grant_table: fix GNTTABOP_cache_flush handling (thx Andrew Cooper).
  + xen/mm: make sure node is less than MAX_NUMNODES (thx George Dunlap).

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 4.8.1-alt10%ubt
- rebuild with ocaml 4.04.2

* Fri Jun 23 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.8.1-alt9%ubt
- Upstream updates:
 + xen/test/Makefile: Fix clean target, broken by pattern rule (thx Ian Jackson).
 + x86: avoid leaking PKRU and BND* between vCPU-s (thx Jan Beulich). XSA-220
 + xen/arm: vgic: Sanitize target mask used to send SGI (thx Julien Grall).
 + gnttab: __gnttab_unmap_common_complete() is all-or-nothing (thx Jan Beulich). XSA-224
 + gnttab: correct logic to get page references during map requests (thx George Dunlap). XSA-224
 + gnttab: never create host mapping unless asked to (thx Jan Beulich). XSA-224
 + gnttab: fix handling of dev_bus_addr during unmap (thx George Dunlap). XSA-224
 + arm: vgic: Don't update the LR when the IRQ is not enabled (thx Julien Grall). XSA-223
 + guest_physmap_remove_page() needs its return value checked (thx Jan Beulich). XSA-222
 + memory: fix return value handing of guest_remove_page() (thx Andrew Cooper). XSA-222
 + evtchn: avoid NULL derefs (thx Jan Beulich). XSA-221
 + x86/shadow: hold references for the duration of emulated writes (thx Andrew Cooper). XSA-219
 + gnttab: correct maptrack table accesses (thx Jan Beulich). XSA-218
 + gnttab: Avoid potential double-put of maptrack entry (thx George Dunlap). XSA-218
 + gnttab: fix unmap pin accounting race (thx Jan Beulich). XSA-218
 + x86/mm: disallow page stealing from HVM domains (thx Jan Beulich). XSA-217
 + Makefile: Provide way to ship livepatch test files (thx Ian Jackson).
 + xen/test/livepatch: Add xen_nop.livepatch to .gitignore (thx Ian Jackson).
 + xen/test/livepatch: Regularise Makefiles (thx Ian Jackson).
 + xen/test/livepatch/Makefile: Install in
   DESTDIR/usr/lib/debug/xen-livepatch (thx Ian Jackson).
 + xen/arm: p2m: Fix incorrect mapping of superpages (thx Julien Grall).
 + vgic: refuse irq migration when one is already in progress (thx Stefano Stabellini).
 + arm: remove irq from inflight, then change physical affinity (thx Stefano Stabellini).
 + xen/arm: Survive unknown traps from guests (thx Julien Grall).
 + xen/arm: do_trap_hypervisor: Separate hypervisor and guest traps (thx Julien Grall).
 + xen/arm: Save ESR_EL2 to avoid using mismatched value in syndrome
   check (thx Wei Chen).
 + stop_machine: fill fn_result only in case of error (thx Gregory Herrero).
 + hvmloader: avoid tests when they would clobber used memory (thx Jan Beulich).
 + arm: fix build with gcc 7 (thx Jan Beulich).
 + x86: fix build with gcc 7 (thx Jan Beulich).
 + x86/mm: fix incorrect unmapping of 2MB and 1GB pages (thx Igor Druzhinin).
 + x86/pv: Align %%rsp before pushing the failsafe stack frame (thx Andrew Cooper).
 + x86/pv: Fix bugs with the handling of int80_bounce (thx Andrew Cooper).
 + x86/vpmu_intel: fix hypervisor crash by masking PC bit in
   MSR_P6_EVNTSEL (thx Mohit Gambhir).
 + hvm: fix hypervisor crash in hvm_save_one() (thx Jan Beulich).
 + x86/32on64: properly honor add-to-physmap-batch's size (thx Jan Beulich).

* Wed Jun 07 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.8.1-alt8%ubt
- fix ubt-macro usage in changelog

* Wed Jun 07 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.8.1-alt7%ubt
- Upstream updates:
 + ibxc: fix segfault on uninitialized xch->fmem
 + tools/libxc: Tolerate specific zero-content records in migration v2 streams
 + tools: ocaml: In configure, check for ocamlopt

* Mon May 08 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.8.1-alt6%ubt
- Upstream updates:
 + kexec: clear kexec_image slot when unloading kexec image
 + memory: exit early from memory_exchange() upon write-back error
 + memory: don't hand MFN info to translated guests
 + x86/mce: make 'severity_cpu' private to its users
 + x86/mce: always re-initialize 'severity_cpu' in mcheck_cmn_handler()

* Sat May 06 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.8.1-alt5%ubt
- added ubt tag

* Fri May 05 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.8.1-alt4
- Upstream updates:
 + multicall: deal with early exit conditions (XSA-213)
 + x86: discard type information when stealing pages (XSA-214)

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 4.8.1-alt3
- rebuild with ocaml 4.04.1

* Wed May 03 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.8.1-alt2
- Rebuild with new ocaml-4.04
- Dependencies cleanup

* Sun Apr 16 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.8.1-alt1
- Upstream updates:
 + x86/vmx: Don't leak host syscall MSR state into HVM guests
 + x86/layout: Correct Xen's idea of its own memory layout
 + xen: credit2: always mark a tickled pCPU as... tickled
 + xen: credit2: don't miss accounting while doing a credit reset
 + x86emul: correct decoding of vzero{all,upper}
 + x86/emul: Correct the decoding of mov to/from cr/dr
 + Don't clear HCR_VM bit when updating VTTBR
 + x86: drop unneeded __packed attributes
 + build/clang: fix XSM dummy policy when using clang 4.0
 + x86/EFI: avoid overrunning mb_modules[]
 + x86/EFI: avoid IOMMU faults on [_end,__2M_rwdata_end)
 + x86/EFI: avoid Xen image when looking for module/kexec position
 + xen: sched: don't call hooks of the wrong scheduler via VCPU2OP
 + memory: properly check guest memory ranges in XENMEM_exchange handling
   (CVE-2017-7228 / XSA-212)
 + x86: use 64 bit mask when masking away mfn bits

* Fri Apr 07 2017 Anton Farygin <rider@altlinux.ru> 4.8.0-alt7
- rebuild with new ocaml-4.04

* Tue Feb 21 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.8.0-alt6
- Upstream updates:
 + IOMMU: always call teardown callback (XSA-207)
 + x86/ept: allow write-combining on !mfn_valid() MMIO mappings again
 + xen/p2m: Fix p2m_flush_table for non-nested cases
 + VMX: fix VMCS race on context-switch paths

* Sat Feb 11 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.8.0-alt5
- Fix packaging errors
- Upstream updates:
 + qemu-xen: cirrus: fix oob access issue (CVE-2017-2615)
 + x86/xstate: Fix array overrun on hardware with LWP
 + x86emul: VEX.B is ignored in compatibility mode
 + x86emul: LOCK check adjustments
 + x86: segment attribute handling adjustments
 + x86emul: correct FPU stub asm() constraints
 + x86/hvm: do not set msr_tsc_adjust on hvm_set_guest_tsc_fixed
 + xen: credit2: use the correct scratch cpumask
 + xen: credit2: never consider CPUs outside of our cpupool
 + xen: credit2: fix shutdown/suspend when playing with cpupools
 + x86/emulate: don't assume that addr_size == 32 implies protected mode

* Sat Jan 21 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.8.0-alt4
- Upstream updates:
 + x86emul: correct PUSHF/POPF
 + xen: Fix determining when domain creation is complete
 + x86emul: CMPXCHG{8,16}B ignore prefixes
 + x86/hvm: don't unconditionally create a default ioreq server
 + x86/VPMU: clear the overflow status of which counter happened to overflow
 + x86emul: MOVNTI does not allow REP prefixes
 + x86emul: ignore most segment bases for 64-bit mode in is_aligned()
 + VT-d: correct dma_msi_set_affinity()
 + x86emul: CMPXCHG16B requires an aligned operand
 + x86/emul: Correct the return value handling of VMFUNC
 + x86/cpu: Don't update this_cpu for get_cpu_vendor(, gcv_guest)
 + libxl: fix libxl_set_memory_target

* Sun Jan 08 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.8.0-alt3
- Upstream updates:
 + xsm: allow relevant permission during migrate and gpu-passthrough
 + libxl: init_acpi_config should return rc in exit path, and set
   to 0 on success
- Added lost requires: seabios, ipxe-roms-qemu

* Mon Dec 26 2016 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.8.0-alt2
- Upstream updates:
 + x86/emul: Correct the handling of eflags with SYSCALL (XSA-204)
 + x86: force EFLAGS.IF on when exiting to PV guests (XSA-202)
 + x86/HVM: add missing NULL check before using VMFUNC hook (XSA-203)
 + x86/emul: add likely()/unlikely() to test harness

* Wed Dec 07 2016 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.8.0-alt1
- 4.8.0 release

* Fri Nov 25 2016 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.7.1-alt2
- Upstream updates:
 + x86/hvm: Fix the handling of non-present segments.
   This is CVE-2016-9386 / XSA-191.
 + x86/HVM: don't load LDTR with VM86 mode attrs during task switch.
   This is CVE-2016-9382 / XSA-192.
 + x86/PV: writes of %%fs and %%gs base MSRs require canonical addresses
   This is CVE-2016-9385 / XSA-193.
 + libelf: fix stack memory leak when loading 32 bit symbol tables.
   This is CVE-2016-9384 / XSA-164.
 + x86emul: fix huge bit offset handling.
   This is CVE-2016-9383 / XSA-195.
 + x86/emul: correct the IDT entry calculation in inject_swint().
   This is CVE-2016-9377 / part of XSA-196.
 + x86/svm: fix injection of software interrupts.
   This is CVE-2016-9378 / part of XSA-196.
 + pygrub: Properly quote results, when returning them to the caller.
   This is CVE-2016-9379 and CVE-2016-9380 / XSA-198.

* Wed Nov 09 2016 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.7.1-alt1
- 4.7.1 release

* Fri Nov 04 2016 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.7.0-alt7
- Fix: SharedLibs Policy Draft violation
  (altlinux-policy-shared-lib-contains-devel-so)
- stubdom: fix and enable stubdom-vtpm build
- Typo fix in /etc/rc.d/init.d/xendriverdomain
- Xen Security Modules is enabled: XSM-FLASK

* Fri Oct 28 2016 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.7.0-alt6
- Upstream updates:
 + Merge branch 'upstream/4.7' into alt/4.7
 + x86: MISALIGNSSE feature depends on SSE
 + vscsiif.h: replace PAGE_SIZE with VSCSIIF_PAGE_SIZE
 + usbif.h: replace PAGE_SIZE with USBIF_RING_SIZE
 + x86/Viridian: don't depend on undefined register state
 + x86emul: fix pushing of selector registers
 + x86/hvm: Clobber %%cs.L when LME becomes set
 + xen/trace: Fix trace metadata page count calculation (revert fbf96e6)
 + x86: defer not-present segment checks
 + xen: credit1: return the 'time remaining to the limit' as next
   timeslice.

* Fri Oct 28 2016 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.7.0-alt5
- Try to eliminate circular deps between xen-ocaml and xen-ocaml-devel

* Thu Oct 27 2016 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.7.0-alt4
- fix files and directories package ownership

* Sun Oct 23 2016 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.7.0-alt3
- ALT-specific SysV init-scripts adaptations (condstop, condrestart)
- Fix unsafe usage of temp files in stubdom-dm script
- Reorganization of file packaging

* Fri Oct 07 2016 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.7.0-alt2
- Upstream updates
 + x86emul: honor guest CR0.TS and CR0.EM

* Mon Sep 26 2016 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 4.7.0-alt1
- 4.7.0 release
- Upstream updates:
 + x86/AMD: apply erratum 665 workaround
 + x86emul: don't allow null selector for LTR
 + x86emul: correct loading of %%ss
 + x86/Intel: hide CPUID faulting capability from guests
 + xen: credit2: properly schedule migration of a running vcpu.
 + xen: credit1: fix mask to be used for tickling in Credit1
 + x86/domctl: Fix migration of guests which are not using xsave
 + x86/domctl: Fix TOCTOU race with the use of XEN_DOMCTL_getvcpuextstate
 + minios: fix build issue with xen_*mb defines
 + minios: make mini-os_app.o depend on included xen libraries

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
