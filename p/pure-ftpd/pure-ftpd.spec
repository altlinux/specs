%undefine _configure_gettext
%define add_build_opts() %{expand:%{?1:%%global default_build_opts %{?default_build_opts:%default_build_opts} %*}}
%define _ssldir %(openssl-config --openssldir)
%define _pemdir %_ssldir/private
%define _pemfile %_pemdir/%name.pem

%def_with altlog
%def_with extauth
%def_with puredb
%def_with cookie
%def_with throttling
%def_with ratios
%def_with quotas
%def_with ftpwho
%def_with uploadscript
%def_with virtualhosts
%def_with virtualchroot
%def_with diraliases
%def_with peruserlimits
%def_with pam

%def_with rfc
%def_with tls

# Optional builds
%def_with pgsql
%def_with mysql
%def_with ldap

Name: pure-ftpd
Version: 1.0.29
Release: alt1.1
URL: http://www.pureftpd.org
Source: %name-%version.tar
Packager: Afanasov Dmitry <ender@altlinux.org>

Source2: %name.init
Source3: %name.logrotate
Source4: %name.xinetd
Source5: ftpallow
Source6: ftpusers
Source7: %name.default

Patch1: %name-1.0.18-conf.patch
Patch2: %name-1.0.26-docs.patch
Patch3: %name-1.0.26-VHOST_PATH.patch

Group: System/Servers
License: BSD
Provides: ftp-server ftpserver pure-ftpd
Summary: Lightweight, fast and secure FTP server

# buildreuiqres
BuildRequires: libcap-devel  

%{?_with_pam:BuildRequires: libpam-devel}
%{?_with_tls:BuildRequires: libssl-devel}

%{?_with_ldap:BuildRequires: libldap-devel}
%{?_with_mysql:BuildRequires: libMySQL-devel zlib-devel}
%{?_with_pgsql:BuildRequires: postgresql-devel}

%description
Pure-FTPd is a fast, production-quality, standard-comformant FTP server,
based upon Troll-FTPd. Unlike other popular FTP servers, it has no known
security flaw, it is really trivial to set up and it is especially designed
for modern Linux and FreeBSD kernels (setfsuid, sendfile, capabilities) .
Features include PAM support, IPv6, chroot()ed home directories, virtual
domains, built-in LS, anti-warez system, bandwidth throttling, FXP, bounded
ports for passive downloads, UL/DL ratios, native LDAP and SQL support,
Apache log files and more.

%package common
Summary: Common files for %name ftp server
Group: System/Servers
Conflicts: wu-ftpd, ncftpd, proftpd, vsftpd
Conflicts: %name < %version-%release
Requires(post,preun): service
%{?_with_tls:Requires(post,preun): openssl}

%description common
Common files for %name ftp server

%package light
Summary: Lightweight, fast and secure FTP server in default configuration
Group: System/Servers
Requires: %name-common
Conflicts: %name-ldap
Conflicts: %name-mysql
Conflicts: %name-pgsql

# obsolete pure-ftpd < 1.0.22-alt1, since its functionality was splitted into
# few pices
Provides: %name = %version-%release
Obsoletes: %name

%description light
Pure-FTPd is a fast, production-quality, standard-comformant FTP server,
based upon Troll-FTPd. Unlike other popular FTP servers, it has no known
security flaw, it is really trivial to set up and it is especially designed
for modern Linux and FreeBSD kernels (setfsuid, sendfile, capabilities) .
Features include PAM support, IPv6, chroot()ed home directories, virtual
domains, built-in LS, anti-warez system, bandwidth throttling, FXP, bounded
ports for passive downloads, UL/DL ratios, native LDAP and SQL support,
Apache log files and more.

This package contains of Pure-FTPd server builded with:
%{?_with_rfc: - RFC2640
}%{?_with_tls: - TLS support
}%{?_with_altlog: - Alternative logging scheme
}%{?_with_extauth: - External authorization (%name-authd daemon)
}%{?_with_virtualhosts: - Virtual hosts support
}%{?_with_diraliases: - Directory aliases
}%{?_with_ratios: - ratios
}%{?_with_quotas: - Quotas
}%{?_with_puredb: - puredb support
}%{?_with_pam: - PAM authorization
}%{?_with_cookie: - Cookie support
}
%package mysql
Summary: Lightweight, fast and secure FTP server with MySQL support.
Group: System/Servers
Requires: %name-common
Conflicts: %name-light
Conflicts: %name-pgsql
Conflicts: %name-ldap

