%def_disable plugins

%def_enable menufile

%undefine cvs

Name: bzflag
Version: 2.4.6
Release: alt2.RC2

Summary: A multiplayer 3D tank battle game
License: LGPLv2.1
Group: Games/Arcade
Packager: Motsyo Gennadi <drool@altlinux.ru>

Url: http://www.bzflag.org
Source: %name-%version.tar

Source2:  bzflag_ru_utf8.po
Source10: %name.16.png
Source11: %name.32.png
Source12: %name.48.png
Source13: %name.menu
Source14: bzfs.init

Patch: bzflag_ru_po.patch
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch1:         %name-1.10.4-ncursespollution.patch

Summary(ru_RU.UTF-8): Трехмерная сетевая игра - битва на танках
Summary(uk_UA.UTF-8): Тривимірна мережева гра на танках

#Requires: %name-server

# Automatically added by buildreq on Sun Jun 05 2016 (-bi)
# optimized out: elfutils libGL-devel libGLU-devel libICE-devel libX11-devel libgpg-error libjson-c libstdc++-devel libtinfo-devel perl pkg-config python-base termutils xorg-xf86vidmodeproto-devel xorg-xproto-devel xz
BuildRequires: catdoc gcc-c++ imake libSDL-devel libSM-devel libXext-devel libXxf86vm-devel libcares-devel libcurl-devel libncurses-devel xorg-cf-files zlib-devel

BuildRequires: catdoc iconv

%description
BZFlag is a multiplayer 3D tank battle game. It's one of the most popular games
ever on Silicon Graphics systems.

%description -l ru_RU.UTF-8
BZFlag - многопользовательская танковая битва.  Одна из игр всех времен и народов
на Silicon Graphics.

%description -l uk_UA.UTF-8
BZFlag - багатокористувацька танкова гра.  Одна з ігор усіх часів та народів
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
%setup
%patch -p1
%patch1 -p1

# iconv %SOURCE2 -f utf8 -t koi8-r | catdoc -d us-ascii -s koi8-r | tr wW vV | sed \
#-e 's/T[Zz]/C/g' \
#-e 's/tz/c/g' \
#-e 's/K[Hh]/H/g' \
#-e 's/kh/h/g' \
#-e 's/kh/h/g' \
#-e 's/DZHo/Joy/g' \
#-e 's/dzho/joy/g' \
#-e 's/DZH/J/g' \
#-e 's/dzh/j/g' \
# > data/l10n/bzflag_ru.po

#-e 's/ь/\'/g' \
#-e 's/ъ/\"/g' \
#-e 's/ы/^i/g' \
#-e 's/щ/s^h\`/g' \
#-e 's/Щ/S^h\`/g' \


cat %SOURCE2 | LC_ALL=ru_RU.utf8 sed \
-e '!s!ь!\`!g' \
-e 's/ъ/\\"/g' \
-e 's/ё/yo/g' \
-e 's/щ/$/g' \
-e 's/Щ/$/g' \
-e 's/Ё/Yo/g' \
-e 's/в/v/g' \
-e 's/В/V/g' \
-e 's/Х/H/g' \
-e 's/х/h/g' \
-e 's/ж/zh/g' \
-e 's/Ж/Zh/g' \
-e 's/ц/c/g' \
-e 's/Ц/C/g' \
-e 's/ч/ch/g' \
-e 's/Ч/Ch/g' \
-e 's/ш/sh/g' \
-e 's/Ш/Sh/g' \
-e 's/ю/yu/g' \
-e 's/Ю/Yu/g' \
-e 's/я/ya/g' \
-e 's/Я/Ya/g' \
-e 's/ой/oj/g' \
-e 's/ый/ij/g' \
-e 's/ий/ij/g' \
-e 's/ай/аj/g' \
-e 's/уй/uj/g' \
-e 's/ей/ej/g' \
> data/l10n/bzflag_ru.po_tmp

iconv -c data/l10n/bzflag_ru.po_tmp -f utf8 -t koi8-u | catdoc -d us-ascii -s koi8-u > data/l10n/bzflag_ru.po
rm data/l10n/bzflag_ru.po_tmp

subst 's/DZHo/Joy/g;s/dzho/joy/g;s/Dzho/Joy/g;s/DZH/J/g;s/dzh/j/g;s/Dzh/J/g'  data/l10n/bzflag_ru.po


%build
%autoreconf
export CARES_DIR=%_includedir
%configure \
	--bindir=%_gamesbindir \
	--datadir=%_gamesdatadir \
	--with-pic \
        --disable-dependency-tracking \
	--enable-threads \
	%{subst_enable plugins} \
	--without-regex \
	--enable-robots

%make_build
cd misc
make
cd ..

%install
%makeinstall_std

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

%post server
%post_service bzfs

%preun server
%preun_service bzfs

%files
%exclude %_gamesbindir/bzadmin 
%exclude %_man6dir/bzadmin.6.*

%exclude %_gamesbindir/bzfs
%exclude %_man6dir/bzfs.6.*

%attr(755, %name, %name) /var/run/%name

%doc README README.Linux

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
%_man6dir/bzadmin.6.*

%files server
%doc misc/bzfs.conf misc/filter.txt misc/groups.conf
%_gamesbindir/bzfs
%_man6dir/bzfs.6.*
%_initdir/bzfs

%changelog
* Sun Jun 05 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.6-alt2.RC2
- Add Russian translation

* Thu Jun 02 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.6-alt1.RC2
- Version 2.4.6-RC2

* Sat Aug 10 2013 Motsyo Gennadi <drool@altlinux.ru> 2.4.2-alt1
- 2.4.2

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

