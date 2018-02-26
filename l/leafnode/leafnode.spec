Name: leafnode
Version: 1.11.8
Release: alt1

Summary: Leafnode - a leafsite NNTP server
License: Artistic
Group: System/Servers

Url: http://www.leafnode.org
Source: ftp://wpxx02.toxi.uni-wuerzburg.de/pub/%name-%version.tar.bz2
Source1: %name.texpire
Source2: %name.filters
Source3: %name.xinetd
Packager: Michael Shigorin <mike@altlinux.org>

Summary(ru_RU.KOI8-R): Leafnode - небольшой NNTP-сервер
Summary(uk_UA.KOI8-U): Leafnode - невеличкий NNTP-сервер

# NOTE: buildreq would catch %_sbindir/tcpd from and add tcp_wrappers :-/
# So don't run that on this. -- mike

BuildRequires: libpcre-devel
Conflicts: inn

%define nntp_server news.talk.ru
%define leafgroup news
%define leafuser news

%description
Leafnode is a small NNTP server for leaf sites without permanent
connection to the internet. It supports a subset of NNTP and is able to
automatically fetch the newsgroups the user reads regularly from the
newsserver of the ISP and push the posted messages.

%description -l ru_RU.KOI8-R
Leafnode - небольшой NNTP-сервер для "домашних" новостей при отсутствии
постоянного соединения с Internet.  Он поддерживает подмножество NNTP
и позволяет автоматически доставлять группы новостей и отправлять
сообщения при помощи news-сервера провайдера.

%description -l uk_UA.KOI8-U
Leafnode - невеличкий NNTP-сервер для "домашн╕х" новин за в╕дсутност╕
пост╕йного з'╓днання з Internet.  В╕н п╕дтриму╓ п╕дмножину NNTP та
дозволя╓ автоматично приймати групи новин та в╕дсилати листи за
допомогою news-серверу провайдера.

%prep
%setup

%build
%configure \
	--sysconfdir=%_sysconfdir/%name \
	--with-spooldir=%_spooldir/news \
	--with-lockfile=%_lockdir/news/fetchnews.lck
%make_build

%install
install -d %buildroot%_sysconfdir/{cron.daily,leafnode}
# carefully working around horrors in Makefile...
make INSTALL="install -p" \
        prefix=%buildroot%prefix \
	SPOOLDIR=%_spooldir/news \
	LOCKFILE=%buildroot%_lockdir/news/fetchnews.lck \
	DESTDIR=%buildroot \
	install

install -pDm600 filters.example %buildroot%_sysconfdir/leafnode/filters
install -pDm755 %SOURCE1 %buildroot%_sysconfdir/cron.daily/texpire
install -pDm644 %SOURCE3 %buildroot%_sysconfdir/xinetd.d/%name

sed \
	-e 's,news.hiof.no,%nntp_server,g' \
	-e 's,^# maxfetch,maxfetch,g' \
	-e 's,^# initialfetch,initialfetch,g' \
	-e 's,^# allow_8bit_headers,allow_8bit_headers,g' \
	< config.example \
	> %buildroot%_sysconfdir/leafnode/config

%post
# get hostname to config -- works for first time
grep -qF host.domain.country %_sysconfdir/%name/config && {
	SERVERNAME=`hostname`
	[ -z "$SERVERNAME" ] && SERVERNAME="localhost"
	TMP=`mktemp -q leafnode-config-XXXXXXXXXX`
	[ $? = 0 ] && sed -e "s,host.domain.country,$SERVERNAME,g" \
		< %_sysconfdir/%name/config \
		> $TMP && \
		cat $TMP > %_sysconfdir/%name/config && rm $TMP
} || :

# force spool perms in case of upgrade (since 1.9.38-alt1)
chown -R %leafuser.%leafgroup %_spooldir/news/
chmod -R u=rwX,go=rX %_spooldir/news/

# NB:
# - we don't need run.*.dist examples -- using xinetd
# - the same with nntp.rules.dist

# TODO
# - use %leafgroup for texpire?
# - config dir should be better guarded probably? (or not?)

