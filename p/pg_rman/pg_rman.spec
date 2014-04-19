Name: pg_rman
Version: 1.2.8
Release: alt1
Summary: pg_rman is an online backup and restore tool for PostgreSQL
License: New BSD
Group: Databases
Url: http://code.google.com/p/pg-rman/
Packager: Andrew Clark <andyc@altlinux.org>
Source0: http://code.google.com/p/pg-rman/%name-%version.tar.gz

# Automatically added by buildreq on Sat Apr 19 2014 (-bi)
# optimized out: elfutils libcloog-isl4 libcom_err-devel libkrb5-devel libpq-devel libsasl2-3 postgresql-devel python-base setproctitle
BuildRequires: libecpg-devel-static libpam-devel libreadline-devel libselinux-devel libssl-devel postgresql9.3-devel-static setproctitle-devel zlib-devel

%description
The goal of the pg_rman project is providing a method for online
backup and PITR as easy as pg_dump. Also, it maintains a backup
catalog per database cluster. Users can maintain old backups
including archive logs with one command.

%prep
%setup -n %name

%build
%make_build USE_PGXS=1

%install
install -pD -m 755 %_builddir/%name/%name %buildroot%_bindir/%name
mkdir -p %buildroot%_docdir/%name/examples
mv %_builddir/%name/sql/ %buildroot%_docdir/%name/examples/
install -pD -m 644 %_builddir/%name/COPYRIGHT %buildroot%_docdir/%name/

%files
%_bindir/*
%_docdir/%name

%changelog
* Sat Apr 19 2014 Andrew Clark <andyc@altlinux.org> 1.2.8-alt1
- version update 1.2.8-alt1

* Tue Jan 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.7-alt1.1
- Fixed build

* Wed Jan 8 2014 Andrew Clark <andyc@altlinux.org> 1.2.7-alt1
- version update 1.2.7-alt1

* Sat Mar 16 2013 Andrew Clark <andyc@altlinux.org> 1.2.5-alt1
- initial build for ALT.

