Name: dzen2
Version: 0.9.5
Release: alt2.svn271
Summary: A general purpose messaging and notification program. 

License: MIT/X
Group: Graphical desktop/Other

Url: http://gotmor.googlepages.com/dzen
# http://dzen.googlecode.com/svn/trunk
Source: %name-%version.tar.bz2
Packager: Timur Batyrshin <erthad@altlinux.org>

Patch0: dzen2-alt-gcpubar.patch
Patch1: dzen2-alt-slavemaxlines.patch

# Automatically added by buildreq on Fri Aug 22 2008
BuildRequires: libX11-devel libXft-devel

%description
Dzen is a general purpose messaging, notification and menuing program for X11.
It was desigend to be scriptable in any language and integrate well with window
managers like dwm, wmii and xmonad though it will work with any windowmanger.

%prep
%setup
pwd
#%patch0 -p0
#%patch1 -p0
subst 's,./dzen2,/usr/bin/dzen2,' help

%build
make
cd gadgets
make

%install
install -pD -m0755 dzen2 %buildroot%_bindir/dzen2
install -pD -m0755 help %buildroot%_docdir/%name/help
install -pD -m0644 CREDITS %buildroot%_docdir/%name/CREDITS
install -pD -m0644 LICENSE %buildroot%_docdir/%name/CREDITS
install -pD -m0644 README %buildroot%_docdir/%name/README
install -pD -m0644 README.dzen %buildroot%_docdir/%name/README.dzen

install -pD -m0644 bitmaps/alert.xbm %buildroot%_docdir/%name/bitmaps/alert.xbm
install -pD -m0644 bitmaps/ball.xbm %buildroot%_docdir/%name/bitmaps/ball.xbm
install -pD -m0644 bitmaps/battery.xbm %buildroot%_docdir/%name/bitmaps/battery.xbm
install -pD -m0644 bitmaps/envelope.xbm %buildroot%_docdir/%name/bitmaps/envelope.xbm
install -pD -m0644 bitmaps/music.xbm %buildroot%_docdir/%name/bitmaps/music.xbm
install -pD -m0644 bitmaps/pause.xbm %buildroot%_docdir/%name/bitmaps/pause.xbm
install -pD -m0644 bitmaps/play.xbm %buildroot%_docdir/%name/bitmaps/play.xbm
install -pD -m0644 bitmaps/volume.xbm %buildroot%_docdir/%name/bitmaps/volume.xbm

install -pD -m0755 gadgets/dbar %buildroot%_bindir/dbar
install -pD -m0755 gadgets/gdbar %buildroot%_bindir/gdbar
install -pD -m0755 gadgets/gcpubar %buildroot%_bindir/gcpubar
install -pD -m0755 gadgets/textwidth %buildroot%_bindir/textwidth

install -pD -m0755 gadgets/kittscanner.sh %buildroot%_docdir/%name/gadgets/kittscanner.sh
install -pD -m0755 gadgets/noisyalert.sh %buildroot%_docdir/%name/gadgets/noisyalert.sh
install -pD -m0755 gadgets/README.kittscanner %buildroot%_docdir/%name/gadgets/README.kittscanner
install -pD -m0755 gadgets/README.dbar %buildroot%_docdir/%name/gadgets/README.dbar
install -pD -m0755 gadgets/README.gdbar %buildroot%_docdir/%name/gadgets/README.gdbar
install -pD -m0755 gadgets/README.gcpubar %buildroot%_docdir/%name/gadgets/README.gcpubar
install -pD -m0755 gadgets/README.textwidth %buildroot%_docdir/%name/gadgets/README.textwidth

%files
%_bindir/*
%doc %_docdir/%name/

%changelog
* Tue Dec 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt2.svn271
- Avoid strip binary files

* Sun Dec 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1.svn271
- Version 0.9.5

* Tue Jan 12 2010 Timur Batyrshin <erthad@altlinux.org> 0.8.5-alt4.svn267.1
- svn267

* Fri Sep 05 2008 Timur Batyrshin <erthad@altlinux.org> 0.8.5-alt3
- fixed crash on -l 0 command line param

* Tue Aug 26 2008 Timur Batyrshin <erthad@altlinux.org> 0.8.5-alt2
- fixed gcpubar to work correctly with -c 1

* Mon Aug 25 2008 Timur Batyrshin <erthad@altlinux.org> 0.8.5-alt1
- Initial build for Sisyphus

