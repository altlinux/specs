%define _unpackaged_files_terminate_build 1
# Busted not in sisyphus yet.
%def_without check
%define luarocks_revision 1

Name: lua5.4-module-luasystem
Version: 0.4.5
Release: alt1_lr%luarocks_revision

Summary: Platform independent system calls for Lua
License: MIT
Group: Development/Other
Url: https://lunarmodules.github.io/luasystem/
Vcs: https://github.com/lunarmodules/luasystem

Source: %name-%version.tar

Provides: luarocks5.4(luasystem) = %EVR

BuildRequires(pre): rpm-macros-lua
BuildRequires: lua5.4-luarocks
BuildRequires: liblua5.4-devel

%description
Luasystem is a platform independent system call library for Lua.
Supports Unix, Windows, MacOS, Lua >= 5.1 and luajit >= 2.0.0.

Lua is typically platform independent, but it requires adhering to very
old C standards. This in turn means that many common features
(according to todays standards) are not available. This module attempts
to overcome some of those hurdles by providing functions that cover
those common needs.

%prep
%setup

%build
luarocks-5.4 make --verbose --local --deps-mode all --pack-binary-rock \
	rockspecs/luasystem-%version-%luarocks_revision.rockspec

%install
luarocks-5.4 install --verbose --local --deps-mode none \
	--no-manifest --tree %buildroot%prefix *.rock

%check
luarocks-5.4 test --test-type busted rockspecs/luasystem-%version-%luarocks_revision.rockspec

%files
%doc LICENSE.md
%luarocks_dbdir/luasystem
%lua_modulesdir_noarch/system/init.lua
%lua_modulesdir/system/core.so

%changelog
* Mon Apr 08 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.4.5-alt1_lr1
- Initial build.
