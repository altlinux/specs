Name: decibel-audio-player
Version: 1.05
Release: alt1.1

Summary: a simple audio player for GNOME
License: GPLv2+
Group: Sound
Url: http://decibel.silent-blade.org/

Source0: http://decibel.silent-blade.org/uploads/Main/%name-%version.tar.gz

Patch0: decibel-audio-player-1.01-alt-desktop-file.patch

Packager: Ilya Mashkin <oddity@altlinux.ru>

%add_python_req_skip gui media modules tools

BuildArch: noarch

%description
Decibel Audio Player is a GTK+ open-source (GPL license)
audio player designed for GNU/Linux, which aims at being
very straightforward to use by mean of a very clean and
user friendly interface. It is especially targeted at
Gnome and will follow as closely as possible the Gnome HIG.

It aims also at being a real audio player and, as such, it
does not include features that are not meant to be part of
an audio player. These features (e.g., tagging) generally
have a really better support in specialized software. If
you're looking for an audio player than can also make
coffee, then you should stay away from Decibel and give
a try to other players (e.g., Amarok, Exaile).

%prep
%setup -q
%patch0 -p1

%build

%install
%make_install DESTDIR=%buildroot prefix=/usr install

mkdir -p %buildroot%_liconsdir/
mkdir -p %buildroot%_niconsdir/
mkdir -p %buildroot%_miconsdir/
install -m644 pix/decibel-audio-player.png %buildroot%_liconsdir/decibel-audio-player.png
install -m644 pix/decibel-audio-player-32.png %buildroot%_niconsdir/decibel-audio-player.png
install -m644 pix/decibel-audio-player-16.png %buildroot%_miconsdir/decibel-audio-player.png

%find_lang %name

%files -f %name.lang
%doc doc/ChangeLog
%_bindir/*
%_datadir/applications/decibel-audio-player.desktop
%dir %_datadir/decibel-audio-player
%_datadir/decibel-audio-player/
%_datadir/pixmaps/decibel-audio-player.png
%_man1dir/*
%_liconsdir/decibel-audio-player.png
%_niconsdir/decibel-audio-player.png
%_miconsdir/decibel-audio-player.png

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.05-alt1.1
- Rebuild with Python-2.7

* Sun Sep 26 2010 Ilya Mashkin <oddity@altlinux.ru> 1.05-alt1
- 1.05

* Tue Jan 12 2010 Igor Zubkov <icesik@altlinux.org> 1.03-alt1
- 1.02 -> 1.03

* Mon Dec 14 2009 Igor Zubkov <icesik@altlinux.org> 1.02-alt1
- 1.01 -> 1.02

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.01-alt1.1
- Rebuilt with python 2.6

* Sun Sep 13 2009 Igor Zubkov <icesik@altlinux.org> 1.01-alt1
- 1.00 -> 1.01

* Mon Jan 19 2009 Igor Zubkov <icesik@altlinux.org> 1.00-alt2
- fix desktop file

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 1.00-alt1
- 0.11 -> 1.00

* Sat Nov 15 2008 Igor Zubkov <icesik@altlinux.org> 0.11-alt1
- 0.10 -> 0.11

* Sat Nov 15 2008 Igor Zubkov <icesik@altlinux.org> 0.10-alt4
- apply patch from repocop

* Fri Jul 11 2008 Igor Zubkov <icesik@altlinux.org> 0.10-alt3
- fix desktop file

* Thu Jul 10 2008 Igor Zubkov <icesik@altlinux.org> 0.10-alt2
- fix icons

* Wed May 28 2008 Igor Zubkov <icesik@altlinux.org> 0.10-alt1
- 0.09 -> 0.10

* Thu Apr 10 2008 Igor Zubkov <icesik@altlinux.org> 0.09-alt2
- run %%clean_menus after uninstall
- run %%update_desktopdb && %%clean_desktopdb
  after install/uninstall (repocop fix)

* Thu Feb 21 2008 Igor Zubkov <icesik@altlinux.org> 0.09-alt1
- 0.08 -> 0.09

* Fri Feb 08 2008 Grigory Batalov <bga@altlinux.ru> 0.08-alt1.1
- Rebuilt with python-2.5.

* Fri Jan 18 2008 Igor Zubkov <icesik@altlinux.org> 0.08-alt1
- 0.06 -> 0.08

* Fri Sep 28 2007 Igor Zubkov <icesik@altlinux.org> 0.06-alt1
- 0.04 -> 0.06
- run update menu after install and uninstall

* Mon Jul 09 2007 Igor Zubkov <icesik@altlinux.org> 0.04-alt1
- build for Sisyphus


