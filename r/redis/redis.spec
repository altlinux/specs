%global _unpackaged_files_terminate_build 1
%define redis_user      _redis
%define redis_group     _redis

%ifarch %arm %mips32
%def_disable check
%else
%def_enable check
%endif

Name: redis
Version: 7.2.0
Release: alt2

Summary: Redis is an advanced key-value store

Group: Databases
# redis, hiredis: BSD-3-Clause
# hdrhistogram, jemalloc, lzf, linenoise: BSD-2-Clause
# lua: MIT
# fpconv: BSL-1.0
License: BSD-3-Clause AND BSD-2-Clause AND MIT AND BSL-1.0
URL: http://redis.io/
#URL: https://github.com/antirez/redis

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Source2: redis-benchmark.1
Source3: redis-cli.1
Source4: redis-server.1
Source5: redis-cli.bash_completion
Source6: redis-server.logrotate
Source7: redis.init
Source8: redis.sysconfig
Source9: redis.service
Source10: redis-sentinel.service

BuildRequires: gcc-c++ libssl-devel libsystemd-devel

# for check section
BuildRequires: tcl >= 8.5  tcl-tls openssl
BuildRequires: /proc

Provides: %name-server = %EVR
Provides: %name-sentinel = %EVR
Requires: %name-cli = %EVR

%description
Redis is an advanced key-value store. It is similar to memcached but
the dataset is not volatile, and values can be strings, exactly like in
memcached, but also lists, sets, and ordered sets. All this data types can
be manipulated with atomic operations to push/pop elements, add/remove
elements, perform server side union, intersection, difference between
sets, and so forth. Redis supports different kind of sorting abilities.

In order to be very fast but at the same time persistent the whole dataset
is taken in memory, and from time to time saved on disc asynchronously
(semi persistent mode) or alternatively every change is written into an
append only file (fully persistent mode). Redis is able to rebuild the
append only file in background when it gets too big.

Redis supports trivial to setup master-slave replication, with very
fast non-blocking first synchronization, auto reconnection on net split,
and so forth.

Redis is written in ANSI C and works in most POSIX systems like Linux,
*BSD, Mac OS X, Solaris, and so on. Redis is free software released under
the very liberal BSD license. Redis is reported to compile and work
under WIN32 if compiled with Cygwin, but there is no official support
for Windows currently.

%package cli
Summary: Development header for Redis module development
Group: Networking/Other
Provides: %name-tools = %EVR

%description cli
Header file required for building loadable Redis modules.

%package devel
Summary: Development header for Redis module development
Group: Development/C

%description       devel
Header file required for building loadable Redis modules.

%prep
%setup
%patch0 -p1
#%%patch1

%build

# For e2k - force use libc malloc instead jemalloc (see #35473)
USE_MALLOC=
%ifarch %e2k
USE_MALLOC="USE_JEMALLOC=no MALLOC=libc"
%else
USE_MALLOC="USE_JEMALLOC=yes"
%endif

%global make_flags CXXFLAGS="%optflags" CFLAGS="%optflags" OPTIMIZATION="" DEBUG_FLAGS="" DEBUG="" V="echo" PREFIX=%buildroot%_prefix $USE_MALLOC BUILD_TLS=yes USE_SYSTEMD=yes

%make_build %make_flags all

%check
./utils/gen-test-certs.sh
./runtest --clients 1 --verbose --tags -largemem:skip --skipunit unit/oom-score-adj --skipunit unit/memefficiency  --skiptest "CONFIG SET rollback on apply error" --tls
./runtest-moduleapi
timeout 30m ./runtest-cluster --tls
./runtest-sentinel

%install
%make_install %make_flags install
mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%_sysconfdir/%name
mv %buildroot%_bindir/redis-server %buildroot%_sbindir/
mv %buildroot%_bindir/redis-sentinel %buildroot%_sbindir/
ln -nsf ../sbin/redis-server %buildroot%_bindir/redis-check-aof
ln -nsf ../sbin/redis-server %buildroot%_bindir/redis-check-rdb

mkdir -p %buildroot%_sharedstatedir/%name
mkdir -p %buildroot%_logdir/%name

