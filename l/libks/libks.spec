%define soversion 2
Name: libks
Version: 2.0.6
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
%_libdir/libks2.so.%{soversion}*

%files devel
%doc %_docdir/libks2/copyright
%_includedir/libks2
%_libdir/pkgconfig/libks2.pc
%_libdir/libks2.so

%changelog
* Tue Jul 30 2024 Anton Farygin <rider@altlinux.ru> 2.0.6-alt1
- 2.0.5 -> 2.0.6

* Mon Apr 29 2024 Anton Farygin <rider@altlinux.ru> 2.0.5-alt1
- 2.0.4 -> 2.0.5

* Fri Apr 12 2024 Anton Farygin <rider@altlinux.ru> 2.0.4-alt1
- 1.8.2 -> 2.0.4

* Tue Feb 28 2023 Anton Farygin <rider@altlinux.ru> 1.8.2-alt1
- 1.8.0 -> 1.8.2

* Sat Feb 12 2022 Anton Farygin <rider@altlinux.ru> 1.8.0-alt1
- 1.7.0 -> 1.8.0

* Thu Nov 25 2021 Anton Farygin <rider@altlinux.ru> 1.7.0-alt1
- first build for ALT
