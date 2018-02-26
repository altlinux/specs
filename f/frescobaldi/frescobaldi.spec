Name: frescobaldi
Version: 1.0.2
Release: alt1.1

Summary: LilyPond music score editor for KDE4
License: %gpl2plus
Group: Publishing

# http://lilykde.googlecode.com/svn/
URL: http://www.frescobaldi.org/
Packager: Artem Zolochevskiy <azol@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Mon Aug 17 2009
BuildRequires: ImageMagick-tools gcc-c++ ghostscript-classic kde4libs-devel lilypond python-module-kde4
BuildRequires: librsvg-utils
BuildArch: noarch

Source: %name-%version.tar

%description
Frescobaldi is a LilyPond music score editor for KDE4, with following
features:

* Enter LilyPond scores, build and preview them with a mouseclick
* Point-and-click support: click on notes or error messages to jump to the
  correct position
* A powerful Score Wizard to quickly setup a musical score
* Editing tools to:
  - manipulate the rhythm
  - hyphenate lyrics
  - quickly enter or add articulations and other symbols to existing music
  - run the document through convert-ly to update it to a newer LilyPond version
  - translate pitch names
* Context sensitive autocomplete, helping you to quickly enter LilyPond commands
* Expansion manager to enter larger snippets of LilyPond input using short
  mnemonics
* A powerful Rumor plugin, using the Rumor program to quickly enter music by
  playing it on a MIDI keyboard or even your computer keyboard
* Quick buttons to open, send, play or print LilyPond-generated files.
* Built-in comprehensive User Guide
* Translated into Dutch, English, French, German, Italian, Czech, Russian,
  Spanish, Turkish and Polish.

%prep
%setup

%build
%K4build

%install
%K4install
%K4find_lang --with-kde %name
install -d %buildroot%_liconsdir/
rsvg -w 48 -h 48  \
  %buildroot%_K4iconsdir/hicolor/scalable/apps/%name.svgz \
  %buildroot%_liconsdir/%name.png

%files -f %name.lang
%doc ChangeLog README THANKS TODO
%_K4bindir/*
%_K4apps/%name
%_K4xdg_apps/%name.desktop
%_K4iconsdir/hicolor/scalable/apps/%name.svgz
%_liconsdir/%name.png

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt1.1
- Rebuild with Python-2.7

* Mon Feb 22 2010 Artem Zolochevskiy <azol@altlinux.ru> 1.0.2-alt1
- update to 1.0.2

* Tue Jan 19 2010 Artem Zolochevskiy <azol@altlinux.ru> 1.0.1-alt1
- update to 1.0.1

* Sun Dec 27 2009 Artem Zolochevskiy <azol@altlinux.ru> 1.0.0-alt1
- update to 1.0.0

* Mon Dec 14 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.7.17-alt1
- update to 0.7.17

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.15-alt1.svn1604.1
- Rebuilt with python 2.6

* Mon Nov 09 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.7.15-alt1.svn1604
- update to svn1604

* Wed Oct 14 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.7.15-alt1
- update to v0.7.15

* Sun Oct 11 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.7.14-alt1.svn1513
- update to svn1513

* Mon Aug 17 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.7.14-alt1.svn1456
- initial build for Sisyphus (svn1456)
