%define luaver 5.4

%def_without duckdb

Name: lua%luaver-module-dbi
Version: 0.7.5
Release: alt3

License: MIT
Url: https://github.com/mwild1/luadbi
Group: Databases
Summary: Database interface library for Lua

Source0: luadbi-%version.tar
Patch0: Fix-duckdb-install.patch
Patch1: Fix-FTBS-duckdb.patch

Provides: lua-dbi = %EVR
Provides: lua%luaver-dbi = %EVR
Obsoletes: lua%luaver-dbi < %EVR

BuildRequires: lua%luaver
BuildRequires: liblua%luaver-devel
BuildRequires: libsqlite3-devel
BuildRequires: libmariadb-devel
BuildRequires: libpq-devel
%if_with duckdb
%ifnarch %ix86
BuildRequires: duckdb duckdb-devel-static
%endif
%endif

%description
LuaDBI is a database interface library for Lua. It is designed to provide a
RDBMS agnostic API for handling database operations. LuaDBI also provides
support for prepared statement handles, placeholders and bind parameters for
all database operations.

Currently LuaDBI supports DB2, Oracle, MySQL, PostgreSQL and SQLite databases
with native database drivers.

%prep
%setup -n luadbi-%version

%patch0 -p1
%patch1 -p1

%build
%make_build mysql \
	CFLAGS="%optflags" \
	LUA_V=%current_lua_version LUA_INC="-I%_includedir" \
	MYSQL_LDFLAGS="-L%_libdir/mysql -lmysqlclient"

%make_build psql \
	CFLAGS="%optflags" \
	LUA_V=%current_lua_version LUA_INC="-I%_includedir"

%make_build sqlite3 \
	CFLAGS="%optflags" \
	LUA_V=%current_lua_version LUA_INC="-I%_includedir"

%if_with duckdb
%ifnarch %ix86
%make_build duckdb \
	CFLAGS="%optflags" \
	LUA_V=%current_lua_version LUA_INC="-I%_includedir"
%endif
%endif

%install
make install_mysql INSTALL='install -p' \
	CFLAGS="%optflags" \
	LUA_V=%current_lua_version LUA_INC="-I%_includedir" \
	LUA_CDIR=%buildroot%lua_modulesdir LUA_LDIR=%buildroot%lua_modulesdir_noarch \
	MYSQL_LDFLAGS="-L%_libdir/mysql -lmysqlclient"

make install_psql INSTALL='install -p' \
	CFLAGS="%optflags" \
	LUA_V=%current_lua_version LUA_INC="-I%_includedir" \
	LUA_CDIR=%buildroot%lua_modulesdir LUA_LDIR=%buildroot%lua_modulesdir_noarch

make install_sqlite3 INSTALL='install -p' \
	CFLAGS="%optflags" \
	LUA_V=%current_lua_version LUA_INC="-I%_includedir" \
	LUA_CDIR=%buildroot%lua_modulesdir LUA_LDIR=%buildroot%lua_modulesdir_noarch

%if_with duckdb
%ifnarch %ix86
make install_duckdb INSTALL='install -p' \
	CFLAGS="%optflags" \
	LUA_V=%current_lua_version LUA_INC="-I%_includedir" \
	LUA_CDIR=%buildroot%lua_modulesdir LUA_LDIR=%buildroot%lua_modulesdir_noarch
%endif
%endif

%check
lua%luaver -e \
	'package.cpath="%buildroot%lua_modulesdir/?.so;"..package.cpath;
	package.path="%buildroot%lua_modulesdir_noarch/?.lua;"..package.path;
	local DBI = require("DBI"); print("Hello from "..DBI._VERSION.."!");'

%files
%doc COPYING README.md
%lua_modulesdir/dbd/
%lua_modulesdir_noarch/DBI.lua

%changelog
* Sun Jun 28 2026 Alexei Takaseev <taf@altlinux.org> 0.7.5-alt3
- Disable duckdb support by default

* Thu May 28 2026 Alexei Takaseev <taf@altlinux.org> 0.7.5-alt2
- Change BR duckdb duckdb-devel -> duckdb duckdb-devel-static

* Thu Oct 23 2025 Alexei Takaseev <taf@altlinux.org> 0.7.5-alt1
- 0.7.5
- Fix FTBFS
- Change BR postgresql-devel -> libpq-devel

* Sat Jul 30 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7.2-alt2
- Rebuilt for consistent package name for all lua versions.
- Provided and obsoleted previous lua-dbi builds.

* Sat Jul 02 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7.2-alt1
- Initial build for ALT Sisyphus based on Fedora spec.
