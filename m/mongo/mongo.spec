Name: mongo
Version: 2.0.6
Release: alt1
Summary: mongo client shell and tools
License: AGPL 3.0
Url: http://www.mongodb.org
Group: Development/Databases

Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version-%release.tar

BuildRequires: libjs-devel libreadline-devel boost-devel libpcre-devel gcc-c++ scons libpcrecpp-devel boost-filesystem-devel boost-program_options-devel libpcrecpp-devel libsnappy-devel

%description
Mongo (from "huMONGOus") is a schema-free document-oriented database.
It features dynamic profileable queries, full indexing, replication
and fail-over support, efficient storage of large binary data objects,
and auto-sharding.

This package provides the mongo shell, import/export tools, and other
client utilities.

%package server
Summary: mongo server, sharding server, and support scripts
Group: Development/Databases

%description server
Mongo (from "huMONGOus") is a schema-free document-oriented database.

This package provides the mongo server software, mongo sharding server
softwware, default configuration files, and init.d scripts.

%package devel
Summary: Headers and libraries for mongo development
Group: Development/Databases

%description devel
Mongo (from "huMONGOus") is a schema-free document-oriented database.

This package provides the mongo static library and header files needed
to develop mongo client software.

%prep
%setup

%build
scons --prefix=%buildroot/usr --use-system-all all
# XXX really should have shared library here

%install
scons --prefix=%buildroot/usr --full --nostrip install
mkdir -p %buildroot%_man1dir
cp debian/*.1 %buildroot%_man1dir/
mkdir -p %buildroot%_initdir/
cp rpm/init.d-mongod %buildroot%_initdir/mongod
chmod a+x %buildroot%_initdir/mongod
mkdir -p %buildroot%_sysconfdir/mongo
cp rpm/mongod.conf %buildroot%_sysconfdir/mongo/mongod.conf
mkdir -p %buildroot%_sysconfdir/sysconfig
cp rpm/mongod.sysconfig %buildroot%_sysconfdir/sysconfig/mongod
mkdir -p %buildroot/var/lib/mongo
mkdir -p %buildroot/var/log/mongo

mkdir -p %buildroot/%_logrotatedir
cp rpm/mongo.logrotate %buildroot/%_logrotatedir/mongo

mkdir -p %buildroot/%systemd_unitdir
cp rpm/mongod.service %buildroot/%systemd_unitdir/

scons -c

%pre server
%_sbindir/groupadd -r -f mongod
%_sbindir/useradd -r -n -g mongod -d /var/lib/mongo -s /bin/false -c "Mongod pseudo user" mongod >/dev/null 2>&1 ||:

%post server
%post_service mongod

%preun server
%preun_service mongod

%files
%doc README GNU-AGPL-3.0.txt

%_bindir/mongo
%_bindir/mongodump
%_bindir/mongoexport
%_bindir/mongofiles
%_bindir/mongoimport
%_bindir/mongorestore
%_bindir/mongostat
%_bindir/mongotop
%_bindir/bsondump

%_man1dir/mongo.1*
%_man1dir/mongodump.1*
%_man1dir/mongoexport.1*
%_man1dir/mongofiles.1*
%_man1dir/mongoimport.1*
%_man1dir/mongorestore.1*
%_man1dir/mongosniff.1*
%_man1dir/mongostat.1*
%_man1dir/bsondump.1*

%files server
%config(noreplace) %_sysconfdir/mongo/mongod.conf
%config(noreplace) %_sysconfdir/sysconfig/mongod
%config(noreplace) %_logrotatedir/mongo
%_bindir/mongod
%_bindir/mongos
%_man1dir/mongos.1*
%_man1dir/mongod.1*
%_initdir/mongod
%systemd_unitdir/mongod.service
%attr(0750,mongod,mongod) %dir /var/lib/mongo
%attr(0750,mongod,mongod) %dir /var/log/mongo

%files devel
%_includedir/mongo
%_libdir/libmongoclient.a

%changelog
* Mon Jun 18 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.6-alt1
- 2.0.6

* Mon May 21 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.5-alt1
- 2.0.5

* Sat May 05 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.4-alt2
- Add systemd unit file

* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt1.1
- Rebuilt with Boost 1.49.0

* Mon Mar 26 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.4-alt1
- 2.0.4

* Mon Dec 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.1
- Rebuilt with Boost 1.48.0

* Wed Nov 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Tue Sep 06 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.3-alt1
- 1.8.3

* Mon Aug 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.2-alt2
- add logrotate script (ALT #25966)

* Sun Jul 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.2-alt1.1
- Rebuilt with Boost 1.47.0

* Fri Jul 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Thu Apr 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Thu Apr 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.0-alt2
- enable journaling by default

* Mon Apr 04 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.0-alt1
- 1.8.0 release

* Wed Mar 16 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.5-alt2
- repair build with boost-1.46

* Wed Dec 29 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.5-alt1
- 1.6.5

* Mon Dec 06 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.4-alt1
- 1.6.4

* Thu Nov 11 2010 Konstantin Pavlov <thresh@altlinux.org> 1.6.3-alt1
- 1.6.3

* Fri Aug 06 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Wed Jun 30 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.4-alt1
- 1.4.4

* Mon May 31 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.3-alt1
- 1.4.3

* Tue May 18 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Tue Apr 13 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Mon Feb 15 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.2-alt1
- initial
