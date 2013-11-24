%define set_disable() %{expand:%%force_disable %{1}} %{expand:%%undefine _enable_%{1}}
%define set_without() %{expand:%%force_without %{1}} %{expand:%%undefine _with_%{1}}

%define base_flavour el
%define sub_flavour def
%define flavour %base_flavour-%sub_flavour

Name: kernel-image-%flavour
Version: 2.6.32
Release: alt13
%define erelease 431.el6

%define kernel_req %nil
%define kernel_prov %nil
%define kernel_branch %version
%define kernel_stable_version 32
%define kernel_extra_version %nil

%define krelease %release

%define kmandir %{_man9dir}l
# Build options
# You can change compiler version by editing this line:
%define kgcc_version	4.4

%def_disable verbose
%def_with src
%def_enable docs
%def_enable htmldocs
%def_enable man
%def_disable debug
%def_disable crypto_signature
%def_with firmware
%def_without perf

%def_enable debug_section_mismatch

%define strip_mod_opts --strip-unneeded -R .comment

## Don't edit below this line ##################################

%define kversion	%kernel_branch%kernel_extra_version
%define modules_dir	/lib/modules/%kversion-%flavour-%krelease
%define firmware_dir	/lib/firmware/%kversion-%flavour-%krelease

%define kheaders_dir	%_prefix/include/linux-%kernel_branch-%flavour
%define kbuild_dir	%_prefix/src/linux-%kversion-%flavour-%krelease
%define old_kbuild_dir	%_prefix/src/linux-%kversion-%flavour

Summary: The Linux kernel (the core of the Linux operating system)
License: GPL
Group: System/Kernel and hardware
Url: http://www.kernel.org/

Source0: linux-%version-%erelease.tar
Source1: %flavour.x86_64.config
Source2: %flavour.i686.config
Patch: kernel-image-%flavour-%version-%release.patch

ExclusiveOS: Linux
ExclusiveArch: x86_64 i586 i686

%ifarch x86_64 %ix86
%define kernel_arch x86
%else
%define kernel_arch %_target_cpu
%endif

%ifarch x86_64
%define base_arch x86_64
%endif
%ifarch %ix86
%define base_arch x86
%endif

%ifnarch x86_64 i586 i686
%set_disable docs
%set_without src
%endif

%if "%sub_flavour" != "def"
%set_disable docs
%set_without src
%endif

%if_disabled docs
%set_disable htmldocs
%set_disable man
%endif

BuildPreReq: rpm-build-kernel
BuildRequires: dev86 flex
BuildRequires: libdb4-devel
%{?kgcc_version:BuildRequires: gcc%kgcc_version}
BuildRequires: module-init-tools >= 3.1
BuildRequires: patch >= 2.6.1-alt1
%{?_with_src:BuildRequires: pxz}

%{?_enable_htmldocs:BuildRequires: xmlto transfig ghostscript}
%{?_enable_man:BuildRequires: xmlto}
%{?_with_perf:BuildRequires: libnewt-devel python-dev binutils-devel libelf-devel asciidoc elfutils-devel >= 0.138}

Requires: bootloader-utils >= 0.4.21
Requires: module-init-tools >= 3.1
Requires: mkinitrd >= 1:2.9.9-alt1
Requires: startup >= 0.9.8.24.1

Provides: kernel = %kversion
Provides: kernel-modules-md-%flavour = %version-%release

PreReq: coreutils
PreReq: module-init-tools >= 3.1
PreReq: mkinitrd >= 1:2.9.9-alt1
AutoProv: no, %kernel_prov
AutoReq: no, %kernel_req

%description
This package contains the Linux kernel that is used to boot and run
your system.
Most hardware drivers for this kernel are built as modules.  Some of
these drivers are built separately from the kernel; they are available
in separate packages (kernel-modules-*-%flavour).
The "el" variant of kernel packages is derived from sources freely provided
to the public by a prominent North American Enterprise Linux vendor.
This kernel has LTS and suitable for servers and workstations.


