#TODO:
#   1. check rpath is clear
%define oname luarocks

Name: lua5.4-luarocks
Version: 3.9.2
Release: alt2
Summary: A deployment and management system for Lua modules
License: MIT
Group: Development/Tools
Url: http://www.luarocks.org
Provides: %oname = %EVR
Obsoletes: %oname < %EVR
#This is %%luarocks_dbdir_prefix-%current_lua_version
#	which is defined in rpm-macros-lua package
Provides: %_prefix/lib/luarocks/rocks-5.4
Requires: chrpath wget p7zip unzip zip
Requires: rpm-macros-lua >= 1.5.2 rpm-build-lua
%add_findreq_skiplist /usr/bin/*
Requires: lua5.4

Source: http://luarocks.org/releases/%name-%version.tar
#.gz
Source1: %oname.filetrigger
Source2: %oname-files.req.list

BuildPreReq: rpm-macros-lua >= 1.5.2 rpm-build-lua
# Automatically added by buildreq on Wed Sep 20 2017
# optimized out: lua5.3 python-base
BuildRequires: liblua5.4-devel lua5.3 lua5.1 unzip wget

%description
LuaRocks allows you to install Lua modules as self-contained
packages called "rocks", which also contain version dependency
information. This information is used both during installation,
so that when one rock is requested all rocks it depends on are
installed as well, and at run time, so that when a module is
required, the correct version is loaded. LuaRocks supports both
local and remote repositories, and multiple local rocks trees.

This is the instance for lua 5.4

%package -n lua5.3-luarocks
Summary: A deployment and management system for Lua modules
License: MIT
Group: Development/Tools
#This is %%luarocks_dbdir_prefix-%current_lua_version
#	which is defined in rpm-macros-lua package
Provides: %_prefix/lib/luarocks/rocks-5.3
Requires: chrpath wget p7zip unzip zip
Requires: rpm-macros-lua >= 1.5.2 rpm-build-lua
%add_findreq_skiplist /usr/bin/*
Requires: lua5.3
Conflicts: %oname < %EVR
Conflicts: lua5.4-luarocks < %EVR
Conflicts: lua5.4-luarocks > %EVR
Conflicts: %oname > %EVR
Conflicts: rpm-macros-lua < 1.4

%description -n lua5.3-luarocks
LuaRocks allows you to install Lua modules as self-contained
packages called "rocks", which also contain version dependency
information. This information is used both during installation,
so that when one rock is requested all rocks it depends on are
installed as well, and at run time, so that when a module is
required, the correct version is loaded. LuaRocks supports both
local and remote repositories, and multiple local rocks trees.

This is the instance for lua 5.3

%package -n lua5.1-luarocks
Summary: A deployment and management system for Lua modules
License: MIT
Group: Development/Tools
#This is %%luarocks_dbdir_prefix-%current_lua_version
#	which is defined in rpm-macros-lua package
Provides: %_prefix/lib/luarocks/rocks-5.1
Requires: chrpath wget p7zip unzip zip
Requires: rpm-macros-lua >= 1.5.2 rpm-build-lua
%add_findreq_skiplist /usr/bin/*
Requires: lua5.1
Conflicts: %oname < %EVR
Conflicts: lua5.4-luarocks < %EVR
Conflicts: lua5.4-luarocks > %EVR
Conflicts: %oname > %EVR
Conflicts: rpm-macros-lua < 1.4

%description -n lua5.1-luarocks
LuaRocks allows you to install Lua modules as self-contained
packages called "rocks", which also contain version dependency
information. This information is used both during installation,
so that when one rock is requested all rocks it depends on are
installed as well, and at run time, so that when a module is
required, the correct version is loaded. LuaRocks supports both
local and remote repositories, and multiple local rocks trees.

This is the instance for lua 5.1

%prep
%setup
#disable Lua header version check
# we don't need header files for noarch rocks
sed -i 's/for lua_h in/return 0 ; \0/' configure
# FIXME: this subst may be error prone!
subst 's/return nil, mainerr/return mainerr, mainerr/' \
	src/luarocks/deps.lua

%build
for v in 5.1 5.3 5.4; do
	cp -a . ../build-$v
	pushd ../build-$v
	./configure --prefix=%prefix --lua-version=$v \

	make
	popd
done

%install
for v in 5.1 5.3 5.4; do
	%makeinstall_std -C ../build-$v
	for f in %buildroot%_bindir/*{ks,in}; do mv $f $f-$v; done
	sed -i "s|/usr/bin/env lua$|/usr/bin/env lua$v|" %buildroot%_bindir/%{oname}*-$v
	mkdir -p %buildroot{%_datadir/lua/$v/%oname/,%luarocks_dbdir_prefix-$v/}
	#move arch-dependent parts
	# pending https://github.com/keplerproject/luarocks/issues/86
	mkdir -p %buildroot%_libdir/lua/$v/%oname
	#enable lib -> lib64 right path settings
	cat >> %buildroot%_sysconfdir/%oname/config-$v.lua <<EOF
gcc_rpath = false
lib_modules_path = "/%_lib/lua/"..lua_version
EOF
	#%%ghost
	touch %buildroot%luarocks_dbdir_prefix-$v/{index.html,manifest{,-5.{1,2,3,4}}}
done

# RPM triggers
mkdir -p %buildroot%_rpmlibdir/
install -m755 %SOURCE1 %buildroot%_rpmlibdir/
# remove dependency on luarocks
# install -m644 %SOURCE2 %buildroot%_rpmlibdir/

%add_findreq_skiplist /usr/share/lua/*/luarocks/fs/lua.lua
%add_findreq_skiplist /usr/share/lua/*/luarocks/tools/zip.lua
%add_findprov_skiplist %lua51_modulesdir/%oname/*
%add_findprov_skiplist %lua53_modulesdir/%oname/*
%add_findprov_skiplist %lua54_modulesdir/%oname/*
%filter_from_requires /lua5..(luarocks.test.)/d

%files
%dir %_sysconfdir/%oname
%_sysconfdir/%oname/*-5.4.*
%_bindir/%{oname}*-5.4
%dir %_prefix/lib/luarocks
%dir %luarocks_dbdir_prefix-5.4
%ghost %luarocks_dbdir_prefix-5.4/index.html
%ghost %luarocks_dbdir_prefix-5.4/manifest*
%_rpmlibdir/%{oname}*
%lua54_modulesdir/%oname
%lua54_modulesdir_noarch/%oname
%doc COPYING README*

%files -n lua5.3-luarocks
%dir %_sysconfdir/%oname
%_sysconfdir/%oname/*-5.3.*
%_bindir/%{oname}*-5.3
%dir %_prefix/lib/luarocks
%dir %luarocks_dbdir_prefix-5.3
%ghost %luarocks_dbdir_prefix-5.3/index.html
%ghost %luarocks_dbdir_prefix-5.3/manifest*
%_rpmlibdir/%{oname}*
%lua53_modulesdir/%oname
%lua53_modulesdir_noarch/%oname
%doc COPYING README*

%files -n lua5.1-luarocks
%dir %_sysconfdir/%oname
%_sysconfdir/%oname/*-5.1.*
%_bindir/%{oname}*-5.1
%dir %_prefix/lib/luarocks
%dir %luarocks_dbdir_prefix-5.1
%ghost %luarocks_dbdir_prefix-5.1/index.html
%ghost %luarocks_dbdir_prefix-5.1/manifest*
%_rpmlibdir/%{oname}*
%lua51_modulesdir/%oname
%lua51_modulesdir_noarch/%oname
%doc COPYING README*

%changelog
* Wed Jan 17 2024 Ildar Mulyukov <ildar@altlinux.ru> 3.9.2-alt2
- get back to the multi-Lua packaging

* Fri Apr 14 2023 Alexey Shabalin <shaba@altlinux.org> 3.9.2-alt1
- Initial build for lua 5.4

* Sat Jun 15 2019 Ildar Mulyukov <ildar@altlinux.ru> 2.4.2-alt7
- Also:
- Fri Jun 23 2023 Ildar Mulyukov <ildar@altlinux.ru> 2.4.2-alt9
- add Requires: rpm-build-lua
- built rpms no longer have dependency on luarocks
- Fri May 12 2023 Alexandr Shashkin <dutyrok@altlinux.org> 2.4.2-alt8
- luarocks.spec: edit conflicts for lua5.1-luarocks subpackage
- replace lua-devel by liblua5.3-devel
- Sat Jun 15 2019 Ildar Mulyukov <ildar@altlinux.ru> 2.4.2-alt7
- improved %oname.filetrigger (closes: 36897)

* Fri Jun 14 2019 Ildar Mulyukov <ildar@altlinux.ru> 2.4.2-alt6
- fix RPM deps (+Obsoletes, -Provides)

* Wed Jun 05 2019 Ildar Mulyukov <ildar@altlinux.ru> 2.4.2-alt5
- great split: luarocks -> lua@luaversion@-luarocks (with 5.1 and 5.3 versions)
- luarocks tree is now %luarocks_dbdir_prefix-@luaversion@ (separate for different versions)

* Fri Dec 08 2017 Ildar Mulyukov <ildar@altlinux.ru> 2.4.2-alt4
- fix `lib` external dep subdir accidently lost in 2.4.2-alt1

* Fri Oct 06 2017 Ildar Mulyukov <ildar@altlinux.ru> 2.4.2-alt3
- disable liblua.so linking according to https://www.altlinux.org/Lua_Policy
- build luarocks for both Lua 5.3 (latest) and Lua 5.1

* Fri Jul 14 2017 Ildar Mulyukov <ildar@altlinux.ru> 2.4.2-alt2
- minor fixes and improvements to alt1 version

* Thu Jul 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.2-alt1
- Updated to upstream version 2.4.2

* Tue Jul 11 2017 Ildar Mulyukov <ildar@altlinux.ru> 2.4.2-alt1
- new version

* Sat Nov 07 2015 Ildar Mulyukov <ildar@altlinux.ru> 2.2.2-alt1
- new version

* Mon Oct 06 2014 Ildar Mulyukov <ildar@altlinux.ru> 2.2.0-alt1.rc1
- fix rpath for builtin biulds

* Fri Aug 15 2014 Ildar Mulyukov <ildar@altlinux.ru> 2.2.0-alt0.rc1
- new version
- ignored Vladimir Didenko's <cow@> releases

* Fri Jul 4 2014 Vladimir Didenko <cow@altlinux.org> 2.1.2-alt1
- new version

* Thu Jul 12 2012 Ildar Mulyukov <ildar@altlinux.ru> 2.0.9-alt0.rc1
- new version
- convert lib64 fix into a configuration
- add ghost files for proper clean on uninstall

* Tue Jan 11 2011 Ildar Mulyukov <ildar@altlinux.ru> 2.0.4-alt0.rc3
- initial build for ALT Linux Sisyphus
