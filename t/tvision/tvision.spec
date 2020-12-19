Name:       tvision
Version:    586
Release:    alt1
License:    MIT
Group:      Development/C++
URL:        https://github.com/magiblot/tvision
Source:     %name-r%version.tar.gz
Summary:    A modern port of Turbo Vision 2.0
Patch:      tvision-r586-shared.patch
PAtch1:     tvision-r586-nox86.patch

# Automatically added by buildreq on Sat Dec 19 2020
# optimized out: cmake-modules glibc-kernheaders-generic glibc-kernheaders-x86 libncurses-devel libsasl2-3 libstdc++-devel libtinfo-devel python2-base sh4
BuildRequires: cmake gcc-c++ libgpm-devel libncursesw-devel

%description
A modern port of Turbo Vision 2.0, the classical framework for
text-based user interfaces. Now cross-platform and with Unicode support.

%package -n lib%name
Group:      Development/C++
Summary:    A modern port of Turbo Vision 2.0, shared library
%description -n lib%name
%summary

%package devel
Group:      Development/C++
Summary:    A modern port of Turbo Vision 2.0, development environment
Provides:   lib%name-devel = %version-%release
%description devel
%summary

%package examples
Group:      Development/C++
Summary:    A modern port of Turbo Vision 2.0, source and binary examples
%description examples
%summary

%prep
%setup -n %name-r%version
%patch -p0
%patch1 -p0

%build
%cmake
%cmake_build

%install
install -d %buildroot%_libdir
cp -a BUILD/libtvision.so* %buildroot%_libdir/
install -d %buildroot%_includedir
cp -a include/tvision %buildroot%_includedir/
install -d %buildroot%_bindir
install BUILD/tv* %buildroot%_bindir/

%files -n lib%name
%_libdir/*.so.*

%files devel
%doc README.md
%_includedir/%name
%_libdir/*.so

%files examples
%doc examples
%_bindir/*

%changelog
* Sat Dec 19 2020 Fr. Br. George <george@altlinux.ru> 586-alt1
- Initial release for ALT

