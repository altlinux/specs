Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: /usr/bin/gettext
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 1

%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:       fcitx5-m17n
Version:    5.1.0
Release:    alt1_1
Summary:    m17n Wrapper for Fcitx5
License:    LGPLv2+
URL:        https://github.com/fcitx/fcitx5-m17n
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  ctest cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build python3-module-ninja_syntax
BuildRequires:  gettext-tools
BuildRequires:  cmake(Fcitx5Core)
BuildRequires:  libfmt-devel
BuildRequires:  pkgconfig(m17n-gui) > 1.6.3
BuildRequires:  pkgconfig(m17n-db)
BuildRequires:  /usr/bin/appstream-util
Requires:       fcitx5-data
Requires:       pkgconfig(m17n-db)
Source44: import.info

%description
M17N is a large collection of input method, which can cover 
quite a lot languages in the world, including Latin, Arabic, 
etc.

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
%doc --no-dereference LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_libdir}/fcitx5/m17n.so
%{_datadir}/fcitx5/addon/m17n.conf
%dir %{_datadir}/fcitx5/m17n
%{_datadir}/fcitx5/m17n/default
%{_metainfodir}/org.fcitx.Fcitx5.Addon.M17N.metainfo.xml

%changelog
* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 5.1.0-alt1_1
- update to new release by fcimport

* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 5.0.10-alt1_2
- new version

