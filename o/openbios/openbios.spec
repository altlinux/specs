Name: openbios
Version: 1.0
Release: alt1
Summary: OpenBios implementation of IEEE 1275-1994
Group: Emulators
License: GPLv2
Url: http://www.openfirmware.info/OpenBIOS
Packager: Ilya Mashkin <oddity@altlinux.ru>
# Getting openbios tarball:
# svn export -r463 svn://openbios.org/openbios/trunk/openbios-devel openbios-1.0
# tar czvf openbios-1.0.tar.gz openbios-1.0
Source0: %name/%name-%version.tar.gz
Patch0: openbios-noerror.patch
Patch1: openbios-1.0-merge-sbss-into-bss.patch

BuildRequires: libxslt

# debugging firmwares does not goes the same way as a normal program.
# moreover, all architectures providing debuginfo for a single noarch
# package is currently clashing in koji, so don't bother.
%global debug_package %nil
%define _binaries_in_noarch_packages_terminate_build 0

%define ob_desc \
The OpenBIOS project provides you with most free and open source Open Firmware	\
implementations available. Here you find several implementations of		\
IEEE 1275-1994 (Referred to as Open Firmware) compliant firmware. Among its	\
features, Open Firmware provides an instruction set independent device 		\
interface. This can be used to boot the operating system from expansion cards	\
without	native initialization code.						\
\
It is Open Firmware's goal to work on all common platforms, like x86, AMD64,	\
PowerPC, ARM and Mips. With its flexible and modular design, Open Firmware	\
targets servers, workstations and embedded systems, where a sane and unified	\
firmware is a crucial design goal and reduces porting efforts noticably.	\
\
Open Firmware is found on many servers and workstations and there are sever	\
commercial implementations from SUN, Firmworks, CodeGen, Apple, IBM and others. \
\
In most cases, the Open Firmware implementations provided on this site rely on	\
an additional low-level firmware for hardware initialization, such as coreboot	\
or U-Boot.									\
										\

%description %ob_desc
# building firmwares are quite tricky, because they often has to be built on
# their native architecture (or in a cross-capable compiler, that we lack in
# koji), and deployed everywhere. Recent koji builders support a feature
# that allow us to build packages in a single architecture, and create noarch
# subpackages that will be deployed everywhere. Because the package can only
# be built in certain architectures, the main package has to use
# BuildArch: <nativearch>, or something like that.
# Note that using ExclusiveArch is _wrong_, because it will prevent the noarch
# packages from getting into the excluded repositories.
#
# Openbios is even trickier compared to other firmwares, because the same
# source must originate firmwares for multiple architectures. The magic here
# is to only create the subpackages in the architectures that can build it.
%ifarch sparcv9
%package sparc
Summary: OpenBIOS for sparc
BuildArch: noarch
Requires: %name-common = %version-%release

%description sparc %ob_desc
%endif

%ifarch sparc64
%package sparc64
Summary: OpenBIOS for sparc64
BuildArch: noarch
Requires: %name-common = %version-%release

%description sparc64 %ob_desc
%endif

%ifarch ppc ppc64
%package ppc
Summary: OpenBIOS for ppc
BuildArch: noarch
Requires: %name-common = %version-%release

%description ppc %ob_desc
%endif

%package common
Summary: Common files for OpenBIOS
Group: Emulators
BuildArch: noarch

%description common %ob_desc
%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
CFLAGS="%optflags"
%ifarch ppc
/bin/sh ./config/scripts/switch-arch ppc
make build-verbose %{?_smp_mflags}
%endif

%ifarch sparcv9
/bin/sh ./config/scripts/switch-arch sparc32
make build-verbose %{?_smp_mflags}
%endif

%ifarch sparc64
/bin/sh ./config/scripts/switch-arch sparc64
make build-verbose %{?_smp_mflags}
%endif

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/openbios
%ifarch sparcv9
install -p -m 0644  obj-sparc32/openbios-builtin.elf $RPM_BUILD_ROOT%_datadir/openbios/openbios-sparc32
%endif
%ifarch sparc64
install -p -m 0644  obj-sparc64/openbios-builtin.elf $RPM_BUILD_ROOT%_datadir/openbios/openbios-sparc64
%endif
%ifarch ppc
install -p -m 0644  obj-ppc/openbios-qemu.elf $RPM_BUILD_ROOT%_datadir/openbios/openbios-ppc
%endif

%clean
%ifarch sparcv9
%files sparc
%_datadir/openbios/openbios-sparc32
%endif

%ifarch sparc64
%files sparc64
%_datadir/openbios/openbios-sparc64
%endif

%ifarch ppc
%files ppc
%_datadir/openbios/openbios-ppc
%endif

%files common
%dir %_datadir/openbios/
%doc COPYING README

%changelog
* Thu Aug 13 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0-alt1
- Build for ALT Linux

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 21 2009 Mark McLoughlin <markmc@redhat.com> - 1.0-1
- Replace previous attempt to fix bug #494075 with fix from Pavel Roskin
- Drop the 0.x.463 numbering; we are using official upstream 1.0

* Tue Apr 14 2009 Glauber Costa <glommer@redhat.com> - 1.0-0.6.463
- Applied bugfix for #494075

* Wed Mar 04 2009 Glauber Costa <glommer@redhat.com> - 1.0-0.5.463
- created openbios-common instead of openbios-doc. It owns the directories
  and everybody depends on it.

* Wed Mar 04 2009 Glauber Costa <glommer@redhat.com> - 1.0-0.4.463
- Addressed comments on BZ 485420. rpmlint provides no error for me,
  added comentaries, and tell how to get the source.

* Tue Mar 03 2009 Glauber Costa <glommer@redhat.com> - 1.0-0.3.463
- Don't use prebuilt binaries anywhere.

* Fri Feb 13 2009 Glauber Costa <glommer@redhat.com> - 1.0.0.2
- Addressed comments on BZ 485420: clean build environment, own
  directories we create.
* Fri Feb 13 2009 Glauber Costa <glommer@redhat.com> - 1.0-0.1.463
- Created initial build for sparc32/sparc64
