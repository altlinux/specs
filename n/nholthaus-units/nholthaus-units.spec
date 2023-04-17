%define _unpackaged_files_terminate_build 1
%define oname units
%def_enable docs

Name: nholthaus-units
Version: 2.3.3
Release: alt1
Summary: A compile-time, header-only, dimensional analysis and unit conversion library
Group: Development/C++
License: MIT

Url: http://nholthaus.github.io/units/

Source: %oname-%version.tar
Patch: %oname-alt-install.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++
%if_enabled docs
BuildRequires: doxygen
%endif

BuildArch: noarch

%description
A compile-time, header-only, dimensional analysis library built on c++14 with
no dependencies.

%package devel
Summary: A compile-time, header-only, dimensional analysis and unit conversion library 
Group:   Development/C++

%description devel
A compile-time, header-only, dimensional analysis library built on c++14 with
no dependencies.

%if_enabled docs
%package docs
Summary: Unit conversion library documentation
Group:   Documentation

%description docs
Documentation for a compile-time, header-only, dimensional analysis library built on c++14 with
no dependencies.
%endif

%prep
%setup -n %oname-%version
%patch -p1

%build
%cmake \
%if_enabled docs
  -DBUILD_DOCS=ON \
%endif
  -DCMAKE_INSTALL_LIBDIR:PATH=%_datadir \
  -DBUILD_TESTS=OFF
%cmake_build

%install
%cmakeinstall_std
%if_enabled docs
mkdir -p %buildroot%_man3dir
cp -ar docs/man/man3/* %buildroot%_man3dir/
%endif

%files devel
%doc LICENSE
%doc *.md
%_includedir/*
%_datadir/cmake/*

%if_enabled docs
%files docs
%doc docs/html
%_man3dir/*
%endif

%changelog
* Wed Mar 29 2023 L.A. Kostis <lakostis@altlinux.ru> 2.3.3-alt1
- Initial build for ALTLinux.