%package -n kernel-headers-modules-%flavour
Summary: Headers and other files needed for building kernel modules
Group: Development/Kernel
%{?kgcc_version:Requires: gcc%kgcc_version}
Provides: kernel-headers-modules-%flavour = %version-%release
Provides: kernel-devel-%flavour = %version-%release
%{?base_flavour:Provides: kernel-devel-%base_flavour = %version-%release}
Provides: kernel-devel = %version-%release
#Obsoletes: kernel-headers-modules-%flavour = %version
AutoProv: no

%description -n kernel-headers-modules-%flavour
This package contains header files, Makefiles and other parts of the
Linux kernel build system which are needed to build kernel modules for
the Linux kernel package %name-%version-%release.

If you need to compile a third-party kernel module for the Linux
kernel package %name-%version-%release, install this package
and specify %kbuild_dir as the kernel source directory.


%if_with firmware
%package -n firmware-kernel-%flavour
Summary: Firmware for drivers from %name
Group: System/Kernel and hardware
AutoProv: no
AutoReq: no

%description -n firmware-kernel-%flavour
Firmware for drivers from %name.
%endif


%if_with perf
%package -n perf
Summary: Performance analysis tools for Linux
Group: Development/Tools
AutoReq: yes,noperl,nopython
AutoProv: yes,noperl,nopython

%description -n perf
Performance counters for Linux are a new kernel-based subsystem that provide
a framework for all things performance analysis. It covers hardware level
(CPU/PMU, Performance Monitoring Unit) features and software features
(software counters, tracepoints) as well.
This package contains performance analysis tools for Linux
%endif


%package -n kernel-headers-%flavour
Summary: Header files for the Linux kernel
Group: Development/Kernel
Requires: kernel-headers-common >= 1.1.5
Provides: kernel-headers = %version
%{?base_flavour:Provides: kernel-headers-%base_flavour = %version}
Provides: kernel-headers-%flavour = %version-%release
#Obsoletes: kernel-headers-%flavour = %version
Provides: %kheaders_dir/include
AutoProv: no

%description -n kernel-headers-%flavour
This package makes Linux kernel headers corresponding to the Linux
kernel package %name-%version-%release available for building
userspace programs (if this version of headers is selected by
adjust_kernel_headers).


%if_enabled docs
%define kernel_doc_package_std_body() \
Group: Documentation \
%{?base_flavour:Provides: kernel-%{1}-%base_flavour = %version-%release} \
BuildArch: noarch \
AutoProv: no \
AutoReq: no

%package -n kernel-doc-%flavour
Summary: Linux kernel %kversion-%flavour documentation
%kernel_doc_package_std_body doc

%description -n kernel-doc-%flavour
This package contains documentation files for Linux kernel package
kernel-image-%flavour-%kversion-%krelease
The documentation files contained in this package may be different
from the similar files in upstream kernel distributions, because some
patches applied to the corresponding kernel packages may change things
in the kernel and update the documentation to reflect these changes.


%if_enabled htmldocs
%package -n kernel-docbook-%flavour
Summary: Linux kernel %kversion-%flavour HTML API documentation
%kernel_doc_package_std_body docbook

%description -n kernel-docbook-%flavour
This package contains API documentation HTML files for Linux kernel
package kernel-image-%flavour-%kversion-%krelease
The documentation files contained in this package may be different
from the similar files in upstream kernel distributions, because some
patches applied to the corresponding kernel packages may change things
in the kernel and update the documentation to reflect these changes.
%endif


%if_enabled man
%package -n kernel-man-%flavour
Summary: Linux kernel %kversion-%flavour man pages
%kernel_doc_package_std_body man

