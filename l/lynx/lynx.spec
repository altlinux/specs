%define ver	2.8.6
%define subver  rel.2
%define bver	2-8-6

Name: lynx
Version: %ver
Release: alt8.%subver.2

Summary: Text based browser for the world wide web
License: GPL
Url: http://lynx.browser.org
Group: Networking/WWW

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: lynx.tar
Source1: %name.wmconfig

Source100: lynx-16.xpm
Source101: lynx-32.xpm
Source102: lynx-48.xpm

Requires: %name-data = %version-%release

Patch: %name-pld.patch
Patch1: lynx2-8-5-alt-cfg.patch
Patch2: %name-tmpdir.patch
Patch3: lynx2-8-4-fix-ugly-color.patch
Patch4: %name-284-ipv6-salen.patch
Patch5: lynx2-8-5-alt-i18n.patch
Patch6: %name.mouse-enable.patch
Patch7: %name.printers.patch

Provides: webclient, lynx-ssl = %version
Obsoletes: lynx-ssl

# Automatically added by buildreq on Wed Apr 03 2002
BuildRequires: lclint libncursesw-devel libssl ncompress openssl-devel postfix sharutils telnet unzip zip zlib-devel

%description
This a terminal based WWW browser. While it does not make any attempt
at displaying graphics, it has good support for HTML text formatting,
forms, and tables.

%package data
Summary: data files for lynx
Group: Networking/WWW
BuildArch: noarch

%description data
Data files for lynx

%prep
%setup  -q -c
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1
#patch4 -p1
%patch5 -p1
%patch6 -p0
%patch7 -p0

%build
#sed -i "s|\\$\\(SSL_DIR\\)/include|%_includedir/openssl|" makefile.in
#don't use configure macros
#	--libdir=/etc \
CFLAGS="$RPM_OPT_FLAGS -w -DUSE_SSL -D_USE_PLD -U_GNU_SOURCE " LDFLAGS=-s \
./configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--enable-warnings \
	--enable-color-style \
	--enable-default-colors \
	--enable-externs \
	--enable-internal-links \
	--enable-nsl-fork \
	--enable-persistent-cookies \
	--enable-cgi-links	\
	--enable-nls \
	--enable-charset-choice\
	--enable-ipv6 \
	--enable-nested-tables\
	--enable-prettysrc \
	--enable-source-cache \
	--enable-libjs \
	--enable-scrollbar \
	--enable-read-eta \
	--enable-file-upload \
	--enable-addrlist-page \
	--enable-justify-elts \
	--with-ssl \
	--with-zlib $SOCKS5 \
	--with-screen=ncursesw

# removed --enable-exec-links --enable-exec-scripts,
# it goes together with LOCAL_EXECUTION_LINKS_* in lynx.cfg

# (cf INSTALLATION file for more about the options)
# --with-included-gettext  is the default
# --enable-kbd-layout not useful enough
# --enable-cjk not needed for CJK and may go away in a future release

#make_build
# non SMP compatible build
make

%install
install -d %buildroot%_sysconfdir/X11/wmconfig
install -d %buildroot%_datadir/lynx/{lynx_help/keystrokes,test}

%makeinstall libdir=%buildroot/etc mandir=%buildroot%_man1dir

for i in `find lynx_help test -type f `; do
	install $i %buildroot%_datadir/lynx/$i
done

install %SOURCE1 %buildroot%_sysconfdir/X11/wmconfig/lynx
install -m644 samples/lynx.lss %buildroot%_sysconfdir/

