Name: cfdg
Version: 2.2
Release: alt3

Summary: Context Free is a program that generates images from written instructions
License: GPLv2
Group: Graphics
Url: http://www.contextfreeart.org

Packager: Timur Batyrshin <erthad@altlinux.org>
Source: %name-%version.tar.bz2

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

%build
%make_build

%install
install -pD -m0755 cfdg %buildroot%_bindir/cfdg

%files
%doc LICENSE.txt README.txt input
%_bindir/*

%changelog
* Tue Jun 23 2009 Timur Batyrshin <erthad@altlinux.org> 2.2-alt3
- rebuild with libpng-1.2.37-alt2

* Wed May 13 2009 Timur Batyrshin <erthad@altlinux.org> 2.2-alt2
- gcc version fix

* Tue Apr 07 2009 Timur Batyrshin <erthad@altlinux.org> 2.2-alt1
- initial build for sisyphus

