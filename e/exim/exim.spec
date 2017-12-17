# Conditional build:
%def_with pgsql	# with PostgreSQL support
%def_with mysql	# with MySQL support
%def_with ldap	# with LDAP support
%def_with heavy	# with all features included

%define ftpurl ftp://ftp.exim.org/pub/exim/exim4
%define openssldir /var/lib/ssl

Name: exim
Version: 4.84
Release: alt1.1.1.1.1

Summary: Exim Mail Transport Agent
License: GPLv2+
Group: System/Servers

Packager: Anton Gorlov <stalker@altlinux.ru>

URL: http://www.exim.org/
Source0: %ftpurl/exim-%version.tar.bz2

Source7: %ftpurl/config.samples.tar.bz2

Source9: exim.init
Source10: exim.logrotate
Source101: exim.sysconfig
Source11: eximon.desktop
Source12: exim_aliases
Source13: exim.aliases
Source14: exim.cron
Source15: eximclean
Source18: exim.pam
Source19: exim-altdefault.conf
Source21: eximon.conf
Source22: exim-addMakefile.heavy
Source23: exim-addMakefile.ldap
Source24: exim-addMakefile.mysql
Source25: exim-addMakefile.pgsql
Source26: exim-addMakefile.light
Source31: oview.txt
Source32: oview.ps
Source33: oview.pdf
Source34: oview.texinfo
Source36: README.ALT

Source38: eximon.png
Source43: smtpauthpwd

Patch1: exim-4.84-buildoptions.patch
Patch3: exim-4.34-texinfo.patch
Patch4: exim-4.76-pcre.patch
Patch5: CVE-2012-5671.patch

# Automatically added by buildreq on Tue Apr 26 2011
# ...and edited:
# - to move non-core dependencies to separate lines
# - to separate versioned build requirements
# optimized out: libICE-devel libSM-devel libX11-devel libXmu-devel libXt-devel libcom_err-devel libkrb5-devel libpq-devel xorg-xproto-devel
BuildRequires: libXaw-devel libXext-devel libdb4-devel libpam-devel libpcre-devel libsqlite3-devel libssl-devel libwrap-devel perl-devel

BuildRequires: libspf2-devel > 1.0.4
BuildRequires: libsrs_alt-devel > 0.5

BuildRequires: perl-Pod-Parser

# needed for all builds except -light
BuildRequires: libwhoson-devel libsasl2-devel

# comment next line if you build --without ldap
BuildRequires: libldap-devel

# comment next line if you build --without mysql
BuildRequires: libmysqlclient-devel

# comment next line if you build --without pgsql
BuildRequires: postgresql-devel libpq-devel

# comment next line if you build --without heavy
BuildRequires: libldap-devel libMySQL-devel postgresql-devel libpq-devel

# package %name is virtual package. It depends on exim-common and exim-light
Requires: %name-common = %version-%release
Requires: %name-light = %version-%release

%description 
Smail like Mail Transfer Agent with single configuration file.
Features: flexible retry algorithms, header & envelope rewriting,
multiple deliveries down single connection or multiple deliveries in
parallel, regular expressions in configuration parameters, file
lookups, supports sender and/or reciever verification, selective
relaying, supports virtual domains, built-in mail filtering and can be
configured to drop root privilleges when possible.
It is virtual package. It requires an exim-common and exim-light

%package common
Summary: Exim MTA
Group: System/Servers

Provides: smtpdaemon, smtpd, MTA, MailTransferAgent
#Requires: exim-mta
#Requires: perl-base libpam0 libwrap libdb4.2 libssl
# libwhoson whoson-server
Requires: exim-control
Requires: sendmail-common
# Required for generation of certificates at install time
Requires(post): openssl

%description common
Smail like Mail Transfer Agent with single configuration file.
Features: flexible retry algorithms, header & envelope rewriting,
multiple deliveries down single connection or multiple deliveries in
parallel, regular expressions in configuration parameters, file
lookups, supports sender and/or reciever verification, selective
relaying, supports virtual domains, built-in mail filtering and can be
configured to drop root privilleges when possible.

%package monitor
Summary: Exim - Exceptional Internet Mailer - X mail monitor
Group: Monitoring
Requires: %name-common = %version-%release

