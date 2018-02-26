
%define courier_piddir %_var/run
%define _ssldir %_localstatedir/ssl
%define _pemdir %_ssldir/private
%define rev %nil

Name: courier-imap
Version: 4.10.0
Release: alt0.2%rev

Summary: IMAP/POP3 server with Maildir support
License: GPL
Group: System/Servers
URL: http://www.courier-mta.org

Requires(pre): cert-sh-functions >= 0.1-alt2 shadow-utils
Requires(post,preun): service
Requires: courier-imap-utils = %version
Requires: libgamin-fam

Source0: %name-%version%rev.tar.bz2
Source1: courier-imapd.init
Source2: courier-imaps.init
Source3: courier-pop3d.init
Source4: courier-pop3s.init
Source7: %name.README-ALT

Patch0: %name-4.10.0-alt-pkgname.patch
Patch1: %name-4.5.0-alt-pamconf.patch
Patch2: %name-3.0.8-alt-quotawarn.patch
Patch3: %name-4.10.0-alt-config.patch
Patch4: %name-4.5.0-alt-shareddir.patch
Patch5: %name-4.4.1-alt-makefile.patch
Patch6: %name-4.4.1-alt-configure.patch

BuildPreReq: libcourier-authlib-devel = 0.63.0

# Automatically added by buildreq on Sun Apr 27 2008
BuildRequires: gcc-c++ libdb4-devel libgamin-devel libkrb5-devel libpcre-devel libssl-devel openssl libpam-devel pam-config libidn-devel

%description
Courier-IMAP is an IMAP server for Maildir mailboxes.  This package contains
the standalone version of the IMAP server that's included in the Courier
mail server package.  This package is a customized version for use with
other mail servers.


%package utils
Summary: Maildir utilities
Group: Networking/Mail
Provides: courier-common-utils
Requires: courier-authlib
Conflicts: maildrop-utils
Conflicts: courier-maildrop-utils

%description utils
Some common maildir utilities for courier-maildrop
and courier-imap packages.

%prep
%setup -q -n %name-%version%rev
%patch0 -p2 -b .p0
%patch1 -p1 -b .p1
%patch2 -p1 -b .p2
%patch3 -p2 -b .p3
%patch4 -p2 -b .p4
%patch5 -p1 -b .p5
%patch6 -p1 -b .p6

%build
#libtoolize --force --install
%configure \
    --enable-unicode \
    --with-userdb=%_sysconfdir/%name/userdb \
    --with-makedatprog=%_datadir/%name/makedatprog \
    --with-db=db \
    --with-certsdir=%_localstatedir/ssl/private \
    --with-certdb=%_datadir/ca-certificates/ca-bundle.crt \
    --with-piddir=%courier_piddir \
    --without-ipv6 \
    --with-redhat

%make_build

%install

# adjust $RPM_BUILD for install
%__mkdir_p %buildroot/%_sysconfdir/pam.d
%__mkdir_p %buildroot/%_initdir
%__mkdir_p %buildroot/%_localstatedir/%name
touch %buildroot/%_localstatedir/%name/couriersslcache

%__make DESTDIR=%buildroot install

# tune configfiles
for i in `ls %buildroot/%_sysconfdir/%name/*.dist | %__sed -e 's/\.dist//'`; do
	%__mv $i.dist $i
done

# install configs and inint scripts
%__install -m 0755 %SOURCE1 %buildroot/%_initdir/courier-imapd
%__install -m 0755 %SOURCE2 %buildroot/%_initdir/courier-imaps
%__install -m 0755 %SOURCE3 %buildroot/%_initdir/courier-pop3d
%__install -m 0755 %SOURCE4 %buildroot/%_initdir/courier-pop3s

%__mkdir_p -m 0755 %buildroot%_pemdir
touch %buildroot%_pemdir/imapd.pem
touch %buildroot%_pemdir/pop3d.pem

%__mv %buildroot/%_sysconfdir/%name/quotawarnmsg.example %buildroot/%_sysconfdir/%name/quotawarnmsg

