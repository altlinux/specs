Name:		backlite
Summary:	%name is a lite version of k9copy
License:	GPLv2
Group:		Video
Version:	1.0.1
Release:	alt1.2
Packager:	Motsyo Gennadi <drool@altlinux.ru>
URL:		http://k9copy.sourceforge.net/
Source0:	http://downloads.sourceforge.net/k9copy/%name-%version.tar.gz

Patch0:		%name-0.2.0-alt_path.diff
Patch1: %name-ffmpeg-0.7.1.diff

BuildRequires: gcc-c++ libavformat-devel libmpeg2-devel libqt4-devel phonon-devel

%description
backlite is a lite version of k9copy which can run without all the KDE stuff.
It means that it doesn't have dependencies with KDE libraries and can be built without them.

%prep
%setup
%patch0 -p1
%patch1 -p2

%build
export PATH=$PATH:%_qt4dir/bin
qmake "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" "PREFIX=%prefix" %name.pro
%make_build

%install
make INSTALL_ROOT=%buildroot install

%files
%_bindir/*
%_desktopdir/*.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_iconsdir/hicolor/22x22/apps/%name.png
%_pixmapsdir/%name.png

%changelog
* Sat Aug 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.2
- Rebuilt with ffmpeg 0.7.1

* Mon Oct 11 2010 Motsyo Gennadi <drool@altlinux.ru> 1.0.1-alt1.1
- fix BuildReq for phonon package

* Sat Aug 14 2010 Motsyo Gennadi <drool@altlinux.ru> 1.0.1-alt0.M51.1
- build for M51

* Fri Aug 13 2010 Motsyo Gennadi <drool@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Sun Dec 20 2009 Motsyo Gennadi <drool@altlinux.ru> 0.2.0-alt1
- initial build for ALT Linux
