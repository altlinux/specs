Name: macrofusion
Version: 0.7.3
Release: alt1

Summary: GUI to combine photos to get deeper DOF or HDR
License: GPLv3+
Group: Graphics

URL: http://sourceforge.net/projects/macrofusion/
Source: http://download.sourceforge.net/macrofusion/macrofusion_%version.orig.tar.gz
Patch1: macrofusion-0.7.2-notry.patch
Patch2: macrofusion-0.7.2-desktop.patch

Requires: enblend hugin

# Automatically added by buildreq on Sun Jan 01 2012 (-bi)
BuildRequires: python-module-distribute rpm-build-gir

BuildArch: noarch

%description
MacroFusion is a neat little GUI for great tool Enfuse (command line).
It makes easy fusion few photos to one with great DOF (Deep of Field) or
DR (Dynamic Range). It can be useful for every macro lovers or
landscapers.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build

%install
install -pDm755 macrofusion.py %buildroot%_bindir/macrofusion
install -d %buildroot%_datadir/mfusion
cp -a ui %buildroot%_datadir/mfusion
install -pDm644 images/macrofusion.png %buildroot%_datadir/pixmaps/macrofusion.png
install -pDm644 images/logoSplash.png %buildroot%_datadir/mfusion/images/logoSplash.png
install -pDm644 macrofusion.desktop %buildroot%_desktopdir/macrofusion.desktop

%files
%_bindir/*
%_datadir/mfusion
%_pixmapsdir/*
%_desktopdir/*

%changelog
* Sat Feb 25 2012 Victor Forsiuk <force@altlinux.org> 0.7.3-alt1
- 0.7.3

* Sun Jan 01 2012 Victor Forsiuk <force@altlinux.org> 0.7.2-alt1
- Initial build.
