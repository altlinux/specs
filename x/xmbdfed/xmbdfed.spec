Name: xmbdfed
Version: 4.7
Release: alt3

%define prefix /usr/X11R6

Summary: XmBDFEditor is a Motif-based BDF font editor
License: MIT
Group: Publishing
URL: http://crl.nmsu.edu/~mleisher/%name.html

Source: http://crl.nmsu.edu/~mleisher/%name-%version.tar.bz2
Source1: %name.menu

Patch0:		xmbdfed-4.7-patch1
Patch1:		xmbdfed-4.7-linux.patch
Patch2:		xmbdfed-4.7-staticfix.patch
Patch3:		xmbdfed-4.7-getline.patch
Patch100: %name-4.7patch1-debian-3.patch
Patch101: %name-4.7-alt-makefile.patch

# Automatically added by buildreq on Tue Aug 28 2012
# optimized out: fontconfig libICE-devel libSM-devel libX11-devel libXau-devel libXt-devel libfreetype-devel xorg-printproto-devel xorg-xproto-devel
BuildRequires: libXext-devel libXmu-devel libXpm-devel libopenmotif-devel zlib-devel

%description
XmBDFEditor is a Motif-based BDF font editor with the following features:

  o  Multiple fonts can be loaded from the command line.
  o  Multiple fonts can be open at the same time.
  o  Cutting and pasting glyphs between fonts.
  o  Multiple glyph bitmap editors can be open at the same time.
  o  Cutting and pasting between glyph bitmap editors.
  o  Export of XBM files from glyph bitmap editors.
  o  Automatic correction of certain metrics when a font is loaded.
  o  Generation of XLFD font names for fonts without XLFD names.
  o  Update an XLFD font name from the font properties.
  o  Update the font properties from an XLFD font name.
  o  Font property editor.
  o  Font comment editor.
  o  Supports unencoded glyphs (ENCODING of -1).
  o  Display of glyph encodings in octal, decimal, or hex.
  o  Builtin on-line help.
  o  Imports PK/GF fonts.
  o  Imports HBF (Han Bitmap Font) fonts.
  o  Imports Linux console fonts (PSF, CP, and FNT).
  o  Imports Sun console fonts (vfont format).
  o  Imports fonts from the X server.
  o  Imports Windows FON/FNT fonts.
  o  Imports TrueType fonts and collections.
  o  Exports PSF fonts.
  o  Exports HEX fonts.
  o  Edits two and four bits per pixel gray scale fonts.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch100 -p1
%patch101 -p1

%build
%make_build CFLAGS="%optflags"

%install
mkdir -p %buildroot{%_bindir,%_man1dir}
install -pDm755 %name %buildroot%_bindir/%name
install -pDm644 %name.man %buildroot%_man1dir/%name.1
install -pDm644 %SOURCE1 %buildroot%_menudir/%name

%files
%_bindir/*
%_man1dir/*
%_menudir/*
%doc README COPYRIGHTS CHANGES xmbdfedrc

%changelog
* Tue Aug 28 2012 Fr. Br. George <george@altlinux.ru> 4.7-alt3
- Resurrect from orphaned
- Merge FC patches

* Fri Dec 12 2008 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt2
- Removed obsolete %%update_menus/%%clean_menus calls.
- Updated build dependencies.

* Tue Dec 09 2008 Valery Inozemtsev <shrek@altlinux.ru> 4.7-alt1.1
- NMU: updated BuildRequires

* Sun Jun 12 2005 Sergey Vlasov <vsu@altlinux.ru> 4.7-alt1
- Version 4.7 (+patch1).
- Removed obsolete patches.
- Added patch from Debian package (xmbdfed_4.7patch1-3).
- Dropped support for buildind with lesstif (no lesstif package in Sisyphus).
- Fixed menu file (Applications/Editors section is for text editors).
- Updated BuildRequires.

* Thu Oct 31 2002 Dmitry V. Levin <ldv@altlinux.org> 4.5-alt3
- Rebuilt in new environment.

* Fri Apr 12 2002 Dmitry V. Levin <ldv@alt-linux.org> 4.5-alt2
- Rebuilt with openmotif-2.2.2.

* Sat Nov 24 2001 Sergey Vlasov <vsu@altlinux.ru> 4.5-alt1
- Version 4.5.
- Fixed compilation options.
- Enabled HBF import.
- Patch to fix glyph naming (buffer overflows, stop after unknown code).
- Allow build with either Lesstif or OpenMotif.

* Mon Oct 15 2001 Dmitry V. Levin <ldv@alt-linux.org> 4.4-ipl4mdk
- Built with lesstif-0.93.12.

* Sun Feb 18 2001 AEN <aen@logic.ru>
- group name fixed

* Mon Dec 18 2000 AEN <aen@logic.ru>
- build for 7.2RE with new Lesstif

* Sun Jun 4 2000 AEN <aen@logic.ru>
- initial spec for RE
