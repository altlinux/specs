%def_disable debmenu

Name: irssi
Version: 0.8.15
Release: alt3.1

Summary: Irssi is an IRC client
License: GPL
Group: Networking/IRC

Url: http://irssi.org/
#http://irssi.org/irssi/files/irssi-%version.tar.bz2
Source: %name-%version.tar

# Automatically added by buildreq on Mon Oct 10 2011
BuildRequires: glib2-devel libpopt-devel libssl-devel libtinfo-devel lynx perl-devel

%description
Irssi is a textUI IRC client with IPv6 support written by
Timo Sirainen <a@sicom.fi>.

More information can be found at http://irssi.org

%package devel
Group: Development/C
Summary: Header files and static libs for the development of irssi applications
Requires: %name = %version-%release

%description devel
Header files and static libs for the development of irssi applications.

%package perl
Group: Networking/IRC
Summary: Perl scripts for irssi
Requires: %name = %version-%release

%description perl
Perl scripts for irssi.

%prep
%setup

%build
./autogen.sh
%autoreconf

sed -i 's@$PERL_LDFLAGS -L/usr/lib@$PERL_LDFLAGS -L/usr/%_lib@g' configure

%configure \
	--with-modules \
	--enable-ipv6 \
	--without-socks \
	--with-terminfo \
	--without-ncurses \
	--with-perl=module \
	--with-perl-lib=vendor \
	--with-proxy \
	--with-bot \
	--with-textui

%make_build

%install
%make_install DESTDIR="%buildroot" install

# Menu entries
mkdir -p %buildroot%_iconsdir

%if_enabled debmenu
mkdir -p %buildroot%_menudir

cat << EOF >%buildroot%_menudir/%name
?package(%name): \
needs="text" \
section="Networking/Chat" \
title="Irssi" \
icon="irssi.png" \
longtitle="A Text-UI based Irc Client" \
section="Networking/IRC" \
command="irssi"
EOF
%else
# freedesktop menu
mkdir -p %buildroot%_datadir/applications
install -m 644 irssi.desktop %buildroot%_datadir/applications/irssi.desktop
%endif

# mdk icons
install -D -m 644 irssi-icons/%{name}48.png %buildroot%_liconsdir/%name.png
install -D -m 644 irssi-icons/%{name}32.png %buildroot%_niconsdir/%name.png
install -D -m 644 irssi-icons/%{name}16.png %buildroot%_miconsdir/%name.png

mv %buildroot%_docdir/%name %buildroot%_docdir/%name-%version
bzip2 ChangeLog
mv AUTHORS ChangeLog.bz2 README TODO NEWS %buildroot%_docdir/%name-%version