mkdir -p %buildroot%_man1dir
install -m 644 %SOURCE2 %buildroot%_man1dir/
install -m 644 %SOURCE3 %buildroot%_man1dir/
install -m 644 %SOURCE4 %buildroot%_man1dir/

# Tune default configuration
sed -e '/^timeout[[:blank:]]/ s/0/300/' \
    -e '/^daemonize[[:blank:]]/ s/no/yes/' \
    -e '/^pidfile[[:blank:]]/ s^/var/run/redis_6379.pid^/run/redis/redis-server.pid^' \
    -e '/^logfile[[:blank:]]/ s^""^"/var/log/redis/redis-server.log"^' \
    -e '/^dir[[:blank:]]/ s^\./^/var/lib/redis^' \
    -i %name.conf

sed -e '/^daemonize[[:blank:]]/ s/no/yes/' \
    -e '/^pidfile[[:blank:]]/ s^/var/run/redis-sentinel.pid^/run/redis/redis-sentinel.pid^' \
    -e '/^logfile[[:blank:]]/ s^""^"/var/log/redis/redis-sentinel.log"^' \
    -e '/^dir[[:blank:]]/ s^/tmp^/var/lib/redis^' \
    -i sentinel.conf

install -m644 %name.conf %buildroot%_sysconfdir/%name/
install -m644 sentinel.conf %buildroot%_sysconfdir/%name/

mkdir -p %buildroot%_datadir/bash-completion/completions
install -m 644 %SOURCE5 %buildroot%_datadir/bash-completion/completions/redis-cli

mkdir -p %buildroot%_logrotatedir
install -m 640 %SOURCE6 %buildroot%_logrotatedir/redis-server

mkdir -p  %buildroot%_initdir
install -m 0755 %SOURCE7 %buildroot%_initdir/%name

mkdir -p %buildroot%_sysconfdir/sysconfig
install -m 0640 %SOURCE8 %buildroot%_sysconfdir/sysconfig/%name

mkdir -p  %buildroot%_unitdir
install -m 0644 %SOURCE9  %buildroot%_unitdir/%name.service
install -m 0644 %SOURCE10 %buildroot%_unitdir/%name-sentinel.service

mkdir -p  %buildroot%_tmpfilesdir
echo 'd /run/%name 0755 %redis_user %redis_group' >> %buildroot%_tmpfilesdir/%name.conf

# Install redis module header
install -pDm644 src/%{name}module.h %buildroot%_includedir/%{name}module.h

%pre
# Add the "_redis" user
groupadd -r -f %redis_group 2>/dev/null ||:
useradd  -r -g %redis_group -c 'Redis daemon' \
        -s /dev/null -M -d %_sharedstatedir/%name %redis_user 2>/dev/null ||:

%post
%post_service %name
%post_service %name-sentinel

%preun
%preun_service %name
%preun_service %name-sentinel