# root src documentation
%__mkdir_p %buildroot/%_docdir/%name-%version/html
%__install -m 0644 %SOURCE7 %buildroot/%_docdir/%name-%version/README-ALT.koi8-r
%__install -m 0644 AUTHORS %buildroot/%_docdir/%name-%version
%__install -m 0644 INSTALL %buildroot/%_docdir/%name-%version
%__install -m 0644 NEWS    %buildroot/%_docdir/%name-%version
%__install -m 0644 README  %buildroot/%_docdir/%name-%version
%__install -m 0644 INSTALL.html %buildroot/%_docdir/%name-%version/html
%__install -m 0644 NEWS.html    %buildroot/%_docdir/%name-%version/html

# imap documentation
%__install -m 0644 imap/BUGS      %buildroot/%_docdir/%name-%version
%__install -m 0644 imap/ChangeLog %buildroot/%_docdir/%name-%version
%__install -m 0644 imap/README    %buildroot/%_docdir/%name-%version/README.imap
%__install -m 0644 imap/README.proxy %buildroot/%_docdir/%name-%version
%__install -m 0644 imap/BUGS.html    %buildroot/%_docdir/%name-%version/html
%__install -m 0644 imap/courierpop3d.html %buildroot/%_docdir/%name-%version/html
%__install -m 0644 imap/README.html       %buildroot/%_docdir/%name-%version/html/README.imap.html
%__install -m 0644 imap/README.proxy.html %buildroot/%_docdir/%name-%version/html

# maildir documentation
%__install -m 0644 maildir/README.maildirquota.txt  %buildroot/%_docdir/%name-%version
%__install -m 0644 maildir/README.sharedfolders.txt %buildroot/%_docdir/%name-%version
%__install -m 0644 maildir/maildiracl.html %buildroot/%_docdir/%name-%version/html
%__install -m 0644 maildir/maildir.html    %buildroot/%_docdir/%name-%version/html
%__install -m 0644 maildir/maildirkw.html  %buildroot/%_docdir/%name-%version/html
%__install -m 0644 maildir/maildirmake.html  %buildroot/%_docdir/%name-%version/html
%__install -m 0644 maildir/maildirquota.html %buildroot/%_docdir/%name-%version/html
%__install -m 0644 maildir/README.imapkeywords.html  %buildroot/%_docdir/%name-%version/html
%__install -m 0644 maildir/README.maildirfilter.html %buildroot/%_docdir/%name-%version/html
%__install -m 0644 maildir/README.maildirquota.html  %buildroot/%_docdir/%name-%version/html
%__install -m 0644 maildir/README.sharedfolders.html %buildroot/%_docdir/%name-%version/html

# tcpd documentation
%__install -m 0644 tcpd/README.couriertls %buildroot/%_docdir/%name-%version

%post
# adjust config for generating SSL certs
HOSTNAME=`hostname -f`
for i in `ls %_sysconfdir/%name/*.cnf`; do
   %__subst "s|^CN=.*$|CN=$HOSTNAME|g;s|^emailAddress=.*$|emailAddress=root@$HOSTNAME|g" $i
done

%__subst "s|__HOSTNAME__|$HOSTNAME|g" %_sysconfdir/%name/quotawarnmsg

# try to update configs from .rpmsave
for i in imapd pop3d; do
	if [ -f %_sysconfdir/%name/$i.rpmsave ]; then
		. %_sysconfdir/%name/$i.rpmsave
		%__subst "s|^ADDRESS=127.0.0.1|ADDRESS=$ADDRESS|" %_sysconfdir/%name/$i
	fi
done
for i in imapd-ssl pop3d-ssl; do
	if [ -f %_sysconfdir/%name/$i.rpmsave ]; then
		. %_sysconfdir/%name/$i.rpmsave
		%__subst "s|^SSLADDRESS=127.0.0.1|SSLADDRESS=$SSLADDRESS|" %_sysconfdir/%name/$i
	fi
done

%post_service courier-imapd
%post_service courier-pop3d
%post_service courier-imaps
%post_service courier-pop3s
 
