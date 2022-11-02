%ifarch %valgrind_arches
%def_enable valgrind
%endif

Name: mongo
Version: 4.4.17
Release: alt2
Summary: mongo client shell and tools
License: SSPL-1.0

Group: Development/Databases

Url: https://www.mongodb.org
Source: %name-%version.tar
Packager: Vladimir Didenko <cow@altlinux.org>

# From https://docs.mongodb.com/manual/installation
# Changed in version 3.4: MongoDB no longer supports 32-bit x86 platforms.
ExclusiveArch: x86_64 aarch64 ppc64le %e2k

BuildRequires(pre): rpm-macros-valgrind

BuildRequires: /proc gcc-c++ python3-module-pymongo python3-module-pkg_resources scons
BuildRequires: boost-devel boost-filesystem-devel boost-program_options-devel
BuildRequires: libssl-devel libpcre-devel libpcrecpp-devel libreadline-devel
BuildRequires: libpcap-devel libsnappy-devel
BuildRequires: systemd-devel libgperftools-devel libsasl2-devel libstemmer-devel
BuildRequires: libyaml-cpp-devel zlib-devel python-modules-json
BuildRequires: python3-module-Cheetah python3-module-yaml python3-module-psutil
BuildRequires: libcurl-devel
BuildRequires: liblzma-devel

%if_enabled valgrind
BuildRequires: valgrind-devel
%endif

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

# CRLF -> LF
sed -i 's/\r//' README


%build
%ifarch aarch64
%define ccflags_arch_opts "-march=armv8-a+crc"
%endif

%ifarch %e2k
%define opt_wt --wiredtiger=off
%else
%define opt_wt --wiredtiger=on
%endif
%define build_opts \\\
       -j 4 \\\
       --use-system-tcmalloc \\\
       --use-system-pcre \\\
       --use-system-snappy \\\
       %{?_enable_valgrind:--use-system-valgrind} \\\
       --use-system-zlib \\\
       --use-system-stemmer \\\
       --use-system-yaml \\\
       --nostrip \\\
       --use-sasl-client \\\
       %opt_wt \\\
       --ssl=on \\\
       MONGO_VERSION="%{version}-%{release}" \\\
       --disable-warnings-as-errors \\\
       CCFLAGS="%{?optflags} %{?ccflags_arch_opts} `pkg-config --cflags libpcrecpp`"

scons %build_opts --install-mode=legacy core

%install

# cow@: It seems that mongo 4.2 + scons 3.1.1 doesn't provide a clean way to
# specify location to install binaries (at least I wasn't able to find it).
install -p -D -m 755 mongod %buildroot%_bindir/mongod
install -p -D -m 755 mongos %buildroot%_bindir/mongos
install -p -D -m 755 mongo %buildroot%_bindir/mongo

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

