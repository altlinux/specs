Name: xplanet
Version: 1.2.2
Release: alt1

Summary: OpenGL based planet renderer
License: GPL
Group: Toys

Url: http://xplanet.sourceforge.net
Source0: http://prdownloads.sourceforge.net/%name/%name-%version.tar.gz
Patch0: xplanet-1.2.0-g++43-missing-header.patch
Patch1:	xplanet-1.2.1-g++44.patch

# Automatically added by buildreq on Thu Sep 08 2005
BuildRequires: fontconfig-devel freetype2-devel gcc4.3-c++ glib2-devel libjpeg-devel
BuildRequires: libpango-devel libpng-devel libstdc++-devel libtiff-devel
BuildRequires: libungif-devel pkgconfig zlib-devel netpbm libXt-devel
BuildRequires: perl-Math-Complex

Packager: Ilya Mashkin <oddity@altlinux.ru>

%description
Xplanet is similar to Xearth, where an image of the earth is rendered
into an X window. Azimuthal, Mercator, Mollweide, orthographic, or
rectangular projections can be displayed as well as a window with a
globe the user can rotate interactively. The other planets and some
satellites may also be displayed. The latest version, as well as maps
for other planets can be found at http://xplanet.sourceforge.net.
Xplanet can support separate night and day maps, as well as a separate
cloud map.

%prep
%setup
%patch0 -p1 -b .gcc43
#patch1 -p1 -b .g++

%build
export CC=gcc-4.3 CXX=g++-4.3
%configure --with-cspice=no
%make

%install
%makeinstall

%files
%_bindir/*
%_datadir/%name/*
%_man1dir/*
%doc ChangeLog README AUTHORS TODO

%changelog
* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 1.2.2-alt1
- 1.2.2 (thx fedorawatch)
- patch1 merged upstream

* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 1.2.1-alt1.1.1
- rebuilt with perl 5.12

* Sat Aug 08 2009 Ilya Mashkin <oddity@altlinux.ru> 1.2.1-alt1.1
- rebuild with gcc4.3

* Fri Jul 10 2009 Ilya Mashkin <oddity@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Fri Nov 13 2008 Ilya Mashkin <oddity@altlinux.ru> 1.2.0-alt3
- fix build with gcc4.3

* Tue Oct 06 2008 Ilya Mashkin <oddity@altlinux.ru> 1.2.0-alt2.1
- rebuild

* Tue Feb 14 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2.0-alt2
- Enabled pnm support
- Removed xorg-x11-devel-static from buildrequires
- Added libXt-devel to buildrequires

* Fri Sep 09 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2.0-alt1
- Initial build for Sisyphus
