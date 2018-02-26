Name: inn
Version: 2.4.5
Release: alt4.3

Summary: The InterNetNews (INN) system, an Usenet news server
License: GPL
Group: System/Servers

Url: http://www.isc.org/products/INN
Packager: Vladimir V Kamarzin <vvk@altlinux.ru>

# ftp://ftp.isc.org/isc/inn/inn-2.4.3.tar.gz
Source0: %name-%version.tar
Source1: %name-default-active
Source2: %name-default-distributions
Source3: %name-default-newsgroups
Source4: %name-cron-expire
Source5: %name-cron-rnews
Source6: %name-etc-nnrp.access
Source7: %name-cron-nntpsend
Source8: innd.init
# ftp://ftp.exit109.com/users/jeremy/cleanfeed-latest.tar.bz2
Source9: cleanfeed-latest.tar
# ftp://ftp.isc.org/pub/pgpcontrol/pgpverify-1.2.1
Source10: pgpverify-1.2.1
Source11: %name-faq.tar

BuildPreReq: autoconf = 2.13
Requires: lib%name = %version-%release

# Automatically added by buildreq on Mon Dec 12 2005 (-bi)
BuildRequires: ctags flex gnupg libdb4-devel libe2fs-devel
BuildRequires: libkrb5-devel libpam-devel libssl-devel ncompress
BuildRequires: perl-Math-BigInt perl-devel perl-libnet python-base
BuildRequires: python-modules-compiler python-modules-encodings su tcl time uucp
BuildRequires: wget

%description
INN (InterNetNews) is a complete system for serving Usenet news and/or
private newsfeeds.  INN includes innd, an NNTP (NetNews Transport
Protocol) server, and nnrpd, a newsreader that is spawned for each client.
Both innd and nnrpd vary slightly from the NNTP protocol, but not in ways
that are easily noticed.

Install the inn package if you need a complete system for serving and
reading Usenet news.  You may also need to install inn-devel, if you are
going to use a separate program which interfaces to INN, like newsgate or
tin.

!!! ATTENTION !!! ATTENTION !!! ATTENTION !!! ATTENTION !!! ATTENTION !!! ATTENTION !!!
!!! ATTENTION !!!                                                     !!! ATTENTION !!!
!!! ATTENTION !!!        THIS PACKAGE IS COMPLETELY INSECURE.         !!! ATTENTION !!!
!!! ATTENTION !!! DON'T INSTALL IT UNLESS YOU DON'T CARE OF SECURITY. !!! ATTENTION !!!
!!! ATTENTION !!!                                                     !!! ATTENTION !!!
!!! ATTENTION !!! ATTENTION !!! ATTENTION !!! ATTENTION !!! ATTENTION !!! ATTENTION !!!

%package -n lib%name-devel
Summary: The INN (InterNetNews) development header files and libraries
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
The inn-devel package contains the INN (InterNetNews) library, which
several programs that interface with INN need in order to work (for
example, newsgate and tin).

%package -n lib%name-devel-static
Summary: The INN (InterNetNews) development static libraries.
Group: Development/Other
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
The inn-devel package contains the INN (InterNetNews) static library,
which several programs that interface with INN need in order to work
(for example, newsgate and tin).

%package -n lib%name
Summary: The shared libraries required for inn server.
Group: System/Libraries

%description -n lib%name
The inn-libs package provides the essential shared libraries for inn server.
You will need to install this package to use inn package or any clients that
need to connect to a inn server.

%package -n inews
Summary: Sends Usenet articles to a local news server for distribution
Group: System/Servers
Requires: lib%name = %version-%release

%description -n inews
The inews program is used by some news programs (for example, inn and
trn) to post Usenet news articles to local news servers.  Inews reads an
article from a file or standard input, adds headers, performs some
consistency checks and then sends the article to the local news server
specified in the inn.conf file.

Install inews if you need a program for posting Usenet articles to local
news servers.

%prep
%setup -q -a9 -a11

