%define _unpackaged_files_terminate_build 1
%def_with check
%define luarocks_revision 1

Name: lua5.4-module-luautf8
Version: 0.2.1
Release: alt1_lr%luarocks_revision

Summary: A utf-8 support module for Lua and LuaJIT
License: MIT
Group: Development/Other
Url: https://github.com/starwing/luautf8
Vcs: https://github.com/starwing/luautf8

Source: %name-%version.tar

Provides: luarocks5.4(luautf8) = %EVR

BuildRequires(pre): rpm-macros-lua
BuildRequires: lua5.4-luarocks
BuildRequires: liblua5.4-devel

%description
This module adds UTF-8 support to Lua.

It uses data extracted from Unicode Character Database, and tested on
Lua 5.2.3, Lua 5.3.0 and LuaJIT.

parseucd.lua is a pure Lua script which generates unidata.h, to support
converting characters and checking characters' category.

It is compatible with Lua's own string module and passes all string and
pattern matching tests in the Lua test suite2.

It also adds some useful routines against UTF-8 features, such as:

1. A convenient interface to escape Unicode sequences in strings.
2. String insert/remove, since UTF-8 substring extraction may be
expensive.
3. Calculate Unicode width, useful when implementing e.g. console
emulator.
4. A useful interface to translate Unicode offsets and byte
offsets.
5. Checking UTF-8 strings for validity and removing invalid byte
sequences.
6. Converting Unicode strings to normal form.

%prep
%setup

%build
luarocks-5.4 make --verbose --local --deps-mode all --pack-binary-rock \
	rockspecs/luautf8-%version-%luarocks_revision.rockspec

%install
luarocks-5.4 install --verbose --local --deps-mode none \
	--no-manifest --tree %buildroot%prefix *.rock

%check
luarocks-5.4 test --test-type command \
	rockspecs/luautf8-%version-%luarocks_revision

%files
%doc LICENSE
%luarocks_dbdir/luautf8/
%lua_modulesdir/lua-utf8.so

%changelog
* Tue Mar 03 2026 Sergey Zhidkih <rx1513@altlinux.org> 0.2.1-alt1_lr1
- New version (0.2.1).

* Tue Dec 16 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.2.0-alt1_lr1
- New version (0.2.0).

* Tue Sep 09 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.1.7-alt1_lr1
- New version (0.1.7).

* Tue Apr 08 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.1.6-alt1_lr1
- Initial build.
