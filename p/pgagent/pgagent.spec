Name: pgagent
Version: 3.3.0
Release: alt1
Summary: Job scheduler for PostgreSQL which may be managed using pgAdmin
License: BSD
Group: Databases
Url: http://www.postgresql.org/ftp/pgadmin3/release/pgagent/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: cmake postgresql-devel libwxGTK-devel gcc-c++

%description
pgAgent is a job scheduler for PostgreSQL which may be managed using
pgAdmin.  Prior to pgAdmin v1.9, pgAgent shipped as part of pgAdmin.
From pgAdmin v1.9 onwards, pgAgent is shipped as a separate application.

%prep
%setup

%build
cmake \
	-DCMAKE_INSTALL_PREFIX:PATH='%prefix' \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DCMAKE_CXX_FLAGS:STRING='%optflags' \
	-DCMAKE_STRIP:FILEPATH='/bin/echo' \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DPostgreSQL_CONFIG_EXECUTABLE:FILEPATH='%_bindir/pg_config' \
	-DwxWidgets_CONFIG_EXECUTABLE:FILEPATH='%_bindir/wx-config' \
	-DSTATIC_BUILD:BOOL=OFF \
	-DwxWidgets_USE_STATIC:BOOL=OFF \
	-DwxWidgets_USE_UNICODE:BOOL=ON \
	-DwxWidgets_wxrc_EXECUTABLE:FILEPATH='%_bindir/wxrc' \
	.

%make_build VERBOSE=1

%install
%makeinstall_std VERBOSE=1

%files
%doc LICENSE
%_bindir/*
%_datadir/*.sql

%changelog
* Sat Dec 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt1
- Initial build for Sisyphus (ALT #28193)

