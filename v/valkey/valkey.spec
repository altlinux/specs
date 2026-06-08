%global _unpackaged_files_terminate_build 1
%define valkey_user      _valkey
%define valkey_group     _valkey
%def_disable check

# tls as no,module,yes
%define tls yes

Name: valkey
Version: 9.0.4
Release: alt1

Summary: A persistent key-value database
License: BSD-3-Clause AND BSD-2-Clause AND MIT AND BSL-1.0
Group: Databases

Url: https://valkey.io
Vcs: https://github.com/valkey-io/valkey
Source0: %name-%version.tar
Source2: valkey.service
Source3: valkey-sentinel.service
Source4: valkey.logrotate
Patch: %name-%version.patch
Patch100: valkey-loadmod.patch

BuildRequires: gcc-c++ libssl-devel libsystemd-devel
BuildRequires: rdma-core-devel
# for check section
%if_enabled check
BuildRequires: tcl >= 8.5 tcl-tls openssl procps
BuildRequires: /proc /dev/pts
%endif
Provides: %name-server = %EVR
Provides: %name-sentinel = %EVR
Provides: %name-cli = %EVR
%if "%tls" == "yes"
Provides: %name-tls = %EVR
Obsoletes: %name-tls < %EVR
%endif

%global valkey_modules_dir %_libdir/%name/modules
%global valkey_modules_cfg %_sysconfdir/%name/modules

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

%package rdma
Summary: RDMA module for %name
Group: Databases
Requires: %name = %EVR

%description rdma
%summary.
See https://valkey.io/topics/RDMA/

%package tls
Summary: TLS module for %name
Group: Databases
Requires: %name = %EVR

%description tls
%summary.
See https://valkey.io/topics/encryption/

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
%autopatch -p1

# See https://bugzilla.redhat.com/2240293
# See https://src.fedoraproject.org/rpms/jemalloc/blob/rawhide/f/jemalloc.spec#_34
%ifarch %ix86 %arm x86_64 s390x
sed -e 's/--with-lg-quantum/--with-lg-page=12 --with-lg-quantum/' -i deps/Makefile
%endif
%ifarch ppc64 ppc64le aarch64
sed -e 's/--with-lg-quantum/--with-lg-page=16 --with-lg-quantum/' -i deps/Makefile
%endif

%build
# For e2k - force use libc malloc instead jemalloc (see #35473)
USE_MALLOC=
%ifarch %e2k
USE_MALLOC="USE_JEMALLOC=no MALLOC=libc"
USE_WERROR="USE_WERROR=0"
%else
USE_MALLOC="USE_JEMALLOC=yes"
USE_WERROR="USE_WERROR=1"
%endif
%if "%tls" == "yes"
BUILD_TLS="BUILD_TLS=yes"
%elif "%tls" == "module"
BUILD_TLS="BUILD_TLS=module"
%else
BUILD_TLS=""
%endif

%global make_flags CXXFLAGS="%optflags" CFLAGS="%optflags" OPTIMIZATION="" DEBUG_FLAGS="" DEBUG="" V="echo" PREFIX=%buildroot%_prefix $USE_MALLOC $USE_WERROR $BUILD_TLS USE_SYSTEMD=yes BUILD_RDMA=module

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
mkdir -p %buildroot%valkey_modules_dir
mkdir -p %buildroot%valkey_modules_cfg

mkdir -p %buildroot%_sysconfdir/%name
install -m640 %name.conf %buildroot%_sysconfdir/%name/
install -m640 sentinel.conf %buildroot%_sysconfdir/%name/
install -dm750  %buildroot%valkey_modules_cfg

install -pDm644 src/%{name}module.h %buildroot%_includedir/%{name}module.h

install -pDm644 src/redismodule.h %buildroot%_includedir/redismodule.h

# RDMA configuration file
cat <<__EOF__ >%buildroot%valkey_modules_cfg/rdma.conf
# RDMA module
loadmodule %valkey_modules_dir/rdma.so
__EOF__

install -pm755 src/valkey-rdma.so %buildroot%valkey_modules_dir/rdma.so

%if "%tls" == "module"
# TLS configuration file
cat <<__EOF__ >%buildroot%valkey_modules_cfg/tls.conf
# TLS module
loadmodule %valkey_modules_dir/tls.so
__EOF__

install -pm755 src/valkey-tls.so %buildroot%valkey_modules_dir/tls.so
%endif

