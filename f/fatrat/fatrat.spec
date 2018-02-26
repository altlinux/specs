BuildRequires: desktop-file-utils
%define		git 20110222

Name:		fatrat
Version:	1.1.3
Release:	alt0.2.%git.qa4
Summary:	FatRat is an open source download/upload manager
License: 	GPLv2
Group: 		Networking/File transfer
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://fatrat.dolezel.info/
Source0:	http://www.dolezel.info/download/data/%name/%name-%version.tar.gz
Patch0:		%name-1.1.3-fix_old_libtorrent-rasterbar.diff
Patch1: %name-1.1.3-alt-link.diff

Requires:	libqt4-core

# Automatically added by buildreq on Wed Mar 16 2011 (-bi)
BuildRequires: ImageMagick-tools cmake gcc-c++ libcurl-devel libgloox-devel libpion-net-devel libqt4-help libqt4-svg libqt4-webkit libqt4-xmlpatterns libtorrent-rasterbar-devel phonon-devel

BuildRequires: /usr/bin/qcollectiongenerator-qt4

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
# #%patch0 -p1
%patch1 -p2

%build
export PATH=$PATH:%_qt4dir/bin
doc/generate.sh
cmake \
	-DCMAKE_INSTALL_PREFIX=%_prefix \
	-DCMAKE_CXX_FLAGS:STRING="%optflags -DBOOST_FILESYSTEM_VERSION=2" \
	-DCMAKE_C_FLAGS:STRING="%optflags -DBOOST_FILESYSTEM_VERSION=2" \
	-DWITH_SFTP=ON \
	-DWITH_BITTORRENT=ON \
	-DWITH_JABBER=ON \
	-DWITH_NLS=ON \
	-DWITH_WEBINTERFACE=ON \
	-DWITH_CURL=ON \
	-DWITH_DOCUMENTATION=ON

%install
%make DESTDIR=%buildroot install

# Icons
mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 gfx/%name.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 gfx/%name.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 gfx/%name.png %buildroot%_miconsdir/%name.png
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=FileTransfer \
	%buildroot%_desktopdir/fatrat.desktop

%files
%dir %_datadir/%name
%_bindir/%name
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
