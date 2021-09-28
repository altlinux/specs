Name: pgagent
Version: 4.2.1
Release: alt1

Summary: Job scheduler for PostgreSQL which may be managed using pgAdmin

License: BSD
Group: Databases
Url: http://www.postgresql.org/ftp/pgadmin3/release/pgagent/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%define REL %(echo "%version" | sed -e "s|\\.|_|g")

# Source-url: https://github.com/postgres/pgagent/archive/REL-%REL.tar.gz
Source: %name-%version.tar

# Automatically added by buildreq on Wed Sep 29 2021
# optimized out: boost-devel boost-devel-headers cmake cmake-modules glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libsasl2-3 libstdc++-devel python3 python3-base python3-module-paste python3-module-repoze sh4 sssd-client tzdata
BuildRequires: boost-asio-devel boost-filesystem-devel cmake gcc-c++ libssl-devel postgresql-devel

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
rm -f %buildroot/usr/{LICENSE,README}

%files
%doc LICENSE
%_bindir/*
%_datadir/*.sql
%_datadir/pgsql

%changelog
* Wed Sep 29 2021 Vitaly Lipatov <lav@altlinux.ru> 4.2.1-alt1
- new version 4.2.1 (with rpmrb script)
- update buildreqs

* Wed Dec 06 2017 Vitaly Lipatov <lav@altlinux.ru> 3.4.1-alt1
- set Source-url
- new version 3.4.1 (with rpmrb script)

* Mon Jun 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Version 3.4.0

* Sat Dec 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt1
- Initial build for Sisyphus (ALT #28193)

