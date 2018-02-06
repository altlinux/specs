#%luarocks_dbdir is defined in rpm-macros-lua package

#TODO:
#   1. check rpath is clear

Name: luarocks
Version: 2.4.2
Release: alt4
Summary: A deployment and management system for Lua modules
License: MIT
Group: Development/Tools
Url: http://www.luarocks.org
Packager: Ildar Mulyukov <ildar@altlinux.ru>
#%%luarocks_dbdir
Provides: %_prefix/lib/luarocks/rocks

Source: http://luarocks.org/releases/%name-%version.tar
#.gz
Source1: %name.filetrigger
Source2: %name-files.req.list

Requires: chrpath wget p7zip unzip zip
# We want any of /usr/bin/lua-5.x
%add_findreq_skiplist %_bindir/*
Requires: lua5

BuildPreReq: rpm-macros-lua >= 1.3
# Automatically added by buildreq on Wed Sep 20 2017
# optimized out: lua5.3 python-base
BuildRequires: lua-devel lua5.1 unzip wget

%description
LuaRocks allows you to install Lua modules as self-contained
packages called "rocks", which also contain version dependency
information. This information is used both during installation,
so that when one rock is requested all rocks it depends on are
installed as well, and at run time, so that when a module is
required, the correct version is loaded. LuaRocks supports both
local and remote repositories, and multiple local rocks trees.

%prep
%setup
sed -i 's/^if .*header_version.*LUA_VERSION.*$/if [ OK ]/' configure

%build
for v in 5.1 5.3; do
	cp -a . ../build-$v
	pushd ../build-$v
	./configure --prefix=%prefix --lua-version=$v
	make
	popd
done

%install
mkdir -p %buildroot{%lua_modulesdir/%name/,%luarocks_dbdir/,%_rpmlibdir/}
for v in 5.1 5.3; do
	%makeinstall_std -C ../build-$v
	sed -i "s|/usr/bin/env lua$|/usr/bin/env lua$v|" %buildroot%_bindir/%{name}*-$v
#move arch-dependent parts
# pending https://github.com/keplerproject/luarocks/issues/86
mkdir -p %buildroot%_libdir/lua/$v/%name
mv %buildroot%_datadir/lua/$v/%name/\
site_config.lua \
	%buildroot%_libdir/lua/$v/%name
#enable lib -> lib64 right path settings
cat >> %buildroot%_sysconfdir/%name/config-$v.lua <<EOF
gcc_rpath = false
lib_modules_path = "/%_lib/lua/"..lua_version
EOF

SITECFG_ADDITION="site_config.LUAROCKS_EXTERNAL_DEPS_SUBDIRS =\\
    {\\
      bin = \"bin\",\\
      lib = \"%_lib\",\\
      include = \"include\"\\
    }"
sed -i "/^return/ i $SITECFG_ADDITION" \
	%buildroot%_libdir/lua/$v/%name/site_config.lua
done

#%%ghost
touch %buildroot%luarocks_dbdir/{index.html,manifest{,-5.{1,2,3}}}
# RPM triggers
install -m755 %SOURCE1 %buildroot%_rpmlibdir/
install -m644 %SOURCE2 %buildroot%_rpmlibdir/

%files
%_sysconfdir/%name
%_bindir/%{name}*
%dir %_prefix/lib/luarocks
%dir %luarocks_dbdir
%ghost %luarocks_dbdir/index.html
%ghost %luarocks_dbdir/manifest*
%_rpmlibdir/%{name}*
%lua_modulesdir/%name
%lua_modulesdir_noarch/%name
%lua51_modulesdir/%name
%lua51_modulesdir_noarch/%name
%doc COPYING README*

%changelog
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
