Summary:        JSON Parser/Constructor for Lua
Name:           lua5-json
Version:        1.3.3
Release:        alt1
URL:            http://luaforge.net/projects/luajson/
Packager: 	Valentin Rosavitskiy <valintinr@altlinux.org>
License:        MIT
Group: 		Development/Other

BuildRequires:  liblua5-devel lua5
BuildArch:      noarch
Source0:        %name-%version.tar

%description
LuaJSON is a customizable JSON decoder/encoder, using LPEG for parsing.

%prep
%setup -q

%build

%install
mkdir -p %buildroot%_datadir/lua5
cp -pr lua/* %buildroot%_datadir/lua5/

%files
%doc LICENSE docs/* README
%_datadir/lua5/*

%changelog
* Tue Nov 04 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 1.3.3-alt1
- Inital build for ALT