%description -n kernel-man-%flavour
This package contains man pages for Linux kernel package
kernel-image-%flavour-%kversion-%krelease
The man pages contained in this package may be different from the similar
files in upstream kernel distributions, because some patches applied to
the corresponding kernel packages may change things in the kernel and
update the documentation to reflect these changes.
%endif
%endif


%if_with src
%package -n kernel-src-%flavour
Summary: Linux kernel %kversion-%flavour sources
Group: Development/Kernel
%{?base_flavour:Provides: kernel-src-%base_flavour = %version-%release}
BuildArch: noarch
AutoProv: no
AutoReq: no

%description -n kernel-src-%flavour
This package contains sources for Linux kernel package
kernel-image-%flavour-%kversion-%krelease
%endif


%prep
%setup -c -n kernel-image-%flavour-%kversion-%krelease
cd linux-%version-%erelease
%patch -p1

# get rid of unwanted files resulting from patch fuzz
#find . -name "*.orig" -delete -or -name "*~" -delete

# this file should be usable both with make and sh (for broken modules
# which do not use the kernel makefile system)
%ifdef kgcc_version
GCC_VERSION="%kgcc_version"
%else
GCC_VERSION="$(%__cc --version | head -1 | cut -d' ' -f3 | cut -d. -f1-2)"
%endif
echo -n "export GCC_VERSION=$GCC_VERSION" > gcc_version.inc

sed -i 's/CC.*$(CROSS_COMPILE)gcc/CC\t\t:= '"gcc-$GCC_VERSION/g" Makefile

%if_with src
cd ..
find linux-%kversion-%erelease -type f -or -type l -not -name '*.orig' -not -name '*~' -not -name '.git*' > kernel-src-%flavour.list
cd -
%endif

install -m644 %SOURCE1 %SOURCE2 .


%build
cd linux-%version-%erelease
export ARCH=%base_arch

config_disable()
{
	local e
	while [ -n "$1" ]; do
		e="$e"'/^CONFIG_'$1'=/s|^\(.*\)=.*$|# \1 is not set|;'
		shift
	done
	sed -i "$e" .config
}

config_enable()
{
	local e s a
	while [ -n "$1" ]; do
		a=${1%%=*}
		[ "$a" = "$1" ] && s="=y" || s=
		e="$e"'/^#[[:blank:]]*CONFIG_'$a'[[:blank:]]/s/^#[[:blank:]]*\(CONFIG_'$a'\) .*$/\1'$s'/;'
		shift
	done
	sed -i "$e" .config
}

cp -vf \
%ifarch %ix86
	%flavour.i686.config \
%else
	%flavour.%_target_cpu.config \
%endif
	.config

sed -i '/^CONFIG_LOCALVERSION=/s/=.*$/="-%flavour-%krelease"/' .config

config_disable \
	%{?_disable_debug_section_mismatch:DEBUG_SECTION_MISMATCH} \
	%{?_disable_debug:DEBUG_INFO} \
	%{?_disable_crypto_signature:MODULE_SIG CRYPTO_SIGNATURE} \
	BUILD_DOCSRC

echo "Building kernel %kversion-%flavour-%krelease"

%make_build oldconfig
%make_build %{?_enable_verbose:V=1} bzImage modules
%if_with perf
%make_build -C tools/perf %{?_enable_verbose:V=1} \
	prefix=%_prefix perfexecdir=%_libexecdir/perf \
	EXTRA_CFLAGS="%optflags %{?_disable_debug:-g0}"
%make_build -C tools/perf %{?_enable_verbose:V=1} man
%endif

echo "Kernel built %kversion-%flavour-%krelease"

# psdocs, pdfdocs don't work yet
%{?_enable_htmldocs:%def_enable builddocs}
%{?_enable_man:%def_enable builddocs}
%if_enabled builddocs
echo "Building kernel docs %kversion-%flavour-%krelease"
%{?_enable_htmldocs:%make_build htmldocs}
%{?_enable_man:%make_build mandocs 2>mandocs.err.log}
echo "Kernel docs built %kversion-%flavour-%krelease"
%endif


