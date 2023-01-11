%define _unpackaged_files_terminate_build 1
%def_enable embedded_cryptopp

Name: urbackup-client
Version: 2.5.22
Release: alt1
Summary: Efficient Client-Server backup system for Linux and Windows
Group: Archiving/Backup
License: AGPL-3.0+
Url: http://www.urbackup.org/
Source: %name-%version.tar.gz
Source2: %name-snapshot.cfg
Patch1: urbackup-client-fix-link-sqlite3.patch

BuildRequires: gcc-c++
BuildRequires: zlib-devel
BuildRequires: libzstd-devel
%{?_disable_embedded_cryptopp:BuildRequires: libcryptopp-devel}
BuildRequires: libsqlite3-devel
BuildRequires: libssl-devel
BuildRequires: libdevmapper-devel

Requires: urbackup-common

%description
Efficient Client-Server Backup system for Linux and Windows
with GPT and UEFI partition. A client for Windows lets you
backup open files and complete partition images. Backups
are stored to disks in a efficient way (deduplication)
on either Windows or Linux servers.

%prep
%setup -n %name-%version.0
%patch1 -p1

sed -i "s@/usr/local/sbin/urbackupclientbackend@%_sbindir/urbackupclientbackend@g" urbackupclientbackend-redhat.service
sed -i 's,armhf,armh,' cryptoplugin/src/configure.ac
sed -i 's,gnueabihf,gnueabi,' cryptoplugin/src/configure.ac

%build
export SUID_CFLAGS=-fPIE
export SUID_LDFLAGS=-fpie
%ifarch %ix86
%add_optflags -msse2
%endif
%ifarch %e2k
%add_optflags -mno-sse4.2 -mno-avx
%endif

%ifnarch x86_64
# Does not build with PIC by default on x86, see
# http://groups.google.com/group/cryptopp-users/browse_thread/thread/d639907b0b1816b9
%__subst '1 i #define CRYPTOPP_DISABLE_SSE2' cryptoplugin/src/config.h
%endif

%autoreconf
%configure \
    %{?_enable_embedded_cryptopp:--enable-embedded-cryptopp} \
    --without-embedded-sqlite3 \
    --enable-headless

%make_build

%install
%makeinstall_std
mkdir -p %buildroot{%_unitdir,%_man1dir,%_logdir,%_localstatedir/urbackup}
mkdir -p %buildroot%_sysconfdir/sysconfig
mkdir -p %buildroot%_initdir

install -m 644 defaults_client %buildroot%_sysconfdir/sysconfig/urbackupclient
install -m 644 urbackupclientbackend-redhat.service %buildroot%_unitdir/%name.service
install -m 644 docs/urbackupclientbackend.1 %buildroot%_man1dir/urbackupclientbackend.1

for f in linux_snapshot/*_snapshot; do
    [ -f "$f" ]
    install -m 755 "$f" "%buildroot%_datadir/urbackup/scripts/"
done

install -m 644 %SOURCE2 %buildroot%_sysconfdir/urbackup/snapshot.cfg
touch %buildroot%_logdir/urbackupclient.log

%post
%post_service %name

%preun
%preun_service %name

%files
%doc AUTHORS COPYING ChangeLog README
%config(noreplace) %_sysconfdir/sysconfig/urbackupclient
%dir %_sysconfdir/urbackup
%config(noreplace) %_sysconfdir/urbackup/*
%_bindir/urbackupclientctl
%_bindir/blockalign
%_sbindir/urbackupclientbackend
%_sbindir/urbackupclient_dmsnaptool
%_unitdir/%name.service
%_man1dir/*
%dir %attr(0755,urbackup,urbackup) %_datadir/urbackup
%attr(-,urbackup,urbackup) %_datadir/urbackup/*
%dir %attr(0755,urbackup,urbackup) %_localstatedir/urbackup
%attr(-,urbackup,urbackup) %_localstatedir/urbackup/*
%ghost %_logdir/urbackupclient.log

%changelog
* Tue Jan 10 2023 Alexey Shabalin <shaba@altlinux.org> 2.5.22-alt1
- 2.5.22

* Fri Nov 12 2021 Alexey Shabalin <shaba@altlinux.org> 2.4.11-alt3
- build with embedded cryptopp

* Thu Jun 10 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.4.11-alt2
- fixed build for Elbrus

* Thu Mar 11 2021 Alexey Shabalin <shaba@altlinux.org> 2.4.11-alt1
- 2.4.11

* Mon May 25 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.4.9-alt3
- dep on urbackup-common added

* Fri May 15 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.4.9-alt2
- file conflict with urbackup-server fixed

* Thu Nov 07 2019 Alexey Shabalin <shaba@altlinux.org> 2.4.9-alt1
- 2.4.9

* Sun Aug 25 2019 Alexey Shabalin <shaba@altlinux.org> 2.4.6.0-alt1
- 2.4.6
- add snapshot scripts

* Sun Jul 14 2019 Alexey Shabalin <shaba@altlinux.org> 2.3.4-alt1
- Initial build