%preun
%preun_service courier-imapd
%preun_service courier-imaps
%preun_service courier-pop3d
%preun_service courier-pop3s

%files
%dir %_sysconfdir/%name
%dir %_datadir/%name
%_initdir/courier-imapd
%_initdir/courier-imaps
%_initdir/courier-pop3d
%_initdir/courier-pop3s
%config %_sysconfdir/%name/imapd
%config %_sysconfdir/%name/pop3d
%config %_sysconfdir/%name/imapd-ssl
%config %_sysconfdir/%name/pop3d-ssl
%config(noreplace) %_sysconfdir/pam.d/imap
%config(noreplace) %_sysconfdir/pam.d/pop3
%config(noreplace) %_sysconfdir/%name/imapd.cnf
%config(noreplace) %_sysconfdir/%name/pop3d.cnf
%_sysconfdir/%name/quotawarnmsg
%_bindir/maildiracl
%_bindir/maildirkw
%_sbindir/couriertcpd
%_sbindir/couriertls
%_sbindir/imapd
%_sbindir/imaplogin
%_sbindir/makedatprog
%_sbindir/pop3d
%_sbindir/pop3login
%_sbindir/sharedindexinstall
%_sbindir/sharedindexsplit
%_libexecdir/%name/*.rc
%_man1dir/couriertcpd.1*
%_man1dir/maildiracl.1*
%_man1dir/maildirkw.1*
%_man8dir/imapd.8*
%dir %_docdir/%name-%version
%doc %_docdir/%name-%version/*
%ghost %attr(0640,root,root) %config(noreplace,missingok) %_pemdir/imapd.pem
%ghost %attr(0640,root,root) %config(noreplace,missingok) %_pemdir/pop3d.pem
%dir %_localstatedir/%name
%dir %_localstatedir/%name/shared
%dir %_localstatedir/%name/shared.tmp
%ghost %attr(0644,root,root) %_localstatedir/%name/couriersslcache

%files utils
%_bindir/deliverquota
%_bindir/maildirmake
%_man1dir/maildirmake.1.*
%_man8dir/deliverquota.8.*

%changelog
* Wed Jan 18 2012 L.A. Kostis <lakostis@altlinux.ru> 4.10.0-alt0.2
- fix pam unmets.

* Mon Jan 16 2012 L.A. Kostis <lakostis@altlinux.ru> 4.10.0-alt0.1
- NMU:
  + updated to 4.10.0 version.
  + Rewrite PAM config file using common-login (by ldv@).

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 4.5.0-alt0.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Mon Aug 31 2009 L.A. Kostis <lakostis@altlinux.ru> 4.5.1-alt0.1
- NMU:
  + updated to 4.5.1 version.

* Sat May 16 2009 L.A. Kostis <lakostis@altlinux.ru> 4.5.0-alt0.1
- NMU:
  + updated to 4.5.0 version.
  + fix cacerts dir.
  + cleanup buildreq (remove gnutls cause it's not used anyway).
  + update -alt patches -{pkgname,shareddir,config}.
  + generate ssl certificates via cert-sh-functions.

* Sat Sep 06 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 4.4.1-alt1
- 4.4.1

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 4.3.1-alt1.1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Sat Jun 14 2008 ALT QA Team Robot <qa-robot@altlinux.org> 4.3.1-alt1.1
- Automated rebuild with libdb-4.7.so.

* Sun Apr 27 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 4.3.1-alt1
- 4.3.1

* Tue Mar 27 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 4.1.2-alt1
- 4.1.2

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 4.1.1-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sat Jul 01 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 4.1.1-alt1
- 4.1.1

* Tue Jun 27 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 4.1.0-alt2
- fix typo in the courier-imapd init-script

* Sat Apr 29 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 4.1.0-alt1
- 4.1.0
- replace libfam build requres to libgamin
- fix spec-file for x86_64 build
- change syslog identity for courier daemons:
  + courier-imapd: imapd     to courier-imapd
  + courier-imaps: imapd-ssl to courier-imaps
  + courier-imapd: pop3d     to courier-pop3d
  + courier-imapd: pop3d-ssl to courier-pop3s

* Wed Mar 08 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 4.0.6-alt4
- fix build with --as-needed

* Mon Dec 26 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 4.0.6-alt3
- #8675 fixed

* Tue Dec 13 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 4.0.6-alt2
- fix courier-imapd initscript

* Sat Nov 26 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 4.0.6-alt1
- 4.0.6
- spec-file fix:
  + remove abstract virtual packages IMAPD & POP3D
  + remove conflicts for that packages

* Mon May 23 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 4.0.3-alt1
- 4.0.3
- #6550 fixed

* Sat Apr 02 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 4.0.2-alt3
- fix for #5763

* Mon Mar 28 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 4.0.2-alt2
- spec-file fixes
- minimal config migration from old versions of this packages
- README-ALT.koi8-r added

* Tue Mar 08 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 4.0.2-alt1
- 4.0.2

* Fri Jan 07 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 4.0.0-alt1
- 4.0.0

* Wed Dec 01 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 3.0.8-alt2.20041129
- new beta

* Tue Nov 30 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 3.0.8-alt2.20041120
- spec-file fixes

* Tue Nov 23 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 3.0.8-alt1.20041120
- 3.0.8 rev 20041120

* Sat Nov 13 2004 ALT QA Team Robot <qa-robot@altlinux.org> 3.0.7-alt1.1
- Rebuilt with openldap-2.2.18-alt3.

* Sat Aug 14 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 3.0.7-alt1
- New version

* Mon Jun 28 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 3.0.5-alt4
- New version
- changes/patches from Andrey Orlov <cray@altlinux.ru>

* Tue May 11 2004 ALT QA Team Robot <qa-robot@altlinux.org> 2.1.2-alt2.1
- Rebuilt with openssl-0.9.7d.

* Fri Feb 20 2004 Denis Smirnov <mithraen@altlinux.ru> 2.1.2-alt2
- building with libdb4.2

* Fri Oct 03 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Mon Aug 25 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.0-alt3
- fix BuildRequires

* Sat Aug 23 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.0-alt2
- package structure changed:
  + authdaemon as an independed package;
  + courier-imap-(ldap|mysql|pgsql) renamed
    to courier-authdaemon-(ldap|mysql|pgsql);

* Fri Jul 04 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Sun Jun 08 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.7.3-alt1
- 1.7.3

* Fri May 23 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.7.2-alt1.2
- option '-lock=filename ' added to couriertcpd -- full path to lock-file
- init-scripts redesign
- PAM configs changed according to new ALT policy

* Fri May 16 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.7.2-alt1
- 1.7.2
- IMAPD-SSL init-script typo fixed

* Sun Mar 30 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.7.1-alt1
- new version -- 1.7.1;
- packages group changed to 'System/Servers'
- set max number of IMAP connections to 10 per one ip-address

* Tue Feb 11 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.6.2-alt3
- spec-file fix:
  + provide abstract IMAPD & POP3D services (as virtual pkgs) and
    describe the relations with other such pkgs (fixes #2168)

* Sat Feb 01 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.6.2-alt2
- SSL/TLS certs generation during package install
- fix paths for .lock, .pid and .pem files according to
  FHS and ALT policy
- courier-imap-doc removed, documentation is moved into courier-imap
- spec-file cleanup

* Mon Jan 06 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.6.2-alt1
- 1.6.2
- pop3d/imapd daemons logging improvement
- spec-file fixes

* Tue Oct 29 2002 Dmitry Lebkov <dlebkov@altlinux.ru> 1.5.3-alt2
- fix 'post' and 'preun' sections of the spec-file
- add 'START_AUTHD' variable to /etc/sysconfig/courier-imap
  This variable is checked by courier-authdaemon script

* Wed Sep 11 2002 Dmitry Lebkov <dlebkov@altlinux.ru> 1.5.3-alt1
- initial package for ALT Linux