# obsolete pure-ftpd < 1.0.22-alt1, since its functionality was splitted into
# few pices
Provides: %name = %version-%release
Obsoletes: %name

%description mysql
Pure-FTPd is a fast, production-quality, standard-comformant FTP server,
based upon Troll-FTPd. Unlike other popular FTP servers, it has no known
security flaw, it is really trivial to set up and it is especially designed
for modern Linux and FreeBSD kernels (setfsuid, sendfile, capabilities) .
Features include PAM support, IPv6, chroot()ed home directories, virtual
domains, built-in LS, anti-warez system, bandwidth throttling, FXP, bounded
ports for passive downloads, UL/DL ratios, native LDAP and SQL support,
Apache log files and more.

This package contains of Pure-FTPd server builded with:
%{?_with_rfc: - RFC2640
}%{?_with_tls: - TLS support
}%{?_with_altlog: - Alternative logging scheme
}%{?_with_extauth: - External authorization (%name-authd daemon)
}%{?_with_virtualhosts: - Virtual hosts support
}%{?_with_diraliases: - Directory aliases
}%{?_with_ratios: - ratios
}%{?_with_quotas: - Quotas
}%{?_with_puredb: - puredb support
}%{?_with_pam: - PAM authorization
}%{?_with_cookie: - Cookie support
} - MySQL support.

%package ldap
Summary: Lightweight, fast and secure FTP server with LDAP support.
Group: System/Servers
Requires: %name-common
Conflicts: %name-light
Conflicts: %name-mysql
Conflicts: %name-pgsql

# obsolete pure-ftpd < 1.0.22-alt1, since its functionality was splitted into
# few pices
Provides: %name = %version-%release
Obsoletes: %name

%description ldap
Pure-FTPd is a fast, production-quality, standard-comformant FTP server,
based upon Troll-FTPd. Unlike other popular FTP servers, it has no known
security flaw, it is really trivial to set up and it is especially designed
for modern Linux and FreeBSD kernels (setfsuid, sendfile, capabilities) .
Features include PAM support, IPv6, chroot()ed home directories, virtual
domains, built-in LS, anti-warez system, bandwidth throttling, FXP, bounded
ports for passive downloads, UL/DL ratios, native LDAP and SQL support,
Apache log files and more.

This package contains of Pure-FTPd server builded with:
%{?_with_rfc: - RFC2640
}%{?_with_tls: - TLS support
}%{?_with_altlog: - Alternative logging scheme
}%{?_with_extauth: - External authorization (%name-authd daemon)
}%{?_with_virtualhosts: - Virtual hosts support
}%{?_with_diraliases: - Directory aliases
}%{?_with_ratios: - ratios
}%{?_with_quotas: - Quotas
}%{?_with_puredb: - puredb support
}%{?_with_pam: - PAM authorization
}%{?_with_cookie: - Cookie support
} - LDAP support

%package pgsql
Summary: Lightweight, fast and secure FTP server with PostgreSQL support
Group: System/Servers
Requires: %name-common
Conflicts: %name-light
Conflicts: %name-mysql
Conflicts: %name-ldap

# obsolete pure-ftpd < 1.0.22-alt1, since its functionality was splitted into
# few pices
Provides: %name = %version-%release
Obsoletes: %name

%description pgsql
Pure-FTPd is a fast, production-quality, standard-comformant FTP server,
based upon Troll-FTPd. Unlike other popular FTP servers, it has no known
security flaw, it is really trivial to set up and it is especially designed
for modern Linux and FreeBSD kernels (setfsuid, sendfile, capabilities) .
Features include PAM support, IPv6, chroot()ed home directories, virtual
domains, built-in LS, anti-warez system, bandwidth throttling, FXP, bounded
ports for passive downloads, UL/DL ratios, native LDAP and SQL support,
Apache log files and more.

This package contains of Pure-FTPd server builded with:
%{?_with_rfc: - RFC2640
}%{?_with_tls: - TLS support
}%{?_with_altlog: - Alternative logging scheme
}%{?_with_extauth: - External authorization (%name-authd daemon)
}%{?_with_virtualhosts: - Virtual hosts support
}%{?_with_diraliases: - Directory aliases
}%{?_with_ratios: - ratios
}%{?_with_quotas: - Quotas
}%{?_with_puredb: - puredb support
}%{?_with_pam: - PAM authorization
}%{?_with_cookie: - Cookie support
} - PostgreSQL support

%prep
%setup -q -n %name-%version
%patch1 -p1
%patch2 -p1 
%patch3 -p1

%build
# configure options for all parts
%add_build_opts -- --sysconfdir=%_sysconfdir/%name
%add_build_opts -- %{subst_with altlog}
%add_build_opts -- %{subst_with extauth}
%add_build_opts -- %{subst_with puredb}
%add_build_opts -- %{subst_with cookie}
%add_build_opts -- %{subst_with throttling}
%add_build_opts -- %{subst_with ratios}
%add_build_opts -- %{subst_with quotas}
%add_build_opts -- %{subst_with ftpwho}
%add_build_opts -- %{subst_with uploadscript}
%add_build_opts -- %{subst_with virtualhosts}
%add_build_opts -- %{subst_with virtualchroot}
%add_build_opts -- %{subst_with diraliases}
%add_build_opts -- %{subst_with peruserlimits}
%add_build_opts -- %{subst_with pam}
%add_build_opts -- --with-vhostpath="%_sysconfdir/%name/vhost"

# enable tls and language support for all
%add_build_opts -- %{?_with_tls:--with-tls --with-certfile=%_pemfile}
%add_build_opts -- %{?_with_rfc:--with-rfc2640}

%autoreconf

%if_with ldap
%configure %default_build_opts --with-ldap
%make_build
cp src/pure-ftpd pure-ftpd-ldap
%make clean
%endif

%if_with mysql
%configure %default_build_opts --with-mysql
%make_build
cp src/pure-ftpd pure-ftpd-mysql
%make clean
%endif

%if_with pgsql
%configure %default_build_opts --with-pgsql
%make_build
cp src/pure-ftpd pure-ftpd-pgsql
%make clean
%endif

%configure %default_build_opts
%make_build

%install 
%make_install DESTDIR=%buildroot install

%__mkdir_p %buildroot%_sysconfdir/%name
%__mkdir_p %buildroot%_sysconfdir/%name/vhost
%__mkdir_p %buildroot%_sysconfdir/xinetd.d/
%__mkdir_p %buildroot%_sysconfdir/sysconfig/
%__mkdir_p %buildroot%_sysconfdir/pam.d/
%__mkdir_p %buildroot%_sysconfdir/logrotate.d/
%__mkdir_p %buildroot%_initrddir
%__mkdir_p %buildroot%_var/log/%name
%__mkdir_p -m 700 %buildroot%_var/run/%name

%__install -m 600 pam/pure-ftpd %buildroot%_sysconfdir/pam.d/%name
%__install -m 644 %SOURCE3 %buildroot%_sysconfdir/logrotate.d/%name
%__install -m 644 %SOURCE4 %buildroot%_sysconfdir/xinetd.d/%name
%__install -m 644 %SOURCE5 %buildroot%_sysconfdir/ftpallow
%__install -m 644 %SOURCE6 %buildroot%_sysconfdir/ftpusers
%__install -m 644 %SOURCE7 %buildroot%_sysconfdir/sysconfig/%name

%__install -m 644 configuration-file/pure-ftpd.conf %buildroot%_sysconfdir/%name/%name.conf
%__install -m 755 configuration-file/pure-config.pl %buildroot%_sbindir/pure-config

%__install -m 644 man/pure-ftpd.8 %buildroot%_man8dir
%__install -m 644 man/pure-ftpwho.8 %buildroot%_man8dir
%__install -m 644 man/pure-mrtginfo.8 %buildroot%_man8dir
%__install -m 644 man/pure-uploadscript.8 %buildroot%_man8dir
%__install -m 644 man/pure-pw.8 %buildroot%_man8dir
%__install -m 644 man/pure-pwconvert.8 %buildroot%_man8dir
%__install -m 644 man/pure-statsdecode.8 %buildroot%_man8dir
%__install -m 644 man/pure-quotacheck.8 %buildroot%_man8dir
%__install -m 644 man/pure-authd.8 %buildroot%_man8dir

