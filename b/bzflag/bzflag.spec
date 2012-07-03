%undefine cvs

%def_disable plugins

%def_disable menufile

Name: bzflag
Version: 2.4.0
Release: alt1.1

Summary: A multiplayer 3D tank battle game
License: GPL
Group: Games/Arcade
Packager: Motsyo Gennadi <drool@altlinux.ru>

Url: http://www.bzflag.org
Source: %name-%version.tar.bz2

Source10: %name.16.png
Source11: %name.32.png
Source12: %name.48.png
Source13: %name.menu
Source14: bzfs.init

Summary(ru_RU.KOI8-R): Трехмерная сетевая игра - битва на танках
Summary(uk_UA.KOI8-U): Тривим╕рна мережева гра на танках

Requires: %name-server

# Automatically added by buildreq on Sun Mar 25 2012 (-bi)
# optimized out: elfutils libGL-devel libGLU-devel libICE-devel libX11-devel libcom_err-devel libkrb5-devel libstdc++-devel libtinfo-devel pkg-config termutils xorg-xf86vidmodeproto-devel xorg-xproto-devel
BuildRequires: gcc-c++ imake libSDL-devel libSM-devel libXext-devel libXxf86vm-devel libcares-devel libcurl-devel libglew-devel libidn-devel libncurses-devel libssl-devel xorg-cf-files zlib-devel

%description
BZFlag is a multiplayer 3D tank battle game. It's one of the most popular games
ever on Silicon Graphics systems.

%description -l ru_RU.KOI8-R
BZFlag - многопользовательская танковая битва.  Одна из игр всех времен и народов
на Silicon Graphics.

%description -l uk_UA.KOI8-U
BZFlag - багатокористувацька танкова гра.  Одна з ╕гор ус╕х час╕в та народ╕в
на Silicon Graphics.

%package admin
Summary: BZFlag administration utility.
Group: Games/Arcade

%description admin
This package contains BZFlag game server administration utility.

%package server
Summary: BZFlag BZFS standalone server.
Group: Games/Arcade

%description server
This package contains BZFlags standalone game server.

%prep