%description monitor
X Window based monitor & administration utility for the Exim Mail
Transfer Agent.

%package light
Summary: Main exim MTA program, compiled with basic libraries
Group: System/Servers
Provides: exim-mta, smtpd, smtpdaemon
Provides: %name-light = %version-%release
Provides: /usr/sbin/exim
Conflicts: exim-mysql, exim-pgsql, exim-heavy, exim-ldap
PreReq:	%name-common = %version-%release

%description light
The main exim MTA program, compiled with all basic dbm lookups support,
TLS (SSL) and all the main transports.  This should suit all general
purpose systems, and is the smallest binary.

%package mysql
Summary: Main exim MTA program, compiled with basic libraries + perl + mysql
Group: System/Servers
Provides: exim-mta
Provides: /usr/sbin/exim
Conflicts: exim-light,  exim-pgsql, exim-heavy, exim-ldap
PreReq:	%name-common = %version-%release

Requires(post,preun): %__subst

%description mysql
The main exim MTA program, compiled with all basic dbm lookups support,
TLS (SSL) and all the main transports, plus embedded perl support
and mysql db lookup support.

%package pgsql
Summary: Main exim MTA program, compiled with basic libraries + perl + pgsql
Group: System/Servers
Provides: exim-mta
Provides: /usr/sbin/exim
Conflicts: exim-light, exim-mysql, exim-heavy, exim-ldap
PreReq:	%name-common = %version-%release

%description pgsql
The main exim MTA program, compiled with all basic dbm lookups support,
TLS (SSL), LDAP and all the main transports, plus embedded perl support
and postgresql lookups.

%package heavy
Summary: Main exim MTA program, compiled with basic libraries + perl + pgsql + MySQL
Group: System/Servers
Provides: exim-mta, smtpd, smtpdaemon
Provides: %name-heavy = %version-%release
Provides: /usr/sbin/exim
Conflicts: exim-light, exim-pgsql, exim-mysql, exim-ldap
PreReq:	%name-common = %version-%release

%description heavy
The main exim MTA program, compiled with all basic dbm lookups support,
TLS (SSL), LDAP and all the main transports, plus embedded perl support
and postgresql and MySQL lookups.

%package ldap
Summary: Main exim MTA program, compiled with basic libraries + perl + ldap
Group: System/Servers
Provides: exim-mta
Provides: /usr/sbin/exim
Conflicts: exim-light, exim-mysql, exim-heavy, exim-pgsql
PreReq:	%name-common = %version-%release

%description ldap
The main exim MTA program, compiled with all basic dbm lookups support,
TLS (SSL), LDAP and all the main transports, plus embedded perl support.

%package utils
Summary: Misc utils for debugging exim
Group: System/Servers
Requires: exim-mta

BuildArch: noarch

%description utils
Misc utils for debugging exim.

%prep
%setup -n exim-%version

cp %SOURCE7 %SOURCE31 %SOURCE32 %SOURCE33 %SOURCE34 %SOURCE36 doc/

install -d Local

%patch1 -p1
# temporarily suspended
#patch3 -p1

#patch4 -p1
#patch5 -p1

install %SOURCE21 Local/eximon.conf

%build
# we build several versions here...
mkdir -p bins
versions="light"
%if_with ldap
versions="ldap $versions"
%endif
%if_with mysql
versions="mysql $versions"
%endif
%if_with pgsql
versions="pgsql $versions"
%endif
%if_with heavy
versions="heavy $versions"
%endif

%define compiledir build-`scripts/os-type`-`scripts/arch-type`

 sed -i 's#MYLIBDIR#%{_libdir}#g' src/EDITME

for version in $versions
do
 sed -i 's#MYLIBDIR#%{_libdir}#g' %_sourcedir/exim-addMakefile.$version
 cat src/EDITME %_sourcedir/exim-addMakefile.$version >Local/Makefile
 make CFLAGS="-I/usr/include/pcre $RPM_OPT_FLAGS -DLDAP_DEPRECATED" FULLECHO='' EXIM_CHMOD=''
 cp %compiledir/exim bins/exim-$version
done

