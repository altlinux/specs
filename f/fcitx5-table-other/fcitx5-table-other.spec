%define _unpackaged_files_terminate_build 1

Name: fcitx5-table-other
Version: 5.1.8
Release: alt1

Summary: Other tables for Fcitx5
License: GPLv3
Group: Graphical desktop/Other

Url: https://github.com/fcitx/fcitx5-table-other
Vcs: https://github.com/fcitx/fcitx5-table-other

Source: %name-%version.tar.xz

BuildArch: noarch

Requires: icon-theme-hicolor
Requires: fcitx5-data

BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: /usr/bin/gettext gcc-c++
BuildRequires: gnupg2
BuildRequires: ctest
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: ninja-build
BuildRequires: python3-module-ninja_syntax
BuildRequires: boost-complete
BuildRequires: cmake(Fcitx5Utils)
BuildRequires: libime-devel
BuildRequires: gettext-tools
BuildRequires: libappstream-glib
BuildRequires: libappstream-glib-gir

%description
Fcitx-table-other provides some other tables
for Fcitx, fork from ibus-table-others, scim-tables.

%prep
%setup

%build
%fedora_v2_cmake -GNinja -DCMAKE_PREFIX_PATH="%_libdir/cmake;%{_libdir}64/cmake"
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

%files
%doc --no-dereference LICENSES/GPL-3.0-only.txt
%doc README NEWS
%_datadir/fcitx5/inputmethod/*
%_datadir/fcitx5/table/*
%_datadir/icons/hicolor/*/apps/*
%_metainfodir/org.fcitx.Fcitx5.Addon.TableOther.metainfo.xml

%changelog
* Fri Oct 02 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.1.8-alt1
- 5.1.0 -> 5.1.8 (ALT #52994)

* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 5.1.0-alt1_1
- update to new release by fcimport

* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 5.0.10-alt1_2
- new version

