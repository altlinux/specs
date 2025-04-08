%define _unpackaged_files_terminate_build 1
%def_with check
%define luarocks_revision 2

Name: lua5.4-module-lpeg
Version: 1.1.0
Release: alt1_lr%luarocks_revision

Summary: LPeg is a pattern-matching library for Lua, based on Parsing Expression Grammars
License: MIT and X11
Group: Development/Other
Url: https://www.inf.puc-rio.br/~roberto/lpeg/
Vcs: https://luarocks.org/modules/gvvaughan/lpeg/

Source: %name-%version.tar

Provides: luarocks5.4(lpeg) = %EVR

BuildRequires(pre): rpm-macros-lua
BuildRequires: lua5.4-luarocks
BuildRequires: liblua5.4-devel

%description
LPeg is a new pattern-matching library for Lua, based on Parsing
Expression Grammars (PEGs). The nice thing about PEGs is that it
has a formal basis (instead of being an ad-hoc set of features),
allows an efficient and simple implementation, and does most things
we expect from a pattern-matching library (and more, as we can
define entire grammars).

%package doc
Summary: Documentation for lpeg
Group: Documentation
BuildArch: noarch

%description doc
Documentation for lpeg.

%prep
%setup

%build
luarocks-5.4 make --verbose --local --deps-mode all --pack-binary-rock \
	lpeg-%version-%luarocks_revision.rockspec

%install
luarocks-5.4 install --verbose --local --deps-mode none \
	--no-manifest --tree %buildroot%prefix *.rock

%check
luarocks-5.4 test --verbose --local --test-type command \
	lpeg-%version-%luarocks_revision.rockspec

%files
%doc LICENSE
%luarocks_dbdir/lpeg/
%lua_modulesdir_noarch/re.lua
%lua_modulesdir/lpeg.so

%files doc
%doc lpeg.html
%doc re.html

%changelog
* Tue Apr 08 2025 Sergey Zhidkih <rx1513@altlinux.org> 1.1.0-alt1_lr2
- Initial build.
