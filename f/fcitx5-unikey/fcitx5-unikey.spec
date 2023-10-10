Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: /usr/bin/gettext
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 1

%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:       fcitx5-unikey
Version:    5.1.1
Release:    alt1_1
Summary:    Unikey support for Fcitx5
License:    GPLv2+ and LGPLv2+
URL:        https://github.com/fcitx/fcitx5-unikey
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  ctest cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build python3-module-ninja_syntax
BuildRequires:  cmake(Fcitx5Core)
BuildRequires:  cmake(Fcitx5Qt5WidgetsAddons)
BuildRequires:  qt5-base-devel
BuildRequires:  gettext-tools
BuildRequires:  libappstream-glib libappstream-glib-gir
Requires:       icon-theme-hicolor
Requires:       fcitx5-data
Source44: import.info

%description
Unikey (Vietnamese Input Method) engine support for Fcitx5.

%prep
%setup -q


%build
%{fedora_v2_cmake} -GNinja
%fedora_v2_cmake_build

%install
%fedora_v2_cmake_install
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%find_lang %{name}

%files -f %{name}.lang
%doc --no-dereference LICENSES/GPL-2.0-or-later.txt LICENSES/LGPL-2.0-or-later.txt
%doc README ChangeLog 
%{_libdir}/fcitx5/libunikey.so
%{_libdir}/fcitx5/qt5/libfcitx5-unikey-macro-editor.so
%{_libdir}/fcitx5/qt5/libfcitx5-unikey-keymap-editor.so
%{_datadir}/fcitx5/addon/unikey.conf
%{_datadir}/fcitx5/inputmethod/unikey.conf
%{_datadir}/icons/hicolor/*/apps/fcitx-unikey.png
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx-unikey.png
%{_metainfodir}/org.fcitx.Fcitx5.Addon.Unikey.metainfo.xml

%changelog
* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 5.1.1-alt1_1
- update to new release by fcimport

* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 5.0.11-alt1_2
- new version

