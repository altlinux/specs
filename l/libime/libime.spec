# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: boost-devel boost-filesystem-devel boost-program_options-devel openmpi-devel python3-devel rpm-build-python3
# END SourceDeps(oneline)
Group: Development/C
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 2

Name:       libime  
Version:    1.0.16
License:    LGPLv2+ and MIT and BSD
Release:    alt1_2
Summary:    This is a library to support generic input method implementation
URL:        https://github.com/fcitx/libime
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}_dict.tar.xz
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}_dict.tar.xz.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires: gnupg2
BuildRequires: ctest cmake
BuildRequires: ninja-build python3-module-ninja_syntax
BuildRequires: gcc-c++
BuildRequires: fcitx5-devel
BuildRequires: boost-complete
BuildRequires: extra-cmake-modules
BuildRequires: python3
BuildRequires: doxygen
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(eigen3)
Requires:      %{name}-data
Source44: import.info


%description
This is a library to support generic input method implementation.

%package data
Group: Development/C
Summary:        Data files of %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       icon-theme-hicolor

%description data
The %{name}-data package provides shared data for %{name}.

%package devel
Group: Development/C
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       boost-complete

%description devel
Development files for %{name}

%prep
%setup -q


%build
%{fedora_v2_cmake} -GNinja
%fedora_v2_cmake_build

%install
%fedora_v2_cmake_install

%check
%fedora_v2_ctest

%files
%doc --no-dereference LICENSES/LGPL-2.1-or-later.txt src/libime/core/kenlm/LICENSE
%doc README.md 
%{_bindir}/%{name}_history
%{_bindir}/%{name}_pinyindict
%{_bindir}/%{name}_prediction
%{_bindir}/%{name}_slm_build_binary
%{_bindir}/%{name}_tabledict
%{_bindir}/%{name}_migrate_fcitx4_pinyin
%{_bindir}/%{name}_migrate_fcitx4_table
%{_libdir}/libIMECore.so.0
%{_libdir}/libIMEPinyin.so.0
%{_libdir}/libIMETable.so.0
# upstream's soname and soversion dont match 
# libxxx.so.X* won't work
%{_libdir}/libIMECore.so.*.*
%{_libdir}/libIMEPinyin.so.*.*
%{_libdir}/libIMETable.so.*.*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/zh_CN.lm
%{_libdir}/%{name}/zh_CN.lm.predict

%files data
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.dict

%files devel
%{_libdir}/libIMECore.so
%{_libdir}/libIMEPinyin.so
%{_libdir}/libIMETable.so
%{_libdir}/cmake/LibIME*
%{_includedir}/LibIME/



%changelog
* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 1.0.16-alt1_2
- update to new release by fcimport

* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 1.0.15-alt1_1
- update to new release by fcimport

* Tue Sep 20 2022 Igor Vlasenko <viy@altlinux.org> 1.0.14-alt1_1
- new version

