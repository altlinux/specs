%define _unpackaged_files_terminate_build 1

%define oname luarocks-build-luke
%define rockspecrev 1
%define oversion %version-%rockspecrev
%global luaver 5.4

Name: lua%luaver-module-%oname
Version: 0.3.2
Release: alt1.%rockspecrev

Summary: LuaRocks build backend for luke
License: MIT
Group: Development/Other
Url: https://github.com/gvvaughan/luke
Vcs: https://github.com/gvvaughan/luke
BuildArch: noarch

Source: %name-%version.tar

Requires: lua%luaver-luarocks

BuildRequires(pre): rpm-macros-lua
BuildRequires: rpm-build-lua
BuildRequires: lua%luaver-luarocks

# One smushed file with the luke and std.* modules bundled inside.
%add_findreq_skiplist %lua_modulesdir_noarch/luarocks/build/luke.lua

%description
Build a rock from the recipe in the build table of its rockspec, with
build.type = 'luke'. The backend is one file that needs nothing else
installed.

%prep
%setup

%build
luarocks-%luaver make --verbose --local --deps-mode all --pack-binary-rock \
	%oname-%oversion.rockspec

%install
luarocks-%luaver install --verbose --local --deps-mode none \
	--no-manifest --tree %buildroot%prefix %oname-%oversion.all.rock
%luarocks_move_docs doc

%files
%doc LICENSE README.md docs_from_rockstree/luke.md
%lua_modulesdir_noarch/luarocks/build/luke.lua
%luarocks_dbdir/%oname

%changelog
* Thu Nov 12 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.3.2-alt1.1
- Initial build for ALT Sisyphus.
