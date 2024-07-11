%define _unpackaged_files_terminate_build 1
# busted not in sisyphus yet
%def_without check
%define luarocks_revision 1

Name: lua5.4-module-luacheck
Version: 1.2.0
Release: alt1_lr%luarocks_revision

Summary: A tool for linting and static analysis of Lua code
License: MIT
Group: Development/Other
Url: https://luarocks.org/modules/lunarmodules/luacheck
Vcs: https://github.com/lunarmodules/luacheck
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

# in any case, it can work without it
# see src/luacheck/vendor/sha1/init.lua
%filter_from_requires /lua5.4(bit.*/d
# self-dependencies
%filter_from_requires /luacheck\..*/d

BuildRequires(pre): rpm-macros-lua
BuildRequires: lua5.4-luarocks
BuildRequires: lua5.4-module-argparse
BuildRequires: lua5.4-module-luafilesystem

%description
Luacheck is a static analyzer and a linter for Lua.

Luacheck detects various issues such as usage of undefined global variables,
unused variables and values, accessing uninitialized variables, unreachable
code and more.

Most aspects of checking are configurable, there are options for:
 - defining custom project-related globals
 - selecting set of standard globals (version of Lua standard library)
 - filtering warnings by type and name of related variable, etc.

The options can be used on the command line, put into
a config or directly into checked files as Lua comments.

%prep
%setup
%autopatch -p1

%build
luarocks-5.4 make --verbose --local --deps-mode all --pack-binary-rock \
	rockspecs/luacheck-%version-%luarocks_revision.rockspec

%install
luarocks-5.4 install --verbose --local --deps-mode none \
	--tree %buildroot%prefix *.rock

# see https://github.com/luarocks/luarocks/wiki/Manifest-file-format
rm -v %buildroot%luarocks_dbdir/manifest

%files
%doc README* LICENSE
%_bindir/luacheck
%luarocks_dbdir/luacheck/
%lua_modulesdir_noarch/luacheck/

%changelog
* Fri Jul 05 2024 Ajrat Makhmutov <rauty@altlinux.org> 1.2.0-alt1_lr1
- First build for ALT.
