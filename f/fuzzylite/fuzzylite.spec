%def_disable check

# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var

# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name fuzzylite
%define major   6.0
%define libname lib%name%major
%define devname lib%name-devel

Name: fuzzylite
Version: 6.0
Release: alt1
Summary: A fuzzy logic control library in C++
Group: System/Libraries
License: GPL-3.0-only
Url: http://www.fuzzylite.com

Source: %name-%version.tar
%if_disabled check
%else
# PATCH-FIX-UPSTREAM fix-tests.patch -- https://github.com/fuzzylite/fuzzylite/issues/94
Patch0: fix-tests.patch
%endif

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake 
#ccmake 
%if_disabled check
%else
BuildRequires: ctest
BuildRequires: catch2-devel
%endif

Requires: %libname = %EVR

%description
Fuzzylite is a free and open-source fuzzy logic control library
programmed in C++ for multiple platforms (Windows, Linux, Mac, iOS).
Its goal is to allow you to easily create fuzzy logic controllers
in a few steps utilizing object-oriented programming without
requiring any third-party libraries.

This package contains the %name console application.

%package -n %libname
Summary: A fuzzy logic control library in C++
Group: System/Libraries

%description -n %libname
Fuzzylite is a free and open-source fuzzy logic control library
programmed in C++ for multiple platforms (Windows, Linux, Mac, iOS).
Its goal is to allow you to easily create fuzzy logic controllers
in a few steps utilizing object-oriented programming without
requiring any third-party libraries.

%package -n %devname
Summary: Development files for %name
Group: Development/C++
Requires: %libname = %EVR
Provides: %devname = %EVR

%description -n %devname
Development headers and library for %name.

%prep
%setup
%autopatch -p1

%build
%add_optflags -Wno-error

# Build with SSE / NEON prevent https://github.com/fuzzylite/fuzzylite/issues/89
%ifarch x86_64
#add_optflags -mfpmath=sse -msse2
%else
%ifarch aarch64
%add_optflags -O2 -ftree-vectorize
%endif
%endif

pushd %name
%cmake -DFL_BUILD_STATIC=OFF \
       -DFL_BACKTRACE=ON \
       -DFL_CPP11=ON \
%if_disabled check
       -DFL_BUILD_TESTS=OFF \
%else
       -DFL_BUILD_TESTS=ON \
%endif
       -DFL_INSTALL_LIBDIR=%_libdir \
       -DFL_VERSION=%major
%cmake_build
popd

%install
pushd %name
%cmakeinstall_std
install -m 644 -D fuzzylite.1 %buildroot/%_man1dir/fuzzylite.1
popd

%check
%if_disabled check
# Fails without sse / neon
%ifarch x86_64 aarch64
cd %name/%_cmake__builddir
ctest -VV
%endif
%endif

%files
%_bindir/%name
%_man1dir/fuzzylite.1*

%files -n %libname
%_libdir/lib%name.so.%{major}*

%files -n %devname
%doc AUTHOR NEWS README.md
%_includedir/fl/
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%changelog
* Thu Sep 15 2022 Anton Midyukov <antohami@altlinux.org> 6.0-alt1
- new version 6.0

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 5.1-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 5.1-alt2
- NMU: remove %ubt from release

* Mon Apr 30 2018 Anton Midyukov <antohami@altlinux.org> 5.1-alt1%ubt
- Initial build for ALT Sisyphus
