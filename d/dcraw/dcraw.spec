Name: dcraw
Version: 9.12
Release: alt1

Summary: Command-line decoder for raw digital photos
License: Freely distributable
Group: Graphics

URL: http://www.cybercom.net/~dcoffin/dcraw
Source: %url/archive/dcraw-%version.tar.gz

Source3: %url/dcraw.html
Source4: %url/.badpixels
Source5: %url/ahd_maze.png
Source6: %url/vng_grid.png

# Automatically added by buildreq on Sun Jul 31 2011
BuildRequires: libjasper-devel libjpeg-devel liblcms-devel

# TODO: patch to use lcms2 instead of lcms

%description
dcraw decodes raw photos, displays metadata, and extracts thumbnails.

%prep
%setup -n dcraw

install -m644 %SOURCE3 %SOURCE4 %SOURCE5 %SOURCE6 .

%build
# -O4 shows best speed in benchmarks!
%define _optlevel 4
gcc -I/usr/include/lcms -DLOCALEDIR=\"/usr/share/locale/\" \
	%optflags -o dcraw dcraw.c -ljpeg -lm -llcms -ljasper

%install
install -pD -m755 dcraw %buildroot%_bindir/dcraw
install -pD -m644 dcraw.1 %buildroot%_man1dir/dcraw.1

for lang in ca cs da de eo es fr hu it pl pt ru sv zh_CN zh_TW
do
  mkdir -p -m 755 %buildroot%_mandir/$lang/man1
  cp dcraw_$lang.1 %buildroot%_mandir/$lang/man1/dcraw.1
  mkdir -p -m 755 %buildroot/usr/share/locale/$lang/LC_MESSAGES
  msgfmt -o %buildroot/usr/share/locale/$lang/LC_MESSAGES/dcraw.mo dcraw_$lang.po
done
# No man page exists for Dutch localisation
  mkdir -p -m 755 %buildroot/usr/share/locale/nl/LC_MESSAGES
  msgfmt -o %buildroot/usr/share/locale/nl/LC_MESSAGES/dcraw.mo dcraw_nl.po

%find_lang --with-man dcraw