%add_findreq_skiplist %_datadir/irssi/scripts/*

%files
#%doc AUTHORS ChangeLog.bz2 README TODO NEWS
%_docdir/%name-%version
%attr(755,root,root) %_bindir/*
%_datadir/irssi
%exclude %_datadir/irssi/scripts
%config(noreplace) %_sysconfdir/irssi.conf
%_liconsdir/*.png
%_miconsdir/*.png
%_niconsdir/*.png
%if_enabled debmenu
%_menudir/irssi
%else
%_datadir/applications/irssi.desktop
%endif
%_mandir/man?/*
%dir %_libdir/irssi
%dir %_libdir/irssi/modules
%_libdir/irssi/modules/*proxy*.so

%files perl
%perl_vendor_archlib/Irssi*
%perl_vendor_autolib/Irssi
%_libdir/irssi/modules/*perl*.so
%_datadir/irssi/scripts

%files devel
%_libdir/irssi/modules/*.a
%_includedir/irssi

%changelog
* Mon Oct 10 2011 Alexey Tourbin <at@altlinux.ru> 0.8.15-alt3.1
- rebuilt for perl-5.14

* Thu Mar 17 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 0.8.15-alt3
- Revert buggy patch applied in 0.8.15-alt2

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.8.15-alt2.1
- rebuilt with perl 5.12

* Wed Oct 06 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.8.15-alt2
- Apply patch for fix recoding of channel names
- Rebuild with libssl.so.10 and libcrypto.so.10

* Mon Apr 19 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.8.15-alt1
- 0.8.15 (Closes: #23317). Security fixes:
  + CVE-2010-1155 (poor verification the hostname of the server when
    using SSL connections)
  + CVE-2010-1156 (A NULL-pointer dereference error in
    src/core/nicklist.c can be exploited to cause a crash)

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.8.14-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for irssi
  * postclean-05-filetriggers for spec file

* Tue Oct 06 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.8.14-alt1
- 0.8.14 (Closes: #19627)

* Wed Sep 23 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.8.12-alt6
- Add raorn's script for xchat-like nick colorization

* Thu Jun 18 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.8.12-alt5
- cherry-picked upstream fix for CVE-2009-1959

* Tue May 19 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.8.12-alt4
- Fix building with fresh toolchain

* Thu Apr 16 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.8.12-alt3
- Applied upstream fix for ignoring DNS not found errors when considering
  reconnect (Closes: #17866)
- Add dependency on main irssi package to -perl subpackage
- Remove obsolete %%update_menus/%%clean_menus macros

* Tue Nov 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.8.12-alt2
- 0.8.12 release.

* Fri Sep 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.8.12-alt1.RC1
- 0.8.12 RC1.
- Minor spec cleanup.

* Fri Apr 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.8.11-alt1
- 0.8.11 release.

* Sun Mar 11 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.8.11-alt0.rc1
- 0.8.11 rc1.
- Removed dcc-free patch (#3), applied upstream.

* Fri Aug 18 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.10-alt3
- Package docs properly.
- Added patch4 to build irssi with system libpopt (closes #8264).

* Wed Mar 01 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.10-alt2
- backported dcc-free patch from trunk (closes #9105).

* Fri Feb 03 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.10-alt1
- Adopting package.
- Moved out INSTALL file.
- Bzip2'ed ChangeLog (closes #8989).
- Added _disable/_enable the debian menu file, defaults to disable.
- When debian menu is disabled, freedesktop menu file is getting installed.

* Sun Jan 08 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.10-alt0.4.2
- NMU (yet another one).
- Fixed #8726.
- Spec cleanups ($RPM_BUILD_ROOT to %%buildroot)
- Fixed building on current Sisyphus.

* Tue Dec 20 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.8.10-alt0.4.1
- NMU.
- 0.8.10 release.
- Removed gcc-g77 from buildrequires.
- Removed versioned dependancy on libtool.
- Updated patch: irssi-0.8.10-perl_scripts.fix.alt.patch.

* Tue Jun 23 2005 Nazar Yurpeak <phoenix@altlinux.org> 0.8.10-alt0.4
- Updated BuildRequires
- Fixed bug #6920

* Tue Oct 05 2004 Nazar Yurpeak <phoenix@altlinux.org> 0.8.10-alt0.3
- CVS 0.8.10-rc5

* Mon Aug 23 2004 Nazar Yurpeak <phoenix@altlinux.org> 0.8.10-alt0.2
- CVS Aug 23 2004

* Mon Jul 16 2004 Nazar Yurpeak <phoenix@altlinux.org> 0.8.10-alt0.1
- CVS 0.8.10-rc4

* Mon May 31 2004 Nazar Yurpeak <phoenix@altlinux.org> 0.8.9-alt3
- Updated BuildRequires

* Thu May 27 2004 Nazar Yurpeak <phoenix@altlinux.org> 0.8.9-alt2
- fixed perl scripts

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.8.9-alt1.1
- Rebuilt with openssl-0.9.7d.

* Thu Jan 22 2004 Nazar Yurpeak <phoenix@altlinux.org> 0.8.9-alt1
- 0.8.9
- temprorary removed perl scripts

* Wed Dec 10 2003 Nazar Yurpeak <phoenix@altlinux.org> 0.8.8-alt1
- 0.8.8

* Tue Aug 12 2003 Rider <rider@altlinux.ru> 0.8.6-alt4
- fix bug #0002794 (menu group changed to Chat)

* Tue Jan 21 2003 Rider <rider@altlinux.ru> 0.8.6-alt3
- fix russian summary

* Thu Jan 16 2003 Rider <rider@altlinux.ru> 0.8.6-alt2
- build with perl
- updated build requires
- build with glib2

* Fri Nov 22 2002 Rider <rider@altlinux.ru> 0.8.6-alt1
- new version
- remove perl core dump fix (included to mainstream)

* Wed Oct 09 2002 Rider <rider@altlinux.ru> 0.8.5-alt3
- removed perl scripts

* Tue Oct 08 2002 Rider <rider@altlinux.ru> 0.8.5-alt2
- requires & buildrequires fix

* Sat Oct 05 2002 Rider <rider@altlinux.ru> 0.8.5-alt1
- new version
- update specfile from MDK
- build without perl

* Wed Apr 03 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.7.98.4-alt4
- Build without bind-devel.

* Sat Feb 09 2002 Rider <rider@altlinux.ru> 0.7.98.4-alt3
- 0.7.98.4
- removed menu entry

* Thu Jul 26 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.7.98.3-alt3
- Rebuilt with new perl.

* Mon Jun 25 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.7.98.3-alt2
- Specfile minor cleanup.
- Rebuilt with perl-5.6.1

* Mon May 14 2001 Sergie Pugachev <fd_rag@altlinux.ru> 0.7.98.3-alt1
- new version

* Sun Jan 14 2001 AEN <aen@logic.ru>
- RE adaptation

* Thu Nov 16 2000 David BAUDENS <baudens@mandrakesoft.com> 0.7.96-2mdk
- Fix again build for archs <> than i386

* Mon Nov 13 2000 Daouda Lo <daouda@mandrakesoft.com> 0.7.96-1mdk
- big release ;-)
- build with bot , perl , mysql support
- text based support
- provides all icons
- mv from /usr/doc to /usr/share/doc

* Fri Sep 29 2000 Daouda Lo <daouda@mandrakesoft.com> 0.7.20.1-10mdk
- icons should be transparents.
- include menu entry in the body of spec file.
- more macrozifications.

* Mon Sep 25 2000 Daouda Lo <daouda@mandrakesoft.com> 0.7.20.1-9mdk
- add 32*32 icon for menu & replace gif icons format by xpm format.

* Wed Sep 20 2000 David BAUDENS <baudens@mandrakesoft.com> 0.7.20.1-8mdk
- %%config(noreplace)
- Remove stupid hard coded PATH in Menu entry
- Macros
- Use %%_tmppath for BuidRoot
- Spec clean up
- Remove french Description and Summary
- Fix typos in longtile (Menu entry)

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.7.20.1-7mdk
- automatically added BuildRequires

* Tue Apr 11 2000 Daouda Lo <daouda@mandrakesoft.com> 0.7.20.1-6mdk
- change icons
- clean spec.

* Fri Apr 04 2000 Daouda Lo <daouda@mandrakesoft.com> 0.7.20.1-5mdk
- add icons

* Sat Apr 1 2000 Daouda Lo <daouda@mandrakesoft.com> 0.7.20.1-3mdk
- add menu entry

* Sat Mar 25 2000 Daouda Lo <daouda@mandrakesoft.com> 0.7.20.1-2mdk
- group fix

* Thu Dec 02 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- 0.7.20.1

* Thu Nov 04 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Clean up the file section (removes xmms conflict)

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- 0.7.18 :
    - Authors Note :
    There's still a small bug in 0.7.18 irssi, if you
    use GtkText to print text it won't scroll down
    automatically. Solution: Use irssi text widget..
- update URL & src url
- Enable SMP check/build & add bzip2 macro

* Mon Aug 23 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 0.7.14

* Mon Jul 26 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Rebuild (4mdk)

* Thu Jul 15 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- --sysconfdir=/etc

* Tue May 11 1999 Alexandre Dussart <adussart@mandrakesoft.com>
- Make Mandrake compliant again

* Fri Apr 30 1999 GaÌl Duval <gael@linux-mandrake.com>
- lipstick

* Fri Apr 16 1999 Alexandre Dussart <adussart@mandrakesoft.com>
- Mandrake compliant
- Change Group to Internet

* Mon Mar 29 1999 JT Traub <jtraub@dragoncat.net>
- Updated to 0.7.6.
- text mode client re-added.

* Thu Mar 25 1999 JT Traub <jtraub@dragoncat.net>
- Updated sources

* Sat Mar 13 1999 JT Traub <jtraub@dragoncat.net>
- Updated to 0.7.4 sources
- Added the irssi-text bin to the package.

* Mon Feb 22 1999 JT Traub <jtraub@dragoncat.net>
- Made spec file compliant with RHCN guidelines.

* Sun Feb 13 1999 JT Traub <jtraub@dragoncat.net>
- Updated to 0.6.0 sources.
- Cleaned up spec file to make it relocatable on install

* Sun Feb 7 1999  JT Traub <jtraub@dragoncat.net>
- Updated sources to 0.5.0
- removed obsolete patch lines

* Sat Feb 3 1999  JT Traub <jtraub@dragoncat.net>
- Updated sources to 0.4.0
- Deleted old patch line

* Sat Jan 30 1999  JT Traub <jtraub@dragoncat.net>
- Updated sources to 0.3.6
- Updated spec to install the .desktop file.
- Removed the now obsolete patch lines

* Wed Jan 27 1999  JT Traub <jtraub@dragoncat.net>
- Upgraded to 0.3.5

* Sun Jan 24 1999  JT Traub <jtraub@dragoncat.net>
- First attempt at building this

