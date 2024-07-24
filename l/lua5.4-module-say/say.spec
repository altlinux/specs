%define _unpackaged_files_terminate_build 1
# busted not in sisyphus yet
%def_without check
%define luarocks_revision 3

Name: lua5.4-module-say
Version: 1.4.1
Release: alt1_lr%luarocks_revision

Summary: Lua string hashing library, useful for internationalization
License: MIT
Group: Development/Other
Url: https://luarocks.org/modules/lunarmodules/say
Vcs: https://github.com/lunarmodules/say
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-lua
BuildRequires: lua5.4-luarocks

%description
Say is a simple string key/value store for i18n
or any other case where you want namespaced strings.

%prep
%setup

%build
luarocks-5.4 make --verbose --local --deps-mode all --pack-binary-rock \
	rockspecs/say-%version-%luarocks_revision.rockspec

%install
luarocks-5.4 install --verbose --local --deps-mode none \
	--no-manifest --tree %buildroot%prefix *.rock

%files
%doc LICENSE README.*
%luarocks_dbdir/say/
%lua_modulesdir_noarch/say/

%changelog
* Wed Jul 24 2024 Ajrat Makhmutov <rauty@altlinux.org> 1.4.1-alt1_lr3
- First build for ALT.
