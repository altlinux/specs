Name: cfdg
Version: 3.0.8
Release: alt1

Summary: Context Free is a program that generates images from written instructions
License: GPLv2
Group: Graphics
Url: http://www.contextfreeart.org

Source: %name-%version.tar.bz2
Patch: cfdg-2.2-alt-DSO.patch
Patch1: cfdg-2.2-alt-flex.patch

# Automatically added by buildreq on Thu Apr 09 2009
BuildRequires: flex gcc-c++ libpng-devel

%description
Chris Coyne created a small language for design grammars called CFDG.
These grammars are sets of non-deterministic rules to produce images.
The images are surprisingly beautiful, often from very simple grammars.

Context Free is a full graphical environment for editing, rendering,
and exploring CFDG design grammars.

Features:

    * Simultaneously available for Macintosh, Windows and Posix/Unix.
    * Progressive image update: watch it generate
    * Save generated images in PNG or SVG format.
    * Produce animations
    * Edit grammars and re-render easily.
    * Render very large images (as large as 100 Mega-pixels).
    * Can handle generated images with millions of shapes.
    * Carefully tuned graphics rendering
    * Many built-in examples
    * Automatic checking for updates (Mac only).
    * It's free, as in beer and as in speech. 

%prep
%setup
#patch -p2
#patch1 -p2

%build
%make_build

%install
install -pD -m0755 cfdg %buildroot%_bindir/cfdg

%files
%doc LICENSE.txt README.txt input
%_bindir/*

%changelog
* Fri Sep 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.8-alt1
- Version 3.0.8

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt3.2
- Rebuilt with libpng15

* Tue Jul 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt3.1
- Fixed build

* Tue Jun 23 2009 Timur Batyrshin <erthad@altlinux.org> 2.2-alt3
- rebuild with libpng-1.2.37-alt2

* Wed May 13 2009 Timur Batyrshin <erthad@altlinux.org> 2.2-alt2
- gcc version fix

* Tue Apr 07 2009 Timur Batyrshin <erthad@altlinux.org> 2.2-alt1
- initial build for sisyphus

