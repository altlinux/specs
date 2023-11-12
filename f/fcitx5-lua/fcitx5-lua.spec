%filter_from_requires /^luaimeapi.fcitx./d
Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: /usr/bin/gettext
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 1

%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:           fcitx5-lua
Version:        5.0.11
Release:        alt2_1
Summary:        Lua support for fcitx
License:        LGPLv2+
URL:            https://github.com/fcitx/fcitx5-lua
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:        https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  ctest cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  ninja-build python3-module-ninja_syntax
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(Fcitx5Core)
BuildRequires:  pkgconfig(Fcitx5Module)
BuildRequires:  /usr/bin/appstream-util
Requires:       fcitx5-data
Source44: import.info

%description
Lua support for fcitx.

%package devel
Group: Graphical desktop/Other
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
Devel files for fcitx5-lua

%prep
%setup -q


%build
%{fedora_v2_cmake} -GNinja
%fedora_v2_cmake_build 

%install
%fedora_v2_cmake_install
install -d  %{buildroot}%{_datadir}/lua/imeapi/extensions
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%find_lang %{name}

%check
#fedora_v2_ctest

%files -f %{name}.lang
%doc --no-dereference LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_libdir}/fcitx5/libluaaddonloader.so
%{_datadir}/fcitx5/addon/imeapi.conf
%{_datadir}/fcitx5/addon/luaaddonloader.conf
%{_datadir}/fcitx5/lua
%{_metainfodir}/org.fcitx.Fcitx5.Addon.Lua.metainfo.xml

%files devel
%{_includedir}/Fcitx5/Module/fcitx-module/luaaddonloader
%{_libdir}/cmake/Fcitx5ModuleLuaAddonLoader


%changelog
* Sun Nov 12 2023 Igor Vlasenko <viy@altlinux.org> 5.0.11-alt2_1
- quick hack; fixed build for p11 branching

* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 5.0.11-alt1_1
- update to new release by fcimport

* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 5.0.10-alt1_1
- new version