%install
install -d %buildroot{%_bindir,%_sbindir,%_man8dir,%_libdir} \
	%buildroot%_var/{spool/exim/{db,input,msglog},log/exim}

install bins/exim* %buildroot/usr/sbin

install %compiledir/exim_{fixdb,tidydb,dbmbuild,dumpdb,lock} \
	%compiledir/exi{cyclog,next,what} %SOURCE12 %SOURCE15 \
	util/{cramtest.pl,logargs.sh,unknownuser.sh} \
	%compiledir/{exigrep,exim_checkaccess,eximstats,exipick,exiqsumm,exiqgrep} \
	%buildroot%_bindir
install %compiledir/eximon.bin %buildroot%_bindir
install %compiledir/eximon %buildroot%_bindir

install -pD -m755 %_sourcedir/exim.cron %buildroot/etc/cron.daily/exim
install -pD -m755 %_sourcedir/exim.init %buildroot/etc/rc.d/init.d/exim
install -pD -m644 %_sourcedir/exim.sysconfig %buildroot/etc/sysconfig/exim
install	-pD -m644 %_sourcedir/exim.logrotate %buildroot/etc/logrotate.d/exim
install -pD -m644 %_sourcedir/exim.pam %buildroot/etc/pam.d/exim
install -pD -m644 %_sourcedir/exim-altdefault.conf %buildroot/etc/exim/exim.conf
install -pD -m644 %_sourcedir/smtpauthpwd %buildroot/etc/exim/smtpauthpwd
install -pD -m644 doc/exim.8 %buildroot%_man8dir/exim.8

#install %{SOURCE13} %buildroot%{_sysconfdir}/exim/aliases

#ln -sf %{_bindir}/exim %buildroot%{_sbindir}/exim
ln -sf %_sbindir/exim %buildroot%_sbindir/sendmail
#ln -sf %{_sbindir}/exim %buildroot%{_libdir}/sendmail
#ln -sf %_sbindir/exim %buildroot%_sbindir/mailq
ln -sf %_sbindir/exim %buildroot%_sbindir/rsmtp
ln -sf %_sbindir/exim %buildroot%_sbindir/rmail
ln -sf %_sbindir/exim %buildroot%_sbindir/runq

install -pD -m644 %_sourcedir/eximon.desktop %buildroot%_desktopdir/eximon.desktop
install -pD -m644 %_sourcedir/eximon.png %buildroot%_liconsdir/eximon.png

touch %buildroot%_sysconfdir/%name/aliases
ln -sf  %_sysconfdir/%name/aliases %buildroot%_sysconfdir/aliases

pod2man --center=EXIM --section=8 \
	%buildroot%_bindir/eximstats \
	%buildroot%_man8dir/eximstats.8
pod2man --center=EXIM --section=8 \
	%buildroot%_bindir/exipick \
	%buildroot%_man8dir/exipick.8

# generate ghost .pem files
mkdir -p %buildroot%openssldir/{certs,private}
touch %buildroot%openssldir/{certs,private}/exim.pem
chmod 600 %buildroot%openssldir/{certs,private}/exim.pem

%post common
#post_service exim
ALIASES=%_sysconfdir/%name/aliases /usr/share/sendmail-common/rebuild_aliases
#exim_aliases
chown -R mail:mail /var/spool/exim/{db,input,msglog} /var/log/exim

if [ ! -f %openssldir/certs/exim.pem ] ; then
  umask 077
  FQDN=`hostname`
  if [ "x${FQDN}" = "x" ]; then
    FQDN=localhost.localdomain
  fi
  cat << EOF | openssl req -new -x509 -days 365 -nodes -out %openssldir/certs/exim.pem -keyout %openssldir/private/exim.pem 2>/dev/null
--
SomeState
SomeCity
SomeOrganization
SomeOrganizationalUnit
${FQDN}
root@${FQDN}
EOF
chown mail.mail %openssldir/{private,certs}/exim.pem
chmod 600 %openssldir/{private,certs}/exim.pem
fi

%preun common
%preun_service exim

%post light
ln -sf /usr/sbin/exim-light /usr/sbin/exim
%post_service exim

%preun light
%preun_service exim

