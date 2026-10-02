%define _unpackaged_files_terminate_build 1
%global __provides_exclude_from ^%_libdir/fcitx5/.*\\.so$

Name: fcitx5-libthai
Version: 5.1.11
Release: alt1

Summary: Libthai Wrapper for Fcitx5
License: GPLv2+
Group: Graphical desktop/Other

Url: https://github.com/fcitx/fcitx5-libthai
Vcs: https://github.com/fcitx/fcitx5-libthai

Source: %name-%version.tar.xz

Requires: icon-theme-hicolor
Requires: fcitx5-data

BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: /usr/bin/gettext
BuildRequires: gnupg2
BuildRequires: ctest
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: python3-module-ninja_syntax
BuildRequires: cmake(Fcitx5Core)
BuildRequires: pkgconfig(libthai)
BuildRequires: gettext-tools
BuildRequires: /usr/bin/appstream-util

%description
%summary.

%prep
%setup

%build
%fedora_v2_cmake -GNinja
%fedora_v2_cmake_build

%install
%fedora_v2_cmake_install
appstream-util validate-relax --nonet %buildroot%_metainfodir/*.metainfo.xml
%find_lang %name

%files -f %name.lang
%doc --no-dereference LICENSES/GPL-2.0-or-later.txt
%_libdir/fcitx5/libthai.so
%_datadir/fcitx5/addon/libthai.conf
%_datadir/fcitx5/inputmethod/libthai.conf
%_metainfodir/org.fcitx.Fcitx5.Addon.LibThai.metainfo.xml

%changelog
* Fri Oct 02 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.1.11-alt1
- 5.1.0 -> 5.1.11 (ALT #52991)

* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 5.1.0-alt1_1
- update to new release by fcimport

* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 5.0.10-alt1_1
- new version

