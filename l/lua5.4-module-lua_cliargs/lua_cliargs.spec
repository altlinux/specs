%define _unpackaged_files_terminate_build 1
# Busted not in sysiphus yet.
%def_without check
%define luarocks_revision 1

Name: lua5.4-module-lua_cliargs
Version: 3.0.2
Release: alt1_lr%luarocks_revision

Summary: Cliargs is a command-line argument parser for Lua
License: MIT
Group: Development/Other
Url: https://github.com/lunarmodules/lua_cliargs
Vcs: https://github.com/lunarmodules/lua_cliargs
BuildArch: noarch

Source: %name-%version.tar

Provides: luarocks5.4(lua_cliargs) = %EVR

# Unsuported by upstream.
# https://github.com/lunarmodules/lua_cliargs/issues/76
%if "%(rpmvercmp '5.4' '5.4')" >= "0"
%filter_from_requires /lua5.4(yaml)/d
%endif

BuildRequires(pre): rpm-macros-lua
BuildRequires: lua5.4-luarocks

%description
Cliargs is a command-line argument parser for Lua. It supports several
types of arguments:

1. required arguments

2. optional arguments with different notations: -short-key VALUE and/or
--expanded-key=VALUE

3. optional arguments with multiple-values that get appended to a list

4. optional "flag" arguments (on/off options) with notations:
-short-key and/or --expanded-key

5. a single optional "splat" argument which can be repeated (must be
the last argument)

Optional arguments can have default values (strings), flags always
default to 'true'.

%prep
%setup

%build
luarocks-5.4 make --verbose --local --deps-mode all --pack-binary-rock \
	rockspecs/lua_cliargs-%version-%luarocks_revision.rockspec

%install
luarocks-5.4 install --verbose --local --deps-mode none \
	--no-manifest --tree %buildroot%prefix *.rock

%check
luarocks-5.4 test --test-type busted \
	rockspecs/lua_cliargs-%version-%luarocks_revision.rockspec

%files
%doc LICENSE
%luarocks_dbdir/lua_cliargs/
%lua_modulesdir_noarch/cliargs
%lua_modulesdir_noarch/cliargs.lua

%changelog
* Mon Apr 22 2025 Sergey Zhidkih <rx1513@altlinux.org> 3.0.2-alt1_lr1
- First build for alt.
