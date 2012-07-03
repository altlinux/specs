Name: skytools
Version: 2.1.12
Release: alt1.1.1

Summary:Skytools are database management tools to WAL shipping, queueing and replication
Group: Databases
License: BSD
URL: http://pgfoundry.org/projects/skytools/
Packager: Sergey Alembekov <rt@altlinux.ru>
Source: %name.tar.gz
Requires: python
BuildRequires: postgresql-devel postgresql-server postgresql9.1-contrib python-devel

%description
This is a package of tools in use in Skype for replication and
failover.  Also it includes a generic queuing mechanism PgQ and
utility library for Python scripts.
Skytools are database management tools to WAL shipping, queueing
and replication. This package has Python parts of skytools:

londiste - PostgreSQL replication engine written in Python
pgqadm - PgQ tickter and administration interface
walmgr - Tools for managing WAL-based replication for PostgreSQL.

%prep
%setup -n %name

%build
%configure
%make

%install
%make DESTDIR=%buildroot install

%files
%_bindir/bulk_loader.py
%_bindir/cube_dispatcher.py
%_bindir/londiste.py
%_bindir/pgqadm.py
%_bindir/queue_mover.py
%_bindir/queue_splitter.py
%_bindir/scriptmgr.py
%_bindir/skytools_upgrade.py
%_bindir/table_dispatcher.py
%_bindir/walmgr.py
%python_sitelibdir/londiste
%python_sitelibdir/pgq
%python_sitelibdir/skytools
%_libdir/pgsql/logtriga.so
%_libdir/pgsql/pgq_lowlevel.so
%_libdir/pgsql/pgq_triggers.so
%python_sitelibdir/skytools-%version-*.egg-info
%_datadir/doc/postgresql/contrib/README.londiste
%_datadir/doc/postgresql/contrib/README.pgq
%_datadir/doc/postgresql/contrib/README.pgq_ext
%_datadir/pgsql/contrib/logtriga.sql
%_datadir/pgsql/contrib/londiste.sql
%_datadir/pgsql/contrib/londiste.upgrade.sql
%_datadir/pgsql/contrib/pgq.sql
%_datadir/pgsql/contrib/pgq.upgrade.sql
%_datadir/pgsql/contrib/pgq_ext.sql
%_datadir/pgsql/contrib/pgq_lowlevel.sql
%_datadir/pgsql/contrib/pgq_triggers.sql
%_datadir/pgsql/contrib/uninstall_pgq.sql
%_datadir/skytools
%_datadir/doc/skytools
%_man1dir/*
%_man5dir/*


%changelog
* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.12-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.12-alt1.1
- Rebuild with Python-2.7

* Fri Feb 04 2011 Sergey Alembekov <rt@altlinux.ru> 2.1.12-alt1
- 2.1.12 
- now working with postgresql9.0

* Wed Aug 18 2010 Sergey Alembekov <rt@altlinux.ru> 2.1.11-alt1
- new version 

* Thu Jul 29 2010 Sergey Alembekov <rt@altlinux.ru> 2.1.10-alt2
- rebuild with postgresql8.4

* Wed Sep 02 2009 Sergey Alembekov <rt@altlinux.ru> 2.1.10-alt1
- init build 
