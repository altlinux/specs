%define _unpackaged_files_terminate_build 1

%define luaver 5.3
%define oname luaposix
%define rockspecrev 1
%define oversion %version-%rockspecrev

Name: lua%luaver-module-%oname
Version: 38
Release: alt1.%rockspecrev

Summary: Lua bindings for POSIX APIs
License: MIT
Group: Development/Other
Url: https://github.com/luaposix/luaposix
Vcs: https://github.com/luaposix/luaposix

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-lua
BuildRequires: rpm-build-lua
BuildRequires: liblua%luaver-devel
BuildRequires: lua%luaver-luarocks
BuildRequires: lua%luaver-module-luarocks-build-luke

# A computed require('posix.' .. name) yields a bogus lua(posix.).
%filter_from_requires /lua%luaver(posix\.)/d

%description
This is a POSIX binding for LuaJIT, Lua 5.3; like most libraries it
simply binds to C APIs on the underlying system, so it won't work on
non-POSIX systems. However, it does try to detect the level of POSIX
conformance of the underlying system and bind only available APIs.

For a while, luaposix contained support for curses functionality too,
but now that has its own lcurses repository again, where it is being
maintained separately.

%prep
%setup

%build
luarocks-%luaver make --verbose --local --deps-mode all --pack-binary-rock \
	%oname-%oversion.rockspec

%install
luarocks-%luaver install --verbose --local --deps-mode none \
	--no-manifest --tree %buildroot%prefix %oname-%oversion.*.rock
%luarocks_move_docs doc

%files
%doc LICENSE README.md docs_from_rockstree/*
%lua_modulesdir/posix
%lua_modulesdir_noarch/posix
%luarocks_dbdir/%oname

%changelog
* Thu Nov 12 2026 Alexandr Shashkin <dutyrok@altlinux.org> 38-alt1.1
- Updated to 38.

* Tue Oct 27 2026 Alexandr Shashkin <dutyrok@altlinux.org> 37.0-alt1.1
- Updated to 37.0.

* Mon Feb 17 2025 Alexandr Shashkin <dutyrok@altlinux.org> 36.3-alt1.1
- Updated to 36.3.

* Fri Aug 04 2023 Alexandr Shashkin <dutyrok@altlinux.org> 36.2.1-alt1.1
- 36.1 -> 36.2.1

* Sun Feb 19 2023 Alexandr Shashkin <dutyrok@altlinux.org> 36.1-alt1
- Initial build for sisyphus
