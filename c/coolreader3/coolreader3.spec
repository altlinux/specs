%define real_name    cr3

Name:     coolreader3
Version:  3.2.32
Release:  alt3

Summary:  E-Book reader
License:  %gpl2only
Group:    Text tools

Url:      https://github.com/buggins/coolreader/
#URL:     http://sourceforge.net/projects/crengine
Packager: Nikolay Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar

Source1: %real_name-16.png
Source2: %real_name-32.png
Source3: %real_name-48.png

BuildRequires(pre): rpm-build-licenses

BuildRequires: cmake gcc-c++ libicu-devel libjpeg-devel qt5-phonon-devel
BuildRequires: qt5-tools-devel libfreetype-devel fontconfig-devel
BuildRequires: libpcre-devel libuuid-devel libexpat-devel
BuildRequires(pre): libpng-devel

%description
CoolReader is fast and small cross-platform XML/CSS based
E-Book reader for desktops and handheld devices.
Supported formats: FB2, TXT, RTF, DOC, TCR, HTML, EPUB,
CHM, PDB.

%prep
%setup
%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -name '*.cpp' -o -name '*.h' | xargs sed -ri 's,^\xEF\xBB\xBF,,'
%endif
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
mkdir qtbuild
cd qtbuild
cmake -D GUI=QT5 \
    -DCMAKE_BUILD_TYPE=Release \
    -DMAX_IMAGE_SCALE_MUL=2 \
    -DDOC_DATA_COMPRESSION_LEVEL=3 \
    -DDOC_BUFFER_SIZE=0x1400000 \
    -DCMAKE_INSTALL_PREFIX=/usr \
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
* Thu Dec 12 2019 Grigory Ustinov <grenka@altlinux.org> 3.2.32-alt3
- Fix URL (Closes: #36164).

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 3.2.32-alt2
- Build new version.

* Wed May 22 2019 Michael Shigorin <mike@altlinux.org> 3.2.29-alt2
- E2K: strip UTF-8 BOM to fix build with lcc < 1.24

* Thu Mar 07 2019 Grigory Ustinov <grenka@altlinux.org> 3.2.29-alt1
- Build new version (Closes: #36164).
- Transfer to Qt5.

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
