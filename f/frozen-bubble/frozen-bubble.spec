# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(File/ShareDir.pm) perl(File/Slurp.pm) perl(File/Which.pm) perl(Locale/Maketext/Simple.pm) perl(Math/Trig.pm)
# END SourceDeps(oneline)
Name: frozen-bubble
Version: 2.212
Release: alt1

Summary(ru_RU.UTF-8): игра Frozen Bubble
Summary: Frozen Bubble arcade game
License: GPL
Group: Games/Arcade

Url: http://www.frozen-bubble.org/
Source: %name-%version.tar
Source2: fb-server.service
Patch0:	frozen-bubble-2.2.1-setuid.patch
Patch1:	0001-Fix-buffer-size-when-formatting-current-date.patch

Requires: %name-data = %version

#BuildRequires: perl-Math-Complex

BuildRequires:	perl(Alien/SDL.pm)
BuildRequires:	perl(Archive/Extract.pm)
BuildRequires:	perl(autodie.pm)
BuildRequires:	perl(Compress/Bzip2.pm)
BuildRequires:	perl(IPC/System/Simple.pm)
BuildRequires:	perl(Locale/Maketext/Extract.pm)
BuildRequires:	perl(parent.pm)
BuildRequires:	perl-SDL
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer) >= 1.2.2
BuildRequires:	pkgconfig(SDL_Pango)
BuildRequires:	libsmpeg-devel