# compat systemd symlinks
ln -sr %buildroot%_unitdir/%name.service %buildroot%_unitdir/redis.service
ln -sr %buildroot%_unitdir/%name-sentinel.service %buildroot%_unitdir/redis-sentinel.service

%check
./utils/gen-test-certs.sh
./runtest --verbose --dump-logs --skipunit unit/oom-score-adj --skipunit unit/memefficiency --skiptest "CONFIG SET rollback on apply error" \
%if "%tls" == "yes"
--tls \
%elif "%tls" == "module"
--tls --tls-module \
%endif
%nil

%ifnarch ppc64 ppc64le
./runtest-moduleapi
%endif
timeout 120m ./runtest-cluster \
%if "%tls" == "yes"
--tls \
%endif
%nil

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
%attr(0750, %valkey_user, %valkey_group) %dir %valkey_modules_cfg
%config(noreplace) %_logrotatedir/valkey-server

%dir %attr(0750,%valkey_user,%valkey_group) %_logdir/%name
%dir %attr(0750,%valkey_user,%valkey_group) %_sharedstatedir/%name
%dir %_libdir/%name

%files rdma
%config(noreplace) %attr(0640, %valkey_user, %valkey_group) %valkey_modules_cfg/rdma.conf
%valkey_modules_dir/rdma.so

%if "%tls" == "module"
%files tls
%config(noreplace) %attr(0640, %valkey_user, %valkey_group) %valkey_modules_cfg/tls.conf
%valkey_modules_dir/tls.so
%endif

%files compat-redis
%_bindir/redis-*
%_unitdir/redis.service
%_unitdir/redis-sentinel.service

%files devel
%_includedir/%{name}module.h

%files compat-redis-devel
%_includedir/redismodule.h

%changelog
* Mon Jun 08 2026 Evgeny Sinelnikov <sin@altlinux.org> 9.0.4-alt1
- Update to latest stable release of Valkey 9.0
- Security fixes (Fixes: CVE-2026-23479, CVE-2026-25243, CVE-2026-23631).

* Tue Mar 03 2026 Alexey Shabalin <shaba@altlinux.org> 9.0.3-alt1
- updated from 9.0.2 to 9.0.3 (Fixes: CVE-2025-67733, CVE-2026-21863, CVE-2026-27623)

* Thu Feb 12 2026 Alexey Shabalin <shaba@altlinux.org> 9.0.2-alt1
- New version 9.0.2

* Wed Nov 26 2025 Alexey Shabalin <shaba@altlinux.org> 8.1.4-alt2
- Fixed load modules without execute permissions (ALT#57024).
- Drop sub-package for TLS module: TLS as module not supported by sentinel.

* Thu Oct 16 2025 Alexey Shabalin <shaba@altlinux.org> 8.1.4-alt1
- New version 8.1.4 (Fixes: CVE-2025-49844, CVE-2025-46817, CVE-2025-46818, CVE-2025-46819).
- Add /etc/valkey/modules drop-in directory for module configuration files.
- Add sub-packages for TLS and RDMA modules

* Mon Jul 14 2025 Alexey Shabalin <shaba@altlinux.org> 8.1.3-alt1
- New version 8.1.3 (Fixes: CVE-2025-32023, CVE-2025-48367).

* Tue Jun 17 2025 Alexey Shabalin <shaba@altlinux.org> 8.1.2-alt1
- New version 8.1.2 (Fixes: CVE-2025-27151).
- Enable %%check for x86_64 only.

* Fri May 09 2025 Alexey Shabalin <shaba@altlinux.org> 8.1.1-alt1
- New version 8.1.1 (Fixes: CVE-2025-21605).

* Mon Apr 14 2025 Alexey Shabalin <shaba@altlinux.org> 8.1.0-alt1
- New version 8.1.0.

* Thu Jan 23 2025 Alexey Shabalin <shaba@altlinux.org> 8.0.2-alt1
- New version 8.0.2 (Fixes: CVE-2024-51741, CVE-2024-46981).

* Sun Dec 15 2024 Alexey Shabalin <shaba@altlinux.org> 8.0.1-alt2
- Update and fix systemd units.

* Fri Dec 13 2024 Alexey Shabalin <shaba@altlinux.org> 8.0.1-alt1
- Build to Sisyphus.

* Wed Dec 11 2024 Maxim Slipenko <maks1ms@altlinux.org> 8.0.1-alt0.1
- Initial build

