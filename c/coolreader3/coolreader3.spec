# SPEC file for Cool Reader 3
#

%define real_name    cr3

Name:     coolreader3
Version:  3.0.56
Release:  alt3

Summary: E-Book reader

Group:    Text tools
License:  %gpl2only
URL:      http://coolreader.org
#URL: http://sourceforge.net/projects/crengine
Packager: Nikolay Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Source1: %real_name-16.png
Source2: %real_name-32.png
Source3: %real_name-48.png

Patch1: %name-3.0.54-alt-desktop.patch
Patch2: %name-3.0.56-save_settings.patch
Patch3: %name-3.0.56-alt-gcc6.patch

BuildRequires(pre): rpm-build-licenses


# Automatically added by buildreq on Wed Sep 10 2014
# optimized out: cmake-modules fontconfig fontconfig-devel libcloog-isl4 libfreetype-devel libpng-devel libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-xml libstdc++-devel pkg-config zlib-devel
BuildRequires: cmake gcc-c++ libicu50 libjpeg-devel phonon-devel
BuildRequires(pre): libpng-devel

%description
CoolReader is fast and small cross-platform XML/CSS based
E-Book reader for desktops and handheld devices.
Supported formats: FB2, TXT, RTF, DOC, TCR, HTML, EPUB,
CHM, PDB.

%prep
%setup
%patch0 -p1

%patch1
%patch2 -p1
%patch3

ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
mkdir qtbuild
cd qtbuild
cmake -D GUI=QT -D CMAKE_BUILD_TYPE=Release -D MAX_IMAGE_SCALE_MUL=2 -D DOC_DATA_COMPRESSION_LEVEL=3 -D DOC_BUFFER_SIZE=0x1400000 -D CMAKE_INSTALL_PREFIX=/usr \
	-DCMAKE_C_FLAGS="%optflags" \
	-DCMAKE_CXX_FLAGS="%optflags" \
	..
%make VERBOSE=1

%install
cd qtbuild
%makeinstall_std

mkdir -p -- %buildroot%_miconsdir %buildroot%_liconsdir %buildroot%_niconsdir
install -m0644 -- %SOURCE1 %buildroot%_miconsdir/%real_name.png
install -m0644 -- %SOURCE2 %buildroot%_niconsdir/%real_name.png
install -m0644 -- %SOURCE3 %buildroot%_liconsdir/%real_name.png

%files
%doc changelog
%doc --no-dereference COPYING

%_bindir/%real_name

%_datadir/%{real_name}*

%_pixmapsdir/%real_name.*
%_desktopdir/%real_name.desktop
%_man1dir/%{real_name}*

%exclude %_datadir/doc/%real_name/*

%_miconsdir/%{real_name}*
%_niconsdir/%{real_name}*
%_liconsdir/%{real_name}*

%changelog
* Thu Jan 26 2017 Nikolay A. Fetisov <naf@altlinux.org> 3.0.56-alt3
- Fix build with GCC 6.3

* Wed Sep 10 2014 Nikolay A. Fetisov <naf@altlinux.ru> 3.0.56-alt2
- Fix save settings bug (Closes: 29721)

* Wed Jun 12 2013 Nikolay A. Fetisov <naf@altlinux.ru> 3.0.56-alt1
- New version

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.54-alt1.1
- Rebuilt with libpng15

* Thu Jan 05 2012 Nikolay A. Fetisov <naf@altlinux.ru> 3.0.54-alt1
- Initial build for ALT Linux Sisyphus
