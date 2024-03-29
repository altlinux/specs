%def_enable snapshot

%define modname luajson
%define luaver 5.4
%define luapkgdir %_datadir/lua/%luaver

%def_disable check

Name: lua-module-%modname
Version: 1.3.4
Release: alt1.1

Summary: JSON Parser/Constructor for Lua
Group: Development/Other
License: MIT
Url: http://luaforge.net/projects/%modname/
Vcs: https://github.com/harningt/luajson.git
Source: %modname-%version.tar

BuildArch: noarch

%define lpeg_ver 1.0.1
%define lunit_ver 0.4

Requires: lua >= %luaver lua-lpeg >= %lpeg_ver

%if_enabled check
BuildRequires: lua%luaver-module-lpeg
BuildRequires: lua%luaver-module-luafilesystem
BuildRequires: lua >= %luaver lua-lpeg >= %lpeg_ver
BuildRequires: lua-lunit >= %lunit_ver lua-module-luafilesystem
%endif

%description
LuaJSON is a customizable JSON decoder/encoder, using LPEG for parsing.

%prep
%setup -n %modname-%version
# set VERSION outside git repo
sed -i 's/\(^VERSION=\).*$/\1%version/' Makefile

%build

%install
mkdir -p %buildroot%luapkgdir
cp -a -r lua/* %buildroot%luapkgdir/

%check
%make check LUA_BIN=lua-%luaver

%files
%luapkgdir/*
%doc LICENSE docs/LuaJSON.txt docs/ReleaseNotes-%version.txt

%changelog
* Mon Feb 05 2024 Pavel Skrylev <majioa@altlinux.org> 1.3.4-alt1.1
- ! fixed FTBFS: build for lua 5.3 explicitly

* Wed Jun 13 2018 Yuri N. Sedunov <aris@altlinux.org> 1.3.4-alt1
- first build for Sisyphus




