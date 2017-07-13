Name: rpm-macros-lua
Version: 1.2
Release: alt1
Summary: RPM helper macros to build Lua packages
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
* Tue Jun 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2-alt1
- Added macro %lua_version
  Update other macros to depend on it

* Mon Aug 06 2012 Ildar Mulyukov <ildar@altlinux.ru> 1.1-alt1
- add macros:
  +%lua_path_add_buildroot
  +%luarocks_make
  +%luarocks_move_docs

* Sun Dec 19 2010 Ildar Mulyukov <ildar@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus
