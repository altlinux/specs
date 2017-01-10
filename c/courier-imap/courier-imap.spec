%define courier_confdir	%_sysconfdir/%name
%define courier_datadir	%_datadir/%name
%define courier_localstatedir %_localstatedir/%name
%define courier_piddir %_var/run
%define _ssldir %_localstatedir/ssl
%define _pemdir %_ssldir/private
%define rev %nil

Name: courier-imap
Version: 4.17.2
Release: alt0.3%rev

Summary: IMAP/POP3 server with Maildir support
License: GPL
Group: System/Servers
Url: http://www.courier-mta.org

Requires(pre): cert-sh-functions >= 0.1-alt2 shadow-utils
Requires(post,preun): service
Requires: courier-common-utils
Requires: gamin

Source0: %name-%version%rev.tar.bz2
Source1: courier-imapd.init
Source2: courier-imaps.init
Source3: courier-pop3d.init
Source4: courier-pop3s.init
Source7: %name.README-ALT
Source8: common-login.authpam
Source9: ssl-sh-functions

Patch0: %name-%version-alt-makefile.patch
Patch1: %name-%version-alt-rc.in.patch
Patch2: %name-%version-alt-imapaccess.patch
Patch3: %name-%version-alt-imap-ssl-configure.patch
Patch4: %name-%version-alt-pamconf.patch
Patch5: %name-%version-alt-quotawarn.patch
Patch6: %name-%version-alt-shareddir.patch
Patch7: %name-%version-alt-sysconftool.patch
Patch8: %name-%version-alt-tls-enforce-config.patch
Patch9: %name-%version-alt-config.patch

BuildPreReq: libcourier-authlib-devel = 0.66.4

# Automatically added by buildreq on Sun Apr 27 2008
BuildRequires: gcc-c++ libdb4-devel libgamin-devel libkrb5-devel libpcre-devel libssl-devel openssl libpam-devel pam-config libidn-devel
BuildRequires: courier-unicode-devel

%description
Courier-IMAP is an IMAP server for Maildir mailboxes.  This package contains
the standalone version of the IMAP server that's included in the Courier
mail server package.  This package is a customized version for use with
other mail servers.

%prep
%setup -n %name-%version%rev
%patch0 -p2 -b .p0
%patch1 -p2 -b .p1
%patch2 -p2 -b .p2
%patch3 -p2 -b .p3
%patch4 -p2 -b .p4
%patch5 -p2 -b .p5
%patch6 -p2 -b .p6
%patch7 -p2 -b .p7
%patch8 -p2 -b .p8
%patch9 -p2 -b .p9
cp %SOURCE8 libs/imap/

%build
%autoreconf
%configure \
    --sysconfdir=%courier_confdir \
    --localstatedir=%courier_localstatedir \
    --datadir=%courier_datadir \
    --enable-unicode \
    --with-userdb=%courier_confdir/userdb \
    --with-makedatprog=%_bindir/makedatprog \
    --with-db=db \
    --with-certsdir=%_localstatedir/ssl/private \
    --with-certdb=%_datadir/ca-certificates/ca-bundle.crt \
    --with-piddir=%courier_piddir \
    --with-mailer=%_sbindir/sendmail \
    --with-redhat

%make_build

%install
# adjust $RPM_BUILD for install
mkdir -p %buildroot%_sysconfdir/pam.d
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%courier_localstatedir
touch %buildroot%courier_localstatedir/couriersslcache

make DESTDIR=%buildroot install

# tune configfiles
for i in `ls %buildroot%courier_confdir/*.dist | sed -e 's/\.dist//'`; do
	mv $i.dist $i
done
touch %buildroot%courier_confdir/{imap,pop3}d.custom.cnf
install -m 0644 %SOURCE9 %buildroot%courier_confdir

# install configs and init scripts
install -m 0755 %SOURCE1 %buildroot%_initdir/courier-imapd
install -m 0755 %SOURCE2 %buildroot%_initdir/courier-imaps
install -m 0755 %SOURCE3 %buildroot%_initdir/courier-pop3d
install -m 0755 %SOURCE4 %buildroot%_initdir/courier-pop3s

mkdir -p -m 0755 %buildroot%_pemdir
touch %buildroot%_pemdir/imapd.pem
touch %buildroot%_pemdir/pop3d.pem

mv %buildroot%courier_confdir/quotawarnmsg.example %buildroot%courier_confdir/quotawarnmsg

# root src documentation
mkdir -p %buildroot%_docdir/%name-%version/html
install -m 0644 %SOURCE7 %buildroot%_docdir/%name-%version/README-ALT.utf8
install -m 0644 AUTHORS %buildroot%_docdir/%name-%version
install -m 0644 INSTALL %buildroot%_docdir/%name-%version
install -m 0644 NEWS    %buildroot%_docdir/%name-%version
install -m 0644 README  %buildroot%_docdir/%name-%version
install -m 0644 INSTALL.html %buildroot%_docdir/%name-%version/html
install -m 0644 NEWS.html    %buildroot%_docdir/%name-%version/html

# imap documentation
install -m 0644 libs/imap/BUGS      %buildroot%_docdir/%name-%version
install -m 0644 libs/imap/ChangeLog %buildroot%_docdir/%name-%version
install -m 0644 libs/imap/README    %buildroot%_docdir/%name-%version/README.imap
install -m 0644 libs/imap/README.proxy %buildroot%_docdir/%name-%version
install -m 0644 libs/imap/BUGS.html    %buildroot%_docdir/%name-%version/html
install -m 0644 libs/imap/courierpop3d.html %buildroot%_docdir/%name-%version/html
install -m 0644 libs/imap/courierpop3d.8 %buildroot%_man8dir
install -m 0644 libs/imap/README.html       %buildroot%_docdir/%name-%version/html/README.imap.html
install -m 0644 libs/imap/README.proxy.html %buildroot%_docdir/%name-%version/html

# maildir documentation
install -m 0644 libs/maildir/README.maildirquota.txt  %buildroot%_docdir/%name-%version
install -m 0644 libs/maildir/README.sharedfolders.txt %buildroot%_docdir/%name-%version
install -m 0644 libs/maildir/maildiracl.html %buildroot%_docdir/%name-%version/html
install -m 0644 libs/maildir/maildir.html    %buildroot%_docdir/%name-%version/html
install -m 0644 libs/maildir/maildirkw.html  %buildroot%_docdir/%name-%version/html
install -m 0644 libs/maildir/maildirmake.html  %buildroot%_docdir/%name-%version/html
install -m 0644 libs/maildir/maildirquota.html %buildroot%_docdir/%name-%version/html
install -m 0644 libs/maildir/README.imapkeywords.html  %buildroot%_docdir/%name-%version/html
install -m 0644 libs/maildir/README.maildirfilter.html %buildroot%_docdir/%name-%version/html
install -m 0644 libs/maildir/README.maildirquota.html  %buildroot%_docdir/%name-%version/html
install -m 0644 libs/maildir/README.sharedfolders.html %buildroot%_docdir/%name-%version/html

# tcpd/tls documentation
install -m 0644 libs/tcpd/README.couriertls %buildroot%_docdir/%name-%version
install -m 0644 libs/tcpd/couriertls.html %buildroot%_docdir/%name-%version/html
install -m 0644 libs/tcpd/couriertls.1 %buildroot%_man1dir

%post
# try to update configs from .rpmsave
for i in imapd pop3d; do
	if [ -f %courier_confdir/$i.rpmsave ]; then
		. %courier_confdir/$i.rpmsave
		subst "s|^ADDRESS=127.0.0.1|ADDRESS=$ADDRESS|" %courier_confdir/$i
	fi
done
for i in imapd-ssl pop3d-ssl; do
	if [ -f %courier_confdir/$i.rpmsave ]; then
		. %courier_confdir/$i.rpmsave
		subst "s|^SSLADDRESS=127.0.0.1|SSLADDRESS=$SSLADDRESS|" %courier_confdir/$i
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
%_initdir/courier-imapd
%_initdir/courier-imaps
%_initdir/courier-pop3d
%_initdir/courier-pop3s
%dir %courier_confdir
%courier_confdir/ssl-sh-functions
%config %courier_confdir/imapd
%config %courier_confdir/pop3d
%config %courier_confdir/imapd-ssl
%config %courier_confdir/pop3d-ssl
%config(noreplace) %_sysconfdir/pam.d/imap
%config(noreplace) %_sysconfdir/pam.d/pop3
%ghost %attr(0640,root,root) %config(noreplace,missingok) %courier_confdir/imapd.custom.cnf
%ghost %attr(0640,root,root) %config(noreplace,missingok) %courier_confdir/pop3d.custom.cnf
%courier_confdir/quotawarnmsg
%_bindir/maildiracl
%_bindir/maildirkw
%_bindir/makeimapaccess
%_sbindir/couriertls
%_sbindir/couriertcpd
%_sbindir/imapd
%_sbindir/imaplogin
%_sbindir/pop3d
%_sbindir/pop3login
%_sbindir/sharedindexinstall
%_sbindir/sharedindexsplit
%_man1dir/couriertcpd.1*
%_man1dir/couriertls.1*
%_man1dir/maildiracl.1*
%_man1dir/maildirkw.1*
%_man8dir/courierpop3d.8*
%_man8dir/imapd.8*
%_man8dir/makeimapaccess.8*
%dir %_docdir/%name-%version
%doc %_docdir/%name-%version/*
%ghost %attr(0640,root,root) %config(noreplace,missingok) %_pemdir/imapd.pem
%ghost %attr(0640,root,root) %config(noreplace,missingok) %_pemdir/pop3d.pem
%dir %attr(-,root,root) %courier_localstatedir
%dir %attr(0750,root,root) %courier_localstatedir/imapaccess
%ghost %attr(0600,root,root) %courier_localstatedir/couriersslcache

%changelog
* Tue Jan 10 2017 L.A. Kostis <lakostis@altlinux.ru> 4.17.2-alt0.3
- ssl-sh-functions: fix a typo.

* Tue Jan 10 2017 L.A. Kostis <lakostis@altlinux.ru> 4.17.2-alt0.2
- Rewrite tls cert operations.
- Added gamin to requires.
  Strict TLS settings in -alt-tls-enforce-config.patch:
  + TLS proto now 1.2+
  + cipher suite changed to AES128+EECDH:AES128+EDH.

* Sun Jan 08 2017 L.A. Kostis <lakostis@altlinux.ru> 4.17.2-alt0.1
- Updated to 4.17.2.
- Major .spec cleanup.
- Rewrite all patches.
- Fixed file intersections with courier-common-utils.
- Build with courier-unicode and libidn.

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
