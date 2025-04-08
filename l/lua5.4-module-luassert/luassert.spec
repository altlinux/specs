%define _unpackaged_files_terminate_build 1
# Busted not in sisyphus yet.
%def_without check
%define luarocks_revision 1

Name: lua5.4-module-luassert
Version: 1.9.0
Release: alt1_lr%luarocks_revision

Summary: Assertion library for Lua
License: MIT
Group: Development/Other
Url: https://github.com/lunarmodules/luassert
Vcs: https://github.com/lunarmodules/luassert
BuildArch: noarch

Source: %name-%version.tar

Provides: luarocks5.4(luassert) = %EVR

BuildRequires(pre): rpm-macros-lua
BuildRequires: lua5.4-luarocks
BuildRequires: lua5.4-module-say

%description
Luassert extends Lua's built-in assertions to provide additional tests
and the ability to create your own. You can modify chains of assertions
with not.

%prep
%setup

%build
luarocks-5.4 make --verbose --local --deps-mode all --pack-binary-rock \
	rockspecs/luassert-%version-%luarocks_revision.rockspec

%install
luarocks-5.4 install --verbose --local --deps-mode none \
	--no-manifest --tree %buildroot%prefix *.rock

%check
luarocks-5.4 test --test-type busted rockspecs/luassert-%version-%luarocks_revision.rockspec

%files
%doc LICENSE
%luarocks_dbdir/luassert/%version-%luarocks_revision
%lua_modulesdir_noarch/luassert

%changelog
* Tue Apr 08 2025 Sergey Zhidkih <rx1513@altlinux.org> 1.9.0-alt1_lr1
- First build for alt.
