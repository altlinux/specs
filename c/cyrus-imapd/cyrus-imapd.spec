%define _cyrususer cyrus
%define _cyrusgroup cyrus
%define _vardata %_var/lib/imap
%define _spooldata %_var/spool/imap
%define _cyrexecdir %_libexecdir/cyrus
%define _confdir master/conf
%define _contribdir %_datadir/%name/contrib
%define _cyrusconf %_confdir/prefork.conf

Name: cyrus-imapd
Version: 2.4.12
Release: alt1.1

Summary: A high-performance mail store with IMAP and POP3 support
License: CMU License
Group: System/Servers

# old import was made by:
# $ git-cvsimport -v -r git-cvs -i -k -d :pserver:anoncvs@cvs.andrew.cmu.edu:/cvs cyrus
# fresh sources available via git at git://git.cyrusimap.org/cyrus-imapd/
Url: http://www.cyrusimap.org/

Source0: %name-%version.tar
Source1: cyrus-procmailrc
Source2: cyrus-user-procmailrc.template
Source3: %name.logrotate
Source4: %name.imap-2.1.x-conf
Source5: README.ALT
Source6: %name.control
Source7: %name.pam-config
Source8: %name-procmail+cyrus.mc
Source10: %name.sysconfig
Source11: %name.cvt_cyrusdb_all
Source12: %name.magic
Source13: %name.sasl-conf
Source14: %name.cron-daily
Source16: folderxfer
Source17: imapcreate.pl
Source18: inboxfer
Source19: %name-README.HOWTO-recover-mailboxes.db
Source20: %name-sendmail-8.12.9-cyrusv2.m4
Source21: %name.init

#Patch7: http://servercc.oakton.edu/~jwade/cyrus/cyrus-imapd-2.1.3/cyrus-imapd-2.1.3-flock.patch

PreReq: e2fsprogs /sbin/chkconfig /sbin/service cert-sh-functions
Requires: su
Provides: MDA imap IMAPD POP3D

BuildRequires: control flex gcc-c++ groff-extra groff-ps libdb4-devel libldap-devel libsasl2-devel
BuildRequires: libssl-devel perl-Pod-Parser perl-Term-ReadLine-Gnu perl-devel transfig zlib-devel
BuildRequires: libwrap-devel libnet-snmp-devel libnl-devel libsensors3-devel

%description
The %name package contains the core of the Cyrus IMAP server.
It is a scaleable enterprise mail system designed for use from
small to large enterprise environments using standards-based
internet mail technologies.

A full Cyrus IMAP implementation allows a seamless mail and bulletin
board environment to be set up across multiple servers. It differs from
other IMAP server implementations in that it is run on "sealed"
servers, where users are not normally permitted to log in. The mailbox
database is stored in parts of the filesystem that are private to the
Cyrus IMAP server. All user access to mail is through software using
the IMAP, POP3, or KPOP protocols. TLSv1 and SSL are supported for
security.

%package murder
Group: System/Servers
Summary: Cyrus IMAP server murder aggregator system files
Requires: %name = %version-%release

%description murder
The %name-murder package contains the Cyrus murder aggregator system,
i.e. IMAP, POP3 and LMTP proxies, and the mupdate mailbox master daemon.
It allows for cluster setups where there are many backend Cyrus spools
and frontend proxy servers.

%package ldap
Group: System/Servers
Summary: Cyrus IMAP server ldap auth system
Requires: %name = %version-%release

%description ldap
The %name-ldap package contains the Cyrus ldap auth system.

%package devel
Group: Development/C
Summary: Cyrus IMAP server development files

%description devel
The %name-devel package contains header files and libraries
necessary for developing applications which use the imclient library.

%package -n perl-Cyrus
Group: Development/Perl
Summary: Cyrus IMAP server utility Perl modules
Provides: perl(Cyrus/IMAP.pm) perl(Cyrus/IMAP/Admin.pm)

%description -n perl-Cyrus
The perl-Cyrus package contains Perl modules necessary to use the
Cyrus IMAP server administration utilities.

%package utils
Group: System/Servers
Summary: Cyrus IMAP server administration utilities
Requires: perl-Cyrus = %version-%release perl(Term/ReadLine.pm)

%description utils
The %name-utils package contains administrative tools for the
Cyrus IMAP server. It can be installed on systems other than the
one running the server.

