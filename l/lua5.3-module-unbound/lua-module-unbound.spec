%define oname luaunbound
%define lua_major 5.3

Name: lua%lua_major-module-unbound
Version: 1.0
Release: alt1

Summary: binding to libunbound

License: MIT
Group: Development/Other
Url: https://www.zash.se/luaunbound.html

# repacked https://code.zash.se/dl/luaunbound/luaunbound-%version.tar.gz
Source: %oname-%version.tar

BuildRequires(pre): rpm-macros-lua >= 1.4
BuildRequires: liblua5.3-devel
BuildRequires: libunbound-devel

Provides: lua-module-unbound = %EVR

%description
Lua bindings for the Unbound APIs.

%prep
%setup -n %oname-%version

%build
%make_build \
	LUA_VERSION=%lua_major \
	MYCFLAGS="%optflags" \
	MYLDFLAGS="%optflags" \
	CC=gcc \
	LD=gcc \
	#

%install
%makeinstall_std LUA_LIBDIR=%lua_modulesdir

%check
# based on Fedora lua-unbound package check
%lua -e \
	'package.cpath="%buildroot%lua_modulesdir/?.so;"..package.cpath;
	local lunbound = require("lunbound");
	print("Hello from "..lunbound._LIBVER.."!");'

%files
%doc LICENSE README.markdown
%lua_modulesdir/lunbound.so*

%changelog
* Mon Mar 21 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.0-alt1
- Initial build for ALT Sisyphus.
