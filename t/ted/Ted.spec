Summary:        An easy Rich Text Processor
Name:           ted
Version:        2.23
Release:        alt2
License:        GPLv2+
Group:          Office
Source:         ftp://ftp.nluug.nl/pub/editors/ted/ted-2.23.src.tar.gz
URL:            http://www.nllgg.nl/Ted/index.html

# Automatically added by buildreq on Tue Apr 30 2013
# optimized out: fontconfig fontconfig-devel glib2-devel libICE-devel libSM-devel libX11-devel libXft-devel libXrender-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libpng-devel libwayland-client libwayland-server pkg-config xorg-renderproto-devel xorg-xproto-devel zlib-devel
BuildRequires: ImageMagick-tools gtk+-devel libXpm-devel libgtk+2-devel libjpeg-devel libopenmotif-devel libpaper-devel libpcre-devel libtiff-devel lsb-release

%description
Ted is an easy rich text processor. It can edit RTF files
in a WYSIWYG manner. It supports multiple fonts and can
print to PostScript printers.  Additionally Ted is an rtf2ps,
rtf2pdf, rtf2html and an rtf2epub converter.

Ted consists of a general part: The program, something.afm files
and an American spelling checker. Additional packages with
spell checking dictionaries for different languages exist.

This package is the general part.

%prep
%setup -n Ted-%version
sed -i '/Icon=/s/.*/Icon=Ted/' tedPackage/Ted.desktop.in

%build
make CONFIGURE_OPTIONS=--with-GTK
%make package
for N in 16 24 32 48 64; do convert Ted/tedmain.xpm $N.png; done

%install
mkdir -p %buildroot
%make -C tedPackage DESTDIR=%buildroot install
for N in 16 24 32 48 64; do
  install -D $N.png %buildroot/%_iconsdir/hicolor/${N}x${N}/apps/Ted.png
done

