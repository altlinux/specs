%define _unpackaged_files_terminate_build 1
# Busted not in sisyphus yet.
%def_without check
%define luarocks_revision 1

Name: lua5.4-module-penlight
Version: 1.14.0
Release: alt1_lr%luarocks_revision

Summary: Penlight is a set of pure Lua libraries for making it easier to work with common tasks
License: MIT and X11
Group: Development/Other
Url: https://lunarmodules.github.io/Penlight/
Vcs: https://github.com/lunarmodules/Penlight
BuildArch: noarch

Source: %name-%version.tar

Provides: luarocks5.4(luasystem) = %EVR

# self-dependencies
%filter_from_requires /lua5.4(animal)/d
%filter_from_requires /lua5.4(sip)/d
%filter_from_requires /lua5.4(mod52)/d
%filter_from_requires /lua5.4(mymod)/d
%filter_from_requires /lua5.4(luabalanced)/d
%filter_from_requires /lua5.4(\[\[pl\.utils\]\])/d

%filter_from_requires /luaanimal.lua(pl\..*)/d
%filter_from_requires /luamymod.lua(pl\..*)/d
%filter_from_requires /luamod52.lua(pl\..*)/d

BuildRequires(pre): rpm-macros-lua
BuildRequires: lua5.4-luarocks
BuildRequires: lua5.4-module-luafilesystem

%description
Penlight brings together a set of generally useful pure Lua modules,
focusing on input data handling (such as reading configuration files),
functional programming (such as map, reduce, placeholder expressions,
etc), and OS path management. Much of the functionality is inspired by
the Python standard libraries.

%prep
%setup
# 1.14.0-alt1_lr1
# Replace lua with appropriate intrepreter.
sed -i "s|#!/usr/bin/env lua|#!/usr/bin/env lua5.4|g" run.lua
sed -i "s|#!/usr/bin/env lua|#!/usr/bin/env lua5.4|g" docs_topics/06-data.md
sed -i "s|#!/usr/bin/env lua|#!/usr/bin/env lua5.4|g" docs/manual/06-data.md.html

%build
luarocks-5.4 make --verbose --local --deps-mode all --pack-binary-rock \
	rockspecs/penlight-%version-%luarocks_revision.rockspec

%install
luarocks-5.4 install --verbose --local --deps-mode none \
	--no-manifest --tree %buildroot%prefix *.rock

%check
luarocks-5.4 test --test-type busted \
	rockspecs/luautf8-%version-%luarocks_revision

%files
%doc LICENSE.md
%luarocks_dbdir/penlight/
%lua_modulesdir_noarch/pl/

%changelog
* Wed Apr 09 2025 Sergey Zhidkih <rx1513@altlinux.org> 1.14.0-alt1_lr1
- First build for alt.
