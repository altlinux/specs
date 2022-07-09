Name: lua5.3-module-dbi
Version: 0.7.2
Release: alt1

License: MIT
Url: https://github.com/mwild1/luadbi
Group: Databases
Summary: Database interface library for Lua

Source0: luadbi-%version.tar

Provides: lua-dbi = %EVR

BuildRequires: lua5.3
BuildRequires: liblua5.3-devel
BuildRequires: libsqlite3-devel
BuildRequires: libmariadb-devel
BuildRequires: postgresql-devel

%description
LuaDBI is a database interface library for Lua. It is designed to provide a
RDBMS agnostic API for handling database operations. LuaDBI also provides
support for prepared statement handles, placeholders and bind parameters for
all database operations.

Currently LuaDBI supports DB2, Oracle, MySQL, PostgreSQL and SQLite databases
with native database drivers.

%prep
%setup -n luadbi-%version

%build
%make_build free \
	CFLAGS="%optflags" \
	LUA_V=%current_lua_version LUA_INC="-I%_includedir" \
	MYSQL_LDFLAGS="-L%_libdir/mysql -lmysqlclient"

%install
make install_free INSTALL='install -p' \
	CFLAGS="%optflags" \
	LUA_V=%current_lua_version LUA_INC="-I%_includedir" \
	LUA_CDIR=%buildroot%lua_modulesdir LUA_LDIR=%buildroot%lua_modulesdir_noarch \
	MYSQL_LDFLAGS="-L%_libdir/mysql -lmysqlclient"

%check
lua5.3 -e \
	'package.cpath="%buildroot%lua_modulesdir/?.so;"..package.cpath;
	package.path="%buildroot%lua_modulesdir_noarch/?.lua;"..package.path;
	local DBI = require("DBI"); print("Hello from "..DBI._VERSION.."!");'

%files
%doc COPYING README.md
%lua_modulesdir/dbd/
%lua_modulesdir_noarch/DBI.lua

%changelog
* Sat Jul 02 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7.2-alt1
- Initial build for ALT Sisyphus based on Fedora spec.