# due to conflict perl-SDL <-> perl-SDL_Perl
%filter_from_requires /^perl(SDL/d
Requires:	perl-SDL


%description
Colorful 3D rendered penguin animations, 100 levels of 1p game,
hours and hours of 2p game, nights and nights of 2p/3p/4p/5p game
over LAN or Internet, a level-editor, 3 professional quality
digital soundtracks, 15 stereo sound effects, 8 unique graphical
transition effects, 8 unique logo eye-candies.

%description -l ru_RU.UTF-8
Цветные мультяшные пингвины, 100 уровней однопользовательской игры,
многие часы игры вдвоём, долгие ночи двух-пятипользовательской игры
по локальной сети или через интернет, редактор уровней, три дорожки
звукового сопровождения профессионального качества, 15 стереоэффектов,
8 уникальных эффектов графического перехода и 8 просто красивостей.

%package data
Summary: Frozen Bubble arcade game
Group: Games/Arcade
Conflicts: %name < %version
BuildArch: noarch

%description data
Colorful 3D rendered penguin animations, 100 levels of 1p game,
hours and hours of 2p game, nights and nights of 2p/3p/4p/5p game
over LAN or Internet, a level-editor, 3 professional quality
digital soundtracks, 15 stereo sound effects, 8 unique graphical
transition effects, 8 unique logo eye-candies.

%description -l ru_RU.UTF-8
Данные для игры Frozen Bubble.

%package server
Group: Games/Arcade
Summary: Frozen Bubble network game dedicated server
BuildRequires: libsystemd-devel libudev-devel systemd systemd-analyze systemd-coredump systemd-networkd systemd-portable systemd-services systemd-stateless systemd-sysvinit systemd-utils

%description server
Frozen Bubble network game dedicated server. The server is already included
with the game in order to be launched automatically for LAN games, so you
only need to install this package if you want to run a fully dedicated
Frozen Bubble network game server.

%prep
%setup
%patch1 -p1

# -------- from fedora -----------------------------------------------
# Rename this README since the main server README has the same name
mv server/init/README server/README.init
# Change the example server configuration file to be a working one, which only
# launches a LAN server and doesn't try to register itself on the Internet
sed -ie "s#^a .*#z\nq\nL#" server/init/fb-server.conf
# -------- from fedora -----------------------------------------------


%build
export CFLAGS="%{optflags} -Wno-error=unused-result"
%perl_vendor_build

%install
%perl_vendor_install

mkdir -p %buildroot%_desktopdir
cat <<EOF >%buildroot%_desktopdir/%name.desktop
[Desktop Entry]
Type=Application
Name=Frozen Bubble
Comment=Frozen Bubble Arcade Game
Comment[ru]=Игра Frozen Bubble
TryExec=%name
Exec=%name
Icon=%name
Categories=Game;ArcadeGame;
Terminal=false
StartupNotify=false
EOF

install -pDm644 share/icons/%name-icon-16x16.png %buildroot%_miconsdir/%name.png
install -pDm644 share/icons/%name-icon-32x32.png %buildroot%_niconsdir/%name.png
install -pDm644 share/icons/%name-icon-48x48.png %buildroot%_liconsdir/%name.png

rm -rf %buildroot%perl_vendor_autolib/share/dist/Games-FrozenBubble/icons
mv %buildroot%perl_vendor_autolib/share/dist/Games-FrozenBubble %buildroot%_datadir/%name
ln -s `relative %_datadir/%name %perl_vendor_autolib/share/dist/Games-FrozenBubble` \
   %buildroot%perl_vendor_autolib/share/dist/Games-FrozenBubble


# -------- from fedora -----------------------------------------------
# Install server init script and default configuration
install -D -p -m 0644 %{SOURCE2} \
    %{buildroot}%{_unitdir}/fb-server.service
install -D -p -m 0644 server/init/fb-server.conf \
    %{buildroot}%{_sysconfdir}/fb-server.conf

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
EmailAddress: contact2@frozen-bubble.org
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">frozen-bubble.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>An addictive game about frozen bubbles</summary>
  <description>
    <p>
      Frozen Bubble is a free and open source game in which you throw colorful
      bubbles and build groups to destroy them.
    </p>
    <p>
      You can play this game locally or over the Internet.
      It also contains a level editor for you to create your own games.
    </p>
  </description>
  <url type="homepage">http://www.frozen-bubble.org/</url>
  <screenshots>
    <screenshot type="default">https://www.filepicker.io/api/file/zfCHFlCsR4OnStuPBwmQ</screenshot>
    <screenshot>http://blog.kii.com/wp-content/uploads/2013/06/frozenbubble.jpg</screenshot>
    <screenshot>https://www.filepicker.io/api/file/eqPdEWZMTtS1Un1LoRQ0</screenshot>
  </screenshots>
  <updatecontact>contact2_at_frozen-bubble.org</updatecontact>
</application>
EOF
# -------- from fedora -----------------------------------------------

%post server
/usr/sbin/useradd -r -s /sbin/nologin -d %{_datadir}/%{name} fbubble \
    &>/dev/null || :
%post_service fb-server

%preun server
%preun_service fb-server

%files
%perl_vendor_archlib/G*
%perl_vendor_autolib/G*
%perl_vendor_autolib/share/dist/Games-FrozenBubble

%files data
%doc README AUTHORS HISTORY COPYING
%_bindir/%name
%_bindir/%name-editor
%_man1dir/%name.1*
%_man1dir/%name-editor.1*
%_desktopdir/%name.desktop
%_niconsdir/*.png
%_miconsdir/*.png
%_liconsdir/*.png
%{_datadir}/appdata/%{name}.appdata.xml
%dir %_datadir/%name
%_datadir/%name/data
%_datadir/%name/gfx
%_datadir/%name/snd
%_datadir/%name/locale

%files server
%doc server/AUTHORS server/README*
%doc COPYING
%config(noreplace) %{_sysconfdir}/fb-server.conf
%{_unitdir}/fb-server.service
%{_bindir}/fb-server

# TODO:
# - package server

%changelog
* Sat Mar 02 2019 Igor Vlasenko <viy@altlinux.ru> 2.212-alt1
- new version (2.2.1-beta1, CPAN version is 2.212)

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt4.1
- rebuild with new perl 5.28.1

* Mon Jan 08 2018 Michael Shigorin <mike@altlinux.org> 2.2.0-alt4
- E2K: added openbsd clang patch
- added Russian descriptions (closes: #33776)
- minor spec cleanup

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt3.2.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt3.2.1
- rebuild with new perl 5.24.1

* Tue Jun 14 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt3.2
- preparing for perl-SDL rename

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt3.1
- rebuild with new perl 5.20.1

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 2.2.0-alt3
- built for perl 5.18

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 2.2.0-alt2
- rebuilt for perl-5.16

* Sun Oct 16 2011 Alexey Tourbin <at@altlinux.ru> 2.2.0-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 2.2.0-alt1.1
- rebuilt with perl 5.12

* Fri Feb 19 2010 Alexey Tourbin <at@altlinux.ru> 2.2.0-alt1
- 2.1.0 -> 2.2.0
- split %name-data noarch package

* Wed Feb 03 2010 Repocop Q. A. Robot <repocop@altlinux.org> 2.1.0-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for frozen-bubble
  * pixmap-in-deprecated-location for frozen-bubble
  * postclean-05-filetriggers for spec file

* Thu Dec 14 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.1.0-alt2
- Fixed .desktop file.

* Tue Nov 28 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.1.0-alt1
- 2.1.0 release.

* Sat Nov 18 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.0.0-alt3
- Fixed @LIBDIR@ in fb_stuff.pm.

* Thu Nov 09 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.0.0-alt2
- Packager changed.
- Cleaned up spec file a bit.
- Added freedesktop menu.

* Mon Oct 30 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.0.0-alt1
- 2.0.0 release.
- Removed patch for SDL_Perl-2.x.
- Changed Source URL.
- Altered BuildRequires.
- New Description.

* Fri Feb 04 2005 Alexey Tourbin <at@altlinux.ru> 1.0.0-alt5
- ported to SDL_Perl-2.x API
- abandoned Makefile, reworked specfile

* Fri May 07 2004 Alexey Voinov <voins@altlinux.ru> 1.0.0-alt4
- removed gimp-perl from buildreqs
- little spec cleaun up
- man pages included

* Tue Oct 14 2003 Alexey Tourbin <at@altlinux.ru> 1.0.0-alt3
- unnecessary files removed along with dependencies (#3159)

* Tue Sep 30 2003 Alexey Tourbin <at@altlinux.ru> 1.0.0-alt2
- fixed build (Makefile workarounds)
- specfile cleanup

* Mon Feb 24 2003 Rider <rider@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Thu Jan 09 2003 Konstantin Volckov <goldhead@altlinux.ru> 0.9.3-alt4
- Fixed menu file

* Thu Oct 31 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.9.3-alt3
- Rebuilt with new perl
- Fixed icons permissions

* Thu Oct 24 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.9.3-alt2
- Rebuilt in new environment

* Fri Jun 07 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.9.3-alt1
- 0.9.3
- Remove internal libSDL_mixer
- Remove fixed packager

* Tue Mar 05 2002 Alexander Bokovoy <ab@altlinux.ru> 0.9.2-alt1
- Initial build for ALT Linux

* Thu Feb  7 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.9.2-1mdk
- new version

* Wed Feb  6 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.9.1-1mdk
- first mdk rpm

