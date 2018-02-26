%define srcname kmatrix3d
Name: kde-screensaver-%srcname
Version: 0.1
Release: alt2.6

Summary: OpenGL Matrix-alike 3D Screensaver for KDE
License: GPL
Group: Graphical desktop/KDE
Packager: Motsyo Gennadi <drool@altlinux.ru>

Url: http://kmatrix3d.sourceforge.net/
Source0: http://prdownloads.sourceforge.net/kmatrix3d/kmatrix3d-%version.tar.bz2
Patch0: %srcname-admin-new-autotools.diff
Patch1: %srcname-unused-variables.patch
Patch2: %srcname-fix-desktop-file.patch
Patch3: %srcname-fix-link.patch

Requires: kdebase-wm kdelibs >= %{get_version kdelibs}

BuildRequires(pre): kdelibs

# Automatically added by buildreq on Sat Feb 26 2011 (-bi)
BuildRequires: gcc-c++ imake kdelibs-devel libXt-devel libfreeglut-devel xorg-cf-files

%description
A nice 3D matrix OpenGL screen saver for KDE.

%prep
%setup -q -n %srcname
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
make -f admin/Makefile.common
%configure --disable-rpath --without-arts
%make_build CXXFLAGS+="-I%_includedir/tqtinterface"

%install
%makeinstall

%find_lang kmatrix3d --with-kde

%files -f kmatrix3d.lang
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/*
%_datadir/applnk/*/*/*.desktop
%_datadir/apps/%srcname

%changelog
* Thu May 17 2012 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt2.6
- fix build with recent automake

* Sat Feb 26 2011 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt2.5
- rebuild without aRts
- refresh BuildRequires (buildreq -bi)

* Fri Nov 12 2010 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt2.4
- fix build (libGLU-devel)

* Sun May 31 2009 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt2.3
- normal fix for automake-1.11
- refresh BuildRequires (run buildreq -bi script)
- cleanup spec

* Mon May 25 2009 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt2.2
- ugly fix for automake-1.11

* Tue Dec 25 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt2.1
- fix for autotools-2.6 (thanks to wRAR for hints again)

* Tue Sep 11 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt2
- change GROUP from 'Toys' to 'Graphical desktop/KDE'

* Thu May 17 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt1
- initial build for sisyphus
- enabled patch3

* Sat Feb 24 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt0.M24.1.1
- add kmatrix3d-fix-link.patch (--as-needed) by Damir Shayhutdinov
    (disabled, not actual for ALM-2.4)

* Sat Feb 24 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt0.M24.1
- initial build for ALT Linux 2.4 Master
- use patches from OpenSUSE package
