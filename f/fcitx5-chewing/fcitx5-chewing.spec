%define _unpackaged_files_terminate_build 1
%global __provides_exclude_from ^%_libdir/fcitx5/.*\\.so$

Name: fcitx5-chewing
Version: 5.1.13
Release: alt1

Summary: Chewing Wrapper for Fcitx
License: LGPLv2+
Group: Graphical desktop/Other

Url: https://github.com/fcitx/fcitx5-chewing
Vcs: https://github.com/fcitx/fcitx5-chewing

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
BuildRequires: intltool
BuildRequires: ninja-build
BuildRequires: python3-module-ninja_syntax
BuildRequires: pkgconfig(Fcitx5Core)
BuildRequires: pkgconfig(chewing)
BuildRequires: gettext-tools
BuildRequires: /usr/bin/appstream-util

%description
fcitx5-chewing is a Chewing Wrapper for Fcitx.

Chewing is a set of free intelligent Chinese
Phonetic IME.

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
%doc --no-dereference LICENSES/LGPL-2.1-or-later.txt
%doc README.md
%_libdir/fcitx5/libchewing.so
%_datadir/fcitx5/addon/chewing.conf
%_datadir/fcitx5/inputmethod/chewing.conf
%_datadir/icons/hicolor/*/apps/fcitx-chewing.png
%_datadir/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx-chewing.png
%_metainfodir/org.fcitx.Fcitx5.Addon.Chewing.metainfo.xml

%changelog
* Fri Oct 02 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.1.13-alt1
- 5.1.0 -> 5.1.13 (ALT #52990)

* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 5.1.0-alt1_1
- update to new release by fcimport

* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 5.0.12-alt1_2
- new version

