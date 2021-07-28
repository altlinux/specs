%define _unpackaged_files_terminate_build 1
%def_without static

Name: stlink
Version: 1.6.1
Release: alt1
Epoch: 1

Summary: STM32 microcontrolles programmer and debuger, using STLINKv1/v2/v2-1/v3
License: BSD-3-Clause
Group: Development/Other

URL: https://github.com/texane/stlink.git
Source0: %name-%version.tar

BuildRequires: cmake
BuildRequires: libgtk+3-devel
BuildRequires: libusb-devel
BuildRequires: pandoc
BuildRequires: libpcre-devel
BuildRequires: libffi-devel
BuildRequires: bzlib-devel
BuildRequires: libbrotli-devel

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
# restore pkgconfig generation
# FIXME: resulting pkgconfig is broken anyway
sed -i 's|#add_subdirectory(cmake\/pkgconfig)|add_subdirectory(cmake/pkgconfig)|' CMakeLists.txt
# NB: this may become way too generic in future
sed -i 's|\(.*DESTINATION.*\)\(${PROJECT_NAME}\/\)\(.*\)|\1\3|g' doc/man/CMakeLists.txt src/stlink-gui/CMakeLists.txt
# move stlink-gui.ui out of %%_bindir
sed -i 's|stlink-gui.ui DESTINATION ${CMAKE_INSTALL_BINDIR}|stlink-gui.ui DESTINATION %_datadir/%name|' src/stlink-gui/CMakeLists.txt
sed -i 's|STLINK_UI_DIR="${CMAKE_INSTALL_PREFIX}/bin"|STLINK_UI_DIR="%_datadir/%name"|' src/stlink-gui/CMakeLists.txt

%build
# sysconf/udev policy - /etc is for user
mkdir -p %buildroot%_udevrulesdir/
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DINCLUDE_INSTALL_DIR=%_includedir \
	-DSTLINK_LIBRARY_PATH=%_libdir \
	-DSTLINK_GENERATE_MANPAGES=ON \
	-DSTLINK_UDEV_RULES_DIR=%_udevrulesdir \
	-DSTLINK_MODPROBED_DIR=%_sysconfdir/modprobe.d

# parallel build is broken with NPROCS >=8 and even >=4 on ppc64le
export NPROCS=1
%cmake_build

%install
%cmakeinstall_std


%if_without static
rm -f %buildroot/%_libdir/lib%name.a
%endif

%files
%doc CHANGELOG.md LICENSE.md README.md
%_sysconfdir/modprobe.d/*
%_udevrulesdir/*
%_bindir/st-*
%_man1dir/*

%files gui
%_bindir/%name-gui
%dir %_datadir/%name
%_datadir/%name/%name-gui.ui
%_datadir/applications/*
%_iconsdir/hicolor/scalable/apps/*.svg

%files -n lib%name
%_libdir/lib%name.so*

%files -n lib%name-devel
%if_with static
%_libdir/*.a
%endif
%dir %_includedir/%name
%_includedir/%name.h
# stm32.h: https://github.com/stlink-org/stlink/issues/976
%_includedir/stm32.h
%_includedir/%name/*.h
%_pkgconfigdir/%name.pc

%changelog
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
