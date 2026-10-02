%define _unpackaged_files_terminate_build 1
%global __provides_exclude_from ^%_libdir/fcitx5/.*\\.so$

Name: fcitx5-m17n
Version: 5.1.8
Release: alt1

Summary: m17n Wrapper for Fcitx5
License: LGPLv2+
Group: Graphical desktop/Other

Url: https://github.com/fcitx/fcitx5-m17n
Vcs: https://github.com/fcitx/fcitx5-m17n

Source: %name-%version.tar.xz

Requires: fcitx5-data
Requires: pkgconfig(m17n-db)

BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: /usr/bin/gettext
BuildRequires: gnupg2
BuildRequires: ctest
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: python3-module-ninja_syntax
BuildRequires: gettext-tools
BuildRequires: cmake(Fcitx5Core)
BuildRequires: libfmt-devel
BuildRequires: pkgconfig(m17n-gui) > 1.6.3
BuildRequires: pkgconfig(m17n-db)
BuildRequires: /usr/bin/appstream-util

%description
M17N is a large collection of input method, which can cover
quite a lot languages in the world, including Latin, Arabic,
etc.

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
%doc --no-dereference LICENSES/LGPL-2.1-or-later.txt
%doc README.md
%_libdir/fcitx5/libm17n.so
%_datadir/fcitx5/addon/m17n.conf
%dir %_datadir/fcitx5/m17n
%_datadir/fcitx5/m17n/default
%_metainfodir/org.fcitx.Fcitx5.Addon.M17N.metainfo.xml

%changelog
* Fri Oct 02 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.1.8-alt1
- 5.1.0 -> 5.1.8 (ALT #52984)

* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 5.1.0-alt1_1
- update to new release by fcimport

* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 5.0.10-alt1_2
- new version