%install
export ARCH=%base_arch
cd linux-%version-%erelease

install -Dp -m644 System.map %buildroot/boot/System.map-%kversion-%flavour-%krelease
install -Dp -m644 arch/%base_arch/boot/bzImage %buildroot/boot/vmlinuz-%kversion-%flavour-%krelease
install -Dp -m644 .config %buildroot/boot/config-%kversion-%flavour-%krelease

%make_install \
	INSTALL_MOD_PATH=%buildroot \
	INSTALL_FW_PATH=%buildroot%firmware_dir \
	%{!?_enable_debug:%{?strip_mod_opts:INSTALL_MOD_STRIP="%strip_mod_opts"}} \
	modules_install

install -d -m 0755 %buildroot%kbuild_dir
cp -aL include %buildroot%kbuild_dir/
for t in f d; do
	find %buildroot%kbuild_dir/include/config -type $t -empty -delete
done
for d in arch/%kernel_arch/include; do
	a="$(dirname "$d")"
	install -d -m 0755 %buildroot%kbuild_dir/$a
	cp -a $d %buildroot%kbuild_dir/$a/
	install -p -m 0644 $a/Makefile* %buildroot%kbuild_dir/$a/
done
find %buildroot%kbuild_dir/{include,arch} -type f -name Kbuild -delete

