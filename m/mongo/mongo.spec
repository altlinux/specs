Name: mongo
Version: 2.4.8
Release: alt1
Summary: mongo client shell and tools
License: AGPL 3.0
Url: http://www.mongodb.org
Group: Development/Databases

Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version.tar

Patch1:         mongodb-2.4.5-no-term.patch
##Patch 2 - make it possible to use system libraries
Patch2:         mongodb-2.4.5-use-system-version.patch
##Patch 5 - https://jira.mongodb.org/browse/SERVER-9210
Patch5:         mongodb-2.4.5-boost-fix.patch
##Patch 6 - https://github.com/mongodb/mongo/commit/1d42a534e0eb1e9ac868c0234495c0333d57d7c1
Patch6:         mongodb-2.4.5-boost-size-fix.patch
##Patch 7 - https://bugzilla.redhat.com/show_bug.cgi?id=958014
## Need to work on getting this properly patched upstream
Patch7:         mongodb-2.4.5-pass-flags.patch
##Patch 8 - Compile with GCC 4.8
Patch8:         mongodb-2.4.5-gcc48.patch
##Patch 10 - Support atomics on ARM
Patch10:        mongodb-2.4.5-atomics.patch
##From: Robie Basak <robie.basak@canonical.com>
##  Use a signed char to store BSONType enumerations
##Patch 11 https://jira.mongodb.org/browse/SERVER-9680
Patch11:        mongodb-2.4.5-signed-char-for-BSONType-enumerations.patch


BuildRequires: /proc gcc-c++ python-devel python-module-pymongo scons boost-devel boost-filesystem-devel boost-program_options-devel libssl-devel libpcre-devel libpcrecpp-devel libreadline-devel libpcap-devel libsnappy-devel libv8-3.15-devel systemd-devel libgperftools-devel libsasl2-devel

%description
Mongo (from "huMONGOus") is a schema-free document-oriented database.
It features dynamic profileable queries, full indexing, replication
and fail-over support, efficient storage of large binary data objects,
and auto-sharding.

This package provides the mongo shell, import/export tools, and other
client utilities.

%package server-mongod
Summary: mongo server, sharding server,  and support scripts
Group: Development/Databases
Provides: %name-server
Obsoletes: %name-server

%description server-mongod
Mongo (from "huMONGOus") is a schema-free document-oriented database.

mongod is the primary daemon process for the MongoDB system.
It handles data requests, manages data format,
and performs background management operations.

%package server-mongos
Summary: mongo routing service, and support scripts
Group: Development/Databases

%description server-mongos
Mongo (from "huMONGOus") is a schema-free document-oriented database.

mongos for "MongoDB Shard," is a routing service for MongoDB shard
configurations that processes queries from the application layer,
and determines the location of this data in the sharded cluster,
in order to complete these operations. From the perspective of the
application, a mongos instance behaves identically to any other
MongoDB instance.

%package -n lib%{name}client
Summary: MongoDB shared libraries
Group: System/Libraries

%description -n lib%{name}client
This package provides the shared library for the MongoDB client.

%package -n lib%{name}client-devel
Summary: MongoDB header files
Group: Development/Databases
Provides: %name-devel
Requires: lib%{name}client = %version-%release
Requires: boost-devel

%description -n lib%{name}client-devel
This package provides the header files and C++ driver for MongoDB. MongoDB is
a high-performance, open source, schema-free document-oriented database.

%package -n lib%{name}client-devel-static
Summary: MongoDB static libraries
Group: Development/Databases
Requires: lib%{name}client-devel = %version-%release

%description -n lib%{name}client-devel-static
This package provides the static library for the MongoDB client.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch10 -p1 -b .atomics
%patch11 -p1 -b .type


# spurious permissions
chmod -x README

# wrong end-of-file encoding
sed -i 's/\r//' README

# Put lib dir in correct place
# https://jira.mongodb.org/browse/SERVER-10049
sed -i -e "s@\$INSTALL_DIR/lib@\$INSTALL_DIR/%_lib@g" src/SConscript.client


%build
# NOTE: Build flags must be EXACTLY the same in the install step!
# If you fail to do this, mongodb will be built twice...
%define common_opts \\\
	-j %__nprocs \\\
	--sharedclient \\\
	--use-system-all \\\
	--prefix=%buildroot%_prefix \\\
	--extrapath=%_prefix \\\
	--nostrip \\\
%ifarch x86_64 \
	--use-sasl-client \\\
%endif \
	--full

scons %common_opts

%install
scons install %common_opts

