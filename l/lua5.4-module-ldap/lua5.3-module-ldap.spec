Name: lua5.4-module-ldap
Version: 1.3.0.0.2.5714c5f
Release: alt1

Summary: LDAP client library for Lua, using OpenLDAP
License: MIT
Url: https://github.com/lualdap/lualdap/
Group: Development/Other

VCS: https://github.com/lualdap/lualdap/
Source: %name-%version.tar

BuildRequires: lua5.4
BuildRequires: liblua5.4-devel
BuildRequires: libldap-devel

%description
LuaLDAP is a simple interface from Lua to an LDAP client. It enables a Lua
program to:
* Connect to an LDAP server;
* Execute any operation (search, add, compare, delete, modify and rename);
* Retrieve entries and references of the search result.

%prep
%setup

%build
sed -Ei 's,^((LUA|INST)_LIBDIR\s=\s).*$,\1%lua_modulesdir,' config
export CFLAGS="%optflags"
%make_build LUA_LIBDIR=%lua_modulesdir

%install
%makeinstall_std

%files
%doc README.md docs/*
%lua_modulesdir/lualdap.so*

%changelog
* Sun Jul 03 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.3.0.0.2.5714c5f-alt1
- Updated to v1.3.0-2-g5714c5f.

* Thu May 21 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.2.5.0.15.git8c05faf-alt1
- Initial build for ALT Sisyphus based on heavily reworked Fedora spec.