%package doc
Group: System/Servers
Summary: Cyrus IMAP server documentation
BuildArch: noarch

%description doc
The %name-doc package contains Here the documentation about
Cyrus IMAP server.

%prep
%setup

%build
# kerberos include is needed (because of openssl-0.9.7 ?)
CPPFLAGS="`krb5-config --cflags` $CPPFLAGS"
export CPPFLAGS
CFLAGS="$RPM_OPT_FLAGS -fPIC $CFLAGS"
export CFLAGS
LDFLAGS="`krb5-config --libs` $LDFLAGS"
export LDFLAGS

pushd makedepend
./configure
make
popd

aclocal -I cmulocal
autoheader
autoconf

# this is hack
echo '#define CYRUS_CVSDATE 20071211' > imap/xversion.h

%configure \
  --enable-netscapehack \
  --enable-listext \
  --enable-nntp \
  --enable-murder \
  --with-snmp \
  --with-perl=perl \
  --with-ldap \
  --with-libwrap=%prefix \
  --with-cyrus-prefix=%_cyrexecdir \
  --with-service-path=%_cyrexecdir \
  --with-cyrus-user=%_cyrususer \
  --with-cyrus-group=%_cyrusgroup \
  --with-auth=unix \
  --enable-idled \
  --with-bdb-incdir=%_includedir/db4 \
  --with-devrandom=/dev/urandom \
  --enable-replication

#  --with-krb=%prefix/lib/krb5

make

# produce doc/man
make -C doc -f Makefile.dist dist

# Modify docs master --> cyrus-master
pushd man
  sed -i 's/master(8)/cyrus-master(8)/' *5 *8
popd
pushd doc
  sed -i 's/master/cyrus-master/g' man.html
popd
pushd doc/man
  sed -i 's/master(8)/cyrus-master(8)/' *html
popd

# Modify path in perl scripts
find . -type f -name \*.pl -print0 |
    xargs -r0 perl -pi -e 's@\/usr\/local\/bin\/perl@perl@' --

# Cleanup of doc dir
find doc perl -name CVS -type d | xargs -r rm -fr --
find doc -name "*~" -type f | xargs -r rm -f --
rm -f doc/Makefile.dist
rm -f doc/text/htmlstrip.c

%install
# Do what the regular make install does
make install DESTDIR=%buildroot PREFIX=%prefix mandir=%_mandir \
	INSTALLDIRS=vendor
make -C man install DESTDIR=%buildroot PREFIX=%prefix mandir=%_mandir

install -m 755 imtest/imtest		%buildroot%_cyrexecdir/
install -m 755 perl/imap/cyradm	%buildroot%_cyrexecdir/

