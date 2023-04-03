%define _unpackaged_files_terminate_build 1

%define luaver 5.3
%define oname luaposix
%define oversion 36.1-1

Name: lua%luaver-module-%oname
Version: 36.1
Release: alt1

Summary: Lua bindings for POSIX APIs
License: MIT
Group: Development/Other
Url: https://github.com/luaposix/luaposix

Source0: %name-%version.tar
Source1: %oname-%oversion.rockspec

BuildRequires(pre): lua%luaver-luarocks
BuildRequires(pre): rpm-macros-lua
BuildRequires: liblua%luaver-devel

Provides: luarocks%luaver(%oname) = %EVR

%description
This is a POSIX binding for LuaJIT, Lua 5.3; like most libraries it simply binds
to C APIs on the underlying system, so it won't work on non-POSIX systems.
However, it does try to detect the level of POSIX conformance of the underlying
system and bind only available APIs.

For a while, luaposix contained support for curses functionality too, but now
that has its own lcurses repository again, where it is being maintained
separately.

%prep
%setup

%install
%luarocks_make %SOURCE1
%luarocks_move_docs doc

%files
%doc AUTHORS LICENSE NEWS* README*
%lua_modulesdir/*
%lua_modulesdir_noarch/*
%luarocks_dbdir/%oname
%exclude %luarocks_dbdir/manifest

%changelog
* Sun Feb 19 2023 Alexandr Shashkin <dutyrok@altlinux.org> 36.1-alt1
- Initial build for sisyphus