%files
%_bindir/*
%_datadir/Ted
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/Ted.png
%_man1dir/*

%changelog
* Thu Jan 10 2019 Fr. Br. George <george@altlinux.ru> 2.23-alt2
- Avoid parallel build race

* Tue Apr 30 2013 Fr. Br. George <george@altlinux.ru> 2.23-alt1
- Initial build for ALT from upstream spec

* Mon Feb 04 2013 Mark de Does <mark@mdedoes.com> 2.23-1
- New upstream release.
See http://ftp.nluug.nl/pub/editors/ted/announce.html
- Stability fixes.
- Many-many annoying bugs fixed.
- Some steps to support the few missing features such as absolutely 
positioned objects and shapes.
- Preparations for bidirectional text support
- Comply with LSB directory layout.
- Conformant deb and rpm packages
* Wed Apr 04 2012 Mark de Does <mark@mdedoes.com> 2.22-1
- New upstream release.
See http://ftp.nluug.nl/pub/editors/ted/announce.html
- Thorough brush-up of the internals.
- Undu/Redo/Recovery
- Many-many annoying bugs fixed.
- Some steps to support the few missing features such as absolutely 
positioned objects and shapes.
* Tue Oct 20 2009 Mark de Does <mark@mdedoes.com> 2.21-1
- New upstream release.
See http://ftp.nluug.nl/pub/editors/ted/announce.html
- Many improvements in the rendering of embedded images.
- Removed functionality that is not directly related to word processing 
and document formatting. (Email, Fax)
- Added GUI functionality that I forgot while moving to GTK.
- Can now embed fonts from a true type collection in the printout
- Moved more ad-hoc dialogs to the format tool as a preparation for a 
better UI
* Sun Jun 07 2009 Mark de Does <mark@mdedoes.com> 2.20-1
- New upstream release.
See http://ftp.nluug.nl/pub/editors/ted/announce.html
- Vertical alignment of table cells.
- Multi column layout (of sections).
- Text background and text borders
- Table of Contents
- Unicode compliant (So most scripts and fonts are now supported)
- Use fontconfig: Removed restrictions on the collection of fonts that 
Ted can use; Use Freetype/Xft for anti aliassed text rendering
- Can now render nested tabes. (They are not yet supprted in the user 
interface)
- Versions 2.18 and 2.19 were skipped.
* Fri Jan 28 2005 Mark de Does <mark@mdedoes.com> 2.17-1
- New upstream release.
See http://ftp.nluug.nl/pub/editors/ted/announce.html
- Numbered lists finished.
- Yet more footnote bugs fixed.
- Behaviour of explicit line and page breaks simulates that of MS-Word.
- Made a configurable resources mechanism that works without X11 
for command line calls.
- Improvements in numbered lists functionality: Opened user interface.
- Preliminary support for 'shapes': The newer Word figures mechanism. 
The Word 97 Drawing Objects are mapped to 'shapes'.
* Thu Apr 01 2004 Mark de Does <mark@mdedoes.com> 2.16-1
- New upstream release.
See http://ftp.nluug.nl/pub/editors/ted/announce.html
- Fonts can be embedded in the printout to print on any printer.
- Version 2.15 was skipped.
* Sun Apr 06 2003 Mark de Does <mark@mdedoes.com> 2.14-1
- New upstream release.
See http://ftp.nluug.nl/pub/editors/ted/announce.html
- Table Headers
- Tabs in page headers/footers compatible with MS-Word 2000
* Sat Mar 15 2003 Mark de Does <mark@mdedoes.com> 2.13-1
- New upstream release.
See http://ftp.nluug.nl/pub/editors/ted/announce.html
- Options for making much more compact PostScript when a document 
is printed.
- Support for smallcaps.
- Upgraded the pdfmarks to a version that more recent versions of 
acroread support.
* Sun Dec 01 2002 Mark de Does <mark@mdedoes.com> 2.12-1
- New upstream release.
See http://ftp.nluug.nl/pub/editors/ted/announce.html
- Solid shading of paragraphs and table cells.
- Colored table cell borders, Text colors.
* Fri Mar 01 2002 Mark de Does <mark@mdedoes.com> 2.11-1
- New upstream release.
See http://ftp.nluug.nl/pub/editors/ted/announce.html
- Footnotes and endnotes.
- Detailed manipulation of the tabulator settings with a 'Tabs' tool.
* Mon Apr 30 2001 Mark de Does <mark@mdedoes.com> 2.10-1
- New upstream release.
See http://ftp.nluug.nl/pub/editors/ted/announce.html
- Widow/Orphan control.
- Keep paragraph on one page, Keep paragraph on same page as next supported.
- Better support for sending MIME and HTML mail. Include images in message.
* Wed Jan 31 2001 Mark de Does <mark@mdedoes.com> 2.9-1
- New upstream release.
See http://ftp.nluug.nl/pub/editors/ted/announce.html
- Full support for page headers and footers including page numbers.
- Command line conversion to html or to plain text.
- The improvements in WMF drawing and support for PAGEREF fields make 
the pdf files from the printed postscript very similar to the RTF 
original.
* Sat Apr 15 2000 Mark de Does <mark@mdedoes.com> 2.8-1
- New upstream release.
See http://ftp.nluug.nl/pub/editors/ted/announce.html
- Editing behavior closer to that of Word. E.G. support for Control key 
in navigation and selection has been extended.
- The spelling packages have been renamed since Ted 2.6 to comply 
with naming conventions. If rpm complains about conflicts, please 
remove the conflicting old package using the command rpm -e old_package.
* Fri Dec 31 1999 Mark de Does <mark@mdedoes.com> 2.7-1
- New upstream release.
See http://ftp.nluug.nl/pub/editors/ted/announce.html
- A major step toward wysiwyg vertical layout: Pagination is visible 
on screen.
* Thu Sep 30 1999 Mark de Does <mark@mdedoes.com> 2.6-1
- New upstream release.
See http://ftp.nluug.nl/pub/editors/ted/announce.html
- The HTML produced is now simpler and syntactically correct.
* Sat Jul 31 1999 Mark de Does <mark@mdedoes.com> 2.5-1
- New upstream release.
See http://ftp.nluug.nl/pub/editors/ted/announce.html
- Right aligned and centered text are supported.
* Fri May 21 1999 Mark de Does <mark@mdedoes.com> 2.4-1
- New upstream release.
See http://ftp.nluug.nl/pub/editors/ted/announce.html
- Little bugs that prevented Ted from working with other than Latin1 
fonts removed.
- The Ted document has been improved. It is added as an online document.
* Thu Mar 11 1999 Mark de Does <mark@mdedoes.com> 2.3-1
- New upstream release.
See http://ftp.nluug.nl/pub/editors/ted/announce.html
- Printing of tables.
* Sat Feb 06 1999 Mark de Does <mark@mdedoes.com> 2.2-1
- New upstream release.
See http://ftp.nluug.nl/pub/editors/ted/announce.html
- Usability improvements.
- Version 2.1 was skipped.
* Mon Nov 09 1998 Mark de Does <mark@mdedoes.com> 2.0-1
- First upstream release.
See http://ftp.nluug.nl/pub/editors/ted/announce.html
