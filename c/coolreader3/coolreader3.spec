# SPEC file for Cool Reader 3
#

%define real_name    cr3

Name:     coolreader3
Version:  3.0.54
Release:  alt1

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

BuildRequires(pre): rpm-build-licenses


# Automatically added by buildreq on Wed Jan 04 2012
# optimized out: cmake-modules fontconfig fontconfig-devel libfreetype-devel libpng-devel libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-xml libstdc++-devel pkg-config zlib-devel
BuildRequires: cmake gcc-c++ libjpeg-devel phonon-devel

%description
CoolReader is fast and small cross-platform XML/CSS based
E-Book reader for desktops and handheld devices.
Supported formats: FB2, TXT, RTF, DOC, TCR, HTML, EPUB,
CHM, PDB.

%prep
%setup
%patch0 -p1

%patch1

ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
mkdir qtbuild
cd qtbuild
cmake -D GUI=QT -D CMAKE_BUILD_TYPE=Release -D MAX_IMAGE_SCALE_MUL=2 -D DOC_DATA_COMPRESSION_LEVEL=3 -D DOC_BUFFER_SIZE=0x1400000 -D CMAKE_INSTALL_PREFIX=/usr ..
%make

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
* Thu Jan 05 2012 Nikolay A. Fetisov <naf@altlinux.ru> 3.0.54-alt1
- Initial build for ALT Linux Sisyphus
