Name: mongo
Version: 3.4.10
Release: alt1
Summary: mongo client shell and tools
License: AGPL 3.0
Url: http://www.mongodb.org
Group: Development/Databases
# From https://docs.mongodb.com/manual/installation
# Changed in version 3.4: MongoDB no longer supports 32-bit x86 platforms.
ExclusiveArch: x86_64

Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version.tar

Patch1:         mongodb-2.4.5-no-term.patch

BuildRequires: /proc gcc-c++ python-devel python-module-pymongo scons boost-devel boost-filesystem-devel boost-program_options-devel libssl-devel libpcre-devel libpcrecpp-devel libreadline-devel libpcap-devel libsnappy-devel libv8-3.24-devel systemd-devel libgperftools-devel libsasl2-devel libstemmer-devel libyaml-cpp-devel valgrind-devel zlib-devel python-modules-json

%description
Mongo (from "huMONGOus") is a schema-free document-oriented database.
It features dynamic profileable queries, full indexing, replication
and fail-over support, efficient storage of large binary data objects,
and auto-sharding.

This package provides the mongo shell.

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


%prep
%setup
%patch1 -p1

# CRLF -> LF
sed -i 's/\r//' README

# Disable optimization for s2 library
# https://jira.mongodb.org/browse/SERVER-17511
sed -i -r "s|(env.Append\(CCFLAGS=\['-DDEBUG_MODE=false')(\]\))|\1,'-O0'\2|"  src/third_party/s2/SConscript

%build
# NOTE: Build flags must be EXACTLY the same in the install step!
# If you fail to do this, mongodb will be built twice...
%define common_opts \\\
	-j %__nprocs \\\
	--use-system-tcmalloc \\\
	--use-system-pcre \\\
	--use-system-snappy \\\
	--use-system-valgrind \\\
	--use-system-zlib \\\
	--use-system-stemmer \\\
	--use-system-yaml \\\
	--prefix=%buildroot%_prefix \\\
	--nostrip \\\
	--use-sasl-client \\\
	--wiredtiger=on \\\
	--ssl \\\
	--disable-warnings-as-errors \\\
	MONGO_VERSION="%{version}-%{release}" \\\
	CCFLAGS="%{?optflags} `pkg-config --cflags libpcrecpp`"

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
%_bindir/mongoperf

%_man1dir/mongo.1*
%_man1dir/mongoperf.1*
%exclude %_man1dir/mongodump.1*
%exclude %_man1dir/mongoexport.1*
%exclude %_man1dir/mongofiles.1*
%exclude %_man1dir/mongoimport.1*
%exclude %_man1dir/mongorestore.1*
%exclude %_man1dir/mongosniff.1*
%exclude %_man1dir/mongostat.1*
%exclude %_man1dir/bsondump.1*
%exclude %_man1dir/mongotop.1*
%exclude %_man1dir/mongooplog.1*

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
%attr(1770,root,mongod) %dir %_logdir/%name
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
%attr(1770,root,mongod) %dir %_logdir/%name
%attr(0750,mongod,mongod) %dir %_runtimedir/%name

%changelog
* Fri Nov 24 2017 Vladimir Didenko <cow@altlinux.org> 3.4.10-alt1
- 3.4.10

* Thu Oct 5 2017 Vladimir Didenko <cow@altlinux.org> 3.4.9-alt1
- 3.4.9

* Fri Aug 25 2017 Vladimir Didenko <cow@altlinux.org> 3.4.7-alt1
- 3.4.7

* Tue Jul 4 2017 Vladimir Didenko <cow@altlinux.org> 3.4.5-alt1
- 3.4.5

* Fri Apr 28 2017 Vladimir Didenko <cow@altlinux.org> 3.4.4-alt1
- 3.4.4

* Mon Apr 10 2017 Vladimir Didenko <cow@altlinux.org> 3.4.3-alt1
- 3.4.3

* Fri Feb 3 2017 Vladimir Didenko <cow@altlinux.org> 3.4.2-alt1
- 3.4.2

* Mon Dec 26 2016 Vladimir Didenko <cow@altlinux.org> 3.4.1-alt1
- 3.4.1

* Fri Dec 9 2016 Vladimir Didenko <cow@altlinux.org> 3.4.0-alt1.1
- drop 32-bit packages

* Thu Dec 8 2016 Vladimir Didenko <cow@altlinux.org> 3.4.0-alt1
- 3.4.0
- use bundled boost

* Fri Nov 25 2016 Vladimir Didenko <cow@altlinux.org> 3.2.11-alt1
- 3.2.11

* Tue Oct 4 2016 Vladimir Didenko <cow@altlinux.org> 3.2.10-alt1
- 3.2.10

* Tue Aug 30 2016 Vladimir Didenko <cow@altlinux.org> 3.2.9-alt1
- 3.2.9

* Wed Jul 13 2016 Vladimir Didenko <cow@altlinux.org> 3.2.8-alt1
- 3.2.8

* Thu Jun 9 2016 Vladimir Didenko <cow@altlinux.org> 3.2.7-alt1
- 3.2.7

* Tue May 17 2016 Vladimir Didenko <cow@altlinux.org> 3.2.6-alt1
- 3.2.6

* Mon Apr 25 2016 Vladimir Didenko <cow@altlinux.org> 3.2.5-alt1
- 3.2.5

* Mon Mar 14 2016 Vladimir Didenko <cow@altlinux.org> 3.2.4-alt1
- 3.2.4

* Thu Feb 25 2016 Vladimir Didenko <cow@altlinux.org> 3.2.3-alt1
- 3.2.3

* Mon Jan 18 2016 Vladimir Didenko <cow@altlinux.org> 3.2.1-alt1
- 3.2.1

* Tue Jan  5 2016 Terechkov Evgenii <evg@altlinux.org> 3.2.0-alt2.rc4
- Change mode/owner of /var/log/mongo to 1770/root:mongod according to ALT Secure Packaging Policy (ALT#31676)

* Wed Dec 2 2015 Vladimir Didenko <cow@altlinux.org> 3.2.0-alt1.rc4
- 3.2.0 rc4 (closes: #31540)

* Wed Mar 25 2015 Vladimir Didenko <cow@altlinux.org> 2.6.9-alt1
- 2.6.9
- enable ssl support

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 2.4.9-alt1.1
- Rebuild with boost 1.57.0;
- Add patch that add necessary includes to fix build.

* Wed Jan 29 2014 Dmitry Derjavin <dd@altlinux.org> 2.4.9-alt1
- 2.4.9

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
