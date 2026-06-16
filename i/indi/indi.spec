#
# This is not a mistake. Indi libraries have symbols that are defined in other
# indi libraries. At the stage of linking the target application, everything
# will be resolved.
#
%set_verify_elf_method none

%ifarch %ix86
%def_without check
%else
%def_with check
%endif

%def_without static
%def_with use_system_jsonlib
%def_with use_system_httplib
%def_with use_system_hidapi
%def_with qt

#
# Upstream provides static libraries for some of its components, despite
# the fact that static library building is disabled in CMake.
# See https://www.altlinux.org/LTO
#
%define optflags_lto %nil

%global descr INDI is a distributed control protocol designed to operate\
astronomical instrumentation. INDI is small, flexible, easy to parse,\
and scalable. It supports common DCS functions such as remote control,\
data acquisition, monitoring, and a lot more.

%global soversion 2

Name: indi
Version: 2.2.3.1
Release: alt1

Summary: Instrument Neutral Distributed Interface
License: GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.0-or-later and BSD-3-Clause AND ISC AND MIT AND CFITSIO
Group: System/Libraries
Url: https://indilib.org
Vcs: https://github.com/indilib/indi.git

Source: %name-%version.tar
Patch0: fix-indi2-ALT-SharedLibsPolicy-CMakeLists.txt.patch
Patch1: fix-indi2-ALT-vtable_undefined_symbol-CMakeLists.txt.patch

BuildRequires(Pre): rpm-build-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: libbrotli-devel
BuildRequires: libcfitsio-devel
BuildRequires: libcurl-devel
BuildRequires: libev-devel
BuildRequires: libfftw3-devel
BuildRequires: libjpeg-devel
BuildRequires: libgsl-devel
BuildRequires: libnova-devel
BuildRequires: libusb-devel
BuildRequires: rtl-sdr-devel
BuildRequires: zlib-devel

%if_with use_system_jsonlib
BuildRequires: nlohmann-json-devel
%endif

%if_with use_system_httplib
BuildRequires: libcpp-httplib-devel
BuildRequires: libssl-devel
%endif

%if_with use_system_hidapi
BuildRequires: libhidapi-devel
%endif

%if_with qt
BuildRequires: qt6-base-devel
%endif

%if_with check
BuildRequires: ctest
BuildRequires: libgmock-devel
%endif

Provides: indilib
Obsoletes: indilib <= 1.9.0-alt3

%description
%descr

%package -n lib%name-common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Obsoletes: indilib-common <= 1.9.0-alt3

%description -n lib%name-common
%descr
%summary.

%package -n lib%name%soversion
Group: System/Libraries
Summary: %summary
Requires: lib%name-common
Provides: libindi
Obsoletes: libindi <= 1.9.0-alt3

%description -n lib%name%soversion
%descr
%summary.

%package -n lib%name-devel
Group: Development/C++
Summary: Development files for the %name
Requires: lib%name%soversion
Provides: indi-devel
Provides: indilib-devel

%description -n lib%name-devel
%descr
%summary.

%package -n lib%name-devel-static
Group: Development/C++
Summary: Static libraries from %name
Requires: lib%name-devel
Conflicts: libindi-devel < 1.8.9-alt1

%description -n lib%name-devel-static
%descr
%summary.

%prep
%setup
%autopatch

%build
%add_optflags %optflags_shared
%cmake -G Ninja \
	-DCMAKE_SHARED_LINKER_FLAGS="-Wl,--no-allow-shlib-undefined" \
	-DUDEVRULES_INSTALL_DIR=%_udevrulesdir \
	-DINDI_BUILD_STATIC=%{with static} \
	-DINDI_SYSTEM_JSONLIB=%{with use_system_jsonlib} \
	-DINDI_SYSTEM_HTTPLIB=%{with use_system_httplib} \
	-DINDI_SYSTEM_HIDAPILIB=%{with use_system_hidapi} \
	-DINDI_BUILD_QT_CLIENT=%{with qt} \
	-DINDI_BUILD_UNITTESTS=%{with check} \
	-DINDI_BUILD_INTEGTESTS=%{with check} \
%nil
%cmake_build

%install
%cmake_install

%check
pushd %_cmake__builddir
# This is not an error. The test fails due to hasher limitations.
ctest -E IndiserverSingleDriver.DontLeakFds
popd

%files
%_bindir/%{name}*
%_bindir/shelyak_usis
%_udevrulesdir/80-dbk21-camera.rules
%_udevrulesdir/99-indi_auxiliary.rules

%files -n lib%name-common
%doc ChangeLog README
%_datadir/%name

%files -n lib%name%soversion
%_libdir/%name%soversion
%_libdir/lib%{name}AlignmentDriver.so.%{soversion}*
%_libdir/lib%{name}client.so.%{soversion}*
%_libdir/lib%{name}driver.so.%{soversion}*
%_libdir/lib%{name}lx200.so.%{soversion}*
%if_with qt
%_libdir/lib%{name}clientqt.so.%{soversion}*
%endif

%files -n lib%name-devel
%_includedir/lib%name
%_libdir/lib%{name}AlignmentDriver.so
%_libdir/lib%{name}client.so
%_libdir/lib%{name}driver.so
%_libdir/lib%{name}lx200.so
%if_with qt
%_libdir/lib%{name}clientqt.so
%endif
%_pkgconfigdir/lib%{name}.pc

%files -n lib%name-devel-static
%_libdir/lib%{name}AlignmentClient.a

%changelog
* Mon Jun 15 2026 Ulysses Apokin <ulysses@altlinux.org> 2.2.3.1-alt1
- New version.

* Tue May 05 2026 Ulysses Apokin <ulysses@altlinux.org> 2.2.1.1-alt1
- New version.

* Wed Apr 01 2026 Ulysses Apokin <ulysses@altlinux.org> 2.1.9-alt3
- Used the default linker instead of the bfd linker on all arches.

* Sat Mar 07 2026 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.1.9-alt2
- e2k build fix

* Wed Feb 18 2026 Ulysses Apokin <ulysses@altlinux.org> 2.1.9-alt1
- Initial build for Sisyphus instead of obsolete indilib.