%files
%_mandir/man?/*
%doc ADD-ONS CREDITS INSTALL KNOWNBUGS NEWS *README* FAQ.html FAQ.txt
%doc tools/archivefaq.pl update.sh
%dir %_sysconfdir/%name/
%config(noreplace) %verify(not size mtime md5) %_sysconfdir/xinetd.d/%name
%attr(755,root,root) %config(noreplace) %_sysconfdir/cron.daily/texpire
%attr(640,root,%leafgroup) %config(noreplace) %_sysconfdir/%name/config
%attr(640,root,%leafgroup) %config(noreplace) %_sysconfdir/%name/filters
%attr(710,root,%leafgroup) %_sbindir/*
%attr (775,root,%leafgroup) %_lockdir/news
%attr (755,%leafuser,%leafgroup) %_spooldir/news
%_bindir/*

%changelog
* Mon Jun 14 2010 Michael Shigorin <mike@altlinux.org> 1.11.8-alt1
- 1.11.8 (bugfixes)

* Wed Apr 22 2009 Michael Shigorin <mike@altlinux.org> 1.11.7-alt1
- 1.11.7 (bugfixes, including those backported from leafnode 2)
- NB: I don't use NNTP these days, anyone to maintain a good package?

* Sat Mar 17 2007 Michael Shigorin <mike@altlinux.org> 1.11.6-alt1
- 1.11.6 (minor bugfixes)
- spec cleanup
- removed both patches (unused)

* Sun Apr 09 2006 Michael Shigorin <mike@altlinux.org> 1.11.5-alt1
- 1.11.5 (minor bugfixes)

* Wed Nov 23 2005 Michael Shigorin <mike@altlinux.org> 1.11.4-alt1
- 1.11.4 (minor bugfixes)
- removed patch1 (worked around upstream, coreutils fixed too :)

* Mon Oct 24 2005 Michael Shigorin <mike@altlinux.org> 1.11.3-alt2
- worked around seemingly different coreutils-5.92-alt1 behaviour

* Thu Jun 09 2005 Michael Shigorin <mike@altlinux.ru> 1.11.3-alt1
- 1.11.3 (minor security fixes)
- detects timeouts while downloading the header
  (to avoid denial of service, CAN-2005-1911)

* Thu May 05 2005 Michael Shigorin <mike@altlinux.ru> 1.11.2-alt1
- 1.11.2 (minor security fixes)
- merged in changelog entries from spec in backports/2.4

* Fri Apr 29 2005 Alexey Borovskoy <alb@altlinux.ru> 1.11.1-alt0.M24.1
- 1.11.1

* Sat Mar 19 2005 Alexey Borovskoy <alb@altlinux.ru> 1.11.0-alt0.M24.1
- 1.11.0
- Bugfixes
  + Fix snprintf test

* Sat Jan 29 2005 Alexey Borovskoy <alb@altlinux.ru> 1.10.8-alt0.M24.1
- 1.10.8
- Backport to Master 2.4

* Sat Jan 29 2005 Michael Shigorin <mike@altlinux.ru> 1.10.8-alt1
- 1.10.8 (4 * minor bugfixes)

* Sun Aug 15 2004 Michael Shigorin <mike@altlinux.ru> 1.10.4-alt1
- 1.10.4 (major bugfixes)

* Mon Aug 02 2004 Michael Shigorin <mike@altlinux.ru> 1.10.3-alt1
- 1.10.3 (minor bugfixes)

* Wed Jul 21 2004 Michael Shigorin <mike@altlinux.ru> 1.10.2-alt1
- 1.10.2 (minor bugfixes)

* Sat Jun 26 2004 Michael Shigorin <mike@altlinux.ru> 1.10.1-alt1
- 1.10.1 (minor bugfixes)

* Fri Jun 11 2004 Michael Shigorin <mike@altlinux.ru> 1.10.0-alt1
- 1.10.0 (minor bugfixes)

* Thu May 20 2004 Michael Shigorin <mike@altlinux.ru> 1.9.54-alt1
- 1.9.54 (minor bugfixes)

* Sun Apr 04 2004 Michael Shigorin <mike@altlinux.ru> 1.9.52-alt1
- 1.9.52 (major bugfixes)
- removed patch0

* Sat Jan 31 2004 Michael Shigorin <mike@altlinux.ru> 1.9.49-alt1
- 1.9.49 (minor bugfixes)

* Fri Jan 09 2004 Michael Shigorin <mike@altlinux.ru> 1.9.48-alt1
- 1.9.48 (minor security fixes)
- added missing binaries (newsq and leafnode-version)
- added missing docs
- removed extra config.example
- updated filters.example
- spec cleanup

* Thu Jan 08 2004 Michael Shigorin <mike@altlinux.ru> 1.9.47-alt1
- 1.9.47

* Fri Nov 07 2003 Michael Shigorin <mike@altlinux.ru> 1.9.46-alt1
- 1.9.46 (minor bugfixes)

* Thu Oct 30 2003 Michael Shigorin <mike@altlinux.ru> 1.9.45-alt1
- 1.9.45 (minor bugfixes)

* Wed Oct 22 2003 Michael Shigorin <mike@altlinux.ru> 1.9.44-alt1
- 1.9.44 (minor bugfixes)

* Mon Sep 08 2003 Michael Shigorin <mike@altlinux.ru> 1.9.43-alt1
- 1.9.43
- note that 1.9.3 to 1.9.41 inclusive were vulnerable a bit

* Mon Jun 30 2003 Michael Shigorin <mike@altlinux.ru> 1.9.42-alt1
- 1.9.42
- major bugfixes

* Fri May 30 2003 Michael Shigorin <mike@altlinux.ru> 1.9.41-alt1
- 1.9.41 (major bugfixes)

* Thu May 08 2003 Michael Shigorin <mike@altlinux.ru> 1.9.40-alt1
- 1.9.40 (minor bugfixes)

* Mon May 05 2003 Michael Shigorin <mike@altlinux.ru> 1.9.39-alt1
- 1.9.39 (major bugfixes)

* Wed Apr 23 2003 Michael Shigorin <mike@altlinux.ru> 1.9.38-alt1
- 1.9.38 (minor bugfixes)
- due to changes in upstream, spool is now owned by 'news' user

* Wed Feb 26 2003 Michael Shigorin <mike@altlinux.ru> 1.9.36-alt1
- 1.9.36 (major bugfixes)
- seems that (mis)sync bug was fixed

* Fri Feb 21 2003 Michael Shigorin <mike@altlinux.ru> 1.9.35-alt1
- 1.9.35 (bugfixes)

* Wed Feb 19 2003 Michael Shigorin <mike@altlinux.ru> 1.9.34-alt1
- 1.9.34.rel

* Tue Feb 04 2003 Michael Shigorin <mike@altlinux.ru> 1.9.33-alt1
- 1.9.33 (major bugfixes)

* Sun Dec 29 2002 Michael Shigorin <mike@altlinux.ru> 1.9.31-alt1
- 1.9.31 (major bugfixes)
- WARNING: 1.9.20 through 1.9.29 were vulnerable (DoS; 100%% CPU)
- cleaned up BuildRequires (tcp_wrappers)

* Thu Dec 05 2002 Michael Shigorin <mike@altlinux.ru> 1.9.30-alt1
- 1.9.30 (minor bugfixes)

* Mon Nov 25 2002 Michael Shigorin <mike@altlinux.ru> 1.9.29-alt2
- fixed typo in %_sysconfdir/cron.d/texpire
- fixed perms on %_spooldir/news (was 755,root,news; now 775,root,news
  so leafnode can create directories for newsgroups automatically)
- #1615 is closed
- spec cleanup

* Thu Oct 24 2002 Michael Shigorin <mike@altlinux.ru> 1.9.29-alt1
- 1.9.29 (major bugfixes)

* Wed Oct 16 2002 Michael Shigorin <mike@altlinux.ru> 1.9.27-alt2
- slight adaptations in default config

* Mon Sep 30 2002 Michael Shigorin <mike@altlinux.ru> 1.9.27-alt1
- 1.9.27
- major bugfixes

* Mon Sep 23 2002 Michael Shigorin <mike@altlinux.ru> 1.9.26-alt1
- 1.9.26 (minor bugfixes)

* Wed Jul 10 2002 Michael Shigorin <mike@altlinux.ru> 1.9.24-alt1
- new version (nightly fixes)

* Tue Jul 09 2002 Michael Shigorin <mike@altlinux.ru> 1.9.23-alt1
- new (significantly fixed) version

* Fri May 31 2002 Michael Shigorin <mike@altlinux.ru> 1.9.22-alt1
- new version
- additionally fixed/tightened permissions on sbin files and spool

* Wed Mar 27 2002 Michael Shigorin <mike@altlinux.ru> 1.9.20-alt1
- (inger) modify texpire script (bug #??? in BTS)
- new release
- can post to NewsCache servers
- pay attention to changes in 1.9.20 when upgrading:
  - FQDN required!
  - running without access control deprecated
- no longer enabled by default in xinetd configuration
- patch: don't use quickmkdir as it's broken WRT non-root builds
  (would try to set ownership/permissions of files&dirs or die)
- spec cleanup

* Mon Jan 15 2001 AEN <aen@logic.ru>
- RE adaptation

* Fri Dec 01 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.9.18-1mdk
- new and shiny source.
- remove CHANGES from the filelist (no such file or directory).

* Tue Jan 18 2000 Andre Steden <andre@steden.de>
- build for mandrake-linux
- add leafnode-buildroot.patch
