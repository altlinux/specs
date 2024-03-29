%define oname luaunbound

Name: lua5.3-module-unbound
Version: 1.0
Release: alt2

Summary: binding to libunbound

License: MIT
Group: Development/Other
Url: https://www.zash.se/luaunbound.html

# repacked https://code.zash.se/dl/luaunbound/luaunbound-%version.tar.gz
Source: %oname-%version.tar

BuildRequires(pre): liblua5.3-devel rpm-build-lua
BuildRequires: lua5.3 libunbound-devel

Provides: lua-module-unbound = %EVR

%description
Lua bindings for the Unbound APIs.

%prep
%setup -n %oname-%version

%build
%make_build \
	LUA_VERSION=5.3 \
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
* Sun Jul 03 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.0-alt2
- Rebuild for autogenerated lua provides.

* Mon Mar 21 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.0-alt1
- Initial build for ALT Sisyphus.
