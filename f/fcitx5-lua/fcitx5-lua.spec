%define _unpackaged_files_terminate_build 1
#%%filter_from_requires /^luaimeapi.fcitx./d
%global __provides_exclude_from ^%_libdir/fcitx5/.*\\.so$

Name: fcitx5-lua
Version: 5.0.18
Release: alt1

Summary: Lua support for fcitx
License: LGPLv2+
Group: Graphical desktop/Other

Url: https://github.com/fcitx/fcitx5-lua
Vcs: https://github.com/fcitx/fcitx5-lua

Source: %name-%version.tar.xz

Requires: fcitx5-data
Requires: liblua5.4

AutoReq: yes, nolua

BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: /usr/bin/gettext
BuildRequires: gnupg2
BuildRequires: ctest
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: gettext-tools
BuildRequires: ninja-build
BuildRequires: python3-module-ninja_syntax
BuildRequires: liblua5.4-devel
BuildRequires: pkgconfig(Fcitx5Core)
BuildRequires: pkgconfig(Fcitx5Module)
BuildRequires: /usr/bin/appstream-util

%description
Lua support for fcitx.

%package devel
Group: Graphical desktop/Other
Summary: Development files for %name

%description devel
Devel files for fcitx5-lua

%prep
%setup
subst 's|${FCITX_LUA_HEADER_DIRS}|"${FCITX_LUA_HEADER_DIRS}"|' CMakeLists.txt

%build
%fedora_v2_cmake -GNinja
%fedora_v2_cmake_build

%install
%fedora_v2_cmake_install
install -d  %buildroot%_datadir/lua/imeapi/extensions
appstream-util validate-relax --nonet %buildroot%_metainfodir/*.metainfo.xml
%find_lang %name

%check
#fedora_v2_ctest

%files -f %name.lang
%doc --no-dereference LICENSES/LGPL-2.1-or-later.txt
%doc README.md
%_libdir/fcitx5/libluaaddonloader.so
%_datadir/fcitx5/addon/imeapi.conf
%_datadir/fcitx5/addon/luaaddonloader.conf
%_datadir/fcitx5/lua
%_metainfodir/org.fcitx.Fcitx5.Addon.Lua.metainfo.xml

%files devel
%_includedir/Fcitx5/Module/fcitx-module/luaaddonloader
%_libdir/cmake/Fcitx5ModuleLuaAddonLoader

%changelog
* Thu Oct 01 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.0.18-alt1
- 5.0.11 -> 5.0.18 (ALT #52982)

* Sun Nov 12 2023 Igor Vlasenko <viy@altlinux.org> 5.0.11-alt2_1
- quick hack; fixed build for p11 branching

* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 5.0.11-alt1_1
- update to new release by fcimport

* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 5.0.10-alt1_1
- new version

