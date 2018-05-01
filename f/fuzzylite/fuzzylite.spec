# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var

# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name fuzzylite
%define major   5.1
%define libname lib%name%major
%define devname lib%name-devel

Name: fuzzylite
Version: 5.1
Release: alt1%ubt
Summary: A fuzzy logic control library in C++
Group: System/Libraries
# Next version (6.0) will be: GPLv3 or ASL 2.0
License: LGPLv3
Url: http://www.fuzzylite.com

Source: %name-%version.tar
Patch0: fuzzylite-5.1-fuzzylite.pc-configurable-for-different-architectures.patch

BuildRequires(pre): rpm-macros-cmake rpm-build-ubt
BuildRequires: gcc-c++
BuildRequires: ccmake cmake ctest
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
%patch0 -p1

%build
pushd %name
%cmake -DFL_BUILD_STATIC=OFF \
       -DFL_BACKTRACE=ON \
       -DFL_CPP11=ON \
       -DFL_INSTALL_LIBDIR=%_libdir
%cmake_build
popd

%install
pushd %name
%cmakeinstall_std
popd

%files
%_bindir/%name

%files -n %libname
%_libdir/lib%name.so.%{major}*

%files -n %devname
%doc AUTHOR LICENSE NEWS README.md
%_includedir/fl/
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%changelog
* Mon Apr 30 2018 Anton Midyukov <antohami@altlinux.org> 5.1-alt1%ubt
- Initial build for ALT Sisyphus