%if_with mysql
%post mysql
ln -sf /usr/sbin/exim-mysql /usr/sbin/exim
%post_service exim

%preun mysql
%preun_service exim
%endif

%if_with pgsql
%post pgsql
ln -sf /usr/sbin/exim-pgsql /usr/sbin/exim
%post_service exim

%preun pgsql
%preun_service exim
%endif

%if_with heavy
%post heavy
ln -sf /usr/sbin/exim-heavy /usr/sbin/exim
%post_service exim

%preun heavy
%preun_service exim
%endif

%if_with ldap
%post ldap
ln -sf /usr/sbin/exim-ldap /usr/sbin/exim
%post_service exim

%preun ldap
%preun_service exim
%endif

%files

%files common
%doc ACKNOWLEDGMENTS NOTICE README.UPDATING
%doc doc/{README.SIEVE,ChangeLog,NewStuff,dbm.discuss.txt,filter.txt,oview.txt,spec.txt}
%doc doc/experimental-spec.txt
%doc doc/{OptionLists.txt,config.samples.tar.bz2}
#%doc util/transport-filter.pl

%config(noreplace) %_sysconfdir/exim/exim.conf
%attr(400,mail,mail) %config(noreplace) %_sysconfdir/exim/smtpauthpwd
%ghost %attr( 644,root,root) %config(noreplace) %_sysconfdir/exim/aliases
%_sysconfdir/aliases
%config(noreplace) /etc/sysconfig/exim
%config(noreplace) /etc/logrotate.d/exim
%config %_initdir/exim
%config(noreplace) /etc/pam.d/exim
%config /etc/cron.daily/exim
%attr(0600,root,root) %ghost %config(missingok,noreplace) %verify(not md5 size mtime) %openssldir/certs/exim.pem
%attr(0600,root,root) %ghost %config(missingok,noreplace) %verify(not md5 size mtime) %openssldir/private/exim.pem
#%attr(4755,exim,exim) %{_bindir}/exim