%__install -m 755 %SOURCE2 %buildroot%_initrddir/%name

mkdir -p %buildroot%_defaultdocdir/%name-%version
install -m 755 configuration-file/pure-config.py %buildroot%_defaultdocdir/%name-%version
install -m 644 -pD FAQ THANKS AUTHORS CONTACT HISTORY NEWS pure-ftpd.png %buildroot%_defaultdocdir/%name-%version
install -m 644 -pD contrib/pure-stat.pl contrib/pure-vpopauth.pl contrib/xml_python_processors.txt %buildroot%_defaultdocdir/%name-%version
install -m 644 -pD README README.* pureftpd.schema %buildroot%_defaultdocdir/%name-%version

%if_with ldap
  %__install -m 644 pureftpd-ldap.conf %buildroot%_sysconfdir/%name
  %__install -m 755 pure-ftpd-ldap %buildroot%_sbindir/pure-ftpd-ldap
%endif

%if_with mysql
  %__install -m 644 pureftpd-mysql.conf %buildroot%_sysconfdir/%name
  %__install -m 755 pure-ftpd-mysql %buildroot%_sbindir/pure-ftpd-mysql
%endif

%if_with pgsql
  %__install -m 644 pureftpd-pgsql.conf %buildroot%_sysconfdir/%name
  %__install -m 755 pure-ftpd-pgsql %buildroot%_sbindir/pure-ftpd-pgsql
%endif

%if_with tls
  %__mkdir_p %buildroot%_pemdir
  touch %buildroot%_pemfile
%endif

# bytecompile-python off
unset RPM_PYTHON

%pre common
# by default ftp homedir is /var/ftp and if it is changed then someone is
# awaiting such beheiviour. and hence this command may break local
# configuration
#/usr/sbin/usermod -d /var/ftp ftp >/dev/null 2>&1 || :

%post common
%if_with tls
# create a ssl cert
if [ ! -s %_pemfile ]; then
umask 077
cat << EOF | openssl req -new -x509 -days 365 -nodes -out %_pemfile -keyout %_pemfile &>/dev/null
--
SomeState
SomeCity
SomeOrganization
SomeOrganizationalUnit
localhost.localdomain
root@localhost.localdomain
EOF
chown root.root %_pemfile ||:
chmod 600 %_pemfile ||:
fi
%endif

%post light
%post_service %name

%post ldap
rm -f %_sbindir/%name
ln -s pure-ftpd-ldap %_sbindir/%name ||:
%post_service %name

%post mysql
rm -f %_sbindir/%name
ln -s pure-ftpd-mysql %_sbindir/%name ||:
%post_service %name

%post pgsql
rm -f %_sbindir/%name
ln -s pure-ftpd-pgsql %_sbindir/%name ||:
%post_service %name

%preun light
%preun_service %name

%preun ldap
%preun_service %name

%preun mysql
%preun_service %name

%preun pgsql
%preun_service %name

%files common
%defattr(-, root, root)
%_bindir/pure-pw
%_bindir/pure-pwconvert
%_bindir/pure-statsdecode
%_sbindir/pure-config
%_sbindir/pure-ftpwho
%_sbindir/pure-uploadscript
%_sbindir/pure-mrtginfo
%_sbindir/pure-quotacheck
%_sbindir/pure-authd

%_sysconfdir/ftpallow
%_sysconfdir/ftpusers