%files -f dcraw.lang
%_bindir/*
# original man page listed by find_lang
#%_man1dir/*
%doc dcraw.html *.png .badpixels

%changelog
* Mon Jan 02 2012 Victor Forsiuk <force@altlinux.org> 9.12-alt1
- 9.12

* Sun Oct 23 2011 Victor Forsiuk <force@altlinux.org> 9.11-alt1
- 9.11

* Sun Jul 31 2011 Victor Forsiuk <force@altlinux.org> 9.10-alt1
- 9.10

* Wed May 11 2011 Victor Forsiuk <force@altlinux.org> 9.08-alt1
- 9.08

* Mon Apr 04 2011 Victor Forsiuk <force@altlinux.org> 9.07-alt1
- 9.07

* Tue Feb 01 2011 Victor Forsiuk <force@altlinux.org> 9.06-alt1
- 9.06

* Mon Dec 06 2010 Victor Forsiuk <force@altlinux.org> 9.05-alt1
- 9.05

* Wed Aug 04 2010 Victor Forsiuk <force@altlinux.org> 9.04-alt1
- 9.04

* Thu Jul 01 2010 Victor Forsiuk <force@altlinux.org> 9.03-alt1
- 9.03

* Fri Jun 11 2010 Victor Forsiuk <force@altlinux.org> 9.02-alt1
- 9.02

* Mon May 31 2010 Victor Forsiuk <force@altlinux.org> 9.01-alt1
- 9.01

* Mon Dec 28 2009 Victor Forsyuk <force@altlinux.org> 8.99-alt1
- 8.99

* Mon Sep 28 2009 Victor Forsyuk <force@altlinux.org> 8.98-alt1
- 8.98

* Wed Sep 02 2009 Victor Forsyuk <force@altlinux.org> 8.97-alt1
- 8.97

* Mon Jun 22 2009 Victor Forsyuk <force@altlinux.org> 8.95-alt1
- 8.95

* Mon Feb 09 2009 Victor Forsyuk <force@altlinux.org> 8.91-alt1
- 8.91

* Fri Jan 23 2009 Victor Forsyuk <force@altlinux.org> 8.90-alt1
- 8.90

* Mon Dec 08 2008 Victor Forsyuk <force@altlinux.org> 8.89-alt1
- 8.89

* Fri Sep 19 2008 Victor Forsyuk <force@altlinux.org> 8.88-alt1
- 8.88

* Sun Aug 17 2008 Victor Forsyuk <force@altlinux.org> 8.87-alt1
- 8.87

* Tue Apr 29 2008 Victor Forsyuk <force@altlinux.org> 8.86-alt1
- 8.86

* Mon Apr 07 2008 Victor Forsyuk <force@altlinux.org> 8.84-alt1
- 8.84

* Thu Mar 13 2008 Victor Forsyuk <force@altlinux.org> 8.83-alt1
- 8.83

* Wed Dec 12 2007 Victor Forsyuk <force@altlinux.org> 8.81-alt1
- 8.81

* Wed Nov 14 2007 Victor Forsyuk <force@altlinux.org> 8.80-alt1
- 8.80

* Thu Nov 01 2007 Victor Forsyuk <force@altlinux.org> 8.78-alt1
- 8.78

* Mon Jul 23 2007 Victor Forsyuk <force@altlinux.org> 8.77-alt1
- 8.77

* Mon Jun 04 2007 Victor Forsyuk <force@altlinux.org> 8.73-alt1
- 8.73
- Compile with -O4 optlevel as author suggested.
- Package messages and man-pages localisations.

* Fri May 04 2007 Victor Forsyuk <force@altlinux.org> 8.71-alt1
- 8.71

* Thu Mar 22 2007 Victor Forsyuk <force@altlinux.org> 8.68-alt1
- 8.68

* Mon Feb 05 2007 Victor Forsyuk <force@altlinux.org> 8.53-alt1
- 8.53

* Tue Dec 12 2006 Victor Forsyuk <force@altlinux.org> 8.45-alt1
- 8.45

* Fri Jul 28 2006 Victor Forsyuk <force@altlinux.ru> 8.26-alt1
- 8.26

* Thu Apr 13 2006 Victor Forsyuk <force@altlinux.ru> 8.13-alt1
- 8.13

* Fri Feb 10 2006 Victor Forsyuk <force@altlinux.ru> 8.05-alt1
- 8.05
- v8 major changes:
  + Added "-e" option to extract thumbnail images.
  + Added "-o" option to select output colorspace.
  + Enabled "-p" option for ICC color profiles by default.
  + Generate monochrome or four-color output in some cases.
  + Use more memory to flip images five times faster.
  + Use the correct formula for Kodak YCbCr images.

* Tue Jan 17 2006 Victor Forsyuk <force@altlinux.ru> 7.94-alt1
- 7.94

* Mon Nov 21 2005 Victor Forsyuk <force@altlinux.ru> 7.84-alt1
- 7.84

* Thu Sep 29 2005 Victor Forsyuk <force@altlinux.ru> 7.70-alt1
- 7.70

* Tue Jul 12 2005 Victor Forsyuk <force@altlinux.ru> 7.39-alt1
- 7.39

* Fri May 20 2005 Victor Forsyuk <force@altlinux.ru> 7.22-alt1
- Build with liblcms.
- Changes: 
  + Added color matrices for the Canon EOS D6000 and NIKON D2X.
  + Set "filters" based on rotation for Leaf Valeo backs.
  + Added "-z" option to fix timestamps.
  + Added the Nikon E880.
  + Added "-j" option, check for corrupt CRW files.
  + Added colorcheck() function, and a color matrix for
    the MINOLTA DiMAGE Z2, created with colorcheck().

* Tue Apr 26 2005 Victor Forsyuk <force@altlinux.ru> 7.16-alt1
- Changes: Added the Casio EX-P505.

* Mon Apr 25 2005 Victor Forsyuk <force@altlinux.ru> 7.15-alt1
- Changes:
  + [7.15] Support little-endian Phase One images
  + [7.14] Added support for the Nikon D2Hs
  + [7.13] Added camera white balance for the Nikon D2X

* Mon Apr 11 2005 Victor Forsyuk <force@altlinux.ru> 7.12-alt1
- Fix URL.
- Change version from RCS revision to announced in program output.

* Fri Jun 13 2003 Michael Shigorin <mike@altlinux.ru> 1.119-alt1
- built for ALT Linux
- based on initial package by Pyatnitskich Evgeniy <pem@rbcmail.ru>
  - spec cleanup
    - renamed from raw-tools to dcraw as it's all that's left
    - fixed version to RCS one
    - fixed package group
    - clarified license
  - gimp plugin moved to gimp-plugin-rawphoto
  - built with ljpeg_decode thus should support EOS-1D RAWs
  - added webpage to docs
