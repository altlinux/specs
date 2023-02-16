%def_enable snapshot
%define _name mysofa

%def_enable check

Name: lib%_name
Version: 1.3.1
Release: alt1

Summary: Reader for AES SOFA files to get better HRTFs 
License: BSD-3-Clause
Group: System/Libraries
Url: https://github.com/hoene/libmysofa

Vcs: https://github.com/hoene/libmysofa.git
%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Source: %url/archive/v%version/%name-%version.tar
%endif

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ zlib-devel
%{?_enable_check:BuildRequires: ctest CUnit-devel nodejs}

%description
This is a simple set of C functions to read AES SOFA files, if they
contain HRTFs stored according to the AES69-2015 standard
(http://www.aes.org/publications/standards/search.cfm?docID=99)

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n %name-%version
# fix path to mysofa2json
sed -i 's;\/build\/;/%_cmake__builddir/;' tests/compare*.sh

%build
%cmake \
    -DBUILD_STATIC_LIBS=OFF \
    %{?_disable_check:-DBUILD_TEST=OFF}
%nil
%cmake_build

%install
%cmake_install

%check
export ARGS="--rerun-failed --output-on-failure"
%cmake_build -t test

%files
%_bindir/mysofa2json
%_libdir/%name.so.*
%_datadir/%name/
%doc README* SECURITY* LICENSE

%files devel
%_includedir/%_name.h
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%changelog
* Thu Feb 16 2023 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- first build for Sisyphus (v1.3.1-8-gbed445b)