%_man8dir/*

%dir %_sysconfdir/%name/vhost
%dir %_var/log/%name
%dir %_var/run/%name

%_defaultdocdir/%name-%version

%config %_initrddir/%name
%config(noreplace) %_sysconfdir/%name/%name.conf
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/pam.d/%name
%config(noreplace) %_sysconfdir/logrotate.d/%name
%config(noreplace) %_sysconfdir/xinetd.d/%name

%{?_with_tls: %ghost %attr(0600,root,root) %verify(not md5 size mtime) %config(missingok,noreplace) %_pemdir/%name.pem}

%files light
%_sbindir/pure-ftpd

%if_with ldap
%files ldap
%config(noreplace) %_sysconfdir/%name/pureftpd-ldap.conf
%_sbindir/pure-ftpd-ldap
%endif

%if_with mysql
%files mysql
%config(noreplace) %_sysconfdir/%name/pureftpd-mysql.conf
%_sbindir/pure-ftpd-mysql
%endif

%if_with pgsql
%files pgsql
%config(noreplace) %_sysconfdir/%name/pureftpd-pgsql.conf
%_sbindir/pure-ftpd-pgsql
%endif

%changelog
* Mon Dec 06 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.29-alt1.1
- rebuild with new libmysqlclient by request of libmysqlclient maintainer

* Tue Mar 23 2010 Afanasov Dmitry <ender@altlinux.org> 1.0.29-alt1
- 1.0.29

* Fri Feb 26 2010 Afanasov Dmitry <ender@altlinux.org> 1.0.28-alt1
- 1.0.28

* Sat Dec 19 2009 Afanasov Dmitry <ender@altlinux.org> 1.0.27-alt1
- 1.0.27

* Tue Nov 17 2009 Afanasov Dmitry <ender@altlinux.org> 1.0.26-alt1
- 1.0.26

* Thu Sep 03 2009 Afanasov Dmitry <ender@altlinux.org> 1.0.22-alt6
- rebuild pure-ftpd-ldap with libldap v2.4

* Sat Jun 06 2009 Afanasov Dmitry <ender@altlinux.org> 1.0.22-alt5
- remove executeble bit from /usr/share/doc files (closes: #20347)

* Mon May 18 2009 Afanasov Dmitry <ender@altlinux.org> 1.0.22-alt4
- fix initd script - use pure-config.
- add conflicts to common subpackage against old pure-ftpd.
- obsolete previous pure-ftpd in all subpackages.
- comment last print in config scripts

* Thu May 07 2009 Afanasov Dmitry <ender@altlinux.org> 1.0.22-alt3
- use pure-config.pl as service starter
- install pure-config.pl as pure-config
- don't use CAP_NET_ADMIN (fix: #19964)

* Tue May 05 2009 Afanasov Dmitry <ender@altlinux.org> 1.0.22-alt2
- split into four packages: light package, package with ldap, mysql and pgsql
  authentication scheme support. old pure-ftpd package is obsoleted.

* Mon Apr 27 2009 Afanasov Dmitry <ender@altlinux.org> 1.0.22-alt1
- 1.0.22
- update pure-ftpd-1.0.22-docs.patch

* Mon Dec 01 2008 Afanasov Dmitry <ender@altlinux.org> 1.0.21-alt1
- new version 1.0.21
- enable RFC 2640 (UTF-8 encoding for file names) support

* Thu Jan 12 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.19-alt1.1
- Rebuilt for new style PAM dependencies generated by rpm-build-4.0.4-alt55.

* Mon Jun 21 2004 Konstantin Klimchev <koka@altlinux.ru> 1.0.19-alt1
- new version 1.0.19
- comments master2.2 build

* Mon Apr 12 2004 Konstantin Klimchev <koka@altlinux.ru> 1.0.18-alt1
- disable xinetd server by default, using the standalone one

* Thu Mar 18 2004 Konstantin Klimchev <koka@altlinux.ru> 1.0.18-alt0.1
- add Sisyphus-style init-script
- add seperate build (Sisyphus vs Master)

* Fri Feb 27 2004 Konstantin Klimchev <koka@altlinux.ru> 1.0.17a-alt0.2
- return init-script (ALTM22-style). Sisyphus-style - TODO.
- add VHOST_PATH

* Tue Feb 3 2004 Konstantin Klimchev <koka@altlinux.ru> 1.0.17a-alt0.1
- initial build for Daedalus

* Mon Feb 2 2004 Konstantin Klimchev <koka@atvc.ru> 1.0.17a-2
- fixed path of ssl-cert file

* Wed Nov 26 2003 Konstantin Klimchev <koka@atvc.ru> 1.0.17a-1
- disabled standalone by default, using the xinetd server

* Tue Nov 18 2003 Konstantin Klimchev <koka@atvc.ru> 1.0.16c-2
- add %_sysconfdir/sysconfig/pure-ftpd

* Thu Nov 12 2003 Konstantin Klimchev <koka@atvc.ru> 1.0.16c-1
- 1.0.16c
- edit spec

* Wed Aug 13 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.0.16-1mdk
- 1.0.16

* Sat Jul 19 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.14-6mdk
- rebuild

* Sat Apr 19 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.0.14-5mdk
- use configure2_5x macro
- remove anonftp provides

* Wed Apr 02 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.14-4mdk
- rebuild against libmysql12

* Mon Feb 03 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.14-3mdk
- disable xinetd server by default, using the standalone one

* Mon Feb 03 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.14-2mdk
- source 3 : add xinetd support

* Mon Feb  3 2003 Laurent Culioli <laurent@pschit.net> 1.0.14-1mdk
- 1.0.14

* Tue Jan 16 2003 Laurent Culioli <laurent@pschit.net> 1.0.13a-1mdk
- 1.0.13a
- remove hardcoded packager tag

* Tue Dec 31 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.0.12-6mdk
- from Brook Humphrey <bah@webmedic.net> :
	- fixed anonymous users
	- fixed ftp user not being added to ftp groups

* Mon Sep  9 2002 Arnaud Desmons <adesmons@mandrakesoft.com> 1.0.12-5mdk
- fixed invalid-packager Laurent Culioli

* Fri Aug 23 2002 Laurent Culioli <laurent@pschit.net> 1.0.12-4mdk
- fix logrotate
- add --with-diraliases options

* Tue Aug 13 2002 Laurent Culioli <laurent@pschit.net> 1.0.12-3mdk
- add logrotate support

* Tue Jun 18 2002 Laurent Culioli <laurent@mandrakesoft.com> 1.0.12-2mdk
- add user-limit support
- add pure-ftpd.png

* Tue Jun 11 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.0.12-1mdk
- 1.0.12

* Fri Mar  8 2002 Laurent Culioli <laurent@mandrakesoft.com> 1.0.10-1mdk
- 1.0.10

* Fri Feb 22 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.0.9-1mdk
- 1.0.9

* Fri Jan 25 2002 Laurent Culioli <laurent@mandrakesoft.com> 1.0.8-3mdk
- really add postgresql support
- add extauth support
- add conflict with vsftpd

* Fri Jan 25 2002 Laurent Culioli <laurent@mandrakesoft.com> 1.0.8-2mdk
- add support for pgsql and virtual-chroot
- add mdkconf patch ( change _sysconfigdir from /etc to /etc/pure-ftpd )

* Fri Jan 25 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.0.8-1mdk
- 1.0.8

* Sun Dec 30 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.0.7-1mdk
- 1.0.7
- remove now integrated patch

* Tue Nov 13 2001 Laurent Culioli <laurent@mandrakesoft.com> 1.0.1-2mdk
- add BuildRequires

* Thu Nov  8 2001 Laurent Culioli <laurent@mandrakesoft.com> 1.0.1-1mdk
- updated to 1.0.1
- pam-support is back
- enabling virtual-user ( with puredb )
- patch config.pl to use the maxdiskusagepct option ( thanks to thomas.mangin@free.fr )
- update pure-ftpd.init
- clean specfile

* Wed Sep 19 2001 Laurent Culioli <laurent@mandrakesoft.com> 0.99.2a-1mdk
- updated to 0.99.2.a 

* Mon Sep 17 2001 Laurent Culioli <laurent@mandrakesoft.com> 0.99.2-2mdk
- fix files section

* Mon Sep 17 2001 Laurent Culioli <laurent@mandrakesoft.com> 0.99.2-1mdk
- updated to 0.99.2

* Sun Sep 02 2001 Laurent Culioli <laurent@mandrakesoft.com> 0.99.1b-5mdk
- fix

* Thu Aug 30 2001 Laurent Culioli <laurent@mandrakesoft.com> 0.99.1b-4mdk
- aarggh...fix changelog ( i'm jeune , i'm naif )

* Thu Aug 30 2001 Laurent Culioli <laurent@mandrakesoft.com> 0.99.1b-3mdk
- use pure-config.pl for pure-ftpd.init
- dont use -with-pam in configure

* Thu Aug 30 2001 Laurent Culioli <laurent@mandrakesoft.com> 0.99.1b-2mdk
- fix pure-ftpd.init

* Wed Aug 29 2001 Laurent Culioli <laurent@mandrakesoft.com> 0.99.1b-1mdk
- first mandrake package
