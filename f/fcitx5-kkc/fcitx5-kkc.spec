%define _unpackaged_files_terminate_build 1
%global __provides_exclude_from ^%_libdir/fcitx5/.*\\.so$

Name: fcitx5-kkc
Version: 5.1.11
Release: alt1

Summary: Libkkc input method support for Fcitx5
License: GPLv3+
Group: Graphical desktop/Other

Url: https://github.com/fcitx/fcitx5-kkc
Vcs: https://github.com/fcitx/fcitx5-kkc

Source: %name-%version.tar.xz

Requires: icon-theme-hicolor
Requires: fcitx5-data
Requires: libkkc-data

BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: /usr/bin/gettext
BuildRequires: gnupg2
BuildRequires: ctest
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: python3-module-ninja_syntax
BuildRequires: extra-cmake-modules
BuildRequires: cmake(Fcitx5Core)
BuildRequires: cmake(Fcitx5Qt5WidgetsAddons)
BuildRequires: pkgconfig(kkc-1.0)
BuildRequires: pkgconfig(Qt6Core) >= 5.7
BuildRequires: pkgconfig(Qt6Gui) >= 5.7
BuildRequires: pkgconfig(Qt6Widgets) >= 5.7
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: gettext-tools
BuildRequires: /usr/bin/appstream-util

%description
This provides libkkc input method support for fcitx5. Released under GPL3+.

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
%doc README.md
%doc --no-dereference LICENSES/GPL-3.0-or-later.txt
%_libdir/fcitx5/kkc.so
%_libdir/fcitx5/qt?/libfcitx5-kkc-config.so

%_datadir/fcitx5/addon/kkc.conf
%_datadir/fcitx5/inputmethod/kkc.conf

%dir %_datadir/fcitx5/kkc
%_datadir/fcitx5/kkc/dictionary_list
%_datadir/fcitx5/kkc/rule

%_datadir/icons/hicolor/*/apps/*.png
%_metainfodir/org.fcitx.Fcitx5.Addon.Kkc.metainfo.xml
%changelog
* Fri Oct 02 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.1.11-alt1
- 5.1.0 -> 5.1.11 (ALT #52981)

* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 5.1.0-alt1_1
- update to new release by fcimport

* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 5.0.10-alt1_2
- new version

