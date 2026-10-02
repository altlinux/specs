%define _unpackaged_files_terminate_build 1
%global __provides_exclude_from ^%_libdir/fcitx5/.*\\.so$
%def_without check

Name: fcitx5-chinese-addons
Version: 5.1.15
Release: alt1

Summary: Chinese related addon for fcitx5
License: LGPLv2+
Group: Graphical desktop/Other

Url: https://github.com/fcitx/fcitx5-chinese-addons
Vcs: https://github.com/fcitx/fcitx5-chinese-addons

Source: %name-%version.tar.xz
Source1: py_stroke-20250329.tar.gz
Source2: py_table-20121124.tar.gz

Requires: icon-theme-hicolor
Requires: %name-data = %version-%release
Requires: fcitx5-lua
Requires: fcitx5-data

ExcludeArch: i586

BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: /usr/bin/gettext
BuildRequires: boost-devel
BuildRequires: qt5-base-devel
BuildRequires: gnupg2
BuildRequires: boost-complete
BuildRequires: ctest cmake
BuildRequires: extra-cmake-modules
BuildRequires: fcitx5-qt-devel
BuildRequires: fcitx5-lua-devel
BuildRequires: gcc-c++
BuildRequires: libime-devel
BuildRequires: ninja-build
BuildRequires: python3-module-ninja_syntax
BuildRequires: gettext-tools
BuildRequires: libasprintf-devel
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(Qt5WebKit)
BuildRequires: pkgconfig(Qt5WebKitWidgets)
BuildRequires: pkgconfig(opencc)
BuildRequires: pkgconfig(Fcitx5Core)
BuildRequires: pkgconfig(Fcitx5Module)
BuildRequires: /usr/bin/appstream-util
BuildRequires: nlohmann-json-devel
BuildRequires: qt6-base-devel
BuildRequires: qt6-webengine-devel

%description
This provides pinyin and table input method
support for fcitx5. Released under LGPL-2.1+.

im/pinyin/emoji.txt is derived from Unicode
CLDR with modification.

%package data
Group: Graphical desktop/Other
Summary: Data files of %name
BuildArch: noarch
Requires: icon-theme-hicolor
Requires: fcitx5-lua
Requires: fcitx5-data

%description data
The %name-data package provides shared data for %name.

%package devel
Group: Graphical desktop/Other
Summary: Development files for %name
Requires: %name = %version-%release

%description devel
devel files for fcitx5-chinese-addons

%prep
%setup
cp -a %SOURCE1 modules/pinyinhelper/
cp -a %SOURCE2 modules/pinyinhelper/

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

%check
# workaround for a testing failure due to not finding .dict files
%fedora_v2_ctest

%files -f %name.lang
%doc --no-dereference LICENSES/LGPL-2.1-or-later.txt
%doc README.md
%_bindir/scel2org5
%_libdir/fcitx5/*.so
%_libdir/fcitx5/qt?/*.so

%files data
%_datadir/fcitx5
%_datadir/icons/hicolor/*/apps/*
%_metainfodir/org.fcitx.Fcitx5.Addon.ChineseAddons.metainfo.xml

%files devel
%_includedir/Fcitx5/Module/fcitx-module/*
%_libdir/cmake/Fcitx5Module*

%changelog
* Thu Oct 01 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.1.15-alt1
- 5.1.1 -> 5.1.15 (ALT #53000)
- dropped old patches
- ExcludeArch: i586.

* Mon Nov 24 2025 Nazarov Denis <nenderus@altlinux.org> 5.1.1-alt2_1.1
- NMU: fix build with fmt 12

* Tue May 28 2024 Ivan A. Melnikov <iv@altlinux.org> 5.1.1-alt2_1
- NMU: fix FTBFS (ALT#49537)

* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 5.1.1-alt1_1
- update

* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 5.0.15-alt1_2
- new version