%if 0
# drivers-headers install
install -d -m 0755 %buildroot%kbuild_dir/{drivers/{scsi,md,usb/core,net/wireless},net/mac80211,kernel,lib}
install -m 0644 drivers/scsi/scsi{{,_typedefs}.h,_module.c} %buildroot%kbuild_dir/drivers/scsi/
install -m 0644 drivers/md/dm*.h %buildroot%kbuild_dir/drivers/md/
install -m 0644 drivers/usb/core/*.h %buildroot%kbuild_dir/drivers/usb/core/
install -m 0644 drivers/net/wireless/Kconfig %buildroot%kbuild_dir/drivers/net/wireless/
install -m 0644 lib/hexdump.c %buildroot%kbuild_dir/lib/
install -m 0644 kernel/workqueue.c %buildroot%kbuild_dir/kernel/
install -m 0644 net/mac80211/{ieee80211_i,sta_info}.h %buildroot%kbuild_dir/net/mac80211/
%endif

# Install files required for building external modules (in addition to headers)
for f in \
	.config \
	Makefile \
	Module.symvers \
	scripts/Kbuild.include \
	scripts/Makefile{,.{build,clean,host,lib,mod*}} \
	scripts/bin2c \
	scripts/check{includes,version}.pl \
	scripts/conmakehash \
	scripts/extract-ikconfig \
	scripts/gcc-*.sh \
	scripts/kallsyms \
	scripts/makelst \
	scripts/mk{compile_h,makefile,version} \
	scripts/module-common.lds \
	scripts/pnmtologo \
	scripts/recordmcount.pl \
	scripts/basic/{fixdep,hash} \
	scripts/genksyms/genksyms \
	scripts/kconfig/conf \
	scripts/mod/{modpost,mk_elfconfig} \
	gcc_version.inc
do
	if [ -f "$f" ]; then
		[ -x "$f" ] && mode=0755 || mode=0644
		install -Dp -m $mode {,%buildroot%kbuild_dir/}$f
	fi
done

# Provide kbuild directory with old name (without %%krelease)
ln -s "$(relative %kbuild_dir %old_kbuild_dir)" %buildroot%old_kbuild_dir

# Provide kernel headers for userspace
make -j%__nprocs headers_install INSTALL_HDR_PATH=%buildroot%kheaders_dir
find %buildroot%kheaders_dir -type f -a \( -name .install -o -name ..install.cmd \) -delete

# Fix symlinks to kernel sources in /lib/modules
rm -f %buildroot%modules_dir/{build,source}
ln -s %kbuild_dir %buildroot%modules_dir/build

%if_with perf
%makeinstall_std -C tools/perf prefix=%_prefix perfexecdir=%_libexecdir/perf install install-man
install -d -m 0755 %buildroot%_docdir/perf-%version
install -m 0644 tools/perf/{CREDITS,design.txt,Documentation/examples.txt} %buildroot%_docdir/perf-%version/
%endif

# install documentation
%if_enabled docs
install -d %buildroot%_docdir/kernel-doc-%flavour/
for I in Documentation/*; do
	case "$(basename "$I")" in
		DocBook)
%if_enabled htmldocs
			for J in "$I"/*.tmpl; do
				j=$(basename "$J" .tmpl)
				[ -d "$I/$j" ] || continue
				install -d -m 0755 %buildroot%_docdir/kernel-doc-%flavour/DocBook/"$j"
				install -m 0644 "$I/$j"/*.html %buildroot%_docdir/kernel-doc-%flavour/DocBook/"$j"/
				install -m 0644 "$I/$j.html" %buildroot%_docdir/kernel-doc-%flavour/DocBook/
			done
%endif
			;;
		[a-z][a-z]_[A-Z][A-Z]|Makefile|dontdiff) ;;
		*) cp -aL "$I" %buildroot%_docdir/kernel-doc-%flavour/ ;;
	esac
done
find %buildroot%_docdir/kernel-doc-%flavour -type f -name Makefile -delete
%if_enabled man
install -d %buildroot%kmandir
install -m 0644 Documentation/DocBook/man/* %buildroot%kmandir/
%endif
%endif

cd -

%if_with src
install -d -m 0755 %kernel_srcdir
t="%__nprocs"
[ $t -gt 1 ] && XZ="pxz -T$t" || XZ="xz"
tar	--transform='s/^\(linux-%kversion\)-%erelease/\1-%flavour-%krelease/' \
	--owner=root --group=root --mode=u+w,go-w,go+rX \
	-T kernel-src-%flavour.list \
	-cf - | \
	$XZ -8e > %kernel_srcdir/linux-%kversion-%flavour-%krelease.tar.xz
%endif


%files
/boot/*
%dir %modules_dir
%modules_dir/modules.alias*
%modules_dir/modules.builtin
%modules_dir/modules.dep*
%modules_dir/modules.order
%modules_dir/modules.symbols*
%ghost %modules_dir/modules.builtin.bin
%ghost %modules_dir/modules.devname
%ghost %modules_dir/modules.softdep
%modules_dir/kernel


%files -n kernel-headers-%flavour
%kheaders_dir


%if_with firmware
%files -n firmware-kernel-%flavour
%dir /lib/firmware
%firmware_dir
%endif


%if_with perf
%files -n perf
%doc %_docdir/perf-%version
%_bindir/*
%_libexecdir
%_man1dir/*
%endif


%files -n kernel-headers-modules-%flavour
%kbuild_dir
%old_kbuild_dir
%dir %modules_dir
%modules_dir/build


%if_enabled docs
%files -n kernel-doc-%flavour
%doc %_docdir/kernel-doc-%flavour
%{?_enable_htmldocs:%exclude %_docdir/kernel-doc-%flavour/DocBook}


%if_enabled htmldocs
%files -n kernel-docbook-%flavour
%doc %dir %_docdir/kernel-doc-%flavour
%doc %_docdir/kernel-doc-%flavour/DocBook
%endif


%if_enabled man
%files -n kernel-man-%flavour
%kmandir
%endif
%endif


%if_with src
%files -n kernel-src-%flavour
%_usrsrc/kernel
%endif


%changelog
* Sun Nov 24 2013 Led <led@altlinux.ru> 2.6.32-alt13
- 2.6.32-431.el6:
  + CVE-2013-0228
  + CVE-2013-0268
  + CVE-2013-0343
  + CVE-2013-0349
  + CVE-2013-0871
  + CVE-2013-0913
  + CVE-2013-1767
  + CVE-2013-1773
  + CVE-2013-1774
  + CVE-2013-1792
  + CVE-2013-1796
  + CVE-2013-1797
  + CVE-2013-1798
  + CVE-2013-1826
  + CVE-2013-1827
  + CVE-2013-1928
  + CVE-2013-2164
  + CVE-2013-2234
  + CVE-2013-2851
  + CVE-2013-2888
  + CVE-2013-2889
  + CVE-2013-2892
  + CVE-2013-3231
  + CVE-2013-4345
  + CVE-2013-4387
  + CVE-2012-6537
  + CVE-2012-6542
  + CVE-2012-6545
  + CVE-2012-6546
  + CVE-2012-6547
- updated:
  + feat-drivers-gpu-drm--gma500

* Thu Oct 17 2013 Led <led@altlinux.ru> 2.6.32-alt12
- 2.6.32-358.23.2.el6:
  + CVE-2013-4162
  + CVE-2013-4299

* Wed Aug 28 2013 Led <led@altlinux.ru> 2.6.32-alt11
- 2.6.32-358.18.1.el6:
  + CVE-2012-6544
  + CVE-2013-2146
  + CVE-2013-2206
  + CVE-2013-2224
  + CVE-2013-2237

* Thu Aug 08 2013 Led <led@altlinux.ru> 2.6.32-alt10
- fixed tarball creation of kernel-src
- updated:
  + feat-drivers-gpu-drm--gma500

* Wed Jul 17 2013 Led <led@altlinux.ru> 2.6.32-alt9
- 2.6.32-358.14.1.el6:
  + CVE-2012-6548
  + CVE-2013-0914
  + CVE-2013-1848
  + CVE-2013-2128
  + CVE-2013-2634
  + CVE-2013-2635
  + CVE-2013-2852
  + CVE-2013-3222
  + CVE-2013-3224
  + CVE-2013-3225
  + CVE-2013-3301
- added radeon firmwares

* Tue Jul 02 2013 Led <led@altlinux.ru> 2.6.32-alt8
- fixed freeing RCU-protected IP-options (CVE-2013-2224)

* Thu Jun 13 2013 Led <led@altlinux.ru> 2.6.32-alt7
- 2.6.32-358.11.1.el6:
  + CVE-2013-1935
  + CVE-2013-1943
  + CVE-2013-2017

* Tue May 14 2013 Led <led@altlinux.ru> 2.6.32-alt6
- perf: Treat attr.config as u64 in perf_swevent_init() (CVE-2013-2094)
- added gpu/drm/gma500

* Thu Apr 25 2013 Led <led@altlinux.ru> 2.6.32-alt5
- 2.6.32-358.6.1.el6
- updated Requires
- disabled preun script

* Sun Mar 17 2013 Led <led@altlinux.ru> 2.6.32-alt4
- macvlan: receive multicast with local address

* Wed Mar 13 2013 Led <led@altlinux.ru> 2.6.32-alt3
- 2.6.32-358.2.1.el6

* Sun Mar 03 2013 Led <led@altlinux.ru> 2.6.32-alt2
- 2.6.32-358.0.1.el6
- enabled:
  + DEBUG_SECTION_MISMATCH

* Wed Feb 27 2013 Led <led@altlinux.ru> 2.6.32-alt1
- initial build:
  + 2.6.32-279.22.1.el6
- disabled:
  + BUILD_DOCSRC
  + DEBUG_INFO
  + DEBUG_SECTION_MISMATCH
  + MODULE_SIG
  + CRYPTO_SIGNATURE
- enabled modules:
  + JFS_FS
  + REISERFS_FS
  + FB_UVESA
- usb-storage: add unusual_devs entry for Casio EX-N1 digital camera
- gspca_pac7302: add support for device 093a:2623 Genuis Look 317
