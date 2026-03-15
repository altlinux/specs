%define zapret_datadir %_datadir/%name
%define zapret_confdir %_sysconfdir/%name

Name: zapret
Version: 72.12
Release: alt1

Summary: DPI bypass tool for Linux

License: MIT
Group: Security/Networking
Url: https://github.com/bol-van/zapret
VCS: https://github.com/bol-van/zapret

# Source-url: https://github.com/bol-van/zapret/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: zlib-devel libcap-devel libnetfilter_queue-devel libnfnetlink-devel libmnl-devel

# shell scripts define internal functions (random, zzcat, etc.)
# that clash with system commands, skip false deps
%add_findreq_skiplist %zapret_datadir/common/*
%add_findreq_skiplist %zapret_datadir/ipset/*
%add_findreq_skiplist %zapret_datadir/blockcheck.sh

%description
Zapret is an autonomous DPI (Deep Packet Inspection) bypass tool.
It includes nfqws (NFQUEUE packet modifier), tpws (transparent proxy),
and helper utilities for circumventing network-level blocking and throttling.

%prep
%setup

%build
export CFLAGS="%optflags"
# remove -s (strip) flag from link commands to preserve debug info
sed -i 's/$(CC) -s /$(CC) /' nfq/Makefile tpws/Makefile ip2net/Makefile mdig/Makefile
for dir in nfq tpws ip2net mdig ; do
    %make_build -C $dir
done

%install
# binaries
install -Dpm 0755 nfq/nfqws %buildroot%_sbindir/nfqws
install -Dpm 0755 tpws/tpws %buildroot%_sbindir/tpws
install -Dpm 0755 ip2net/ip2net %buildroot%_bindir/ip2net
install -Dpm 0755 mdig/mdig %buildroot%_bindir/zapret-mdig

# shell scripts infrastructure (Linux only)
mkdir -p %buildroot%zapret_datadir
cp -a common %buildroot%zapret_datadir/
cp -a ipset %buildroot%zapret_datadir/

# init scripts: only sysv and systemd (skip openwrt, macos, pfsense, runit, etc.)
mkdir -p %buildroot%zapret_datadir/init.d
cp -a init.d/sysv %buildroot%zapret_datadir/init.d/
cp -a init.d/systemd %buildroot%zapret_datadir/init.d/
cp -a init.d/custom.d.examples.linux %buildroot%zapret_datadir/init.d/

# fake packet data files
mkdir -p %buildroot%zapret_datadir/files
cp -a files/fake %buildroot%zapret_datadir/files/

install -pm 0755 blockcheck.sh %buildroot%zapret_datadir/

# tmp dir for runtime
mkdir -p %buildroot%zapret_datadir/tmp

# config
install -Dpm 0644 config.default %buildroot%zapret_confdir/config
ln -s %zapret_confdir/config %buildroot%zapret_datadir/config

# systemd service
install -Dpm 0644 init.d/systemd/zapret.service %buildroot%_unitdir/zapret.service
sed -i \
    -e 's|/opt/zapret/init.d/sysv/zapret|%zapret_datadir/init.d/sysv/zapret|g' \
    %buildroot%_unitdir/zapret.service
# install per-instance services
install -pm 0644 init.d/systemd/nfqws@.service %buildroot%_unitdir/nfqws@.service
install -pm 0644 init.d/systemd/tpws@.service %buildroot%_unitdir/tpws@.service
install -pm 0644 init.d/systemd/zapret-list-update.service %buildroot%_unitdir/zapret-list-update.service
install -pm 0644 init.d/systemd/zapret-list-update.timer %buildroot%_unitdir/zapret-list-update.timer
# fix paths in all unit files
sed -i 's|/opt/zapret|%zapret_datadir|g' \
    %buildroot%_unitdir/nfqws@.service \
    %buildroot%_unitdir/tpws@.service \
    %buildroot%_unitdir/zapret-list-update.service
# fix ExecSearchPath for per-instance services (binaries are in /usr/sbin)
sed -i 's|ExecSearchPath=.*/binaries/my|ExecSearchPath=%_sbindir|' \
    %buildroot%_unitdir/nfqws@.service \
    %buildroot%_unitdir/tpws@.service

# symlinks so sysv scripts find binaries at expected paths
mkdir -p %buildroot%zapret_datadir/nfq
ln -s %_sbindir/nfqws %buildroot%zapret_datadir/nfq/nfqws
mkdir -p %buildroot%zapret_datadir/tpws
ln -s %_sbindir/tpws %buildroot%zapret_datadir/tpws/tpws
mkdir -p %buildroot%zapret_datadir/ip2net
ln -s %_bindir/ip2net %buildroot%zapret_datadir/ip2net/ip2net
mkdir -p %buildroot%zapret_datadir/mdig
ln -s %_bindir/zapret-mdig %buildroot%zapret_datadir/mdig/mdig

# documentation
mkdir -p %buildroot%zapret_datadir/docs
install -pm 0644 docs/*.md docs/LICENSE.txt %buildroot%zapret_datadir/docs/

%pre
getent group tpws >/dev/null || groupadd -r tpws
getent passwd tpws >/dev/null || useradd -r -d /dev/null -s /sbin/nologin -g tpws -c "tpws daemon user" tpws ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%_sbindir/nfqws
%_sbindir/tpws
%_bindir/ip2net
%_bindir/zapret-mdig
%dir %zapret_confdir
%config(noreplace) %zapret_confdir/config
%zapret_datadir/
%_unitdir/zapret.service
%_unitdir/nfqws@.service
%_unitdir/tpws@.service
%_unitdir/zapret-list-update.service
%_unitdir/zapret-list-update.timer

%changelog
* Mon Mar 16 2026 Vitaly Lipatov <lav@altlinux.ru> 72.12-alt1
- new version 72.12 (ALT bug 58082)

* Wed Mar 04 2026 Vitaly Lipatov <lav@altlinux.ru> 72.10-alt1
- new version 72.10 (with rpmrb script)
- rename mdig to zapret-mdig to avoid conflict
- remove unnecessary sed patch for ZAPRET_BASE in functions

* Fri Feb 13 2026 Vitaly Lipatov <lav@altlinux.ru> 72.9-alt1
- initial build for ALT Sisyphus
