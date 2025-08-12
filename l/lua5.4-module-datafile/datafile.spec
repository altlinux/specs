%define _unpackaged_files_terminate_build 1
%define luarocks_revision 1
# Disable on bootstrap.
%def_without check

Name: lua5.4-module-datafile
Version: 0.11
Release: alt1_lr%luarocks_revision
BuildArch: noarch

Summary: Platform independent system calls for Lua
License: MIT
Group: Development/Other
Url: https://github.com/hishamhm/datafile
Vcs: https://github.com/hishamhm/datafile

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-lua
BuildRequires: lua5.4-luarocks
BuildRequires: liblua5.4-devel

%description
A Lua library for handling paths when loading data files.

%prep
%setup

%build
luarocks-5.4 make --verbose --local --deps-mode all --pack-binary-rock \
	rockspecs/datafile-%version-%luarocks_revision.rockspec

%install
luarocks-5.4 install --verbose --local --deps-mode none \
	--no-manifest --tree %buildroot%prefix *.rock

%check
luarocks-5.4 test --test-type command \
    test/test-datafile-scm-%luarocks_revision.rockspec

%files
%doc LICENSE README.md
%luarocks_dbdir/datafile/
%lua_modulesdir_noarch/datafile/
%lua_modulesdir_noarch/datafile.lua

%changelog
* Fri Aug 11 2025 Timofei Fedotov <sovtouch@altlinux.org> 0.11-alt1_lr1
- Initial build for ALT Sisyphus.