%build
%set_autoconf_version 2.13

# [hack]: fix path to -ldb
sed -i -e "s,@BERKELEY_DB_LDFLAGS@,-L%_libdir,g" Makefile.global.in
rm -f config.cache
autoconf
export CFLAGS="%optflags %optflags_shared"

./configure %_target_platform \
	--prefix=%prefix  \
	--sysconfdir=%_sysconfdir/news \
	--mandir=%_mandir \
	--with-log-dir=%_logdir/inn \
	--with-syslog-dir=%_logdir/news \
	--with-spool-dir=%_spooldir/news\
	--with-db-dir=%_localstatedir/news \
	--with-run-dir=%_var/run/news \
	--with-etc-dir=%_sysconfdir/news \
	--with-tmp-dir=%_var/run/news/tmp \
	--with-control-dir=%_libdir/%name/control \
	--with-filter-dir=%_sysconfdir/news/filter \
	--with-auth-dir=%_libdir/%name/auth \
	--with-rnews-dir=%_libdir/%name/rnews.libexec \
	--with-lib-dir=%_libdir \
	--with-newslib-dir=%_libdir/%name \
	--with-berkeleydb \
	--enable-libtool \
	--enable-shared \
	--with-perl \
	--with-openssl \
	--with-kerberos \
	--enable-largefiles \
	--enable-pgp-verify \
	--enable-merge-to-groups \
	--with-news-user=news \
	--with-news-group=news \
	--with-news-master=news \
	--with-sendmail=%_sbindir/sendmail

#NO SMP
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make

%install
%make install DESTDIR=%buildroot

# -- Install man pages needed by suck et al.
#for f in clibrary.h config.h dbz.h libinn.h storage.h; do
#	install -pD -m644 ./include/$f "$RPM_BUILD_ROOT%_includedir/%name/$f"
#done

touch %buildroot%_localstatedir/news/subscriptions
chmod 644 %buildroot%_localstatedir/news/subscriptions

#install -m 644 $RPM_SOURCE_DIR/inn-default-active \
#        %buildroot%_localstatedir/news/active
install -m 644 $RPM_SOURCE_DIR/inn-default-distributions \
        %buildroot%_localstatedir/news/distributions
install -m 644 $RPM_SOURCE_DIR/inn-default-newsgroups \
        %buildroot%_localstatedir/news/newsgroups

mkdir -p %buildroot%_sysconfdir/cron.hourly %buildroot%_sysconfdir/cron.daily
install -m755 $RPM_SOURCE_DIR/inn-cron-expire \
        %buildroot%_sysconfdir/cron.daily/inn-cron-expire
install -m755 $RPM_SOURCE_DIR/inn-cron-rnews \
        %buildroot%_sysconfdir/cron.hourly/inn-cron-rnews
install -m755 $RPM_SOURCE_DIR/inn-cron-nntpsend \
        %buildroot%_sysconfdir/cron.hourly/inn-cron-nntpsend

install -m440 $RPM_SOURCE_DIR/inn-etc-nnrp.access \
        %buildroot%_sysconfdir/news/nnrp.access

mkdir -p %buildroot%_initdir
install -m 755 %SOURCE8 \
	%buildroot%_initdir/innd

