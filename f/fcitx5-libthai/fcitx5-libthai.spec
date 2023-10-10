Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: /usr/bin/gettext
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 1

%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:       fcitx5-libthai
Version:    5.1.0
Release:    alt1_1
Summary:    Libthai Wrapper for Fcitx5
License:    GPLv2+
URL:        https://github.com/fcitx/fcitx5-libthai
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  ctest cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build python3-module-ninja_syntax
BuildRequires:  cmake(Fcitx5Core)
BuildRequires:  pkgconfig(libthai)
BuildRequires:  gettext-tools
BuildRequires:  /usr/bin/appstream-util
Requires:       icon-theme-hicolor
Requires:       fcitx5-data
Source44: import.info

%description
%{summary}.

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
%doc --no-dereference LICENSES/GPL-2.0-or-later.txt
%{_libdir}/fcitx5/libthai.so
%{_datadir}/fcitx5/addon/libthai.conf
%{_datadir}/fcitx5/inputmethod/libthai.conf
%{_metainfodir}/org.fcitx.Fcitx5.Addon.LibThai.metainfo.xml

%changelog
* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 5.1.0-alt1_1
- update to new release by fcimport

* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 5.0.10-alt1_1
- new version

