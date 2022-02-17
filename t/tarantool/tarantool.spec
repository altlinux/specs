# Variable _tnt_version is `git describe --long` from original Tarantool repo for this version
%define _tnt_version %version-20-geed93fbbc   

%def_disable static
%def_enable check

ExclusiveArch: x86_64

Name: tarantool
Version: 2.8.3
Release: alt1

Summary: In-memory database and Lua application server
License: BSD
Group: Databases

Url: http://tarantool.org
VCS: https://github.com/tarantool/tarantool.git

Source: %name-%version.tar
Source1: %name-%version-src-lib-msgpuck.tar
Source2: %name-%version-src-lib-small.tar
Source3: %name-%version-test-run.tar
Source4: %name-%version-third_party-decNumber.tar
Source5: %name-%version-third_party-libyaml.tar
Source6: %name-%version-third_party-luafun.tar
Source7: %name-%version-third_party-luajit.tar
Source8: %name-%version-third_party-luarocks.tar
Source9: %name-%version-test-run-lib-checks.tar
Source10: %name-%version-test-run-lib-luatest.tar
Source11: %name-%version-test-run-lib-msgpack-python.tar
Source12: %name-%version-test-run-lib-tarantool-python.tar

BuildRequires: git
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: coreutils
BuildRequires: readline-devel
BuildRequires: openssl-devel
BuildRequires: libicu-devel
BuildRequires: libtool
BuildRequires: zlib-devel
BuildRequires: perl-podlators

BuildRequires: libcurl-devel
BuildRequires: libcares-devel
BuildRequires: libzstd-devel

%ifnarch aarch64
BuildRequires: libunwind-devel
%endif

# Set dependences for tests.
%if_enabled check
BuildRequires: python3
BuildRequires: python3-module-gevent
BuildRequires: python3-module-six
BuildRequires: python3-module-yaml
BuildRequires: /proc
%endif

%if_enabled static
BuildRequires: perl-CPAN
BuildRequires: libstdc++-devel-static
BuildRequires: ctest
%endif

%description
Tarantool is a high performance in-memory NoSQL database and Lua
application server. Tarantool supports replication, online backup and
stored procedures in Lua.

This package provides the server daemon and admin tools.

%package devel
Summary: Server development files for %name
Group: Databases
Requires: %name = %EVR

%description devel
Tarantool is a high performance in-memory NoSQL database and Lua
application server. Tarantool supports replication, online backup and
stored procedures in Lua.

This package provides server development files needed to create
C and Lua/C modules.

%prep
%setup -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12

%build

echo %_tnt_version > VERSION

%if_enabled static
    pushd static-build/
    [ -f Makefile ] && make clean
    [ -f CMakeCache.txt ] && rm CMakeCache.txt
    export PATH="/usr/src/perl5/bin${PATH:+:${PATH}}"
    export PERL5LIB="/usr/src/perl5/lib/perl5${PERL5LIB:+:${PERL5LIB}}"
    export PERL_LOCAL_LIB_ROOT="/usr/src/perl5${PERL_LOCAL_LIB_ROOT:+:${PERL_LOCAL_LIB_ROOT}}"
    export PERL_MB_OPT="--install_base \"/usr/src/perl5\""
    export PERL_MM_OPT="INSTALL_BASE=/usr/src/perl5"
    cpan -IT File::Spec::Win32

    cmake . -DCMAKE_TARANTOOL_ARGS="-DENABLE_WERROR:BOOL=ON"
    %make_build
    popd
%endif

[ -f Makefile ] && make clean
[ -f CMakeCache.txt ] && rm CMakeCache.txt
cmake . \
    -DCMAKE_INSTALL_LOCALSTATEDIR:PATH=%_var \
    -DCMAKE_INSTALL_SYSCONFDIR:PATH=%_sysconfdir \
%ifnarch aarch64
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DENABLE_BACKTRACE:BOOL=ON \
%else
    -DCMAKE_BUILD_TYPE=Release \
    -DENABLE_BACKTRACE:BOOL=OFF \
%endif
    -DWITH_SYSTEMD:BOOL=ON \
    -DSYSTEMD_UNIT_DIR:PATH=%_unitdir \
    -DSYSTEMD_TMPFILES_DIR:PATH=%_tmpfilesdir \
    -DENABLE_DIST:BOOL=ON \
    -DCMAKE_INSTALL_PREFIX=%prefix \
    -DCMAKE_INSTALL_FULL_BINDIR:PATH=%_bindir \
    -DENABLE_BUNDLED_LIBCURL:BOOL=OFF \
    -DENABLE_BUNDLED_ZSTD:BOOL=OFF

%make_build

%install
%makeinstall_std

%if_enabled static
    cp static-build/tarantool-prefix/bin/tarantool %buildroot/%_bindir
%endif

%check
ulimit -n $(ulimit -Hn)

%if_enabled static
    pushd static-build/
    ctest -V
    popd
%endif

make test-force

%pre
/usr/sbin/groupadd -r tarantool > /dev/null 2>&1 || :
/usr/sbin/useradd -M -g tarantool -r -d /var/lib/tarantool -s /sbin/nologin\
    -c "Tarantool Server" tarantool > /dev/null 2>&1 || :

%files
%_bindir/tarantool
%_man1dir/tarantool.1*
%doc README.md
%doc LICENSE AUTHORS

%_bindir/tarantoolctl
%_man1dir/tarantoolctl.1*
%config(noreplace) %_sysconfdir/sysconfig/tarantool
%dir %_sysconfdir/tarantool
%dir %_sysconfdir/tarantool/instances.available
%config(noreplace) %_sysconfdir/tarantool/instances.available/example.lua
# Use 0750 for database files
%attr(0750,tarantool,tarantool) %dir %_var/lib/tarantool/
%attr(0750,tarantool,tarantool) %dir %_var/log/tarantool/
%config(noreplace) %_sysconfdir/logrotate.d/tarantool
# tarantool package should own module directories
%dir %_libdir/tarantool
%dir %_datadir/tarantool
%_datadir/tarantool/luarocks

%_unitdir/tarantool@.service
%_tmpfilesdir/tarantool.conf

%changelog
* Tue Nov 02 2021 Dmitry Kibirev <kdy@altlinux.org> 2.8.3-alt1
- Initial build for Alt

