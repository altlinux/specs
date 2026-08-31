%define _unpackaged_files_terminate_build 1

%define zapret_datadir %_datadir/%name
%define zapret_confdir %_sysconfdir/%name
%define zapret_statedir %_localstatedir/%name

Name: zapret2
Version: 1.0.4
Release: alt1

Summary: DPI bypass tool (zapret v2)
License: MIT
Group: Networking/Other

Url: https://github.com/bol-van/zapret2
VCS: https://github.com/bol-van/zapret2.git
Source: %name-%version.tar
Conflicts: zapret
Requires(pre): systemd

BuildRequires(pre): rpm-macros-systemd
BuildRequires: gcc-c++ make
BuildRequires: zlib-devel
BuildRequires: libcap-devel
BuildRequires: libnetfilter_queue-devel
BuildRequires: libnfnetlink-devel
BuildRequires: libmnl-devel
BuildRequires: libluajit-devel
BuildRequires: libsystemd-devel

# shell scripts define internal functions (random, zzcat, etc.)
# that clash with system commands, skip false deps
%add_findreq_skiplist %zapret_datadir/common/*
%add_findreq_skiplist %zapret_datadir/ipset/*
%add_findreq_skiplist %zapret_datadir/blockcheck2.sh
%add_findreq_skiplist %zapret_datadir/blockcheck2.d/*

%description
Zapret2 is an autonomous DPI (Deep Packet Inspection) bypass tool, a rewrite
of zapret. It includes nfqws2 (NFQUEUE packet modifier) and helper utilities
(ip2net, mdig) for circumventing network-level blocking and throttling.

%prep
%setup
# ip2net/mdig hardcode -s in their link commands; remove to preserve debug info
sed -i 's/$(CC) -s /$(CC) /' ip2net/Makefile mdig/Makefile

# allow CUSTOM_DIR to be overridden from the config file (upstream sets it
# unconditionally from ZAPRET_RW); we keep custom scripts in /etc/zapret2
sed -i 's|^CUSTOM_DIR="$ZAPRET_RW/init.d/sysv"$|CUSTOM_DIR="${CUSTOM_DIR:-"$ZAPRET_RW/init.d/sysv"}"|' \
    init.d/sysv/functions
    
# fix paths in the systemd units (upstream assumes /opt/zapret2, we use the datadir)
sed -i 's|/opt/zapret2|%{zapret_datadir}|g' \
    init.d/systemd/zapret2.service \
    init.d/systemd/nfqws2@.service \
    init.d/systemd/zapret2-list-update.service
    
# per-instance service looks up nfqws2 in PATH; the binary is in /usr/sbin
sed -i 's|ExecSearchPath=.*|ExecSearchPath=%{_sbindir}|' init.d/systemd/nfqws2@.service

# drop upstream's read-only custom.d placeholder; real custom.d lives in /etc
rm -rf init.d/sysv/custom.d

# packaged defaults: daemon user and runtime state in /var
sed -i \
    -e 's|^#WS_USER=nobody|WS_USER=zapret|' \
    -e 's|^#TMPDIR=/opt/zapret2/tmp|#TMPDIR=%{zapret_statedir}/tmp|' \
    config.default
    
# runtime-modifiable data (ip/host lists, autohostlist state, custom.d)
cat >> config.default <<'EOF'

# runtime-modifiable data (ip/host lists, autohostlist state, custom.d)
ZAPRET_RW=%{zapret_statedir}
IPSET_RW_DIR=%{zapret_statedir}/ipset
HOSTLIST_BASE=%{zapret_statedir}/ipset
CUSTOM_DIR=%{zapret_confdir}
EOF

%build
export CFLAGS="%optflags"
%make_build systemd STRIPP=

%install
# binaries
install -Dpm 0755 binaries/my/nfqws2 	%{buildroot}%{_sbindir}/nfqws2
install -Dpm 0755 binaries/my/ip2net 	%{buildroot}%{_bindir}/ip2net
install -Dpm 0755 binaries/my/mdig 		%{buildroot}%{_bindir}/zapret2-mdig

# scripts
mkdir -p %{buildroot}%{zapret_datadir}
cp -a common 		%{buildroot}%{zapret_datadir}/
cp -a ipset 		%{buildroot}%{zapret_datadir}/
cp -a lua 			%{buildroot}%{zapret_datadir}/
cp -a blockcheck2.d %{buildroot}%{zapret_datadir}/
install -pm 0755 blockcheck2.sh %{buildroot}%{zapret_datadir}/

# init scripts: only sysv and systemd (skip openwrt, pfsense, runit, etc.)
mkdir -p %{buildroot}%{zapret_datadir}/init.d
cp -a init.d/sysv 						%{buildroot}%{zapret_datadir}/init.d/
cp -a init.d/systemd 					%{buildroot}%{zapret_datadir}/init.d/
cp -a init.d/custom.d.examples.linux 	%{buildroot}%{zapret_datadir}/init.d/

# fake packet data files
mkdir -p %{buildroot}%{zapret_datadir}/files
cp -a files/fake %{buildroot}%{zapret_datadir}/files/

# config
install -Dpm 0644 config.default %{buildroot}%{zapret_confdir}/config
ln -sr %{buildroot}%{zapret_confdir}/config %{buildroot}%{zapret_datadir}/config
install -pm 0644 config.default  %{buildroot}%{zapret_datadir}/config.default

# systemd units
install -Dpm 0644 init.d/systemd/zapret2.service 			%{buildroot}%{_unitdir}/zapret2.service
install -pm 0644 init.d/systemd/nfqws2@.service 			%{buildroot}%{_unitdir}/nfqws2@.service
install -pm 0644 init.d/systemd/zapret2-list-update.service %{buildroot}%{_unitdir}/zapret2-list-update.service
install -pm 0644 init.d/systemd/zapret2-list-update.timer 	%{buildroot}%{_unitdir}/zapret2-list-update.timer

# symlinks so init scripts find binaries at expected paths
mkdir -p %{buildroot}%{zapret_datadir}/nfq2
mkdir -p %{buildroot}%{zapret_datadir}/ip2net
mkdir -p %{buildroot}%{zapret_datadir}/mdig
ln -sr %{buildroot}%{_sbindir}/nfqws2 		%{buildroot}%{zapret_datadir}/nfq2/nfqws2
ln -sr %{buildroot}%{_bindir}/ip2net 		%{buildroot}%{zapret_datadir}/ip2net/ip2net
ln -sr %{buildroot}%{_bindir}/zapret2-mdig 	%{buildroot}%{zapret_datadir}/mdig/mdig

# custom scripts dir lives in the config dir (/etc), not in runtime state
install -d %{buildroot}%{zapret_confdir}/custom.d

# daemon user and state directory ownership
install -Dpm 0644 zapret2.sysusers %{buildroot}%{_sysusersdir}/zapret2.conf
install -Dpm 0644 zapret2.tmpfiles %{buildroot}%{_tmpfilesdir}/zapret2.conf

%pre
%sysusers_create_package %name zapret2.sysusers
%tmpfiles_create_package %name zapret2.tmpfiles

%post
%post_systemd zapret2.service zapret2-list-update.timer

%preun
%preun_systemd zapret2.service zapret2-list-update.timer

%files
%_sbindir/nfqws2
%_bindir/ip2net
%_bindir/zapret2-mdig
%dir %zapret_confdir
%config(noreplace) %zapret_confdir/config
%doc docs/changes.txt docs/changes_compat.txt docs/manual.md docs/manual.en.md docs/readme.md
%zapret_datadir/
%_unitdir/zapret2.service
%_unitdir/nfqws2@.service
%_unitdir/zapret2-list-update.service
%_unitdir/zapret2-list-update.timer
%_sysusersdir/zapret2.conf
%_tmpfilesdir/zapret2.conf
%dir %zapret_confdir/custom.d

%changelog
* Fri Aug 28 2026 Andrey Alekseev <parovoz@altlinux.org> 1.0.4-alt1
- initial build for ALT Sisyphus
