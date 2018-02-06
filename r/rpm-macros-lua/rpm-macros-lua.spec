Name: rpm-macros-lua
Version: 1.3
Release: alt2
Summary: RPM helper macros to build Lua packages
Url: https://www.altlinux.org/Lua_Policy
License: GPL
Group: Development/Other
BuildArch: noarch
Requires: rpm-build >= 4.0.4-alt78
Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: %name.macros

%description
These helper macros facilitate creation of RPM packages containing Lua code.

%prep
%setup -cT

%install
install -pD -m644 %SOURCE0 %buildroot%_rpmlibdir/macros.d/lua

%files
%_rpmlibdir/macros.d/lua

%changelog
* Tue Oct 10 2017 Ildar Mulyukov <ildar@altlinux.ru> 1.3-alt2
- improve lua interpreter autodetection

* Tue Sep 26 2017 Ildar Mulyukov <ildar@altlinux.ru> 1.3-alt1
- %%luarocks_make modernized to handle cross-Lua builds (build module for 5.1)
  on top of built 5.3 module

* Tue Sep 19 2017 Ildar Mulyukov <ildar@altlinux.ru> 1.2-alt3
- add %%{lua_modules_make_available_for_older_versions} (see https://www.altlinux.org/Lua_Policy)

* Fri Jul 14 2017 Ildar Mulyukov <ildar@altlinux.ru> 1.2-alt2
- replace %%lua_version with %%current_lua_version
- add %%luaXX_modulesdir macros
- minor rpath "safety net"

* Tue Jun 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2-alt1
- Added macro %%lua_version
  Update other macros to depend on it

* Sat Nov 07 2015 Ildar Mulyukov <ildar@altlinux.ru> 1.1-alt2
- improved %%luarocks_make : make local tree more more accurate
- fix %%_bindir commands

* Mon Aug 06 2012 Ildar Mulyukov <ildar@altlinux.ru> 1.1-alt1
- add macros:
  +%%lua_path_add_buildroot
  +%%luarocks_make
  +%%luarocks_move_docs

* Sun Dec 19 2010 Ildar Mulyukov <ildar@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus
