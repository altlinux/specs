%define real_name    cr3

Name:     coolreader3
Version:  3.2.59
Release:  alt2

Summary:  E-Book reader
License:  %gpl2only
Group:    Text tools

Url:      https://github.com/buggins/coolreader/
#URL:     http://sourceforge.net/projects/crengine
Packager: Nikolay Fetisov <naf@altlinux.org>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch
Source1: thirdparty.tar

Source2: %real_name-16.png
Source3: %real_name-32.png
Source4: %real_name-48.png

Patch1: %name-3.2.57-textlang.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: cmake gcc-c++ libicu-devel libjpeg-devel libpng-devel libgif-devel
BuildRequires: qt5-phonon-devel qt5-tools-devel libfreetype-devel fontconfig-devel
BuildRequires: libpcre-devel libuuid-devel libexpat-devel
BuildRequires: libunibreak-devel libfribidi-devel libzstd-devel

%description
CoolReader is fast and small cross-platform XML/CSS based
E-Book reader for desktops and handheld devices.
Supported formats: FB2, TXT, RTF, DOC, TCR, HTML, EPUB,
CHM, PDB.

%prep
%setup
%patch0 -p1
tar xf %SOURCE1

%patch1

%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -name '*.cpp' -o -name '*.h' | xargs sed -ri 's,^\xEF\xBB\xBF,,'
%endif
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
%cmake -D GUI=QT5 \
    -DCMAKE_BUILD_TYPE=Release \
    -DMAX_IMAGE_SCALE_MUL=2 \
    -DDOC_DATA_COMPRESSION_LEVEL=3 \
    -DDOC_BUFFER_SIZE=0x1400000

%cmake_build

%install
%cmake_install

mkdir -p -- %buildroot%_miconsdir %buildroot%_liconsdir %buildroot%_niconsdir
install -m0644 -- %SOURCE2 %buildroot%_miconsdir/%real_name.png
install -m0644 -- %SOURCE3 %buildroot%_niconsdir/%real_name.png
install -m0644 -- %SOURCE4 %buildroot%_liconsdir/%real_name.png

%files
%doc changelog
%doc --no-dereference COPYING

%_bindir/%real_name

%_datadir/%{real_name}*

%_pixmapsdir/%real_name.*
%_desktopdir/%real_name.desktop
%_datadir/metainfo/%real_name.*
%_man1dir/%{real_name}*

%exclude %_datadir/doc/%real_name/*

%_miconsdir/%{real_name}*
%_niconsdir/%{real_name}*
%_liconsdir/%{real_name}*

%changelog
* Wed Sep 13 2023 Nikolay A. Fetisov <naf@altlinux.org> 3.2.59-alt2
- Update BuildRequires

* Sun Nov 21 2021 Nikolay A. Fetisov <naf@altlinux.org> 3.2.59-alt1
- New version

* Mon Jun 28 2021 Nikolay A. Fetisov <naf@altlinux.org> 3.2.57-alt1
- New version

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
