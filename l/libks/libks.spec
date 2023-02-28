%define soversion 1
Name: libks
Version: 1.8.2
Release: alt1
Summary: Foundational support for signalwire C products 
Group: System/Libraries
License: MIT
Url: https://github.com/signalwire/libks
Source0: %name-%version.tar
Patch: %name-%version-%release.patch
BuildRequires: cmake ninja-build gcc-c++ rpm-build-ninja
BuildRequires: pkgconfig(uuid) pkgconfig(openssl)

%description
Foundational support for signalwire C products

%package -n %name%soversion
Summary: Foundational support for signalwire C products
Group: System/Libraries

%description -n %name%soversion
Foundational support for signalwire C products.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name%soversion = %EVR

%description devel
Development files for %name

%prep
%setup
%patch0 -p1

%build
%cmake  -DKS_PLAT_LIN=true \
 	-G Ninja \
	-DCMAKE_BUILD_TYPE=Release
%ninja_build -C %_cmake__builddir
cp copyright %_cmake__builddir/

%install
%ninja_install -C %_cmake__builddir

%files -n %name%soversion
%_libdir/libks.so.%{soversion}*

%files devel
%doc %_docdir/libks/copyright
%_includedir/libks
%_libdir/pkgconfig/libks.pc
%_libdir/libks.so

%changelog
* Tue Feb 28 2023 Anton Farygin <rider@altlinux.ru> 1.8.2-alt1
- 1.8.0 -> 1.8.2

* Sat Feb 12 2022 Anton Farygin <rider@altlinux.ru> 1.8.0-alt1
- 1.7.0 -> 1.8.0

* Thu Nov 25 2021 Anton Farygin <rider@altlinux.ru> 1.7.0-alt1
- first build for ALT
