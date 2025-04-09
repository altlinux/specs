%define _unpackaged_files_terminate_build 1
%def_with check
%define luarocks_revision 1

Name: lua5.4-module-dkjson
Version: 2.8
Release: alt1_lr%luarocks_revision

Summary: Dkjson is a module for encoding and decoding JSON data. It supports UTF-8
License: MIT and X11
Group: Development/Other
Url: http://dkolf.de/dkjson-lua/
Vcs: http://dkolf.de/dkjson-lua/
BuildArch: noarch

Source: %name-%version.tar

Provides: luarocks5.4(dkjson) = %EVR

BuildRequires(pre): rpm-macros-lua
BuildRequires: lua5.4-luarocks

%description
Dkjson is a module for encoding and decoding JSON data.
It supports UTF-8.

%prep
%setup

%build
luarocks-5.4 make --verbose --local --deps-mode all --pack-binary-rock \
	dkjson-%version-%luarocks_revision.rockspec

%install
luarocks-5.4 install --verbose --local --deps-mode none \
	--no-manifest --tree %buildroot%prefix *.rock

%check
lua5.4 jsontest.lua

%files
%luarocks_dbdir/dkjson/
%lua_modulesdir_noarch/dkjson.lua

%changelog
* Wed Apr 09 2025 Sergey Zhidkih <rx1513@altlinux.org> 2.8-alt1_lr1
- Initial build.
