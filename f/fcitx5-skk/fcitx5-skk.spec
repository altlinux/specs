Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: /usr/bin/gettext
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 1

%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:       fcitx5-skk
Version:    5.1.0
Release:    alt1_1
Summary:    Japanese SKK (Simple Kana Kanji) Engine for Fcitx5
License:    GPLv3+
URL:        https://github.com/fcitx/fcitx5-skk
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  gcc-c++
BuildRequires:  ctest cmake
BuildRequires:  ninja-build python3-module-ninja_syntax
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-qt-devel
BuildRequires:  pkgconfig(Fcitx5Core)
BuildRequires:  pkgconfig(libskk)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  gettext-tools
BuildRequires:  intltool
BuildRequires:  /usr/bin/appstream-util
Requires:       skkdic
Requires:       icon-theme-hicolor
Requires:       fcitx5-data
Source44: import.info

%description
Fcitx5-skk is an SKK (Simple Kana Kanji) engine for Fcitx.  It provides
Japanese input method using libskk.

%prep
%setup -q


%build
%{fedora_v2_cmake} -DCMAKE_CXX_STANDARD=17 -GNinja
%fedora_v2_cmake_build

%install
%fedora_v2_cmake_install
# convert symlinked icons to copied icons, this will help co-existing with
# fcitx4
for iconfile in $(find %{buildroot}%{_datadir}/icons -type l)
do
  origicon=$(readlink -f ${iconfile})
  rm -f ${iconfile}
  cp ${origicon} ${iconfile}
done
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%find_lang %{name}

%files -f %{name}.lang
%doc --no-dereference LICENSES/GPL-3.0-or-later.txt
%doc README.md 
%{_libdir}/fcitx5/qt5/libfcitx5-skk-config.so
%{_libdir}/fcitx5/skk.so
%{_datadir}/fcitx5/addon/skk.conf
%{_datadir}/fcitx5/inputmethod/skk.conf
%dir %{_datadir}/fcitx5/skk
%{_datadir}/fcitx5/skk/dictionary_list
%{_datadir}/icons/hicolor/*/apps/fcitx-skk.png
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx-skk.png
%{_metainfodir}/org.fcitx.Fcitx5.Addon.Skk.metainfo.xml

%changelog
* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 5.1.0-alt1_1
- update to new release by fcimport

* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 5.0.13-alt1_2
- new version