bzip2 -9f docs/* README lynx.hlp||true

mkdir -p %buildroot{%_niconsdir,%_miconsdir,%_liconsdir}
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Lynx
Comment=Lynx - A text mode web browser
Icon=%name
Exec=%name
Terminal=true
Categories=Network;WebBrowser;
EOF

sed -i "s!PATH_TO/lynx_help/!"%_datadir"/lynx/lynx_help/!g" %buildroot%_sysconfdir/lynx.cfg

install -m 644 %SOURCE100 %buildroot/%_miconsdir/lynx.xpm
install -D -m 644 %SOURCE101 %buildroot/%_niconsdir/lynx.xpm
install -m 644 %SOURCE101 %buildroot/%_liconsdir/lynx.xpm

%find_lang %name

%files -f %name.lang
%doc docs README.bz2 lynx.hlp.bz2

%config(noreplace) %verify(not size mtime md5) %_sysconfdir/lynx.cfg
%config(noreplace) %verify(not size mtime md5) %_sysconfdir/lynx.lss

%_bindir/*
%_mandir/man?/*
%_desktopdir/%name.desktop
%_niconsdir/%name.xpm
%_liconsdir/%name.xpm
%_miconsdir/%name.xpm

%files data
%_datadir/%name

%changelog
* Sun Apr 17 2011 Igor Vlasenko <viy@altlinux.ru> 2.8.6-alt8.rel.2.2
- NMU: converted menu to desktop file

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 2.8.6-alt8.rel.2.1
- auto rebuild

* Sun Oct 10 2010 Denis Smirnov <mithraen@altlinux.ru> 2.8.6-alt7.rel.2.1
- rebuild with new openssl

* Fri Jul 03 2009 Denis Smirnov <mithraen@altlinux.ru> 2.8.6-alt7.rel.2
- move /usr/share/lynx to separate package

* Tue Apr 21 2009 Denis Smirnov <mithraen@altlinux.ru> 2.8.6-alt6.rel.2
- fix build

* Mon Apr 20 2009 Denis Smirnov <mithraen@altlinux.ru> 2.8.6-alt5.rel.2
- repocop patch for icons applied

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 2.8.6-alt4.rel.2
- cleanup spec

* Sun Mar 23 2008 Denis Smirnov <mithraen@altlinux.ru> 2.8.6-alt3.rel.2
- fix #14341 (UTF-8 console support)

* Tue Oct 17 2006 Denis Smirnov <mithraen@altlinux.ru> 2.8.6-alt2.rel.2
- bug id 1574 -- add 3 printer definitions;
- bug id 1575 -- enable mouse support by default;

* Tue Oct 17 2006 Denis Smirnov <mithraen@altlinux.ru> 2.8.6-alt1.rel.2
- version update
- some patches rediffed
- smoe spec cleanups

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 2.8.5-alt4.dev.16.1
- Rebuilt with openssl-0.9.7d.

* Fri Dec 05 2003 Stanislav Ievlev <inger@altlinux.org> 2.8.5-alt4.dev.16
- dev.16

* Fri Feb 07 2003 Stanislav Ievlev <inger@altlinux.ru> 2.8.5-alt4.dev.9
- removed debug messages

* Fri Dec 20 2002 Stanislav Ievlev <inger@altlinux.ru> 2.8.5-alt3.dev.9
- fix config patch
- update i18n hack

* Thu Dec 19 2002 Stanislav Ievlev <inger@altlinux.ru> 2.8.5-alt2.dev.9
- fix #0001625

* Fri Oct 25 2002 Stanislav Ievlev <inger@altlinux.ru> 2.8.5-alt1.dev.9
- dev9
- removed i18n patch (using our i18n patch instead)
- updated cfg patch (reapply,removed zgv)

* Wed Apr 03 2002 Stanislav Ievlev <inger@altlinux.ru> 2.8.5dev.7-alt1
- 2.8.5

* Fri Jun 15 2001 AEN <aen@logic.ru>  2.8.4dev11-ipl7mdk
- change first page URL
* Sat Dec 09 2000 AEN <aen@logic.ru>
- build for RE

* Thu Nov 23 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.8.4dev.11-5mdk
- fix help location

* Tue Nov 21 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.8.4dev.11-4mdk
- Another color fix patch :p.

* Tue Nov 21 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.8.4dev.11-3mdk
- Install lynx.lss from the samples/ directory (much better color).

* Fri Nov 03 2000 Daouda Lo <daouda@mandrakesoft.com> 2.8.4dev.11-2mdk
- rebuild for gcc-2.96

* Thu Oct 19 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.8.4dev.11-1mdk
- new release

* Sat Oct 07 2000 David BAUDENS <baudens@mandrakesoft.com> 2.8.4dev.8-4mdk
- Fix menu entry (#736)
- Use %%make macro

* Wed Sep 06 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.8.4dev.8-3mdk
- really add SSL (ginette sucks)
- buildrequires&obsoletes fixes for ssl support
- more macros
- add a menu entry

* Tue Sep  5 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.8.4dev.8-2mdk
- add support for SSL

* Fri Aug 25 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.8.4dev.8-1mdk
- new version

* Thu Aug 10 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.8.4dev.7-3mdk
- fix config for lord fred^h^h^hrpmlint
- remove useless wmconfig file

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.8.4-2mdk
- automatically added BuildRequires

* Fri Aug 04 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.8.4dev.7-1mdk
- new release

* Tue Jul 25 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.8.4dev.6-2mdk
- BM
- make it short-circuit compliant

* Tue Jul 18 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.8.4dev.6-1mdk
- new release

* Mon Jul 17 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.8.4dev.5-1mdk
- new release ...
- use new macros
- use spechelper for binaries stripping
- bzip2 doc instead of gzip it

* Mon Jun 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.8.4dev.4-1mdk
- new release

* Thu Jun 08 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.8.4dev.3-1mdk
- new release

* Mon Apr 24 2000 Pixel <pixel@mandrakesoft.com> 2.8.3dev.22-2mdk
- add provides webclient

* Thu Mar 23 2000 Thierry Vignaud <tvignaud@mandrakesoft.com>
- update to 2.8.3dev.22

* Thu Mar 23 2000 Thierry Vignaud <tvignaud@mandrakesoft.com>
- use the new group naming scheme
- use spechelper

* Mon Dec  6 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Define the TEMPDIR to ~/tmp, create it if is no here or fallback to
  /tmp is he can't.

* Sat Nov  6 1999 John Buswell <johnb@mandrakesoft.com>
- Build Release

* Tue Oct  5 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Fix wrong helpfile url (#291).

* Tue Sep  7 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Fix compliance with FTP RFC (needed for wu-ftpd 2.6.0 and other servers)
- 2.8.3dev.8
- Enable file-upload feature

* Fri Aug 20 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 2.8.3dev.6

* Tue Jul 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Redefine the temporary dir to /tmp/ (definitively !!!).

* Thu Jul 15 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- update to 2.8.3dev.4

* Wed Jun 23 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- 2.8.3.2 version.
- Updated patch.

* Fri May 21 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- 2.8.2pre5
- remove no-root patch

* Mon May 10 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- 2.8.2pre2
- change group to Applications/Internet (used to be the only app in
  group Networking).
- handle RPM_OPT_FLAGS

* Tue May 04 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add lynx.lss files.

* Thu Apr 22 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adptations.

* Tue Feb 16 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [2.8.2dev.16-2d]
- build with socks5 support -- if avaiable ..

* Tue Feb 16 1999 Artur Frysiak <wiget@usa.net>
  [2.8.2dev.16-1d]
- moved help and test files to %_datadir/lynx
- added not_for_root patch (this is bugi software, run from root account
  is dangerus)
- changed default color scheme

* Fri Feb 05 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [2.8.2dev15-2d]
- changed group,
- compressed documentation.

* Sun Jan 10 1999 Artur Frysiak <wiget@usa.net>
  [2.8.2dev.12-1d]
- added URL and Group(pl) tags

* Mon Sep 01 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [2.8-5d]
- build against glibc-2.1,
- changed Buildroot to /var/tmp/%%{name}-%%{version}-%%{release}-root,
- changed permission of lynx to 711,
- translation modified for pl.

* Sun Aug 30 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.8-5]
- added -q %%setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- URL in HELPFILE in %_sysconfdir/lynx.cfh changed to localhost,
- removed INSTALLATION from %%doc,
- added %%attr and %%defattr macros in %%files (allow build package from
  non-root account).

