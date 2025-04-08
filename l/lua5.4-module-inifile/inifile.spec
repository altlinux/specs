%define _unpackaged_files_terminate_build 1
# No tests provided.
%def_without check
%define luarocks_revision 1

Name: lua5.4-module-inifile
Version: 1.1
Release: alt1_lr%luarocks_revision

Summary: Inifile is a simple, complete ini parser for lua
License: BSD-2-Clause
Group: Development/Other
Url: https://santoslove.github.io/inifile.html
Vcs: https://github.com/bartbes/inifile
BuildArch: noarch

Source: %name-%version.tar

Provides: luarocks5.4(inifile) = %EVR

BuildRequires(pre): rpm-macros-lua
BuildRequires: lua5.4-luarocks

%description
Inifile is a simple, complete ini parser for lua that intends to
preserve as much information as possible, like the order of the file
and the stored comments. It is also out-of-the-box compatible with
LOVE.

%prep
%setup

%build
luarocks-5.4 make --verbose --local --deps-mode all --pack-binary-rock \
	inifile-%version-%luarocks_revision.rockspec

%install
luarocks-5.4 install --verbose --local --deps-mode none \
	--no-manifest --tree %buildroot%prefix *.rock

%files
%luarocks_dbdir/inifile/
%lua_modulesdir_noarch/inifile.lua

%changelog
* Tue Apr 08 2025 Sergey Zhidkih <rx1513@altlinux.org> 1.1-alt1_lr1
- First build for alt.