rm -f %buildroot%_localstatedir/news/history
touch %buildroot%_localstatedir/news/history
chmod 644 %buildroot%_localstatedir/news/*

#Fix perms in sample directory to avoid bogus dependencies
find samples -name "*.in" -exec chmod a-x {} \;

mkdir -p %buildroot%_spooldir/news/articles
mkdir -p %buildroot%_spooldir/news/overview
mkdir -p %buildroot%_spooldir/news/archive
mkdir -p %buildroot%_spooldir/news/incoming/bad
mkdir -p %buildroot%_spooldir/news/outgoing
mkdir -p %buildroot%_spooldir/news/uniover
mkdir -p %buildroot%_spooldir/news/innfeed
mkdir -p %buildroot%_logdir/inn
mkdir -p %buildroot%_var/run/news/tmp

%post
#if [ `%__cat %_sysconfdir/news/inn.conf | %__grep '^server:' | wc -l` -lt 1 ]; then
#  echo "server: `hostname -f`" >> %_sysconfdir/news/inn.conf
#fi

%post_service innd

%preun
%preun_service innd
if [ -f %_localstatedir/news/history.dir ]; then
	rm -f %_localstatedir/news/history.*
fi

# fix default filter path change introduced in 2.4.5-alt3
%triggerun -- inn =< 2.4.5-alt3
if [ "$2" -eq 0 ]; then
	sed -i -e "s,\(^pathfilter:[ \t]*\)%_libdir/%name/filter,\1%_sysconfdir/news/filter," \
		%_sysconfdir/news/inn.conf
fi

%files
%doc samples README* ChangeLog CONTRIBUTORS LICENSE INSTALL faq NEWS TODO 
%doc doc/checklist doc/compliance-nntp doc/config-design doc/config-semantics doc/config-syntax doc/external-auth
%doc doc/history doc/hook-perl doc/hook-python doc/hook-tcl doc/IPv6-info doc/sample-control
%defattr(2770,root,news)
%dir %_spooldir/news
%dir %_spooldir/news/articles
%dir %_spooldir/news/overview
%dir %_spooldir/news/archive
%dir %_spooldir/news/incoming
%dir %_spooldir/news/incoming/bad
%dir %_spooldir/news/outgoing
%dir %_spooldir/news/uniover
%dir %_spooldir/news/innfeed
%dir %_logdir/%name
%dir %_var/run/news
%dir %_var/run/news/tmp
%dir %_localstatedir/news

%attr(-,news,root) %config(noreplace) %_localstatedir/news/*
%attr(-,root,news) %dir %_sysconfdir/news
%attr(644,root,news) %config(noreplace) %_sysconfdir/news/actsync.cfg
%attr(644,root,news) %config(noreplace) %_sysconfdir/news/actsync.ign
%attr(644,root,news) %config(noreplace) %_sysconfdir/news/buffindexed.conf
%attr(640,root,news) %config(noreplace) %_sysconfdir/news/control.ctl
%attr(644,root,news) %config(noreplace) %_sysconfdir/news/cycbuff.conf
%attr(644,root,news) %config(noreplace) %_sysconfdir/news/distrib.pats
%attr(640,root,news) %config(noreplace) %_sysconfdir/news/expire.ctl
%attr(640,root,news) %config(noreplace) %_sysconfdir/news/incoming.conf
%attr(644,root,news) %config(noreplace) %_sysconfdir/news/inn.conf
%attr(644,root,news) %config(noreplace) %_sysconfdir/news/innfeed.conf
%attr(644,root,news) %config(noreplace) %_sysconfdir/news/innreport.conf
%attr(644,root,news) %config(noreplace) %_sysconfdir/news/innwatch.ctl
%attr(644,root,news) %config(noreplace) %_sysconfdir/news/moderators
%attr(644,root,news) %config(noreplace) %_sysconfdir/news/motd.news
%attr(644,root,news) %config(noreplace) %_sysconfdir/news/news2mail.cf
%attr(644,root,news) %config(noreplace) %_sysconfdir/news/newsfeeds
%attr(644,root,news) %config(noreplace) %_sysconfdir/news/nnrp.access
%attr(644,root,news) %config(noreplace) %_sysconfdir/news/nnrpd.track
%attr(640,root,news) %config(noreplace) %_sysconfdir/news/nntpsend.ctl
%attr(644,root,news) %config(noreplace) %_sysconfdir/news/ovdb.conf
%attr(644,root,news) %config(noreplace) %_sysconfdir/news/overview.fmt
%attr(640,root,news) %config(noreplace) %_sysconfdir/news/passwd.nntp
%attr(644,root,news) %config(noreplace) %_sysconfdir/news/radius.conf
%attr(640,root,news) %config(noreplace) %_sysconfdir/news/readers.conf
%attr(644,root,news) %config(noreplace) %_sysconfdir/news/sasl.conf
%attr(644,root,news) %config(noreplace) %_sysconfdir/news/storage.conf
%attr(644,root,news) %config(noreplace) %_sysconfdir/news/subscriptions

%dir %attr(755,root,news) %_sysconfdir/news/filter
%attr(644,root,news) %config(noreplace) %_sysconfdir/news/filter/*

%%defattr(-,root,root)
%_man5dir/*
%_man8dir/*
%_libdir/%name/
%_bindir/ovdb_init
%_bindir/ovdb_monitor
%_bindir/ovdb_server
%_bindir/ovdb_stat
%_bindir/perl-nocem
%_bindir/tdx-util
%_bindir/innupgrade
%_bindir/ninpaths
%_bindir/innd
%_bindir/inndstart
%_bindir/nnrpd
%_bindir/innfeed
%_bindir/procbatch
%_bindir/startinnfeed
%_bindir/convdate
%_bindir/expire
%_bindir/expireover
%_bindir/expirerm
%_bindir/fastrm
%_bindir/grephistory
%_bindir/makedbz
%_bindir/makehistory
%_bindir/prunehistory
%_bindir/cnfsheadconf
%_bindir/cnfsstat
%_bindir/ctlinnd
%_bindir/getlist
%_bindir/innconfval
%_bindir/mailpost
%_bindir/pullnews
%_bindir/rnews
%_bindir/scanspool
%_bindir/signcontrol
%_bindir/sm
%_bindir/actmerge
%_bindir/actsync
%_bindir/actsyncd
%_bindir/archive
%_bindir/batcher
%_bindir/buffchan
%_bindir/controlbatch
%_bindir/controlchan
%_bindir/cvtbatch
%_bindir/filechan
%_bindir/gpgverify
%_bindir/inndf
%_bindir/innxmit
%_bindir/innxbatch
%_bindir/mod-active
%_bindir/news2mail
%_bindir/nntpget
%_bindir/nntpsend
%_bindir/overchan
%_bindir/pgpverify
%_bindir/send-ihave
%_bindir/send-nntp
%_bindir/send-uucp
%_bindir/sendxbatches
%_bindir/shlock
%_bindir/shrinkfile
%_bindir/inncheck
%_bindir/innmail
%_bindir/innreport
%_bindir/innstat
%_bindir/innwatch
%_bindir/news.daily
%_bindir/scanlogs
%_bindir/simpleftp
%_bindir/tally.control
%_bindir/writelog
%_bindir/docheckgroups
%_bindir/imapfeed
%_bindir/sendinpaths
%_man1dir/convdate.*
%_man1dir/fastrm.*
%_man1dir/getlist.*
%_man1dir/grephistory.*
%_man1dir/innconfval.*
%_man1dir/innfeed.*
%_man1dir/innmail.*
%_man1dir/nntpget.*
%_man1dir/rnews.*
%_man1dir/shlock.*
%_man1dir/shrinkfile.*
%_man1dir/startinnfeed.*
%_man1dir/simpleftp.*
%_man1dir/pgpverify.*
%_man1dir/sm.*
%_man1dir/pullnews.*
%_sysconfdir/cron.hourly/*
%_sysconfdir/cron.daily/*
%_sysconfdir/rc.d/init.d/*

%files -n lib%name
%_libdir/libinn.so.*
%_libdir/libstorage.so.*
%_libdir/libinnhist.so.*

%files -n lib%name-devel
%_libdir/libinn.so
%_libdir/libstorage.so
%_libdir/libinnhist.so
%_includedir/%name
%_man3dir/*

%files -n lib%name-devel-static
%_libdir/libinn.a
%_libdir/libstorage.a
%_libdir/libinnhist.a

%files -n inews
%_bindir/inews
%_man1dir/inews*

%changelog
* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.5-alt4.3
- Removed bad RPATH

* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.5-alt4.2.1
- Rebuild with Python-2.7

* Mon Oct 10 2011 Alexey Tourbin <at@altlinux.ru> 2.4.5-alt4.2
- rebuilt for perl-5.14

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 2.4.5-alt4.1
- rebuilt with perl 5.12

* Tue Oct 05 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 2.4.5-alt4
- Fix upgrade breakage introduced in 2.4.5-alt3 (Closes: #23304)
- Rebuild with libssl.so.10 and libcrypto.so.10

* Mon Feb 01 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 2.4.5-alt3
- Move filter programs to %%_sysconfdir/news/filter (Closes: #22792)
  (tnx asy@)

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.5-alt2.1
- Rebuilt with python 2.6

* Tue May 19 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.4.5-alt2
- Fix building with fresh toolchain

* Tue Jul 08 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 2.4.5-alt1
- 2.4.5

* Tue May 13 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 2.4.4-alt1
- 2.4.4
  Announce in russian: http://www.opennet.ru/opennews/art.shtml?num=15809
- Package pullnews(1) manpage
- Patches now integrated into source tree, see git repo
  http://git.altlinux.org/people/vvk/packages/inn.git

* Mon Dec 25 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 2.4.3-alt3
- Package %%_includedir/%name directory (Closes: #10504)

* Fri Dec 01 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 2.4.3-alt2
- Fix path to -ldb

* Thu Nov 30 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 2.4.3-alt1
- 2.4.3
- Added inn-2.4.3-alt-Makefile.patch - build libinnhist before libstorage,
  link libstorage directly with libinnhist, add path to libstorage in
  libinnhist linkage string
- Fix builing with libdb4 (patch from Debian - inn-2.4.3-deb-libdb4.patch)
- Don't include <db1/ndbm.h> to avoid linking with -ldb1
- Rediffed inn-2.4.1-alt-krb5.patch and renamed to inn-2.4.3-alt-krb5.patch,
  harcoded '#include <et/com_err.h>', hardcoded '-I/usr/include/krb5
  -I/usr/include/et' into authprogs/Makefile instead of using buggy
  option --with-kerberos (Closes: #5971)
- Use %%optflags_shared to prevent TEXTREL entries
- Removed glibc-devel-static from buildreqs
- Use original tar.gz source instead of tar.bz2

* Mon Dec 12 2005 Konstantin Timoshenko <kt@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Sat Feb 12 2005 Konstantin Timoshenko <kt@altlinux.ru> 2.4.1-alt7
- rebuild with BerkeleyDB 4.3

* Fri Jan 28 2005 Konstantin Timoshenko <kt@altlinux.ru> 2.4.1-alt6
- fix #5971
- remove tcl and python scripts. (#5972)

* Fri Jan 25 2005 Konstantin Timoshenko <kt@altlinux.ru> 2.4.1-alt5
- fix buildrequires

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 2.4.1-alt4.1
- Rebuilt with openssl-0.9.7d.

* Fri May 07 2004 Konstantin Timoshenko <kt@altlinux.ru> 2.4.1-alt4
- rebuild with glibc-2.3

* Sun Feb 22 2004 Konstantin Timoshenko <kt@altlinux.ru> 2.4.1-alt3
- rebuild with Berkeley DB 4.2

* Thu Feb 05 2004 Konstantin Timoshenko <kt@altlinux.ru> 2.4.1-alt2
- fix permissions.

* Thu Jan 08 2004 Konstantin Timoshenko <kt@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Wed Dec 17 2003 Konstantin Timoshenko <kt@altlinux.ru> 2.4.0-alt5
- add %name-2.4.0-alt-docs.patch
- fix %name-2.4.0-alt.patch
- fix inncheck
- rebuild with new libtool 

* Wed Oct 22 2003 Konstantin Timoshenko <kt@altlinux.ru> 2.4.0-alt4
- fix startinnfeed code.

* Fri Sep 19 2003 Konstantin Timoshenko <kt@altlinux.ru> 2.4.0-alt3
- remove broken prereq.

* Tue Sep 16 2003 Konstantin Timoshenko <kt@altlinux.ru> 2.4.0-alt2
- add inn-2.4.0-alt-cdb.patch

* Mon Jul 28 2003 Konstantin Timoshenko <kt@altlinux.ru> 2.4.0-alt1
- 2.4.0
- Rewritten start/stop script to new rc scheme.
- remove embedded Python module support.
- remove embedded TCL script support.

* Fri Mar 21 2003 Konstantin Timoshenko <kt@altlinux.ru> 2.3.5-alt1
- 2.3.5

* Wed Jan 29 2003 Konstantin Timoshenko <kt@altlinux.ru> 2.3.4-alt2
-  fix file & directory permissions.

* Fri Jan 17 2003 Konstantin Timoshenko <kt@altlinux.ru> 2.3.4-alt1
- 2.3.4

* Sun Nov 10 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.3.3-alt2
- noreplace active file.
- rebuild with perl-5.8.0

* Thu Jul 25 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Fri May 31 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.3.2-alt8.3
- newsfeeds bugfix

* Mon May 27 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.3.2-alt8.2
- fix file & directory permissions
- moved inn config parameters for shell scripts to %_libdir/%name
- moved the authentication programs to %_libdir/%name/auth
- moved the filter programs to %_libdir/%name/filter
- removed suid & sgid bits

* Tue May 21 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.3.2-alt8.1
- Moved static libraries to devel-static subpackage.
- Split the package - news package inn-libs
-(inger) s/make_build/make/ - no SMP support

* Thu Apr 04 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.3.2-alt7
- Merged inn-devel-static into inn-devel.
- Updated dependencies.
- Fixed %_bindir/{i,r}news permissions.
- Added %_includedir/%name to devel subpackage.
- Added noticeable security warning to inn package description.

* Mon Jan 21 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.3.2-alt6
- fix innd init script

* Fri Dec 14 2001 Konstantin Timoshenko <kt@altlinux.ru> 2.3.2-alt5
- fixed post- & preun- services

* Fri Oct 12 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.3.2-alt4
- Fixed init script
- Fixed post- & pre- services by inger
- Added some scripts from S. Budnevitch

* Thu Jul 26 2001 Stanislav Ievlev <inger@altlinux.ru> 2.3.2-alt3
- Rebuilt with new perl again

* Tue Jun 26 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.3.2-alt2
- Rebuilt with perl-5.6.1
- Fix tmp dir
- Fixed some permissions
- Fixed init script
- Split the package - news package inn-devel-static

* Mon May  7 2001 Kostya Timoshenko <kt@altlinux.ru> 2.3.2-alt1
- clean spec file
- add mktemp patch
- removed cleanfeed
- 2.3.2

* Tue Jan 23 2001 Kostya Timoshenko <kt@petr.kz>
- 2.3.1
- fix innd.init file
- add inn-2.3.1-makefile.patch.bz2

* Tue Jan  2 2001 Kostya Timoshenko <kt@petr.kz>
- remove all patches
- add inn-2.3.0-ipl.patch.bz2
- Build for RE

* Fri Sep 22 2000 Philippe Libat <philippe@mandrakesoft.com> 2.2.2-8mdk
- change /etc/rc.news in  innd.init
- set correct permission file

* Mon Jul 31 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.2.2-7mdk
- Big BM cleanup merge fixes tweaking. (aka: make world).

* Wed Jun 14 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.2.2-6mdk
- Set verifycancels to false.

* Tue May 02 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 2.2.2-5mdk
- Removed appending of news logging, cause it is now
  added to the default syslog.conf file.
- Patch for inn to build with latest perl.

* Sun Apr 09 2000 John Buswell <johnb@mandrakesoft.com> 2.2.2-4mdk
- fixed filelist
- fixed permissions
- removed subdirs in /bin

* Thu Mar 30 2000 John Buswell <johnb@mandrakesoft.com> 2.2.2-3mdk
- Fixed groups
- spec-helper

* Wed Dec 15 1999 John Buswell <johnb@mandrakesoft.com>
- Fixed sendmail path in configure

* Tue Dec 14 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- 2.2.2 (y2k fix).

* Fri Nov 19 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Require Perl.
- Remove defattr(-,root,root).

* Thu Nov  4 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build release.

* Tue Sep 28 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Include all headers (#81 again).

* Tue Sep 14 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- 2.2.1
- Harald Schreiber Release ;-\.

* Tue Jul 06 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Build for new environement (Rel: 12mdk).

* Mon May 24 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- chown news.news /var/lib/news/.*

* Sat May 22 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- add security patch from RH update -9
- update cleanfeed 0.95.5a->0.95.7b
- rename cleanfeed-latest to cleanfeed-0.95.7b, so we see when/if it's
  required to update
- pgpverify 1.12

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS

* Tue Mar 30 1999 Preston Brown <pbrown@redhat.com>
- fixed paths in cron jobs, check to see that innd is enabled

* Fri Mar 26 1999 Preston Brown <pbrown@redhat.com>
- path to makehistory corrected.

* Mon Mar 22 1999 Preston Brown <pbrown@redhat.com>
- fixed permissions on rnews for uucp

* Fri Mar 19 1999 Preston Brown <pbrown@redhat.com>
- make sure init scripts get packaged up, fix other minor bugs
- major fixups to innd.conf for denial of service attacks, sanity, etc.
- make sure history gets rebuilt in an upgrade (added to post section)
- many thanks go out to mmchen@minn.net for these suggestions.

* Fri Feb 19 1999 Cristian Gafton <gafton@redhat.com>
- prereq all the stuff we need in the postinstall scripts

* Sat Feb  6 1999 Bill Nottingham <notting@redhat.com>
- strip -x bits from docs/samples (bogus dependencies)

* Thu Sep 03 1998 Cristian Gafton <gafton@redhat.com>
- updated to version 2.1

* Fri Aug 21 1998 Jeff Johnson <jbj@redhat.com>
- innd.init chkconfig entry was incorrect (problem #855)

* Tue Jun 30 1998 Jeff Johnson <jbj@redhat.com>
- susbsys name must be identical to script name (problem #700)

* Mon Jun 29 1998 Bryan C. Andregg <bandregg@redhat.com>
- fixed startinnfeed paths

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- enhanced initscript

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- fixed innfeed patched to be perl-version independent

* Wed Apr 15 1998 Bryan C. Andregg <bandregg@redhat.com>
- fixed sfnet.* entries in control.ctl

* Mon Apr 13 1998 Bryan C. Andregg <bandregg@redhat.com>
- moved cleanfeed to its own package

* Thu Apr 09 1998 Bryan C. Andregg <bandregg@redhat.com>
- added insync patches
- added cleanfeed
- added innfeed

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- abuse buildroot to simplify the file list
- built against Manhattan

* Tue Mar 24 1998 Bryan C. Andregg <bandregg@redhat.com>
- updated to inn 1.7.2
- Added REMEMBER_TRASH and Poison patch

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- updated to inn 1.7
- added chkconfig support to the initscripts
- orginally released as release 2, leving release 1 if a 4.2.x upgrade
  is ever necessary
- don't start it in any runlevel (by default)
- added inndcomm.h

* Thu Oct 09 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Aug 05 1997 Elliot Lee <sopwith@redhat.com>
- Applied the 1.5.1sec and 1.5.1sec2 patches
- Applied 3 more unoff patches.
- Removed insanity in /etc/cron.hourly/inn-cron-nntpsend, it now
  just runs nntpsend as news.

* Wed Apr 02 1997 Erik Troan <ewt@redhat.com>
- Patch from CERT for sh exploit.
- Changed /usr/ucb/compress reference to /usr/bin/compress

* Mon Mar 17 1997 Erik Troan <ewt@redhat.com>
- Removed inews.1 from main inn package (it's still in the inews packaeg)
- Fixed references to /usr/spoo in sendbatch
- added "-s -" to crosspost line in newsfeeds
- /var/lib/news/active.time is now created as news.news
- /etc/news/nnrp.access and /etc/news/nntpsend.ctl are mode 0440
- included a better rc script which does a better job of shutting down news
- updated /etc/rc.d/rc.news output look like the rest of our initscripts
- hacked sendbatch df stuff to work on machines w/o a separate /var/spool/news

* Tue Mar 11 1997 Erik Troan <ewt@redhat.com>
- added chmod to make sure rnews is 755
- /etc/news/nnrp.access and /etc/news/nntpsend.ctl are news.news not root.news
  or root.root
- install an empty /var/lib/news/.news.daily as a config file
- added dbz/dbz.h as /usr/include/dbz.h
- added /usr/bin/inews link to /usr/lib/news/inews
- changed INEWS_PATH to DONT -- I'm not sure this is right though
- turned off MMAP_SYNC
- added a ton of man pages which were missing from the filelist
- increased CLIENT_TIMEOUT to (30 * 60)
- added a postinstall to create /var/lib/news/active.times if it doesn't
  already exist
- patched rc.news to start inn w/ -L flag
- pulled news.init into a separate source file rather then creating it through
  a patch
- added /etc/rc.d/rc5.d/S95news to the file list
- remove pid files from /var/lock/news/* on shutdown
- use /var/lock/subsys/news rather then /var/lock/subsys/inn or things
  don't shutdown properly

* Mon Mar 10 1997 Christian 'Dr. Disk' Hechelmann <drdisk@ds9.au.s.shuttle.de>
- changed devel package description to include tin.
- the devel package missed libinn.h
- moved libinn.3 man-page to the devel package
- moved changelog up
- in %post some echo statements were messed up. if we put the redirection
  staements in a different line than the echo command we really should use
  a backslash to thell the shell :-)
- in %install a chmod line referenced the same directory twice.
- changed inn-1.5.1-redhat.patch: The patch for news.daily had a side effect.
  as EXPIREOVERFLAGS was set to '-a', expireover would break if there were
  articles to be removed, as '-a' can't be used if '-z' is specified...
  Now there is a separate 'eval expireover -a' after the first eval. Dirty
  but works.

* Wed Feb 26 1997 Erik Troan <ewt@redhat.com>
- Added a /usr/bin/rnews symlink to /usr/lib/news/rnews as other programs like
  to use it.

* Tue Feb 25 1997 Elliot Lee <sopwith@cuc.edu>
- Fixed rnews path in /etc/cron.daily/inn-cron-rnews
- Added overview! and crosspost lines to /etc/news/newsfeeds
- Fixed nntpsend.ctl path in /usr/lib/news/bin/nntpsend, and set a saner
  nntpsend.ctl config file.
- Added automated inn.conf 'server: ' line creation in %post
- Added misc. patches from ftp.isc.org/isc/inn/unoff-patches/1.5
- Removed -lelf from config.data LIBS
- Made RPM_OPT_FLAGS work.
- Bug in rpm meant that putting %post after %files made it not run. Moved
  %post up.
- Added /etc/cron.hourly/inn-cron-nntpsend to send news every hour.
- Fixed most of the misc permissions/ownership stuff that inncheck
  complained about.

* Wed Feb 19 1997 Erik Troan <ewt@redhat.com>
- Incorporated changes from <drdisk@tilx01.ti.fht-esslingen.de> which fixed
  some paths and restored the cron jobs which disappeared in the 1.5.1
  switch. He also made the whole thing use a buildroot and added some files
  which were missing from the file list.
