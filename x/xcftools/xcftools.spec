Name: xcftools
Version: 1.0.7
Release: alt1

Summary: Tools for extracting information from the Gimp's native file format XCF.
Group: Graphics
License: GPL
Url: http://henning.makholm.net/xcftools/
Packager: Afanasov Dmitry <ender@altlinux.org>

BuildRequires: libpng-devel

Source: %name-%version.tar
Patch: %name-%version-alt-changes.patch

%description
Tools is a set of fast command-line tools for extracting information from the
Gimp's native file format XCF. The tools are designed to allow efficient use of
layered XCF files as sources in a build system that use 'make' and similar
tools to manage automatic processing of the graphics. These tools work
independently of the Gimp engine and do not require the Gimp to even be
installed.

"xcf2pnm" converts XCF files to ppm, pgm or pbm format, flattening layers if
necessary. If the image contains transparency, an alpha map can be written to a
separate file, or a background color can be specified on the command line. 

"xcf2png" converts XCF files to PNG format, flattening layers if necessary.
Transparency information can be kept in the image, or a background color can be
specified on the command line. 

"xcfinfo" lists information about layers in an XCF file. 

"xcfview" is a wrapper script that flattens an XCF image and displays it using
an external PNG/PPM viewer. To use this script, you must make sure also to
install an appropriate external viewer, as well as the mime-support package
which provides the mailcap database. 

The tools can either flatten an XCF file as given, or extract specific layers
named on the command line.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_bindir/xcf2png
%_bindir/xcf2pnm
%_bindir/xcfinfo
%_bindir/xcfview
#/usr/lib/mime/packages/xcftools
%doc ChangeLog README
%lang(da) %_mandir/da/man1/*
%_man1dir/*

%changelog
* Wed Jul 08 2009 Afanasov Dmitry <ender@altlinux.org> 1.0.7-alt1
- 1.0.7 release
- remove fix-flattenIncrementally (applied in upstream)

* Tue Jun 23 2009 Afanasov Dmitry <ender@altlinux.org> 1.0.4-alt3
- rebuild with libpng12-1.2.37-al2

* Sat Jun 20 2009 Afanasov Dmitry <ender@altlinux.org> 1.0.4-alt2
- fix buffer overflos (closes: #20502)

* Fri May 15 2009 Afanasov Dmitry <ender@altlinux.org> 1.0.4-alt1
- apply alt changes patch:
  + fix linking: move -llib to the end.
  + add DESTDIR support in Makefile.
- use autoreconf by default.
- initial build