# cow@: Mongo fails to build on Alt Beekeeper machine because there are only 32GB
# of a disk space is available. Right now we reach this limit during the generation
# of debuginfo files. Let's try to hotfix this issue by removing files created during
# the build process.
rm -fr build

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
%doc README LICENSE-Community.txt
%_bindir/mongo
%_man1dir/*

%files server-mongod
%doc README LICENSE-Community.txt
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
%doc README LICENSE-Community.txt
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
* Wed Nov 02 2022 Alexei Takaseev <taf@altlinux.org> 4.4.17-alt2
- Fix typo ppc64le arch

* Fri Oct 28 2022 Alexei Takaseev <taf@altlinux.org> 4.4.17-alt1
- Fix compile with GCC 12
- 4.4.17

* Thu Dec 09 2021 Alexei Takaseev <taf@altlinux.org> 4.4.10-alt1
- 4.4.10

* Wed May 26 2021 Vladimir Didenko <cow@altlinux.org> 4.4.6-alt1
- 4.4.6

* Mon Apr 12 2021 Vladimir Didenko <cow@altlinux.org> 4.4.5-alt1
- 4.4.5

* Sat Feb 20 2021 Vladimir Didenko <cow@altlinux.org> 4.4.4-alt1
- 4.4.4

* Wed Dec 23 2020 Vladimir Didenko <cow@altlinux.org> 4.4.3-alt2
- use /run instead of /var/run and /lock instead of /var/lock

* Wed Dec 23 2020 Vladimir Didenko <cow@altlinux.org> 4.4.3-alt1
- 4.4.3

* Fri Nov 20 2020 Vladimir Didenko <cow@altlinux.org> 4.4.2-alt1
- 4.4.2

* Wed Sep 30 2020 Vladimir Didenko <cow@altlinux.org> 4.4.1-alt1.1
- use rm instead of scons clean

* Wed Sep 30 2020 Vladimir Didenko <cow@altlinux.org> 4.4.1-alt1
- 4.4.1
- try to hotfix build fail on beekeeper machine

* Wed Aug 5 2020 Vladimir Didenko <cow@altlinux.org> 4.4.0-alt1.1
- add missed build dependency
- reduce build jobs count to avoid OOM

* Wed Aug 5 2020 Vladimir Didenko <cow@altlinux.org> 4.4.0-alt1
- 4.4.0

* Mon Jun 29 2020 Vladimir Didenko <cow@altlinux.org> 4.2.8-alt1
- 4.2.8

* Mon Apr 27 2020 Vladimir Didenko <cow@altlinux.org> 4.2.6-alt1
- 4.2.6

* Tue Feb 4 2020 Vladimir Didenko <cow@altlinux.org> 4.2.3-alt1
- 4.2.3

* Fri Dec 20 2019 Vladimir Didenko <cow@altlinux.org> 4.2.2-alt1.1
- remove duplicated Url tag

* Tue Dec 17 2019 Vladimir Didenko <cow@altlinux.org> 4.2.2-alt1
- 4.2.2
- fix license name

* Wed Nov 06 2019 Michael Shigorin <mike@altlinux.org> 4.2.1-alt2
- added ppc64el, %%e2k to ExclusiveArch:
- conditional valgrind build dependency

* Tue Oct 22 2019 Vladimir Didenko <cow@altlinux.org> 4.2.1-alt1
- 4.2.1

* Wed Sep 11 2019 Vladimir Didenko <cow@altlinux.org> 4.2.0-alt1
- 4.2.0

* Thu Aug 1 2019 Vladimir Didenko <cow@altlinux.org> 4.0.11-alt1
- 4.0.11

* Mon Jun 10 2019 Vladimir Didenko <cow@altlinux.org> 4.0.10-alt1
- 4.0.10

* Tue Mar 26 2019 Vladimir Didenko <cow@altlinux.org> 4.0.7-alt1
- 4.0.7

* Fri Feb 15 2019 Vladimir Didenko <cow@altlinux.org> 4.0.6-alt1
- 4.0.6

* Wed Jan 16 2019 Vladimir Didenko <cow@altlinux.org> 4.0.5-alt1
- 4.0.5

* Thu Nov 22 2018 Vladimir Didenko <cow@altlinux.org> 4.0.4-alt1
- 4.0.4

* Thu Oct 11 2018 Vladimir Didenko <cow@altlinux.org> 4.0.3-alt1
- 4.0.3

* Tue Sep 11 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.2-alt2
- NMU: rebuilt with new yaml-cpp.

* Thu Aug 30 2018 Vladimir Didenko <cow@altlinux.org> 4.0.2-alt1
- 4.0.2

* Fri Jul 6 2018 Vladimir Didenko <cow@altlinux.org> 4.0.0-alt1.2
- Fix build on aarch64

* Thu Jul 5 2018 Vladimir Didenko <cow@altlinux.org> 4.0.0-alt1.1
- Remove libv8 from BuildRequires

* Wed Jul 4 2018 Vladimir Didenko <cow@altlinux.org> 4.0.0-alt1
- 4.0.0
- support build on aarch64

* Sat Jun 9 2018 Vladimir Didenko <cow@altlinux.org> 3.6.5-alt1
- 3.6.5

* Wed Apr 25 2018 Vladimir Didenko <cow@altlinux.org> 3.6.4-alt1
- 3.6.4

* Wed Mar 28 2018 Vladimir Didenko <cow@altlinux.org> 3.6.3-alt2
- fix build (use different python cheetah package)

* Tue Mar 13 2018 Vladimir Didenko <cow@altlinux.org> 3.6.3-alt1
- 3.6.3

* Wed Jan 31 2018 Vladimir Didenko <cow@altlinux.org> 3.6.2-alt1
- 3.6.2

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
