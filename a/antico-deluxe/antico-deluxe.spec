%define srcname anticodeluxe

Name: antico-deluxe
Version: 0.1.96
Release: alt1.1
Summary: Antico Deluxe is a Qt4 Window/Desktop manager
Source: http://anticodeluxe.googlecode.com/files/%srcname-%version.tar.bz2
Source1: 07antico-deluxe
Packager: Boris Savelev <boris@altlinux.org>
Patch: %srcname-0.1.96-link.patch
Patch1: antico-deluxe-0.1.96-alt-DSO.patch
Url: http://code.google.com/p/anticodeluxe/
Group: Graphical desktop/Other
License: GPLv2 Artistic

Requires: lib%name = %version-%release

# Automatically added by buildreq on Wed Mar 11 2009 (-bi)
BuildRequires: ImageMagick gcc-c++ libalsa-devel libao-devel libqt4-devel libvorbis-devel

%description
Antico Deluxe is a fork of famous Antico WM/DE (http://antico.wordpress.com/),
with some new features added and many new planned.

The goal is to create very simple and fast Window/Desktop manager with very
aesthetic and familiar look and feel. A very few parameters are autoconfigured
(and can be changed) in few config files, avoiding unnecessary complications,
following the K.I.S.S. philosophy. Any other configurations like themes, icons
etc. should be avoided or minimal. Keeping in very small size while having
relatively rich feature set makes AnticoDeluxe very suitable for netbooks and
low-end computers. The overall look and feel have to be very close to MacOSX
look and feel, which is ORIGINAL WORK FROM APPLE INC.

%package -n lib%name
Summary: Shared libraries for Antico Deluxe
Group: System/Libraries

%description -n lib%name
Shared libraries for Antico Deluxe

%package -n lib%name-devel
Summary: Antico Deluxe header files
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
%name-devel contains the header files needed to develop
programs which make use of Antico Deluxe.

%prep
%setup -q -n %srcname
%patch0 -p1
%patch1 -p2

find -type f -name \*.pro | xargs subst "s|/usr/lib|%_libdir|g"

%build
export PATH=$PATH:%_qt4dir/bin
qmake "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" %name.pro
%make_build

%install
%make INSTALL_ROOT=%buildroot install
install -Dp -m 0644 %SOURCE1 %buildroot%_x11sysconfdir/wmsession.d/07antico-deluxe

mkdir -p %buildroot/%_niconsdir
convert -resize 32x32 wm/theme/default/appicon.png %buildroot%_niconsdir/%name.png

%files
%doc AUTHORS CHANGELOG ROADMAP test BUGS README myxephyr
%dir %_datadir/themes/antico
%dir %_datadir/themes/antico/default
%_bindir/*
%_niconsdir/%name.png
%_datadir/themes/antico/default/*
%_x11sysconfdir/wmsession.d/07antico-deluxe

%files -n lib%name
%_libdir/libame.so.*

%files -n lib%name-devel
%dir %_includedir/ame
%_libdir/libame.so
%_includedir/ame/*

%changelog
* Tue Jul 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.96-alt1.1
- Fixed build

* Tue May 12 2009 Boris Savelev <boris@altlinux.org> 0.1.96-alt1
- initial build for Sisyphus



