%define _unpackaged_files_terminate_build 1
# Tests not provided.
%def_without check
%define luarocks_revision 1

Name: lua5.4-module-lua-term
Version: 0.8
Release: alt1_lr%luarocks_revision

Summary: Lua-term is a Lua module for manipulating a terminal
License: MIT/X11
Group: Development/Other
Url: https://github.com/hoelzro/lua-term
Vcs: https://github.com/hoelzro/lua-term

Source: %name-%version.tar

Provides: luarocks5.4(lua-term) = %EVR

BuildRequires(pre): rpm-macros-lua
BuildRequires: lua5.4-luarocks
BuildRequires: liblua5.4-devel

%description
%summary.

%prep
%setup

%build
luarocks-5.4 make --verbose --local --deps-mode all --pack-binary-rock \
	lua-term-%version-%luarocks_revision.rockspec

%install
luarocks-5.4 install --verbose --local --deps-mode none \
	--no-manifest --tree %buildroot%prefix *.rock

%files
%doc COPYING
%luarocks_dbdir/lua-term/
%lua_modulesdir/term/core.so
%lua_modulesdir_noarch/term/

%changelog
* Tue Apr 08 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.8-alt1_lr1
- First build for alt.
