%define _unpackaged_files_terminate_build 1
%define luarocks_revision 1
%def_with check

Name: lua5.4-module-luacov
Version: 0.16.0
Release: alt1_lr%luarocks_revision
BuildArch: noarch

Summary: LuaCov is a simple coverage analyzer for Lua code
License: MIT
Group: Development/Other
Url: https://lunarmodules.github.io/luacov/
Vcs: https://github.com/lunarmodules/luacov

Source: %name-%version.tar

#self-dependency
%filter_from_requires /lua5.4(cluacov\..*)/d

BuildRequires(pre): rpm-macros-lua
BuildRequires: lua5.4-luarocks
BuildRequires: liblua5.4-devel
BuildRequires: lua5.4-module-datafile
%if_with check
BuildRequires: lua5.4-module-busted
%endif

%description
%summary.

%prep
%setup

%build
luarocks-5.4 make --verbose --local --deps-mode all --pack-binary-rock \
	luacov-scm-%luarocks_revision.rockspec

%install
luarocks-5.4 install --verbose --local --deps-mode none \
	--no-manifest --tree %buildroot%prefix *.rock

%check
luarocks-5.4 test --test-type busted \
    luacov-scm-%luarocks_revision.rockspec

%files
%_bindir/luacov
%lua_modulesdir_noarch/luacov.lua
%lua_modulesdir_noarch/luacov/
%luarocks_dbdir/luacov/
%doc LICENSE README.md

%changelog
* Thu Aug 11 2025 Timofei Fedotov <sovtouch@altlinux.org> 0.16.0-alt1_lr1
- Initial build for ALT Sisyphus.
