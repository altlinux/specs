BuildRequires: desktop-file-utils
%define		git 20140105

Name:		fatrat
Version:	1.2.0
Release:	alt1.beta2.%git.2
Summary:	FatRat is an open source download/upload manager
License: 	GPLv2
Group: 		Networking/File transfer
Url:		http://fatrat.dolezel.info/
# https://github.com/LubosD/fatrat.git
Source:	%name-%version.tar
Patch1: %name-%version-alt-build.patch

Requires:	libqt4-core

# Automatically added by buildreq on Wed Mar 16 2011 (-bi)
BuildRequires: ImageMagick-tools cmake gcc-c++ libcurl-devel libgloox-devel libpion-net-devel libqt4-help libqt4-svg libqt4-webkit libqt4-xmlpatterns phonon-devel 

BuildRequires: /usr/bin/qcollectiongenerator-qt4
BuildRequires: libtorrent-rasterbar-devel libattr-devel libkqueue-devel
BuildRequires: boost-devel boost-asio-devel

%description
FatRat is an open source download manager for Linux
written in C++ and built on top of the Trolltech Qt4
library. It is rich in features and is continuously
extended.

%package -n %name-devel
Summary: FatRat header files
Group: Development/C++
# #Requires: %name = %version-%release
BuildArch: noarch

%description -n %name-devel
%name-devel contains the header files needed to develop
programs which make use of FatRat.

%prep
%setup
%patch1 -p1

%build
export PATH=$PATH:%_qt4dir/bin
doc/generate.sh
%add_optflags -fpermissive
%add_optflags -DWITH_SFTP
cmake \
	-DCMAKE_INSTALL_PREFIX=%_prefix \
	-DCMAKE_INSTALL_LIBDIR=%_libdir \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DWITH_SFTP=ON \
	-DWITH_BITTORRENT=ON \
	-DWITH_JABBER=ON \
	-DWITH_NLS=ON \
	-DWITH_WEBINTERFACE=ON \
	-DWITH_CURL=ON \
	-DWITH_CXX0X=ON \
	-DWITH_DOCUMENTATION=ON

%install
%makeinstall_std VERBOSE=1

# Icons
mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 gfx/%name.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 gfx/%name.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 gfx/%name.png %buildroot%_miconsdir/%name.png
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=FileTransfer \
	%buildroot%_desktopdir/fatrat.desktop
ln -s %name %buildroot%_bindir/%name-nogui

%files
%dir %_datadir/%name
%_bindir/%name
%_bindir/%name-nogui
%_bindir/%name-conf
%_desktopdir/%name.desktop
%_datadir/%name
%_man1dir/%{name}*
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_pixmapsdir/%name.png

%files -n %name-devel
%dir %_includedir/%name
%_includedir/%name

%changelog
* Tue Aug 22 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.0-alt1.beta2.20140105.2
- Updated build with new dependencies and toolchain

* Sat Jun 13 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.2.0-alt1.beta2.20140105.1
- Rebuilt for gcc5 C++11 ABI.

* Fri May 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.beta2.20140105
- Version 1.2.0_beta2

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 1.1.3-alt0.2.20110222.qa10.1
- rebuild with boost 1.57.0

* Thu Jun 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt0.2.20110222.qa10
- Rebuilt with log4cplus 1.2.0-rc1

* Fri Nov 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt0.2.20110222.qa9
- Rebuilt with new libtorrent-rasterbar8

* Thu Jul 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt0.2.20110222.qa8
- Rebuilt with new libtorrent-rasterbar8

* Mon Feb 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt0.2.20110222.qa7
- Rebuilt with Boost 1.53.0

* Wed Feb 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt0.2.20110222.qa6
- Rebuilt with log4cplus 1.1.1-rc3

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt0.2.20110222.qa5
- Rebuilt with Boost 1.52.0

* Mon May 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt0.2.20110222.qa4
- Fixed build

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt0.2.20110222.qa3
- Rebuilt with Boost 1.49.0

* Sat Jul 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt0.2.20110222.qa2
- Rebuilt with Boost 1.47.0

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.1.3-alt0.2.20110222.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for fatrat
  * specfile-macros-get_dep-is-deprecated for fatrat
  * postclean-03-private-rpm-macros for the spec file

* Fri Mar 11 2011 Motsyo Gennadi <drool@altlinux.ru> 1.1.3-alt0.2.20110222
- git snapshot 20110222

* Wed Dec 08 2010 Motsyo Gennadi <drool@altlinux.ru> 1.1.3-alt0.2.20101121.1
- rebuild with new libtorrent-rasterbar

* Sun Nov 21 2010 Motsyo Gennadi <drool@altlinux.ru> 1.1.3-alt0.2.20101121
- git snapshot 20101121

* Tue Sep 21 2010 Motsyo Gennadi <drool@altlinux.ru> 1.1.3-alt0.2.20100920
- git snapshot 20100920

* Sun Aug 29 2010 Motsyo Gennadi <drool@altlinux.ru> 1.1.2.1-alt0.2.20100827
- git snapshot 20100827

* Tue Aug 24 2010 Motsyo Gennadi <drool@altlinux.ru> 1.1.2.1-alt0.2.20100823
- git snapshot 20100823

* Sun Aug 22 2010 Motsyo Gennadi <drool@altlinux.ru> 1.1.2.1-alt0.2.20100821
- git snapshot 20100821

* Thu Aug 19 2010 Motsyo Gennadi <drool@altlinux.ru> 1.1.2.1-alt0.2.20100818
- git snapshot 20100818

* Tue Aug 17 2010 Motsyo Gennadi <drool@altlinux.ru> 1.1.2.1-alt0.2.20100816
- git snapshot 20100816

* Sun Aug 15 2010 Motsyo Gennadi <drool@altlinux.ru> 1.1.2.1-alt0.2.20100808
- git snapshot 20100808

* Wed Jul 28 2010 Motsyo Gennadi <drool@altlinux.ru> 1.1.2.1-alt0.2.20100728
- git snapshot 20100728

* Sat Jun 19 2010 Motsyo Gennadi <drool@altlinux.ru> 1.1.2.1-alt0.2.20100602.1
- added Ukrainian translation
- enabled documentation

* Sun Jun 13 2010 Motsyo Gennadi <drool@altlinux.ru> 1.1.2.1-alt0.2.20100602
- git snapshot 20100602

* Wed Jun 02 2010 Motsyo Gennadi <drool@altlinux.ru> 1.1.2-alt1
- 1.1.2
  + build with SFTP, Bittorrent, jabber, web interface, cURL, NLS support

* Mon Nov 23 2009 Motsyo Gennadi <drool@altlinux.ru> 1.1.1-alt1.1
- rebuild with new libtorrent-rasterbar

* Wed Nov 18 2009 Motsyo Gennadi <drool@altlinux.ru> 1.1.1-alt1
- initial build for ALT Linux
