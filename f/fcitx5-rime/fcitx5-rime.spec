%define _unpackaged_files_terminate_build 1
%global __provides_exclude_from ^%_libdir/fcitx5/.*\\.so$

Name: fcitx5-rime
Version: 5.1.16
Release: alt1

Summary: RIME support for Fcitx
License: LGPLv2+
Group: Graphical desktop/Other

Url: https://github.com/fcitx/fcitx5-rime
Vcs: https://github.com/fcitx/fcitx5-rime

Source: %name-%version.tar.xz

Requires: icon-theme-hicolor
Requires: fcitx5-data
Requires: brise

BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: /usr/bin/gettext
BuildRequires: gnupg2
BuildRequires: brise
BuildRequires: ctest
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: python3-module-ninja_syntax
BuildRequires: gettext-tools
BuildRequires: pkgconfig(Fcitx5Core)
BuildRequires: pkgconfig(Fcitx5Module)
BuildRequires: pkgconfig(rime)
BuildRequires: /usr/bin/appstream-util

%description
RIME(a..a..e..e..a..a..a..a..) is mainly a Traditional Chinese
input method engine.

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

%check
%fedora_v2_ctest

%files -f %name.lang
%doc --no-dereference LICENSES/LGPL-2.1-or-later.txt
%doc README.md
%_libdir/fcitx5/librime.so
%_datadir/fcitx5/*/rime.conf
%_datadir/icons/hicolor/*/*/*
%_datadir/rime-data/fcitx5.yaml
%_metainfodir/org.fcitx.Fcitx5.Addon.Rime.metainfo.xml

%changelog
* Fri Oct 02 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.1.16-alt1
- 5.1.2 -> 5.1.16 (ALT #52985)

* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 5.1.2-alt1_1
- update

* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 5.0.14-alt1_2
- new version

