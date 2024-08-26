%define soversion 1
Name: librime
Version: 1.11.2
Release: alt1
License: GPL-3.0-only
Summary: Rime Input Method Engine Library
Group: Development/C
Url: https://rime.im/
VCS: https://github.com/rime/librime/
Source0: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires(pre): rpm-macros-cmake
BuildRequires: ctest cmake, opencc-devel
BuildRequires: boost-complete >= 1.46
BuildRequires: zlib-devel
BuildRequires: libglog-devel, libgtest-devel
BuildRequires: libyaml-cpp-devel
BuildRequires: libgflags-devel
BuildRequires: libmarisa-devel
BuildRequires: libleveldb-devel

%description
Rime Input Method Engine Library

Support for shape-based and phonetic-based input methods,
including those for Chinese dialects.

A selected dictionary in Traditional Chinese,
powered by opencc for Simplified Chinese output.

%package -n librime%soversion
Summary: Shared library for the %name library
Group: System/Libraries

%description -n librime%soversion
Rime Input Method Engine Library

Support for shape-based and phonetic-based input methods,
including those for Chinese dialects.

A selected dictionary in Traditional Chinese,
powered by opencc for Simplified Chinese output.

This package contains the shared library.

%package devel
Group: Development/C
Summary: Development files for %name
Requires: librime%soversion = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package tools
Group: Development/C
Summary: Tools for %name
Requires: librime1 = %EVR

%description tools
The %name-tools package contains tools for %name.

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files -n librime%soversion
%doc README.md LICENSE
%_libdir/librime.so.%soversion
%_libdir/librime.so.%soversion.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/rime.pc
%dir %_datadir/cmake/rime
%_datadir/cmake/rime/RimeConfig.cmake

%files tools
%_bindir/rime_deployer
%_bindir/rime_dict_manager
%_bindir/rime_patch
%_bindir/rime_table_decompiler

%changelog
* Mon Aug 26 2024 Anton Farygin <rider@altlinux.ru> 1.11.2-alt1
- 1.11.2

* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 1.9.0-alt1_1
- update to new release by fcimport

* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 1.8.5-alt1_3
- update to new release by fcimport

* Thu Apr 20 2023 Igor Vlasenko <viy@altlinux.org> 1.8.5-alt1_1
- update to new release by fcimport

* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 1.8.4-alt1_2
- update to new release by fcimport

* Wed Sep 28 2022 Igor Vlasenko <viy@altlinux.org> 1.7.3-alt1_2
- new version

