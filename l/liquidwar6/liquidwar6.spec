Name: liquidwar6
Version: 0.6.3902
Summary: A unique multiplayer wargame
Summary(fr): Un "wargame" multijoueur inédit.
Summary(de): Ein einzigartiges Kriegspiel für mehrere Spieler.
Release: alt1.1.qa1
License: GPL
Group: Games/Strategy
Source: %name-%version.tar
Url: http://www.gnu.org/software/liquidwar6

Patch: liquidwar6-0.6.3902-alt-Wno-error=deprecated-declarations.patch

# Automatically added by buildreq on Thu Nov 17 2016
# optimized out: fontconfig fontconfig-devel glib2-devel guile18 libGL-devel libGLU-devel libSDL-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgmp-devel libgpg-error libjson-c libltdl7-devel libncurses-devel libpango-devel libpng-devel libtinfo-devel libwayland-client libwayland-server perl perl-Encode perl-Text-Unidecode perl-Unicode-EastAsianWidth perl-Unicode-Normalize perl-libintl perl-unicore pkg-config python-base python-modules xz zlib-devel
BuildRequires: glibc-devel-static guile18-devel lcov libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel libcurl-devel libexpat-devel libgtk+2-devel libjpeg-devel libolpcsound-devel libreadline-devel libsqlite3-devel makeinfo

%description
Liquid War 6 is a unique multiplayer wargame. Your army is a blob of
liquid and you have to try and eat your opponents. Rules are very
simple yet original, they have been invented by Thomas Colcombet. It
is possible to play alone against the computer but the game is really
designed to be played with friends, on a single computer, on a LAN, or
on Internet.

%description -l fr
Liquid War 6 est un wargame multijoueurs unique en son genre. Votre
armée est une masse informe de liquide, et vous devez essayer de
manger votre adversaire. La règle est très simple mais originale, elle
a été inventée par Thomas Colcombet. Il est possible de jouer seul
contre l'ordinateur mais le jeu est vraiment conçu pour être joué à
plusieurs, sur une seule machine, sur un réseau local, ou sur
Internet.

%description -l de
Liquid War 6 ist ein einzigartiges Kriegsspiel für mehrere Spieler. Die
Regeln sind wahrhaft neuartig und wurden von Thomas Colcombet entwickelt.
Man steuert eine flüssige Armee und muss versuchen die Gegner aufzufressen.
Es gibt einen Einzelspielermodus, aber das Spiel ist eindeutig auf mehrere
Spieler ausgelegt und unterstützt das Spielen über Netzwerk.

%description -l dk
Liquid war 6 er et unikt multiplayer krigsspil. Reglerne er
uhyre originale og er opfundet af Thomas Colcombet. Du styrer
en hær af væske og skal prøve at æde dine modstandere.
Liquid War kan spilles alene, men er helt afgjort designet
til multiplayer, og har netværks-support.

# Preparation of the package
%prep
%setup
%patch -p1

# Building the package
%build
%autoreconf
%configure --docdir=%_defaultdocdir/%name-%version --enable-allinone --disable-mod-csound
%make_build
( cd doc; make liquidwar6.html )

# Installing the package
%install
mkdir -p %buildroot%_defaultdocdir/%name-%version
%makeinstall docdir=%buildroot%_defaultdocdir/%name-%version
## No devel stuff in this RPM
rm -rf %buildroot%prefix/include
rm -rf %buildroot%prefix/lib
rm -rf %buildroot%prefix/libexec
%find_lang %name

%files -f %name.lang
%doc ChangeLog README NEWS AUTHORS
%_bindir/*
%_datadir/%{name}*
%_pixmapsdir/*
%_infodir/%{name}*
%_man6dir/*
%_desktopdir/%{name}*

%changelog
* Thu Nov 17 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.6.3902-alt1.1.qa1
- Fixed build with glibc >= 2.24.

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.6.3902-alt1.1
- NMU: added BR: texinfo

* Tue Jul 14 2015 Fr. Br. George <george@altlinux.ru> 0.6.3902-alt1
- Autobuild version bump to 0.6.3902

* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 0.4.3681-alt1
- Autobuild version bump to 0.4.3681

* Tue Feb 18 2014 Fr. Br. George <george@altlinux.ru> 0.2.3551-alt1
- Autobuild version bump to 0.2.3551

* Thu Feb 28 2013 Fr. Br. George <george@altlinux.ru> 0.0.13beta-alt2
- Rebuild without perftools

* Fri Oct 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.13beta-alt1.1
- Rebuilt with libpng15

* Tue May 29 2012 Fr. Br. George <george@altlinux.ru> 0.0.13beta-alt1
- Autobuild version bump to 0.0.13beta

* Wed Aug 24 2011 Fr. Br. George <george@altlinux.ru> 0.0.10beta-alt1
- Initial build from upstream spec

* Fri Jul 23 2010 Christian Mauduit <ufoot@ufoot.org>
- Added GTK dependency.

* Fri Jul 09 2010 Christian Mauduit <ufoot@ufoot.org>
- Added applications directory (contains .desktop file).

* Tue Oct 20 2009 Christian Mauduit <ufoot@ufoot.org>
- Added proper GPG info.

* Mon Oct 05 2009 Christian Mauduit <ufoot@ufoot.org>
- Fixed info postinstall script.

* Tue Sep 09 2009 Christian Mauduit <ufoot@ufoot.org>
- Added Requires and BuildRequires declarations.

* Sat Jan 10 2009 Christian Mauduit <ufoot@ufoot.org>
- Fixed source URL.

* Thu Jan 08 2009 Christian Mauduit <ufoot@ufoot.org>
- Disabled csound support by default.
- Fixed info file handling.

* Wed Nov 07 2007 Christian Mauduit <ufoot@ufoot.org>
- Added version in data path.

* Mon Dec 18 2006 Christian Mauduit <ufoot@ufoot.org>
- Minor fixes, only a single jumbo binary is generated.

* Tue Dec 05 2006 Christian Mauduit <ufoot@ufoot.org>
- First RPM, inspired from Liquid War 5