mkdir -p %buildroot%_logdir/%name
mkdir -p %buildroot%_runtimedir/%name
mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_man1dir
cp debian/*.1 %buildroot%_man1dir/

#mongod
install -p -D -m 644 mongod.logrotate %buildroot%_logrotatedir/mongod
install -p -D -m 755 mongod.init.alt %buildroot%_initddir/mongod
install -p -D -m 644 mongod.conf %buildroot%_sysconfdir/%name/mongod.conf
install -p -D -m 644 mongod.sysconf %buildroot%_sysconfdir/sysconfig/mongod
install -p -D -m 644 mongod.service %buildroot%_unitdir/mongod.service
install -p -D -m 644 mongod.tmpfile %buildroot%_tmpfilesdir/mongod.conf

#mongos
install -p -D -m 644 mongos.logrotate %buildroot%_logrotatedir/mongos
install -p -D -m 755 mongos.init.alt %buildroot%_initddir/mongos
install -p -D -m 644 mongos.conf %buildroot%_sysconfdir/%name/mongos.conf
install -p -D -m 644 mongod.sysconf %buildroot%_sysconfdir/sysconfig/mongos
install -p -D -m 644 mongos.service %buildroot%_unitdir/mongos.service
install -p -D -m 644 mongod.tmpfile %buildroot%_tmpfilesdir/mongos.conf

%pre server-mongod
%_sbindir/groupadd -r -f mongod ||:
%_sbindir/useradd -r -n -g mongod -d /var/lib/mongo -s /bin/false -c "Mongod pseudo user" mongod >/dev/null 2>&1 ||:

%post server-mongod
%post_service mongod

%preun server-mongod
%preun_service mongod

%pre server-mongos
%_sbindir/groupadd -r -f mongod ||:
%_sbindir/useradd -r -n -g mongod -d /var/lib/mongo -s /bin/false -c "Mongod pseudo user" mongod >/dev/null 2>&1 ||:

%post server-mongos
%post_service mongos

%preun server-mongos
%preun_service mongos


%files
%doc README GNU-AGPL-3.0.txt APACHE-2.0.txt

%_bindir/mongo
%_bindir/mongodump
%_bindir/mongoexport
%_bindir/mongofiles
%_bindir/mongoimport
%_bindir/mongorestore
%_bindir/mongostat
%_bindir/mongotop
%_bindir/bsondump
%_bindir/mongotop
%_bindir/mongooplog
%_bindir/mongoperf
%_bindir/mongosniff

%_man1dir/mongo.1*
%_man1dir/mongodump.1*
%_man1dir/mongoexport.1*
%_man1dir/mongofiles.1*
%_man1dir/mongoimport.1*
%_man1dir/mongorestore.1*
%_man1dir/mongosniff.1*
%_man1dir/mongostat.1*
%_man1dir/bsondump.1*
%_man1dir/mongotop.1*
%_man1dir/mongooplog.1*
%_man1dir/mongoperf.1*

%files server-mongod
%doc GNU-AGPL-3.0.txt APACHE-2.0.txt
%config(noreplace) %_sysconfdir/%name/mongod.conf
%config(noreplace) %_sysconfdir/sysconfig/mongod
%config(noreplace) %_logrotatedir/mongod
%_bindir/mongod
%_man1dir/mongod.1*
%_initdir/mongod
%systemd_unitdir/mongod.service
%_tmpfilesdir/mongod.conf
%attr(0750,mongod,mongod) %dir %_localstatedir/%name
%attr(0750,mongod,mongod) %dir %_logdir/%name
%attr(0750,mongod,mongod) %dir %_runtimedir/%name

%files server-mongos
%doc GNU-AGPL-3.0.txt APACHE-2.0.txt
%config(noreplace) %_sysconfdir/%name/mongos.conf
%config(noreplace) %_sysconfdir/sysconfig/mongos
%config(noreplace) %_logrotatedir/mongos
%_bindir/mongos
%_man1dir/mongos.1*
%_initdir/mongos
%systemd_unitdir/mongos.service
%_tmpfilesdir/mongos.conf
%attr(0750,mongod,mongod) %dir %_logdir/%name
%attr(0750,mongod,mongod) %dir %_runtimedir/%name

%files -n lib%{name}client
%doc README GNU-AGPL-3.0.txt APACHE-2.0.txt
%_libdir/libmongoclient.so

%files -n lib%{name}client-devel
%_includedir/mongo

%files -n lib%{name}client-devel-static
%_libdir/libmongoclient.a

%changelog
* Fri Nov 22 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.4.8-alt1
- Update spec
- Add patches from Fedora
- Fix (ALT#28501, ALT#29472, ALT#28746)
- Add subpackages lib%{name}client, lib%{name}client-devel, lib%{name}client-devel-static and mongo-server-mongos
- Rename mongo-server to mongo-server-mongod

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.0.6-alt1.1.qa1
- NMU: rebuilt with libboost_*.so.1.53.0.

* Sat Dec 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.6-alt1.1
- Rebuilt with Boost 1.52.0

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
