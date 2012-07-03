Name: clens
Version: 0.2
Release: alt3

Summary: Corrects lens barrel distortion
License: GPL
Group: Graphics

Url: http://sourceforge.net/projects/panotools
Source0: http://dl.sourceforge.net/panotools/clens-%version.tar.gz
Source1: http://dl.sourceforge.net/hugin/PTLensDB_06-02-08.zip
Patch0: clens-mdk-profile.patch
Patch1: clens-0.2-ptstitcher2nona.patch

# Automatically added by buildreq on Mon Jul 16 2007
BuildRequires: gcc-c++ unzip
# we need nona to actually do correction job:
Requires: hugin

%description
A command-line version of PTLens. Compares your JPEG images with a lens
database and automatically corrects lens barrel distortion.

%prep
%setup
%patch0 -p0
%patch1 -p1
unzip -q %SOURCE1 -d data

%build
%__subst 's|\@\@PROFILE\@\@|%_datadir/%name/profile.txt|g' src/main.c
%configure
%make_build

%install
%make_install install DESTDIR=%buildroot
rm -f %buildroot%_datadir/clens/README
install data/*.txt %buildroot%_datadir/clens

%files
%_bindir/*
%_man1dir/*
%_datadir/clens
%exclude %_includedir
%exclude /usr/doc/clens

%changelog
* Mon Jul 16 2007 Victor Forsyuk <force@altlinux.org> 0.2-alt3
- Better Summary and description.
- Include lens profiles from hugin project.
- Patch (from Mandriva) to set default profile path.
- Change default stitcher from PTStitcher to nona.
- Added run-time requirement of hugin package (contains nona stitcher).

* Mon Sep 05 2005 Sergei Epiphanov <serpiph@altlinux.ru> 0.2-alt2
- Fixing for ALT Linux

* Tue Jul 26 2005 Sergei Epiphanov <serpiph@nikiet.ru> 0.2-alt1
- initial build