%ifdef cvs
%setup -q -n %name
%else
%setup -q
%endif
rm -rf src/c-ares/*.h

%build

%ifdef cvs
%__rm -f missing
%__libtoolize --copy --force
%__aclocal -I m4
%__autoheader
%__automake -a -c --gnu 
%__autoconf
%endif
      
export CARES_DIR=%_includedir
%configure \
	--bindir=%_gamesbindir \
	--datadir=%_gamesdatadir \
	--with-pic \
	--enable-threads \
	%{subst_enable plugins} \
	--without-regex \
	--enable-robots

%make_build

cd misc
make
cd ..

%install
%make_install DESTDIR="%buildroot" install

install -pD -m644 %SOURCE10 %buildroot%_miconsdir/%name.png
install -pD -m644 %SOURCE11 %buildroot%_niconsdir/%name.png
install -pD -m644 %SOURCE12 %buildroot%_liconsdir/%name.png

%if_enabled menufile
install -pD -m644 %SOURCE13 %buildroot%_menudir/%name
%else
mkdir -p %buildroot%_datadir/applications
install -pD -m644 misc/bzflag.desktop %buildroot%_datadir/applications
%endif

install -pD -m755 %SOURCE14 %buildroot%_initdir/bzfs
mkdir -p %buildroot/var/run/%name

%pre
%_sbindir/groupadd -r -f %name &>/dev/null
%_sbindir/useradd -r -g %name -d %_localstatedir/%name -s /dev/null \
        -c "BZFlag Game Server" -M -n %name &>/dev/null ||:

%post
%post_service bzfs

%preun
%preun_service bzfs

%files
%exclude %_gamesbindir/bzadmin 
%exclude %_man6dir/bzadmin.6.gz

%exclude %_gamesbindir/bzfs
%exclude %_man6dir/bzfs.6.bz2

%attr(755, %name, %name) /var/run/%name

%doc README BUGS misc/bzfs_conf.html misc/bzfs.conf misc/groups.conf

%_man6dir/*
%_man5dir/*
%_gamesbindir/*
%_gamesdatadir/%name
%if_enabled menufile
%_menudir/%name
%else
%_datadir/applications/*
%endif
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%files admin
%_gamesbindir/bzadmin
%_man6dir/bzadmin.6.gz

%files server
%_gamesbindir/bzfs
%_man6dir/bzfs.6.bz2
%_initdir/bzfs

%changelog
* Wed Mar 28 2012 Motsyo Gennadi <drool@altlinux.ru> 2.4.0-alt1.1
- updated build requires

* Sun Mar 25 2012 Motsyo Gennadi <drool@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Sat Jul 03 2010 Motsyo Gennadi <drool@altlinux.ru> 2.0.16-alt1
- 2.0.16
- build with system libcares (close #19235)
- refresh BuildRequires

* Fri Nov 06 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.0.12-alt3.1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for bzflag

* Mon Mar 23 2009 Pavlov Konstantin <thresh@altlinux.ru> 2.0.12-alt3
- Rebuild with non-broken curl/c-ares.

* Fri Mar 06 2009 Pavlov Konstantin <thresh@altlinux.ru> 2.0.12-alt2
- Remove unneeded update-menus calls.

* Tue Oct 28 2008 Pavlov Konstantin <thresh@altlinux.ru> 2.0.12-alt1
- 2.0.12 release.

* Mon Dec 03 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.0.10-alt1
- 2.0.10 release.
- Patch1 merged to source tree.

* Sat Jan 13 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.0.8-alt2
- Not starting BZFlag server by default.

* Tue May 16 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.0.8-alt1
- 2.0.8 bugfix release.

* Tue Mar 07 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.0.5.20060307-alt1
- 2.0.5 CVS from 2006 03 07.
- Rebuild with new libglew.

* Mon Feb 06 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.0.5.20060206-alt1
- 2.0.5 CVS from 2006 02 06.
- Fixed building with Xorg7.
- Added .desktop file. 
- Altered buildrequires.

* Fri Oct 07 2005 Pavlov Konstantin <thresh@altlinux.ru> 2.0.5.20051007-alt1
- 2.0.5 CVS from 20051007 due to faulty plugins/python Makefile.
- Seems like all those should be usable without any bzflag data, so:
  + Moved bzadmin with manpage to separate package.
  + Moved bzfs with manpage and initscript to separate package.
- Added requires on bzflag-server to bzflag main package as it can be launched from within a game itself.
- Not building plugins to bzfs, as they re unusable at the moment.
- Adapted bzfs service patch to current sources.

* Thu Mar 24 2005 Pavlov Konstantin <thresh@altlinux.ru> 2.0.2.20050318-alt1
- 2.0.2 release.
- Patched bzfs to understand "+daemon", "-user user", "-group group".
  All those flags should be used together to have an effect.
  Initial patching by Cyril Margorin <cyrilm at korolev-net dot ru>.
- Added bzflag user and group.
- Added bzfs service.
- spec file cleanup.

* Thu Jan 20 2005 Pavlov Konstantin <thresh@altlinux.ru> 2.0.0.20050117-alt1
- 2.0.0 release

* Tue May 25 2004 Michael Shigorin <mike@altlinux.ru> 1.10.6.20040515-alt1
- 1.10.6

* Thu Jul 03 2003 Michael Shigorin <mike@altlinux.ru> 1.7g2-alt1
- 1.7g2
- revamped spec: they're autoconf'ed now!

* Wed Dec 25 2002 Michael Shigorin <mike@altlinux.ru> 1.7g0-alt1
- 1.7g0
- note: 1.7e6 won't build correctly with gcc3!
  (1.7e6-alt2 was botched)

* Fri Oct 18 2002 Stanislav Ievlev <inger@altlinux.ru> 1.7e6-alt2
- rebuild with gcc3

* Thu Jun 27 2002 Michael Shigorin <mike@altlinux.ru> 1.7e6-alt1
- 1.7e6

* Fri Feb 15 2002 Stanislav Ievlev <inger@altlinux.ru> 1.7e4-alt2
- fixed menu entry

* Sat Feb 09 2002 Rider <rider@altlinux.ru> 1.7e4-alt1
- 1.7e4
- specfile cleanup
- png icons

* Wed Jun 20 2001 Sergie Pugachev <fd_rag@altlinux.ru> 1.7e2-alt1
- new version

* Tue Jan 16 2001 Kostya Timoshenko <kt@petr.kz>
- Build for RE

* Mon Nov 27 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.7d.9-5mdk
- recompile with latest gcc from chmou
- provide 48x48 icon

* Fri Nov  3 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.7d.9-4mdk
- recompile against newest libstdc++
- fix compile against gcc-2.96

* Wed Aug 23 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.7d.9-3mdk
- automatically added packager tag

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.7d.9-2mdk
- automatically added BuildRequires

* Wed Aug  2 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.7d.9-1mdk
- first package for Linux-Mandrake

