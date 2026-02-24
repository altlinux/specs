%define _unpackaged_files_terminate_build 1

%define soname 0

# Library build process puts it's major and minor version in the middle of
# library name. This macro is same as %%version, but with the patch part
# cut. Presumably it'll help with future version transitions.
%define version_majmin %(echo %version | awk -F. '{print $1"."$2}')

Name: collada-dom
Version: 2.5.0
Release: alt1

Summary: COLLADA Document Object Model (DOM) C++ Library
License: MIT
Group: Development/C++
Url: https://github.com/rdiankov/collada-dom
Vcs: https://github.com/rdiankov/collada-dom

Source: %name-%version.tar
Patch0: collada-dom-2.5.0-altlinux-boost-1.85-compat.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: boost-filesystem-devel
BuildRequires: liburiparser-devel
BuildRequires: libxml2-devel
BuildRequires: libminizip-devel
BuildRequires: zlib-devel

%description
The COLLADA Document Object Model (DOM) is an application programming
interface (API) that provides a C++ object representation of a COLLADA XML
instance document.

%package -n libcollada-dom%soname
Summary: COLLADA Document Object Model (DOM) C++ Library
Group: Development/C++

%description -n libcollada-dom%soname
The COLLADA Document Object Model (DOM) is an application programming
interface (API) that provides a C++ object representation of a COLLADA XML
instance document.

%package -n libcollada-dom-devel
Summary: COLLADA Document Object Model (DOM) C++ Library Development files
Group: Development/C++

%description -n libcollada-dom-devel
The COLLADA Document Object Model (DOM) C++ Library Development files

%prep
%setup
%autopatch -p1

# We don't need external libraries.
rm -rf ./dom/external-libs

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n libcollada-dom%soname
%doc licenses/license_e.txt licenses/dom_license_e.txt
%_libdir/libcollada-dom%version_majmin-dp.so.%soname
%_libdir/libcollada-dom%version_majmin-dp.so.%version

%files -n libcollada-dom-devel
%doc licenses/license_e.txt licenses/dom_license_e.txt
%_includedir/collada-dom%version_majmin/*
%_libdir/libcollada-dom%version_majmin-dp.so
%_pkgconfigdir/collada-dom.pc
%_pkgconfigdir/collada-dom-141.pc
%_pkgconfigdir/collada-dom-150.pc
%_cmakedir/collada_dom-%version_majmin/*

%changelog
* Fri Nov 7 2025 Pavel Petrykin <silverducks@altlinux.org> 2.5.0-alt1
- Initial build for Alt Linux.
