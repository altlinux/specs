#TODO:
#   1. check rpath is clear
%define oname luarocks

Name: lua5.4-luarocks
Version: 3.9.2
Release: alt1
Summary: A deployment and management system for Lua modules
License: MIT
Group: Development/Tools
Url: http://www.luarocks.org
BuildArch: noarch

#This is %%luarocks_dbdir_prefix-%current_lua_version
#	which is defined in rpm-macros-lua package
Provides: %_prefix/lib/luarocks/rocks-5.4
Requires: chrpath wget p7zip unzip zip

Conflicts: rpm-macros-lua < 1.4
Provides: %oname = %EVR
Conflicts: %oname < %EVR
Conflicts: lua5.3-luarocks
Conflicts: lua5.1-luarocks

Source: http://luarocks.org/releases/%name-%version.tar
#.gz
Source1: %oname.filetrigger
Source2: %oname-files.req.list

BuildPreReq: rpm-macros-lua >= 1.4
BuildRequires: liblua5.4-devel unzip wget

%filter_from_requires /lua5.4(luarocks.test.)/d

%description
LuaRocks allows you to install Lua modules as self-contained
packages called "rocks", which also contain version dependency
information. This information is used both during installation,
so that when one rock is requested all rocks it depends on are
installed as well, and at run time, so that when a module is
required, the correct version is loaded. LuaRocks supports both
local and remote repositories, and multiple local rocks trees.

This is the instance for lua 5.4

%prep
%setup
#disable Lua header version check
sed -i 's/^if .*header_version.*LUA_VERSION.*$/if [ OK ]/' configure

%build
./configure \
  --prefix=%prefix \
  --lua-version=5.4

%install
%makeinstall_std

# RPM triggers
mkdir -p %buildroot%_rpmlibdir/
install -m755 %SOURCE1 %buildroot%_rpmlibdir/%name.filetrigger
install -m644 %SOURCE2 %buildroot%_rpmlibdir/%name-files.req.list

%files
%dir %_sysconfdir/%oname
%config(noreplace) %_sysconfdir/%oname/*
%_bindir/%{oname}*
%_rpmlibdir/%{name}*
%lua_modulesdir_noarch/%{oname}
%doc COPYING README*

%changelog
* Fri Apr 14 2023 Alexey Shabalin <shaba@altlinux.org> 3.9.2-alt1
- Initial build for lua 5.4

* Sat Jun 15 2019 Ildar Mulyukov <ildar@altlinux.ru> 2.4.2-alt7
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
