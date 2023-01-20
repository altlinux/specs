%define _unpackaged_files_terminate_build 1
%global optflags_lto %optflags_lto -ffat-lto-objects

%def_with check

%define soname 1
%define pkgname libversion

Name:%pkgname%soname
Version: 3.0.2
Release: alt1

Summary: Advanced version string comparison library
License: MIT
Group: Development/C
URL: https://github.com/repology/libversion
VCS: https://github.com/repology/libversion.git

Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++
%if_with check
BuildRequires: ctest
%endif

%description
Need to compare software, package or whatever versions?
Comparing 1.0 and 1.1 could be easy, but are you ready 
for more complex cases like 1.2-x.3~alpha4? libversion 
is, which is proven by using the library in Repology 
project which relies on comparing software version strings, 
even if they are written in different formats.

%package -n %pkgname-devel
Summary: Development files of %pkgname
Group: Development/C
Requires: %name = %version-%release

%description -n %pkgname-devel
%summary

%package -n %pkgname-tools
Summary: Version string comparison tools from %pkgname
Group: Development/Tools
Requires: %name = %version-%release

%description -n %pkgname-tools
%summary

%prep
%setup
%autopatch -p1

%build
%cmake
%cmake_build

%install
%cmake_install
# delete static library files
rm %buildroot%_libdir/%pkgname.a

%check
pushd %_cmake__builddir
ctest -V
popd

%files
%_libdir/%pkgname.so.%soname
%_libdir/%pkgname.so.%soname.*

%files -n %pkgname-tools
%_bindir/*

%files -n %pkgname-devel
%doc COPYING README.md CHANGES.md doc/ALGORITHM.md
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/%pkgname.pc
%dir %_libdir/cmake/%pkgname/*.cmake

%changelog
* Thu Dec 08 2022 Elizaveta Morozova <morozovaes@altlinux.org> 3.0.2-alt1
- Initial build fot ALT


