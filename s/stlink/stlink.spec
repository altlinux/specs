Name: stlink
Version: 1.8.0
Release: alt1
Epoch: 1

Summary: STM32 microcontrolles programmer and debuger, using STLINKv1/v2/v2-1/v3
License: BSD-3-Clause
Group: Development/Other
Url: https://github.com/stlink-org/stlink

Conflicts: stlink-gui < 1.8.0

Source0: %name-%version.tar
Patch0: Post-release-patch-for-v1.8.0.patch

BuildRequires: cmake
BuildRequires: libgtk+3-devel
BuildRequires: libusb-devel
BuildRequires: pandoc

%description

Open source version of the STMicroelectronics STlink Tools

STLink is an open source toolset to program and debug STM32 devices and boards
manufactured by STMicroelectronics. It supports several so called STLINK
programmer boards (and clones thereof) which use a microcontroller chip to
translate commands from USB to JTAG/SWD. There are four generations available
on the market which are all supported by this toolset:

 STLINK/v1 (obsolete as of 21-11-2019, continued support by this toolset)
   transport layer: SCSI passthru commands over USB
   stand-alone programmer and present on STM32VL Discovery boards
 STLINK/v2
   transport layer: raw USB commands
   stand-alone programmer and present on STM32L Discovery and Nucleo boards
 STLINK/v2-1
   transport layer: raw USB commands
   present on some STM32 Nucleo boards
 STLINK/v3
   transport layer: raw USB commands
   stand-alone programmer

On the user level there is no difference in handling or operation between these
different revisions.

%package -n lib%name
Summary: Shared library of %name
Group: System/Libraries

%description -n lib%name
Lib files for stlink

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Development files for libstlink

%package gui
Summary: GUI for %name
Group: Development/Other
Requires: %name = %EVR

%description gui
GUI for stlink

%prep
%setup
%patch0 -p1
# no need to set it explicitly
sed -i '/("-D_FORTIFY_SOURCE=2")/d' cmake/modules/c_flags.cmake
echo %version > .version

%build
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DINCLUDE_INSTALL_DIR=%_includedir \
	-DSTLINK_GENERATE_MANPAGES=ON \
	-DSTLINK_UDEV_RULES_DIR=%_udevrulesdir \
	-DSTLINK_MODPROBED_DIR=%_modprobedir

%cmake_build -j1

%install
%cmakeinstall_std
rm -v %buildroot/%_libdir/lib%name.a
# upstream dropped pc generator altogether
mkdir -p %buildroot%_pkgconfigdir
cat > %buildroot%_pkgconfigdir/stlink.pc << 'E_O_F'
prefix=%_prefix
exec_prefix=%_prefix
libdir=%_libdir
includedir=%_includedir

Name: stlink
Description: STLINK library
Version: %version
Libs: -lstlink
Cflags: -I${includedir}/stlink
E_O_F

%files
%doc CHANGELOG.md LICENSE.md README.md
%_modprobedir/*
%_udevrulesdir/*
%_bindir/st-*
%_datadir/stlink
%exclude %_datadir/stlink/stlink-gui.ui
%_man1dir/*

%files gui
%_bindir/stlink-gui
%_datadir/stlink/stlink-gui.ui
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*.svg

%files -n lib%name
%_libdir/libstlink.so.*

%files -n lib%name-devel
%_includedir/stlink
%_libdir/libstlink.so
%_pkgconfigdir/stlink.pc

%changelog
* Tue Feb 04 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1:1.8.0-alt1
- 1.8.0 released

* Mon Jan 29 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:1.6.1-alt2
- Revived the package (no code changes). It's useful, and it has been deleted
  due to a bogus compiler warning:
  error: 'stlink_open_usb' accessing 64 bytes in a region of size 28 [-Werror=stringop-overflow=]
  This warning is a false positive. GCC 11, 12 are known to produce a lot of
  false positives with `-Wstringop-overflow`. As a result Linux (the kernel)
  disables `-Wstringop-overflow` when compiling with GCC 11, see the commit
  a5e0ace04fbf56c17 `init: Kconfig: Disable -Wstringop-overflow for GCC-11`.
  With GCC 13 `-Wstringop-overflow` is much better, so the (same) code
  compiles (and runs) just fine.

* Mon Feb 08 2021 Nikolai Kostrigin <nickel@altlinux.org> 1:1.6.1-alt1
- New version (closes: #34271)
  + switch to new upstream location
  + switch packaging scheme SRPM->gears
  + alter Epoch to change versioning scheme according to upstream
  + switch to use .gear/tags
  + extract gui into a separate package

* Thu Jul 12 2018 Igor Vlasenko <viy@altlinux.ru> 2018.04.18-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * udev-files-in-etc for stlink

* Fri Apr 20 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.04.18-alt2
- fix insane BRs
- fix packaging on 64bit arches other than x86_64

* Wed Apr 18 2018 Grigory Milev <week@altlinux.ru> 2018.04.18-alt1
- Updated to latest git version
- devide package to libs, main tools and devel packages

* Wed Mar 05 2014 Grigory Milev <week@altlinux.ru> 2014.03.05-alt2
- Change 0700 -> 0644 for file saved from flash

* Wed Mar 05 2014 Grigory Milev <week@altlinux.ru> 2014.03.05-alt1
- Initial build.