# Install tools
for tool in tools/* ; do
  test -f ${tool} && install -m 755 ${tool} %buildroot%_cyrexecdir/
done

install -d \
  %buildroot%_sysconfdir/{rc.d/init.d,logrotate.d,pam.d,sysconfig,cron.daily} \
  %buildroot%_libdir/sasl2 \
  %buildroot%_bindir \
  %buildroot%_spooldata/stage. \
  %buildroot%_vardata/{user,quota,proc,log,msg,socket,db,sieve,rpm,backup} \
  %buildroot%_contribdir \
  %buildroot%_datadir/%name/rpm

install -m 755 %SOURCE11   %buildroot%_cyrexecdir/cvt_cyrusdb_all
install -m 755 %SOURCE12   %buildroot%_datadir/%name/rpm/magic

install -m 644 %_cyrusconf %buildroot%_sysconfdir/cyrus.conf
install -m 644 %SOURCE4    %buildroot%_sysconfdir/imapd.conf
install -m 644 %SOURCE7    %buildroot%_sysconfdir/pam.d/pop
install -m 644 %SOURCE7    %buildroot%_sysconfdir/pam.d/imap
install -m 644 %SOURCE7    %buildroot%_sysconfdir/pam.d/sieve
install -m 644 %SOURCE7    %buildroot%_sysconfdir/pam.d/mupdate
install -m 644 %SOURCE7    %buildroot%_sysconfdir/pam.d/lmtp
install -m 644 %SOURCE10   %buildroot%_sysconfdir/sysconfig/%name

install -m 755 %SOURCE21    %buildroot%_initdir/%name
install -m 644 %SOURCE3    %buildroot%_sysconfdir/logrotate.d/%name
install -m 755 %SOURCE14   %buildroot%_sysconfdir/cron.daily/%name
install -pDm600 %SOURCE13 %buildroot%_sysconfdir/sasl2/Cyrus.conf

install -m 755 -d doc/conf
install -m 644 %_confdir/*.conf doc/conf/
install -pD -m 755 %SOURCE6 %buildroot%_controldir/%name

install -m 755 %SOURCE16 %SOURCE17 %SOURCE18  %buildroot%_contribdir
install -m 644 %SOURCE19 %SOURCE20 %SOURCE5 doc/

# Rename 'master' binary and manpage to avoid crash with postfix
mv -f %buildroot%_cyrexecdir/master	%buildroot%_cyrexecdir/cyrus-master
mv -f %buildroot%_mandir/man8/master.8 %buildroot%_mandir/man8/cyrus-master.8
mv -f doc/man/master.8.html doc/man/cyrus-master.8.html

# Move utilites from /usr/libexec/cyrus to /usr/bin
for i in arbitronsort.pl cyradm imtest mupdate-loadgen.pl convert-sieve.pl \
	 mknewsgroups config2header config2man masssievec
do
    mv %buildroot%_cyrexecdir/$i %buildroot/%_bindir/
done

# Create filelist for perl package, compress manpages before
[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress
find %buildroot%perl_vendor_autolib/Cyrus %buildroot%perl_vendor_archlib/Cyrus -type f -print |
  sed "s@^%buildroot@@g" |
  grep -v perllocal.pod |
  grep -v "\.bs" |
  grep -v "\.packlist" > perl-Cyrus-%version-filelist
if [ "$(cat perl-Cyrus-%version-filelist)X" = "X" ] ; then
  echo "ERROR: EMPTY FILE LIST"
  exit -1
fi

# Remove installed but not packaged files
rm -f %buildroot%_cyrexecdir/not-mkdep
find %buildroot -name "perllocal.pod" -exec rm -f {} \;
find %buildroot -name ".packlist" -exec rm -f {} \;

# Create file wich contains information about compiled db backends
for conf in DUPLICATE MBOX SEEN SUBS TLS
do
  echo CONFIG_DB_${conf}=$(grep "CONFIG_DB_${conf}" config.h | sed -e 's/)//' -e 's/_/-/g' | cut -d" " -f3 | cut -d"-" -f2) >> %buildroot%_datadir/%name/rpm/db.cfg
done

# directory for ssl-certs
install -dm750 %buildroot%_vardata/ssl

# imap sessions logs
mkdir -p %buildroot%_vardata/log/cyrus

# needed for %ghost
touch %buildroot%_vardata/ssl/cyrus.cert
touch %buildroot%_vardata/ssl/cyrus.key

%add_findreq_skiplist /usr/bin/cyradm

%pre
/usr/sbin/groupadd -r -f %_cyrusgroup ||:
/usr/sbin/useradd -g %_cyrusgroup -G sasl -c "Cyrus IMAP Server" -d %_vardata \
  -s /dev/null -r %_cyrususer 2> /dev/null ||:

%post
%post_service %name
# Force synchronous updates, usually only on ext2 filesystems
for i in %_vardata/{user,quota} %_spooldata
do
	fstype=`find $i -maxdepth 0 -printf %%F`
	[ x"$fstype" = x"ext2" ] && chattr -R +S $i 2>/dev/null ||:
done

%preun
%preun_service %name

%files
# initscript
%_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name

# other stuff
%config %_controldir/*
%config(noreplace) %_sysconfdir/logrotate.d/%name
%config(noreplace) %_sysconfdir/cron.daily/%name

# cyrus configs
%config(noreplace) %_sysconfdir/cyrus.conf
%config(noreplace) %_sysconfdir/imapd.conf
%config(noreplace) %_sysconfdir/pam.d/imap
%config(noreplace) %_sysconfdir/pam.d/lmtp
%config(noreplace) %_sysconfdir/pam.d/pop
%config(noreplace) %_sysconfdir/pam.d/sieve
%config(noreplace) %attr(640,root,%_cyrusgroup) %_sysconfdir/sasl2/Cyrus.conf

# suid deliver
%attr(4710,%_cyrususer,%_cyrusgroup) %_cyrexecdir/deliver

# data dirs
%dir %attr(1770,root,%_cyrusgroup) %_vardata
%dir %attr(1770,root,%_cyrusgroup) %_vardata/*
%dir %attr(1770,root,%_cyrusgroup) %_vardata/log/*
%dir %attr(1770,root,%_cyrusgroup) %_spooldata
%dir %attr(1770,root,%_cyrusgroup) %_spooldata/*

%_datadir/%name
%_man5dir/*
%_man8dir/*

# ssl-related
%dir %attr(0750,root,%_cyrusgroup) %_vardata/ssl
%ghost %attr(0640,root,%_cyrusgroup) %verify(not md5 mtime size) %_vardata/ssl/cyrus.cert
%ghost %attr(0640,root,%_cyrusgroup) %verify(not md5 mtime size) %_vardata/ssl/cyrus.key

%_cyrexecdir
%exclude %_cyrexecdir/lmtpproxyd
%exclude %_cyrexecdir/mupdate
%exclude %_cyrexecdir/pop3proxyd
%exclude %_cyrexecdir/proxyd
%exclude %_cyrexecdir/ptdump
%exclude %_cyrexecdir/ptexpire
%exclude %_cyrexecdir/ptloader
%exclude %_contribdir

%files doc
%doc COPYRIGHT README README.autocreate
%doc $RPM_SOURCE_DIR/cyrus-procmailrc
%doc $RPM_SOURCE_DIR/cyrus-user-procmailrc.template
%doc $RPM_SOURCE_DIR/%name-procmail+cyrus.mc
%doc doc/*

%files murder
%config(noreplace) %_sysconfdir/pam.d/mupdate
%_cyrexecdir/lmtpproxyd
%_cyrexecdir/mupdate
%_cyrexecdir/pop3proxyd
%_cyrexecdir/proxyd

%files ldap
%_cyrexecdir/ptdump
%_cyrexecdir/ptexpire
%_cyrexecdir/ptloader

%files devel
%_includedir/cyrus
%_libdir/lib*.a
%_man3dir/*

%files -n perl-Cyrus
%perl_vendor_autolib/Cyrus*
%perl_vendor_archlib/Cyrus*
%doc perl/imap/README
%doc perl/imap/Changes
%doc perl/imap/examples

%files utils
%_contribdir
%_bindir/*
%_man1dir/*
%dir %_datadir/%name

%changelog
* Sat Oct 15 2011 Alexey Tourbin <at@altlinux.ru> 2.4.12-alt1.1
- Rebuilt for perl-5.14.

* Thu Oct 06 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.4.12-alt1
- 2.4.12 fixes CVE-2011-3372, authentication bypass in the nntpd daemon.

* Fri Sep 09 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.4.11-alt1
- 2.4.11 fixes CVE-2011-3208, a remotely exploitable buffer overflow in
  the nntpd daemon.

* Wed Jun 22 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.4.9-alt1
- 2.4.9.

* Thu May 12 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.4.8-alt2
- Add libsensors-devel and libnl-devel to buildreqs for fix building.

* Thu Apr 14 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.4.8-alt1
- 2.4.8.

* Fri Apr 01 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.4.7-alt1
- 2.4.7.

* Thu Mar 24 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.4.6-alt3
- Enable libwrap and snmp support.

* Thu Mar 24 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.4.6-alt2
- Fix build by updating build requires.

* Thu Jan 13 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.4.6-alt1
- 2.4.6.
- Apply autocreate and autosieve patches for Cyrus IMAP Server 2.4.x by
  Martin Matuska <mm@freebsd.org>.
- Drop 002-fdatasync patch (unneeded).
- Drop Cyradm_Annotations.patch (merged upstream).

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 2.3.16-alt4.1
- Rebuilt with perl 5.12.

* Mon Oct 04 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3.16-alt4
- Rebuild with libssl.so.10 and libcrypto.so.10.

* Tue Jun 08 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3.16-alt3
- Build with --enable-replication.

* Mon Mar 01 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3.16-alt2
- Add ldap auth support (Closes: #23002).

* Thu Dec 24 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3.16-alt1
- 2.3.16
- Drop TV-annotation-definitions.diff patch (merged upstream).

* Thu Oct 22 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3.15-alt2
- Move ssl cert generation code from spec to initscript.

* Thu Sep 10 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3.15-alt1
- 2.3.15
- Update sieve to cyrus-imapd-2.3.15 release
- Security fix: Cyrus IMAP Server Sieve Buffer Overflow Vulnerability,
  see http://secunia.com/advisories/36629/

* Wed May 13 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3.14-alt2
- Fix building with gcc4.4

* Mon Apr 20 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3.14-alt1
- 2.3.14
- Drop 10-fix_potential_overflows.dpatch (merged by upstream)

* Tue Nov 25 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3.13-alt3
- Updated buildreqs for fix building

* Sat Nov 01 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3.13-alt2
- Fixed bug with pseudouser creation (introduced in 2.2.3-alt4)
- Add cyrus pseudouser to 'sasl' group by default

* Wed Oct 22 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3.13-alt1
- 2.3.13 release

* Mon Aug 25 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 2.3.12p2-alt3
- More carefully handle find(1) errors in %%post (Closes: #16857)

* Tue Jun 17 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 2.3.12p2-alt2
- Fixed linking with libdb4.7

* Tue May 27 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 2.3.12p2-alt1
- 2.3.12p2
- Fixed directory permissions according to ALT Security Policy
- Implemented automatic ssl-certificates generation using cert-sh-functions
  (Closes: #14304)
- Relocate client config for libsasl2 from %%_libdir/sasl2 to
  %%_sysconfdir/sasl2
- Do not package contrib both in cyrus-imapd and cyrus-imapd-utils
- README.ALT: add notice about sasl_mech_list
- Add sasl_mech_list option to default config

* Mon Jan 14 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 2.3.11-alt1
- 2.3.11 release
- Disable cyrus-imapd service autostart by default
- Apply some Kolab patches:
  + cyrus-imap-admin-2.3.8-cyradm.patch
  + TV-annotation-definitions.diff from http://vman.de/cyrus/
  http://wiki.kolab.org/index.php/Kolab-major-app-patches#Cyrus_IMAPD
- Apply some Debian patches:
  + 03-fix_docs
  + 08-clean_socket_closes
  + 10-fix_potential_overflows
  + 30-update_perlcalling.sh
  + 40-rehash_fix_pathes.dpatch, change paths to alt-style
- Update autocreate patch http://email.uoa.gr/projects/cyrus/autocreate/
- README.ALT: recode to utf8, fix typo

* Tue Oct 09 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 2.2.13-alt2
- Add dependency on su(1) (Closes: #9971).
- Fix segfault when use lmtp socket for delivery (Closes: #10094)
- Use "skiplist" as default cyrusdb backend to use for the duplicate delivery
  suppression (Closes: #10476)

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.2.13-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Mon May 15 2006 Alexei Takaseev <taf@altlinux.ru> 2.2.13-alt1
- 2.2.13
- add Requires "perl(Term/ReadLine.pm)" for cyrus-imapd-utils
- Add LDFLAGS and CPPFLAGS for Sysiphus correct Kerberos detection

* Fri May 20 2005 Alexei Takaseev <taf@altlinux.ru> 2.2.12-alt3
- Fix #6902, #6903
- Remove unneeded requires to libsasl2-plugin-gssapi (#6859)

* Fri Apr 22 2005 Alexei Takaseev <taf@altlinux.ru> 2.2.12-alt2
- Fix (not created /var/spool/imap)

* Sat Feb 26 2005 Alexei Takaseev <taf@altlinux.ru> 2.2.12-alt1
- 2.2.12

* Fri Feb 11 2005 Alexei Takaseev <taf@altlinux.ru> 2.2.10-alt3
- Update autocreate patch to cyrus-imapd-2.2.10-autocreate-0.9.1.diff
- Add cyrus-imapd control facilities (for local delivery)
- Update README.ALT

* Wed Dec 08 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.10-alt2
- Update autocreate patch to cyrus-imapd-2.2.10-autocreate-0.1.diff

* Wed Nov 24 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.10-alt1
- 2.2.10
- CAN-2004-1015

* Tue Nov 23 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.9-alt1
- 2.2.9
- This release implements several bugfixes, notably one where lmtpproxyd
  could reuse a freed connection, another involving a pre-authentication
  buffer overrun in "imap magic plus" support (CAN-2004-1011) and lack
  of bounds checking in PARTIAL and FETCH. (CAN-2004-1012, CAN-2004-1013)

* Sat Jul 31 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.8-alt1
- 2.2.8

* Tue Jul 27 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.7-alt1
- 2.2.7
- add README.ALT
- remove cyrus-imapd-2.0.12-deliverman.patch,
  cyrus-imapd-2.0.12-~adm_man_sec.patch, cyrus-imapd-2.1.11-snmpargs.patch

* Wed Jun 23 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.6-alt2
- Update autocreate patch to cyrus-imapd-2.2.6-autocreate-0.2.diff

* Sat Jun 19 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.6-alt1
- 2.2.6

* Fri Jun 11 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.5-alt2
- Update autocreate patch to cyrus-imapd-2.2.5-autocreate-0.2.diff

* Sat May 29 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.5-alt1
- 2.2.5
- remove cyrus-imapd-2.0.9-cflags.patch (fixed in mainstream)

* Tue May 25 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.4-alt1
- 2.2.4
- remove cyrus-imapd-2.0.5-mandir.patch (fixed in mainstream)
- update autocreate patch to 2.2.4-autocreate-0.1

* Mon May 17 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.3-alt4
- cleanup spec-file 

* Thu May 13 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.3-alt2
- cleanup spec-file
- Add MDA, IMAPD and POP3D provides

* Tue Feb 24 2004 Alexander Bokovoy <ab@altlinux.ru> 2.2.3-alt1.2
- Rebuild against libkrb5-1.3.1-alt3

* Sun Jan 25 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.3-alt1.1
- build with db-4.2

* Sun Jan 25 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.3-alt1
- 2.2.3
- Drop cyrus-imapd-2.2.2-idled.patch (fix in upstream)
- Update autocreate patch
- Update imapd.conf (add all options)

* Mon Jan 05 2004 Alexei Takaseev <taf@altlinux.ru> 2.2.2-alt4
- fix imapd.conf - tls_* undefine by default
- fix cyrus.conf - all services is offline by default, path for LMTP
  defined for postfix

* Fri Nov 28 2003 Alexei Takaseev <taf@altlinux.ru> 2.2.2-alt3
- Enable `idle' daemon
- Update autocreate patch to 0.8.3
+ Add cyrus-imapd-2.2.2-idled.patch (fix idled compile)

* Mon Nov 03 2003 Alexei Takaseev <taf@altlinux.ru> 2.2.2-alt2
- fix cyrus-imapd-alt-cyradm.patch (error:
  /usr/bin/cyradm: line 46: `exec perl -MCyrus::IMAP::Shell -e shell -- "$@" ;;')

* Wed Oct 29 2003 Alexei Takaseev <taf@altlinux.ru> 2.2.2-alt1
- 2.2.2
- Disable `idle' daemon

* Sat Sep 13 2003 Alexei Takaseev <taf@altlinux.ru> 2.2.1-alt6
- implemented autodetected / manual distro setting to package initscripts
  for both ALM2.2 (maintenance builds) and Sisyphus (implementation based
  somewhat on aureal-std-up.spec by Alexey Morozov <morozov novosoft ru>)

* Sun Aug 24 2003 Alexei Takaseev <taf@altlinux.ru> 2.2.1-alt5
- removed creation of spool/config dirs, not needed anymore
- add sendmail m4 macro
- just one source for pam default configuration (they were all the same)
- added /etc/pam.d/lmtp
- added murder support

* Tue Aug 05 2003 Alexei Takaseev <taf@altlinux.ru> 2.2.1-alt4
- Fixed definitions of files in perl-Cyrus

* Mon Aug 04 2003 Alexei Takaseev <taf@altlinux.ru> 2.2.1-alt3
- fixed pam0(system-auth) requires

* Mon Aug 04 2003 Alexei Takaseev <taf@altlinux.ru> 2.2.1-alt2
- by ivv:
    + changed main group to System/Servers
    + changed group of perl-Cyrus to Development/Perl
    + changed group of cyrus-imap-utils to System/Servers
    + changed file permissions on /usr/lib/cyrus/deliver to 4710
    + added patch for autocreate mailbox on post or login (see
      email.uoa.gr/autocreate)
    + added some contrib utils - folderxfer,imapcreate.pl,inboxfer

* Fri Jul 25 2003 Alexei Takaseev <taf@altlinux.ru> 2.2.1-alt1
- first build for ALT

