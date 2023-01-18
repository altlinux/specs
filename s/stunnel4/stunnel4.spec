%define _ssldir %(openssl-config --openssldir)
%define _unpackaged_files_terminate_build 1

%def_disable check

Summary: Universal SSL tunnel
Name: stunnel4
Version: 5.67
Release: alt1
License: GPLv2+
Group: Networking/Other

Packager: Alexey Gladkov <legion@altlinux.org>

Source0: ftp://stunnel.mirt.net/stunnel/stunnel-%version.tar.gz
Source1: stunnel.init
Source3: stunnel.inetd

Patch1: stunnel-config.patch
Patch2: stunnel-5.67-authpriv.patch
Patch3: stunnel-5.53-systemd-service.patch

Url: http://www.stunnel.org/

Requires(pre): cert-sh-functions

BuildRequires: libssl-devel >= 0.9.7d
BuildRequires: openssl >= 0.9.7d

# pod2man
BuildRequires: perl-podlators

# pod2html
BuildRequires: perl-devel

# systemd
BuildRequires: libsystemd-devel

# for tests
%if_enabled check
BuildRequires: /proc
BuildRequires: nmap
BuildRequires: iproute2
BuildRequires: lsof
%endif

# bash completion
BuildRequires: bash-completion

%description
The stunnel program is designed to work as SSL encryption wrapper
between remote client and local (inetd-startable) or remote server.
The concept is that having non-SSL aware daemons running on your
system you can easily setup them to communicate with clients over
secure SSL channel. stunnel can be used to add SSL functionality to
commonly used inetd daemons like POP-2, POP-3 and IMAP servers without
any changes in the programs' code.

%package standalone
Summary: stunnel acts as standalone server
Group: Networking/Other
Requires: %name = %version-%release
BuildArch: noarch

%description standalone
stunnel acts as standalone server.

%package inetd
Summary: stunnel acts as inetd service
Group: Networking/Other
Requires: %name = %version-%release
BuildArch: noarch

%description inetd
stunnel acts as inetd service.

%package -n bash-completion-%name
Summary: Bash completion for %name
Group: Shells
BuildArch: noarch
Requires: bash-completion
Requires: %name = %version-%release

%description -n bash-completion-%name
Bash completion for %name.

%prep
%setup -q
%patch1 -p1 -b .fix
%patch2 -p2
%patch3 -p2

%build
#autoreconf

%configure \
	--with-ssl=%_prefix \
	--enable-shared \
	--disable-libwrap \
	--with-bashcompdir=%_datadir/bash-completion/completions

%make_build

%install
install -d \
	%buildroot{/etc/{rc.d/init.d,xinetd.d,sysconfig},%_var/{lib,run}/stunnel} \
	%buildroot/%systemd_unitdir

%make install DESTDIR=%buildroot

mv -f \
	%buildroot%_sysconfdir/stunnel/stunnel.conf-sample \
	%buildroot%_sysconfdir/stunnel/stunnel.conf

mv -f \
	tools/stunnel.service \
	%buildroot/%systemd_unitdir/stunnel.service

install -m755 %SOURCE1 %buildroot/etc/rc.d/init.d/stunnel
install -m644 %SOURCE3 %buildroot/etc/xinetd.d/stunnel

# Ghosts. How to include it in package and remove on
# package remove without checking of size mismatch?
mkdir -p %buildroot%_ssldir/{certs,private}
touch %buildroot%_ssldir/certs/stunnel.pem
touch %buildroot%_ssldir/private/stunnel.pem

rm -rf -- %buildroot%_libdir/stunnel
rm -rf -- %buildroot%_docdir/stunnel
rm -f  -- %buildroot%_sysconfdir/stunnel/stunnel.pem

%check
%if_enabled check
make check
%endif

%pre
%_sbindir/groupadd -r -f stunnel &>/dev/null
%_sbindir/useradd -r -g stunnel -d /var/run/stunnel -s /bin/false \
        -c "stunnel User" -M -n stunnel &>/dev/null ||:

%post standalone
%post_service stunnel

%preun standalone
%preun_service stunnel

%files
# note: this COPYING contains general information not GPL text
%doc *.md doc/en/* doc/stunnel.html
%doc tools/{ca.*,importCA.*}
%attr(750,stunnel,stunnel) %_var/run/stunnel
%attr(750,stunnel,stunnel) %_var/lib/stunnel
%dir %_sysconfdir/stunnel
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/stunnel/stunnel.conf
%attr(755,root,root) %_bindir/*
%_mandir/man8/*

%files standalone
%systemd_unitdir/stunnel.service
%attr(754,root,root) /etc/rc.d/init.d/stunnel
%attr(0600,root,root) %ghost %config(missingok,noreplace) %verify(not md5 size mtime) %_ssldir/certs/stunnel.pem
%attr(0600,root,root) %ghost %config(missingok,noreplace) %verify(not md5 size mtime) %_ssldir/private/stunnel.pem

%files inetd
%config(noreplace) %verify(not md5 mtime size) /etc/xinetd.d/stunnel

%files -n bash-completion-%name
%_datadir/bash-completion/completions/*

%changelog
* Wed Jan 18 2023 L.A. Kostis <lakostis@altlinux.ru> 5.67-alt1
- New version (5.67).
- Added bash-completion package.

* Sun Nov 07 2021 Vladislav Zavjalov <slazav@altlinux.org> 5.60-alt1
- New version (5.60).

* Thu Apr 18 2019 L.A. Kostis <lakostis@altlinux.ru> 5.53-alt1.1
- Disable tests (due hidepid=1 setting on build host).
- Fix noarch warnings.

* Thu Apr 18 2019 L.A. Kostis <lakostis@altlinux.ru> 5.53-alt1
- New version (5.53).
- Enable systemd support.

* Wed Sep 26 2018 Alexey Gladkov <legion@altlinux.ru> 5.49-alt1
- New version (5.49).

* Sun Apr 13 2014 Alexey Gladkov <legion@altlinux.ru> 5.01-alt1
- New version (5.01).

* Sat Mar 23 2013 Alexey Gladkov <legion@altlinux.ru> 4.56-alt1
- New version (4.56).

* Fri Jan 13 2012 Alexey Gladkov <legion@altlinux.ru> 4.52-alt1
- New version (4.52).

* Thu Sep 08 2011 Alexey Gladkov <legion@altlinux.ru> 4.43-alt1
- New version (4.43).

* Sat Aug 20 2011 Alexey Gladkov <legion@altlinux.ru> 4.42-alt1
- New version (4.42).

* Tue May 03 2011 Alexey Gladkov <legion@altlinux.ru> 4.36-alt1
- New version (4.36).

* Thu Apr 21 2011 Alexey Gladkov <legion@altlinux.ru> 4.35-alt1
- New version (4.35).

* Thu Oct 07 2010 Alexey Gladkov <legion@altlinux.ru> 4.34-alt1
- New version (4.34).
- Run stunnel in chroot by default.
- Add cert-sh-functions support.

* Wed Jan 20 2010 Pavlov Konstantin <thresh@altlinux.ru> 4.29-alt1
- Initial build for ALT Linux.


