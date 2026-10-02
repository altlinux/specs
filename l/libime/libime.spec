%define _unpackaged_files_terminate_build 1
%add_optflags %optflags_shared

Name: libime
Version: 1.1.17
Release: alt1

Summary: This is a library to support generic input method implementation
Group: Development/C
License: LGPLv2+ and MIT and BSD

Url: https://github.com/fcitx/libime
Vcs: https://github.com/fcitx/libime

Source: %name-%version.tar.xz
Source1: kenlm.tar
Source2: lm_sc.arpa-20260629.tar.zst
Source3: dict-20260907.tar.zst
Source4: table-20240108.tar.zst

Requires: %name-data

BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat rpm-build-python3
BuildRequires: boost-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-program_options-devel
BuildRequires: liblzma-devel
BuildRequires: openmpi-devel
BuildRequires: python3-devel
BuildRequires: gnupg2
BuildRequires: ctest
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: python3-module-ninja_syntax
BuildRequires: gcc-c++
BuildRequires: fcitx5-devel
BuildRequires: boost-complete
BuildRequires: extra-cmake-modules
BuildRequires: python3
BuildRequires: doxygen
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(eigen3)

%description
This is a library to support generic input method implementation.

%package data
Group: Development/C
Summary: Data files of %name
BuildArch: noarch
Requires: %name = %EVR
Requires: icon-theme-hicolor

%description data
The %name-data package provides shared data for %name.

%package devel
Group: Development/C
Summary: Development files for %name
Requires: %name = %EVR
Requires: boost-complete

%description devel
Development files for %name

%prep
%setup
tar -xf %SOURCE1 -C src/libime/core/
cp -a %SOURCE2 data/
cp -a %SOURCE3 data/
cp -a %SOURCE4 data/

%build
%fedora_v2_cmake -GNinja
%fedora_v2_cmake_build

%install
%fedora_v2_cmake_install

%check
%fedora_v2_ctest

%files
%doc --no-dereference LICENSES/LGPL-2.1-or-later.txt src/libime/core/kenlm/LICENSE
%doc README.md
%_bindir/%{name}_history
%_bindir/%{name}_pinyindict
%_bindir/%{name}_prediction
%_bindir/%{name}_slm_build_binary
%_bindir/%{name}_tabledict
%_bindir/%{name}_migrate_fcitx4_pinyin
%_bindir/%{name}_migrate_fcitx4_table
%_libdir/libIMECore.so.0
%_libdir/libIMEPinyin.so.0
%_libdir/libIMETable.so.0
# upstream's soname and soversion dont match
# libxxx.so.X* won't work
%_libdir/libIMECore.so.*.*
%_libdir/libIMEPinyin.so.*.*
%_libdir/libIMETable.so.*.*
%dir %_libdir/%name
%_libdir/%name/zh_CN.lm
%_libdir/%name/zh_CN.lm.predict

%files data
%dir %_datadir/%name
%_datadir/%name/*.dict

%files devel
%_libdir/libIMECore.so
%_libdir/libIMEPinyin.so
%_libdir/libIMETable.so
%_libdir/cmake/LibIME*
%_includedir/LibIME/

%changelog
* Thu Oct 01 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.1.17-alt1
- 1.1.2 -> 1.1.17 (ALT #52977)
- drop old patch
- spec cleanup

* Mon Jul 27 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.1.2-alt1_3
- NMU: fixed FTBFS

* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 1.1.2-alt1_2
- update to new release by fcimport

* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 1.1.1-alt1_1
- update to new release by fcimport

* Thu Apr 20 2023 Igor Vlasenko <viy@altlinux.org> 1.0.17-alt1_1
- update to new release by fcimport

* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 1.0.16-alt1_2
- update to new release by fcimport

* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 1.0.15-alt1_1
- update to new release by fcimport

* Tue Sep 20 2022 Igor Vlasenko <viy@altlinux.org> 1.0.14-alt1_1
- new version

