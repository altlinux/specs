Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: /usr/bin/gettext gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 1

Name:       fcitx5-table-other
Version:    5.1.0
Release:    alt1_1
Summary:    Other tables for Fcitx5
License:    GPLv3
URL:        https://github.com/fcitx/fcitx5-table-other
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9
BuildArch:  noarch

BuildRequires:  gnupg2
BuildRequires:  ctest cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  ninja-build python3-module-ninja_syntax
BuildRequires:  boost-complete
BuildRequires:  cmake(Fcitx5Utils)
BuildRequires:  libime-devel
BuildRequires:  gettext-tools
BuildRequires:  libappstream-glib libappstream-glib-gir

Requires:       icon-theme-hicolor
Requires:       fcitx5-data
Source44: import.info

%description
Fcitx-table-other provides some other tables 
for Fcitx, fork from ibus-table-others, scim-tables.

%prep
%setup -q


%build 
%{fedora_v2_cmake} -GNinja -DCMAKE_PREFIX_PATH="%{_libdir}/cmake;%{_libdir}64/cmake"
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

%files 
%doc --no-dereference LICENSES/GPL-3.0-only.txt
%doc README NEWS 
%{_datadir}/fcitx5/inputmethod/*
%{_datadir}/fcitx5/table/*
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/org.fcitx.Fcitx5.Addon.TableOther.metainfo.xml

%changelog
* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 5.1.0-alt1_1
- update to new release by fcimport

* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 5.0.10-alt1_2
- new version

