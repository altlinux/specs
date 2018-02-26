Name: epstool
Version: 3.08
Release: alt5

Summary: Working with EPS bounding boxes and preview images
License: GPLv2+
Group: Publishing
Url: http://www.cs.wisc.edu/~ghost/gsview/epstool.htm
Packager: Oleg Parashchenko <olpa@altlinux.ru>

# ftp://mirror.cs.wisc.edu/pub/mirrors/ghost/ghostgum/%name-%version.tar.gz
Source: %name-%version.tar

Patch1: epstool-3.08-olpa-nonconform-severity.patch
Patch2: epstool-3.08-alt-fixes.patch

Requires: ghostscript-classic

%description
Epstool is a utility to create or extract preview images in EPS files,
fix bounding boxes and convert to bitmaps. Features:

* Add EPSI, DOS EPS or Mac PICT previews.
* Extract PostScript from DOS EPS files.
* Uses Ghostscript to create preview bitmaps.
* Create a TIFF, WMF, PICT or Interchange
  preview from part of a bitmap created by Ghostscript.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
# No configure script
%__make

%install
%make_install install \
	EPSTOOL_ROOT=%buildroot/usr \
	EPSTOOL_MANDIR='$(EPSTOOL_ROOT)/share/man'
%find_lang %name

%files -f %name.lang
%doc doc/
%_bindir/*
%_man1dir/*

%changelog
* Fri Dec 12 2008 Dmitry V. Levin <ldv@altlinux.org> 3.08-alt5
- Fixed build with new toolchain.

* Fri Mar 03 2006 Oleg Parashchenko <olpa@altlinux.ru> 3.08-alt4
- Russian translation of "Summary" is deleted
- "Source" now is an URL not just a file name

* Wed Mar 01 2006 Oleg Parashchenko <olpa@altlinux.ru> 3.08-alt3
- Name of the patch is renamed to conform to ALT packaging guidelines.

* Sat Feb 18 2006 Oleg Parashchenko <olpa@altlinux.ru> 3.08-alt2
- Severity of early trailer is decreased to allow processing of some Adobe Illustrator files.

* Fri Feb 17 2006 Oleg Parashchenko <olpa@altlinux.ru> 3.08-alt1
- Initial build.
