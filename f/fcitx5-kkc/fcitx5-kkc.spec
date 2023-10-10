Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: /usr/bin/gettext
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 1

%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:           fcitx5-kkc
Version:        5.1.0
Release:        alt1_1
Summary:        Libkkc input method support for Fcitx5
License:        GPLv3+
Url:            https://github.com/fcitx/fcitx5-kkc
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:        https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  ctest cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build python3-module-ninja_syntax
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Fcitx5Core)
BuildRequires:  cmake(Fcitx5Qt5WidgetsAddons)
BuildRequires:  pkgconfig(kkc-1.0)
BuildRequires:  pkgconfig(Qt5Core) >= 5.7
BuildRequires:  pkgconfig(Qt5Gui) >= 5.7
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.7
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  gettext-tools
BuildRequires:  /usr/bin/appstream-util
Requires:       icon-theme-hicolor
Requires:       fcitx5-data
Requires:       libkkc-data
Source44: import.info

%description
This provides libkkc input method support for fcitx5. Released under GPL3+.

%prep
%setup -q


%build
%{fedora_v2_cmake} -GNinja
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
%doc README.md
%doc --no-dereference LICENSES/GPL-3.0-or-later.txt
%{_libdir}/fcitx5/kkc.so
%{_libdir}/fcitx5/qt5/libfcitx5-kkc-config.so

%{_datadir}/fcitx5/addon/kkc.conf
%{_datadir}/fcitx5/inputmethod/kkc.conf

%dir %{_datadir}/fcitx5/kkc
%{_datadir}/fcitx5/kkc/dictionary_list
%{_datadir}/fcitx5/kkc/rule

%{_datadir}/icons/hicolor/*/apps/fcitx-kkc.png
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx-kkc.png
%{_metainfodir}/org.fcitx.Fcitx5.Addon.Kkc.metainfo.xml
%changelog
* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 5.1.0-alt1_1
- update to new release by fcimport

* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 5.0.10-alt1_2
- new version

