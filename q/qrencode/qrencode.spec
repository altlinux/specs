Name: qrencode
Version: 3.3.1
Release: alt1

Summary: Generate QR 2D barcodes
License: LGPLv2+
Group: File tools

URL: http://megaui.net/fukuchi/works/qrencode/index.en.html
Source: http://megaui.net/fukuchi/works/qrencode/qrencode-%version.tar.gz

# Automatically added by buildreq on Tue Dec 27 2011 (-bi)
BuildRequires: chrpath libSDL-devel libpng-devel

%description
Qrencode is a utility to encode string data in a QR Code and save as a PNG image.

%package -n libqrencode
Summary: A C library for encoding data in a QR Code symbol
Group: System/Libraries

%description -n libqrencode
Libqrencode is a C library for encoding data in a QR Code symbol, a kind of 2D
symbology that can be scanned by handy terminals such as a mobile phone with
CCD. The capacity of QR Code is up to 7000 digits or 4000 characters, and is
highly robustness.

Libqrencode supports QR Code model 2, described in JIS (Japanese Industrial
Standards) X0510:2004 or ISO/IEC 18004.

%package -n libqrencode-devel
Summary: The development files for the qrencode library
Group: Development/C
Requires: libqrencode = %version-%release

%description -n libqrencode-devel
This package contains the development files for the qrencode library.

%prep
%setup

%build
%configure --with-tests
%make_build
cd ./tests
./test_all.sh

%install
%makeinstall_std
chrpath --delete %buildroot%_bindir/qrencode

%files
%_bindir/*
%_man1dir/*

%files -n libqrencode
%_libdir/*.so.*

%files -n libqrencode-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Tue May 15 2012 Victor Forsiuk <force@altlinux.org> 3.3.1-alt1
- 3.3.1

* Mon Apr 02 2012 Victor Forsiuk <force@altlinux.org> 3.3.0-alt1
- 3.3.0

* Tue Dec 27 2011 Victor Forsiuk <force@altlinux.org> 3.2.0-alt1
- 3.2.0

* Mon Apr 04 2011 Victor Forsiuk <force@altlinux.org> 3.1.1-alt1
- Initial build.
