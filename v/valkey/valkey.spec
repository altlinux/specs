%global _unpackaged_files_terminate_build 1
%define valkey_user      _valkey
%define valkey_group     _valkey

Name: valkey
Version: 8.0.1
Release: alt2

Summary: A persistent key-value database
License: BSD-3-Clause AND BSD-2-Clause AND MIT AND BSL-1.0
Group: Databases

Url: https://valkey.io
Vcs: https://github.com/valkey-io/valkey
Source0: %name-%version.tar

Source2: valkey.service
Source3: valkey-sentinel.service
Source4: valkey.logrotate

BuildRequires: gcc-c++ libssl-devel libsystemd-devel
# for check section
BuildRequires: tcl >= 8.5 tcl-tls openssl
BuildRequires: /proc

Provides: %name-server = %EVR
Provides: %name-sentinel = %EVR
Provides: %name-cli = %EVR

%description
Valkey is an advanced key-value store. It is often referred to as a data
structure server since keys can contain strings, hashes, lists, sets and
sorted sets.

You can run atomic operations on these types, like appending to a string;
incrementing the value in a hash; pushing to a list; computing set
intersection, union and difference; or getting the member with highest
ranking in a sorted set.

In order to achieve its outstanding performance, Valkey works with an
in-memory dataset. Depending on your use case, you can persist it either
by dumping the dataset to disk every once in a while, or by appending
each command to a log.

Valkey also supports trivial-to-setup master-slave replication, with very
fast non-blocking first synchronization, auto-reconnection on net split
and so forth.

Other features include Transactions, Pub/Sub, Lua scripting, Keys with a
limited time-to-live, and configuration settings to make Valkey behave like
a cache.

You can use Valkey from most programming languages also.

%package devel
Summary: Development header for Valkey module development
Group: Development/C
BuildArch: noarch

%description devel
Header file required for building loadable Valkey modules.

%package compat-redis
Group: Databases
Summary: Conversion script and compatibility symlinks for Redis
Requires: valkey = %EVR
BuildArch: noarch
Conflicts: redis redis-cli

%description compat-redis
%summary

%package compat-redis-devel
Summary: Compatibility development header for Redis API Valkey modules
Group: Development/C
BuildArch: noarch
Conflicts: redis-devel

%description compat-redis-devel
Header file required for building loadable Valkey modules with the legacy
Redis API.

%prep
%setup
%ifarch %e2k
sed -i 's/-Werror/-Wno-error/g' deps/hiredis/Makefile
%endif

# See https://bugzilla.redhat.com/2240293
# See https://src.fedoraproject.org/rpms/jemalloc/blob/rawhide/f/jemalloc.spec#_34
%ifarch %ix86 %arm x86_64 s390x
sed -e 's/--with-lg-quantum/--with-lg-page=12 --with-lg-quantum/' -i deps/Makefile
%endif
%ifarch ppc64 ppc64le aarch64
sed -e 's/--with-lg-quantum/--with-lg-page=16 --with-lg-quantum/' -i deps/Makefile
%endif

sed -i -e 's|^logfile .*$|logfile /var/log/valkey/valkey.log|g' \
  -e 's|^# unixsocket .*$|unixsocket /run/valkey/valkey.sock|g' \
  -e 's|^pidfile .*$|pidfile /run/valkey/valkey.pid|g' \
  valkey.conf
 
sed -i -e 's|^logfile .*$|logfile /var/log/valkey/sentinel.log|g' \
  -e 's|^pidfile .*$|pidfile /run/valkey/sentinel.pid|g' \
  sentinel.conf

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

%install
%make_install %make_flags install

mkdir -p  %buildroot%_unitdir
install -m 0644 %SOURCE2 %buildroot%_unitdir/%name.service
install -m 0644 %SOURCE3 %buildroot%_unitdir/%name-sentinel.service

mkdir -p %buildroot%_logrotatedir
install -m 640 %SOURCE4 %buildroot%_logrotatedir/valkey-server

mkdir -p %buildroot%_sharedstatedir/%name
mkdir -p %buildroot%_logdir/%name

mkdir -p %buildroot%_sysconfdir/%name
install -m644 %name.conf %buildroot%_sysconfdir/%name/
install -m644 sentinel.conf %buildroot%_sysconfdir/%name/

install -pDm644 src/%{name}module.h %buildroot%_includedir/%{name}module.h

install -pDm644 src/redismodule.h %buildroot%_includedir/redismodule.h

# compat systemd symlinks
ln -sr %buildroot%_unitdir/%name.service %buildroot%_unitdir/redis.service
ln -sr %buildroot%_unitdir/%name-sentinel.service %buildroot%_unitdir/redis-sentinel.service

%check
./utils/gen-test-certs.sh
./runtest --clients 50 --verbose --tags -largemem:skip --skipunit unit/oom-score-adj --skipunit unit/memefficiency  --skiptest "CONFIG SET rollback on apply error" --tls
%ifnarch ppc64 ppc64le
./runtest-moduleapi
%endif
timeout 120m ./runtest-cluster --tls
./runtest-sentinel

%pre
groupadd -r -f %valkey_group 2>/dev/null ||:
useradd  -r -g %valkey_group -c 'Valkey Database Server' \
        -s /dev/null -M -d %_sharedstatedir/%name %valkey_user 2>/dev/null ||:

%post
%post_service %name
%post_service %name-sentinel

%preun
%preun_service %name
%preun_service %name-sentinel

%files
%doc COPYING 00-RELEASENOTES README.md
%attr(0770,root,%valkey_group) %dir %_sysconfdir/%name
%_unitdir/%name.service
%_unitdir/%name-sentinel.service
%_bindir/%name-*

%config(noreplace) %attr(0640, %valkey_user, %valkey_group) %_sysconfdir/%name/valkey.conf
%config(noreplace) %attr(0640, %valkey_user, %valkey_group) %_sysconfdir/%name/sentinel.conf
%config(noreplace) %_logrotatedir/valkey-server

%dir %attr(0750,%valkey_user,%valkey_group) %_logdir/%name
%dir %attr(0750,%valkey_user,%valkey_group) %_sharedstatedir/%name


%files compat-redis
%_bindir/redis-*
%_unitdir/redis.service
%_unitdir/redis-sentinel.service

%files devel
%_includedir/%{name}module.h

%files compat-redis-devel
%_includedir/redismodule.h

%changelog
* Sun Dec 15 2024 Alexey Shabalin <shaba@altlinux.org> 8.0.1-alt2
- Update and fix systemd units.

* Fri Dec 13 2024 Alexey Shabalin <shaba@altlinux.org> 8.0.1-alt1
- Build to Sisyphus.

* Wed Dec 11 2024 Maxim Slipenko <maks1ms@altlinux.org> 8.0.1-alt0.1
- Initial build

