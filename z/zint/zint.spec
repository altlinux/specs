Name:      zint
Version:   2.6.3
Release:   alt1
Summary:   A barcode generator and library
License:   GPLv3+
URL:       http://www.zint.org.uk
Source:    %name-%version.tar
Group:     Graphics

Patch: zint-alt-include-header.patch

BuildRequires: cmake
BuildRequires: libpng-devel
BuildRequires: zlib-devel
BuildRequires: qt5-base-devel qt5-tools-devel-static
BuildRequires: desktop-file-utils

%description
Zint is a C library for encoding data in several barcode variants. The
bundled command-line utility provides a simple interface to the library.
Features of the library:
- Over 50 symbologies including all ISO/IEC standards, like QR codes.
- Unicode translation for symbologies which support Latin-1 and 
  Kanji character sets.
- Full GS1 support including data verification and automated insertion of 
  FNC1 characters.
- Support for encoding binary data including NULL (ASCII 0) characters.
- Health Industry Barcode (HIBC) encoding capabilities.
- Output in the following file formats: PNG, GIF, EPS, WMF, BMP, TIF, SVG.
- Verification stage for SBN, ISBN and ISBN-13 data.


%package -n zint-devel
Summary:       Library and header files for %name
Group:         System/Libraries
Requires:      %name = %version-%release

%description -n zint-devel 
C library and header files needed to develop applications using %name.
The API documentation can be found ont the project website:
http://www.zint.org.uk/zintSite/Manual.aspx


%package -n zint-qt
Summary:       Zint Barcode Studio GUI and library
Group:         Graphics
Requires:      %name = %version-%release

%description -n zint-qt
Zint Barcode Studio is a Qt-based GUI which allows desktop users to generate 
barcodes which can then be embedded in documents or HTML pages, and a library 
which can be used to incorporate barcode generation functionality into other 
software.


%package -n zint-qt-devel
Summary:       Library and header files for %name-qt
Group:         System/Libraries
Requires:      %name-devel = %version-%release
Requires:      %name-qt = %version-%release

%description -n zint-qt-devel 
C library and header files needed to develop applications using %name-qt.


%prep
%setup -q
%patch -p 1

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmakeinstall_std
install -D -p -m 644 %name.png %buildroot%_datadir/pixmaps/%name.png
desktop-file-install --dir %buildroot%_datadir/applications %name-qt.desktop

%files
%doc COPYING README
%_bindir/%name
%_libdir/libzint.so.*

%files -n %name-devel
%_includedir/%name.h
%_libdir/libzint.so

%files -n %name-qt
%_bindir/%name-qt
%_libdir/libQZint.so.*
%_datadir/applications/%name-qt.desktop
%_datadir/pixmaps/%name.png

%files -n %name-qt-devel
%_includedir/qzint.h
%_libdir/libQZint.so


%changelog
* Wed Jun 16 2021 Ivan Razzhivin <underwit@altlinux.org> 2.6.3-alt1
- Initial build