%files
%doc COPYING 00-RELEASENOTES README.md BUGS MANIFESTO
%attr(0750,root,%redis_group) %dir %_sysconfdir/%name
%config(noreplace) %attr(0640, %redis_user, %redis_group) %_sysconfdir/%name/redis.conf
%config(noreplace) %attr(0640, %redis_user, %redis_group) %_sysconfdir/%name/sentinel.conf
%config(noreplace) %_logrotatedir/redis-server
%attr(0640,root,%redis_group) %config(noreplace) %_sysconfdir/sysconfig/%name
%config %_initdir/%name
%_unitdir/*.service
%_tmpfilesdir/%name.conf
%_bindir/%name-check-aof
%_bindir/%name-check-rdb
%_sbindir/%name-server
%_sbindir/%name-sentinel
%_man1dir/%name-server.*
%dir %attr(0750,%redis_user,%redis_group) %_logdir/%name
%dir %attr(0750,%redis_user,%redis_group) %_sharedstatedir/%name

%files cli
%_bindir/%name-cli
%_bindir/%name-benchmark
%_datadir/bash-completion/completions/%name-cli
%_man1dir/%name-benchmark.*
%_man1dir/%name-cli.*

%files devel
%_includedir/%{name}module.h

%changelog
* Fri Sep 01 2023 Alexey Shabalin <shaba@altlinux.org> 7.2.0-alt2
- Fixed start redis-sentinel.service (ALT#47436)

* Mon Aug 28 2023 Alexey Shabalin <shaba@altlinux.org> 7.2.0-alt1
- Release Redis 7.2.0 GA

* Tue Aug 15 2023 Alexey Shabalin <shaba@altlinux.org> 7.0.12-alt1
- 7.0.12
- Fixed License
- Split cli tools to cli subpackage
- Update systemd units
- Update default sentinel config
- Build with systemd support sd_notify
- /var/run -> /run
- Fixed logrotate config
- Fixed permissions for configs
- Move make test to check section
- Enable tests
- Security fixes:
  + CVE-2022-24834 Integer Overflow to Buffer Overflow, Heap-based Buffer Overflow
  + CVE-2022-31144 Out-of-bounds Write, Heap-based Buffer Overflow
  + CVE-2022-33105 Missing Release of Memory after Effective Lifetime
  + CVE-2022-35951 Integer Overflow or Wraparound
  + CVE-2022-35977 Integer Overflow or Wraparound
  + CVE-2022-36021 Inefficient Algorithmic Complexity
  + CVE-2023-22458 Integer Overflow or Wraparound
  + CVE-2023-25155 Integer Overflow or Wraparound
  + CVE-2023-28425 Improper Neutralization of Special Elements used in a Command (Command Injection)
  + CVE-2023-28856 Reachable Assertion
  + CVE-2023-31655 Insufficient Information
  + CVE-2023-36824 Heap overflow in COMMAND GETKEYS and ACL evaluation

* Thu Aug 03 2023 Andrey Cherepanov <cas@altlinux.org> 6.2.8-alt2
- Added SSL/TLS support

* Sat Jan 14 2023 Nikolay A. Fetisov <naf@altlinux.org> 6.2.8-alt1
- New version
- Security fixes:
  + CVE-2022-24736: server crash by a specially crafted Lua script
  + CVE-2022-24735: overcome ACL rules via Lua scripts manipulation

* Sat Nov 20 2021 Nikolay A. Fetisov <naf@altlinux.org> 6.2.6-alt1
- New version
- Security fixes:
  + CVE-2021-41099: buffer overflow with non-default configuration
  + CVE-2021-32762: buffer overflow issue in redis-cli and redis-sentinel
  + CVE-2021-32687: buffer overflow with non-default configuration
  + CVE-2021-32675: Denial Of Service when processing RESP request payloads
  + CVE-2021-32672: random heap reading issue with Lua Debugger
  + CVE-2021-32628: buffer overflow with non-default configuration
  + CVE-2021-32627: buffer overflow with non-default configuration
  + CVE-2021-32626: Lua scripts may result with Heap buffer overflow
  + CVE-2021-32761: integer overflow in BITFIELD on 32-bit versions

* Mon Jun 28 2021 Nikolay A. Fetisov <naf@altlinux.org> 6.2.4-alt1
- New major version (Closes: 40279)

* Sun May 16 2021 Nikolay A. Fetisov <naf@altlinux.org> 5.0.12-alt1
- New version
- Security fixes:
  + CVE-2021-21309: integer overflow on 32-bit systems
- Fix NMU: move local codebase changes to a patch

* Mon Mar 29 2021 Ivan A. Melnikov <iv@altlinux.org> 5.0.8-alt2
- Link with libatomic on %%mips32

* Tue Mar 31 2020 Nikolay A. Fetisov <naf@altlinux.org> 5.0.8-alt1
- New version

* Sun Aug 04 2019 Nikolay A. Fetisov <naf@altlinux.org> 5.0.5-alt1
- New version
  * Fix AOF bug (possible data loss when fsync police is set to 'everysec')
  * Fix memleak in bitfieldCommand
  * Fix memleak when rewriting config file
  * Fix non critical bugs in diskless replication

* Fri May 10 2019 Nikolay A. Fetisov <naf@altlinux.org> 5.0.4-alt1
- New version
- Use libc malloc for e2k arch (Closes: 35473)

* Sun Aug 05 2018 Nikolay A. Fetisov <naf@altlinux.org> 4.0.11-alt1
- New version

* Sat Jun 16 2018 Nikolay A. Fetisov <naf@altlinux.org> 4.0.10-alt1
- New version
  * Fix security issues related to the Lua scripting engine
  * Fix a bug with SCAN/SSCAN/HSCAN/ZSCAN, that may not return all the elements
  * Fix a PSYNC2 bug that can affect partial resynchronization

* Sat Apr 14 2018 Nikolay A. Fetisov <naf@altlinux.org> 4.0.9-alt1
- New version

* Fri Mar 02 2018 Nikolay A. Fetisov <naf@altlinux.org> 4.0.8-alt1
- New version

* Sat Jan 27 2018 Nikolay A. Fetisov <naf@altlinux.org> 4.0.7-alt1
- New version

* Wed Dec 27 2017 Nikolay A. Fetisov <naf@altlinux.org> 4.0.6-alt1
- New version

* Sun Jun 04 2017 Nikolay A. Fetisov <naf@altlinux.org> 3.2.9-alt1
- New version

* Tue Feb 14 2017 Nikolay A. Fetisov <naf@altlinux.org> 3.2.8-alt1
- New version

* Mon Jan 23 2017 Nikolay A. Fetisov <naf@altlinux.org> 3.2.6-alt1
- New version

* Sun Nov 06 2016 Nikolay A. Fetisov <naf@altlinux.ru> 3.2.5-alt1
- New version

* Sat Feb 06 2016 Nikolay A. Fetisov <naf@altlinux.ru> 3.0.7-alt1
- New version

* Sun Dec 20 2015 Nikolay A. Fetisov <naf@altlinux.ru> 3.0.6-alt1
- New version

* Sat Dec 19 2015 Terechkov Evgenii <evg@altlinux.org> 3.0.5-alt2.1
- Change mode of /var/log/redis to 1770 according to ALT Secure Packaging Policy

* Fri Nov 27 2015 Nikolay A. Fetisov <naf@altlinux.ru> 3.0.5-alt2
- Fix unit file access rights (Closes: #31545)

* Sun Oct 25 2015 Nikolay A. Fetisov <naf@altlinux.ru> 3.0.5-alt1
- New version (3.0.5)

* Wed Sep 23 2015 Nikolay A. Fetisov <naf@altlinux.ru> 3.0.4-alt1
- New version (3.0.4)

* Sun Aug 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 3.0.3-alt1
-  New version (3.0.3)

* Sat Jun 06 2015 Nikolay A. Fetisov <naf@altlinux.ru> 3.0.2-alt1
- New version (3.0.2): critical security issue fix

* Fri May 29 2015 Nikolay A. Fetisov <naf@altlinux.ru> 3.0.1-alt1
- New version (3.0.1)
- Fix pid file name (Closes: #30859)

* Wed Feb 27 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.6.10-alt1
- new version (2.6.10) (ALT #28374)
- create temporary dir

* Tue May 15 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.7-alt2
- add systemd unit file (ALT #27334)

* Mon Feb 13 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.4.7-alt1
- new version (2.4.7)

* Sun Jan 29 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.4.6-alt1
- new version (2.4.6) (Closes: #26869)

* Fri Jan 06 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.4.5-alt1
- new version (2.4.5) (Closes: #26782)

* Mon Oct 24 2011 Nikolay A. Fetisov <naf@altlinux.ru> 2.4.1-alt1
- new version (2.4.1) (Closes: #26496)
- adding init script
- adding logrotate script
- moving default config file to the /etc/redis/

* Fri Sep 02 2011 Vitaly Lipatov <lav@altlinux.ru> 2.2.12-alt1
- new version (2.2.12) with rpmbs script (ALT bug #26131)

* Wed Apr 13 2011 Mykola Grechukh <gns@altlinux.ru> 2.2.4-alt1
- new version 2.2.4

* Tue Nov 09 2010 Vitaly Lipatov <lav@altlinux.ru> 2.0.4-alt1
- new version 2.0.4 (with rpmrb script) (ALT bug #24507)

* Sat Oct 16 2010 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- new version 2.0.3 (with rpmrb script) (ALT bug #24322)

* Thu Oct 07 2010 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt1
- new version 2.0.2 (with rpmrb script) (ALT bug #24222)

* Mon Sep 13 2010 Nick S. Grechukh <gns@altlinux.ru> 2.0.1-alt1
- new stable version

* Sun Dec 13 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.91-alt1
- initial build for ALT Linux Sisyphus
