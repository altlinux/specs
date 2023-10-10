Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: /usr/bin/gettext
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 1

%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:           fcitx5-rime
Version:        5.1.2
Release:        alt1_1
Summary:        RIME support for Fcitx
License:        LGPLv2+
URL:            https://github.com/fcitx/fcitx5-rime
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:        https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  brise 
BuildRequires:  ctest cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build python3-module-ninja_syntax
BuildRequires:  gettext-tools
BuildRequires:  pkgconfig(Fcitx5Core)
BuildRequires:  pkgconfig(Fcitx5Module)
BuildRequires:  pkgconfig(rime)
BuildRequires:  /usr/bin/appstream-util
Requires:       icon-theme-hicolor
Requires:       fcitx5-data
Requires:       brise
Source44: import.info

%description
RIME(a..a..e..e..a..a..a..a..) is mainly a Traditional Chinese 
input method engine.

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

%check
%fedora_v2_ctest

%files -f %{name}.lang
%doc --no-dereference LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_libdir}/fcitx5/rime.so
%{_datadir}/fcitx5/*/rime.conf
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/rime-data/fcitx5.yaml
%{_metainfodir}/org.fcitx.Fcitx5.Addon.Rime.metainfo.xml

%changelog
* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 5.1.2-alt1_1
- update

* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 5.0.14-alt1_2
- new version

