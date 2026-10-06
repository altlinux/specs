%define _unpackaged_files_terminate_build 1
%global __provides_exclude_from ^%_libdir/fcitx5/.*\\.so$

Name: fcitx5-skk
Version: 5.1.11
Release: alt1

Summary: Japanese SKK (Simple Kana Kanji) Engine for Fcitx5
License: GPLv3+
Group: Graphical desktop/Other

Url: https://github.com/fcitx/fcitx5-skk
Vcs: https://github.com/fcitx/fcitx5-skk

Source: %name-%version.tar.xz

Requires: skkdic
Requires: icon-theme-hicolor
Requires: fcitx5-data

BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: /usr/bin/gettext
BuildRequires: gnupg2
BuildRequires: gcc-c++
BuildRequires: ctest
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: python3-module-ninja_syntax
BuildRequires: extra-cmake-modules
BuildRequires: fcitx5-qt-devel
BuildRequires: pkgconfig(Fcitx5Core)
BuildRequires: pkgconfig(libskk)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: gettext-tools
BuildRequires: intltool
BuildRequires: /usr/bin/appstream-util

%description
Fcitx5-skk is an SKK (Simple Kana Kanji) engine for Fcitx.  It provides
Japanese input method using libskk.

%prep
%setup

%build
%fedora_v2_cmake -GNinja
%fedora_v2_cmake_build

%install
%fedora_v2_cmake_install
# convert symlinked icons to copied icons, this will help co-existing with
# fcitx4
for iconfile in $(find %buildroot%_datadir/icons -type l)
do
  origicon=$(readlink -f ${iconfile})
  rm -f ${iconfile}
  cp ${origicon} ${iconfile}
done
appstream-util validate-relax --nonet %buildroot%_metainfodir/*.metainfo.xml
%find_lang %name

%files -f %name.lang
%doc --no-dereference LICENSES/GPL-3.0-or-later.txt
%doc README.md
%_libdir/fcitx5/qt?/libfcitx5-skk-config.so
%_libdir/fcitx5/skk.so
%_datadir/fcitx5/addon/skk.conf
%_datadir/fcitx5/inputmethod/skk.conf
%dir %_datadir/fcitx5/skk
%_datadir/fcitx5/skk/dictionary_list
%_datadir/icons/hicolor/*/apps/*.png
%_metainfodir/org.fcitx.Fcitx5.Addon.Skk.metainfo.xml

%changelog
* Tue Oct 06 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.1.11-alt1
- 5.1.0 -> 5.1.11

* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 5.1.0-alt1_1
- update to new release by fcimport

* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 5.0.13-alt1_2
- new version

