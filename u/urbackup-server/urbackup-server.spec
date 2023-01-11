%define _unpackaged_files_terminate_build 1
%def_enable embedded_cryptopp

Name: urbackup-server
Version: 2.5.27
Release: alt1

Summary: Efficient Client-Server backup system for Linux and Windows
License: AGPL-3.0+
Group: Archiving/Backup

Url: http://www.urbackup.org/
Source: %name-%version.tar.gz
Patch1: urbackup-server-fix-link-sqlite3.patch
Patch4: urbackup-server-2.5.27-no-update.patch

%ifnarch %e2k
Requires: guestfs-tools
%endif

BuildRequires: gcc-c++
BuildRequires: libcurl-devel
BuildRequires: libfuse-devel
BuildRequires: zlib-devel
BuildRequires: libzstd-devel
%{?_disable_embedded_cryptopp:BuildRequires: libcryptopp-devel}
BuildRequires: liblmdb-devel
BuildRequires: libsqlite3-devel
BuildRequires: liblua-devel
Requires: urbackup-common = %version-%release

%description
Efficient Client-Server Backup system for Linux and Windows
with GPT and UEFI partition. A client for Windows lets you
backup open files and complete partition images. Backups
are stored to disks in a efficient way (deduplication)
on either Windows or Linux servers.

%package -n urbackup-common
Summary: Common directories and user for urbackup server and client
Group: Archiving/Backup

%description -n urbackup-common
Common directories and user for urbackup server and client

%prep
%setup -n %name-%version
%patch1 -p1
%patch4 -p1

sed -i "s@/var/urbackup@%_localstatedir/urbackup@g" docs/urbackupsrv.1
sed -i "s@/etc/default/urbackupsrv@%_sysconfdir/sysconfig/%name@g" %name.service
sed -i 's,armhf,armhf|armh|armv7l,' cryptoplugin/src/configure.ac
sed -i 's,gnueabihf,gnueabi,' cryptoplugin/src/configure.ac

%ifnarch x86_64
# Does not build with PIC by default on x86, see
# http://groups.google.com/group/cryptopp-users/browse_thread/thread/d639907b0b1816b9
%__subst '1 i #define CRYPTOPP_DISABLE_SSE2' cryptoplugin/src/config.h
%endif

%build
export SUID_CFLAGS=-fPIE
export SUID_LDFLAGS=-fpie
%ifarch %ix86
export CXXFLAGS="-msse2 -O2 -g"
%endif
%autoreconf
%configure \
    --enable-packaging \
    --with-mountvhd \
    %{?_enable_embedded_cryptopp:--enable-embedded-cryptopp} \
    --without-embedded-sqlite3 \
    --without-embedded-lua \
    --without-embedded-lmdb

%make_build

%install
%makeinstall_std
mkdir -p %buildroot{%_unitdir,%_man1dir,%_logrotatedir,%_logdir,%_localstatedir/urbackup}
mkdir -p %buildroot%_sysconfdir/sysconfig
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%prefix/lib/firewalld/services

install -m 644 defaults_server %buildroot%_sysconfdir/sysconfig/%name
install -m 640 urbackup-server-firewalld.xml %buildroot%prefix/lib/firewalld/services/%name.xml
install -m 644 urbackup-server.service %buildroot%_unitdir/%name.service
install -m 644 docs/urbackupsrv.1 %buildroot%_man1dir/%name.1
install -m 644 logrotate_urbackupsrv  %buildroot%_sysconfdir/logrotate.d/%name
touch %buildroot%_logdir/urbackup.log

%pre -n urbackup-common
groupadd -r -f urbackup >/dev/null 2>&1 ||:
useradd -g urbackup -c 'UrBackup pseudo user' \
    -d %_localstatedir/urbackup -s /dev/null -r -l -M urbackup >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc AUTHORS COPYING ChangeLog README
%attr(4710,root,urbackup) %_bindir/urbackup_snapshot_helper
%attr(4710,root,urbackup) %_bindir/urbackup_mount_helper
%attr(-,urbackup,urbackup) %_datadir/urbackup/*
%_bindir/urbackupsrv
%_man1dir/*
%config(noreplace) %_logrotatedir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%prefix/lib/firewalld/services/%name.xml
%ghost %_logdir/urbackup.log
%attr(-,urbackup,urbackup) %_localstatedir/urbackup/dataplan_db.txt
%attr(0644,root,root) %_unitdir/%name.service

%files -n urbackup-common
%dir %attr(0755,urbackup,urbackup) %_datadir/urbackup
%dir %attr(0755,urbackup,urbackup) %_localstatedir/urbackup

%changelog
* Tue Jan 10 2023 Alexey Shabalin <shaba@altlinux.org> 2.5.27-alt1
- 2.5.27

* Mon Jan 17 2022 Alexey Shabalin <shaba@altlinux.org> 2.4.14-alt1
- 2.4.14

* Fri Nov 12 2021 Alexey Shabalin <shaba@altlinux.org> 2.4.13-alt3
- build with embedded cryptopp

* Tue Jun 22 2021 Michael Shigorin <mike@altlinux.org> 2.4.13-alt2
- do not R: guestfs-tools on %%e2k (missing by now)

* Thu Mar 11 2021 Alexey Shabalin <shaba@altlinux.org> 2.4.13-alt1
- 2.4.13

* Mon May 25 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.4.11-alt2
- urbackup-common package introduced

* Thu Nov 07 2019 Alexey Shabalin <shaba@altlinux.org> 2.4.11-alt1
- 2.4.11

* Sun Aug 25 2019 Alexey Shabalin <shaba@altlinux.org> 2.4.7-alt1
- update default config(patch3)
- disable autoudate service(patch4)

* Sun Jul 14 2019 Alexey Shabalin <shaba@altlinux.org> 2.3.8-alt1
- Initial build