%_bindir/exim_*
%_bindir/exinext
%_bindir/exiwhat
%_bindir/exicyclog
%_bindir/exigrep
%_bindir/eximstats
%_bindir/exiqsumm
%_bindir/exiqgrep
#%attr( 755,root,root) %{_sbindir}/exim
#_sbindir/mailq
%_sbindir/rmail
%_sbindir/rsmtp
%_sbindir/runq
%_sbindir/sendmail
%_man8dir/*

%attr(770,root,mail) %dir %_var/spool/exim
%attr(750,mail,mail) %dir %_var/spool/exim/db
%attr(700,mail,mail) %dir %_var/spool/exim/input
%attr(750,mail,mail) %dir %_var/spool/exim/msglog
%attr(750,mail,mail) %dir %_var/log/exim

%files monitor
%_bindir/eximon*
%_desktopdir/*
%_liconsdir/*

%files light
%attr(4711,root,root)/usr/sbin/exim-light
#%ghost /usr/sbin/exim


%if_with mysql
%files mysql
%attr(4711,root,root)/usr/sbin/exim-mysql
#%ghost /usr/sbin/exim
%endif

%if_with pgsql
%files pgsql
%attr(4711,root,root)/usr/sbin/exim-pgsql
#%ghost /usr/sbin/exim
%endif

%if_with ldap
%files ldap
%attr(4711,root,root)/usr/sbin/exim-ldap
#%ghost /usr/sbin/exim
%endif


%if_with heavy
%files heavy
%attr(4711,root,root)/usr/sbin/exim-heavy
#%ghost /usr/sbin/exim
%endif

%files utils
%_bindir/cramtest.pl
%_bindir/logargs.sh
%_bindir/unknownuser.sh
%_bindir/eximclean
%_bindir/exipick

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 4.84-alt1.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 4.84-alt1.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 4.84-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 4.84-alt1.1
- rebuild with new perl 5.20.1

* Tue Nov 04 2014 Anton Gorlov <stalker@altlinux.ru> 4.84-alt1
- 4.84

* Sun May 18 2014 Anton Gorlov <stalker@altlinux.ru> 4.82-alt1
- 4.82 

* Sun May 18 2014 Anton Gorlov <stalker@altlinux.ru> 4.76-alt6
- fix libdir in Makefiles
- fix perl core path

* Mon Sep 23 2013 Sergey Y. Afonin <asy@altlinux.ru> 4.76-alt5
- NMU: rebuilt with cyrus-sasl 2.1.26

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 4.76-alt4
- built for perl 5.18

* Tue Mar 19 2013 Michael Shigorin <mike@altlinux.org> 4.76-alt3
- NMU:
  + applied CVE-2012-5671.patch
  + dropped mailq symlink duplicating sendmail-common's one (ALT#28006)

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 4.76-alt2
- rebuilt for perl-5.16

* Sun Oct 16 2011 Alexey Tourbin <at@altlinux.ru> 4.76-alt1.1
- rebuilt for perl-5.14

* Tue May 10 2011 Victor Forsiuk <force@altlinux.org> 4.76-alt1
- 4.76 (fixes CVS-2011-1764).

* Tue Apr 26 2011 Victor Forsiuk <force@altlinux.org> 4.75-alt1
- 4.75

* Tue Apr 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.72-alt1.2
- fix build

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 4.72-alt1.1
- rebuilt with perl 5.12

* Tue Jul 06 2010 Victor Forsiuk <force@altlinux.org> 4.72-alt1
- 4.72

* Thu Sep 24 2009 ALT QA Team Robot <ldv@altlinux.org> 4.69-alt1.1.1.1
- Automated blind dumb rebuild with libldap-devel-2.4.16-alt4.4.

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 4.69-alt1.1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Sat Jun 14 2008 ALT QA Team Robot <qa-robot@altlinux.org> 4.69-alt1.1
- Automated rebuild with libdb-4.7.so.

* Mon Mar 24 2008 Victor Forsyuk <force@altlinux.org> 4.69-alt1
- 4.69
- Docs now will be built from separate source rpm.

* Thu Apr 26 2007 Victor Forsyuk <force@altlinux.org> 4.67-alt1
- 4.67.
- Remove Conflicts with other MTAs.
- Drop all ancient Obsoletes.
- Drop FAQ from distribution (it was getting obsolete and author strongly
  suggests to use exim wiki instead).

* Fri Mar 30 2007 ALT QA Team Robot <qa-robot@altlinux.org> 4.66-alt2.0
- Rebuilt due to libpq.so.4 -> libpq.so.5 soname change.

* Tue Mar 27 2007 Victor Forsyuk <force@altlinux.org> 4.66-alt2
- Relax build requirements to facilitate rebuild with new postgresql version
  (libpq4-devel --> libpq-devel).

* Thu Jan 18 2007 Victor Forsyuk <force@altlinux.org> 4.66-alt1
- 4.66, with updated docs.

* Thu Oct 19 2006 Victor Forsyuk <force@altlinux.org> 4.63-alt1
- 4.63, with updated docs.

* Tue Jun 20 2006 Victor Forsyuk <force@altlinux.ru> 4.62-alt1
- 4.62
- No need to -HUP daemon when rotating logs.
- Remove old explicit PreReq'ed deps on external libraries.

* Mon Jun 12 2006 ALT QA Team Robot <qa-robot@altlinux.org> 4.60-alt1.1
- Rebuilt with libldap-2.3.so.0.

* Wed Nov 30 2005 Victor Forsyuk <force@altlinux.ru> 4.60-alt1
- 4.60
- Get rid of %%_x11bindir.
- Remove unneeded (and erroneous) explicit Requires in exim-common.

* Mon Oct 10 2005 Victor Forsyuk <force@altlinux.ru> 4.54-alt1
- 4.54.
- Build all flavours with sqlite lookups (yes, even -light).
- Generate man pages (from pod) for eximstats and exipick.
- Fix spec bug that caused failed build on non-ix86 arches.

* Tue Jul 12 2005 Victor Forsyuk <force@altlinux.ru> 4.52-alt1
- 4.52.
- Update default config: add commented CSA check, uncomment support of
  "local part suffixes".

* Wed May 18 2005 Victor Forsyuk <force@altlinux.ru> 4.51-alt1
- 4.51.
- Exiscan now integrated into main source tree.
- Build against postgresql8 libs.
- Add DomainKeys support.

* Thu Feb 10 2005 ALT QA Team Robot <qa-robot@altlinux.org> 4.44-alt1.1
- Updated libdb4 build dependencies.
- Rebuilt with libdb4.3.

* Mon Jan 17 2005 Victor Forsyuk <force@altlinux.ru> 4.44-alt1
- 4.44
- Add SPF and SRS support.
- Autogeneration of certificates for encrypted connections at install time
  (so, now we need openssl package at install time).

* Tue Jan 04 2005 Victor Forsyuk <force@altlinux.ru> 4.43-alt1
- New version.
- Fix buffer overflows in host_aton() and SPA authentication (patch from RH).
- Remove whoson support from -light build.

* Tue Aug 31 2004 Victor Forsyuk <force@altlinux.ru> 4.42-alt1
- New version.
- Remove service restarting from exim package (this is just meta-package
  that contains no files).

* Tue Jun 15 2004 Stanislav Ievlev <inger@altlinux.org> 4.34-alt1.1
- NMU: /etc/aliases not under alternatives control

* Sun May 23 2004 Victor Forsyuk <force@altlinux.ru> 4.34-alt1
- Build with system libpcre.
- exipick now included in exim distribution.
- Fixed texinfo docs.

* Mon Mar 15 2004 Victor V Ismakaev <ivv@altlinux.ru> 4.30-alt3
- change package naming
- Updated exiscan to 4.30-16.
- added some config options to default config

* Thu Feb 19 2004 Victor Forsyuk <force@altlinux.ru> 4.30-alt2
- Updated exiscan to 4.30-15.
- Migrate from %%define's to %%def_with logic.
- Migrate to %%post_service.
- Remove zero-sized /var/log/exim/* files from package!
- Added install-time requirement for update-alternatives.
- Added exipick utility to -utils package.
- Added tidying of callout database to cron script and run it daily
  instead of weekly.

* Thu Dec 04 2003 Victor V Ismakaev <ivv@altlinux.ru> 4.30-alt1.1
- fixes in %files and %post sections

* Thu Dec 04 2003 Victor V Ismakaev <ivv@altlinux.ru> 4.30-alt1
- rebuild with new exiscan-acl-4.30-14.patch

* Wed Dec 03 2003 Victor V Ismakaev <ivv@altlinux.ru> 4.30-alt0.1
- new version 4.30
- added whoson support
- ldap support moved from exim-base subpackage to exim-ldap subpackage
- added saslauthd auth

* Fri Sep 05 2003 Victor Forsyuk <force@altlinux.ru> 4.22-alt0.1
- New version (FAQ and config samples also updated).
- Migrate from user `exim' to `mail'.
- Change ownership of spool and log files to user 'mail' in postinstall
  script.
- Cleaned up weekly cron script.
- Optimized logrotate script.
- Fix mistake in upstream cramtest.pl fixing. :)
- Clean unneeded things from spec (default attrs in filelists, etc).
- Mark logrotate script as %%config file.
- Add exiqgrep to package.
- Drop dependancy on MDA (provided by procmail). Exim itself can
  deliver mail to local users.
- Fix exim-base build (it was by mistake made identical to exim-mysql).
- Add dependancy on exim-mta to main package.

* Wed Jul 30 2003 Victor V Ismakaev <ivv@altlinux.ru> 4.20-alt0.6
- applied patch exiscan-09

* Tue Jul 01 2003 Victor V Ismakaev <ivv@altlinux.ru> 4.20-alt0.5
- some fix's in exim scripts

* Mon Jun 09 2003 Victor V Ismakaev <ivv@altlinux.ru> 4.20-alt0.4
- rebuild with libdb4.1

* Thu Jun 05 2003 Victor V Ismakaev <ivv@altlinux.ru> 4.20-alt0.3
- fixing file permissions on exim's binary files

* Wed Jun 04 2003 Victor V Ismakaev <ivv@altlinux.ru> 4.20-alt0.2
- rebuild with libdb4.0
- fixing spec

* Mon Jun 02 2003 Victor V Ismakaev <ivv@altlinux.ru> 4.20-alt0.1
- first release for ALTLinux
