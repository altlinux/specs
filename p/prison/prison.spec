
%define sover 0
Name: prison
Version: 1.0
Release: alt1

Group: Graphics
Summary: Qt api to produce QRCode and DataMatrix barcodes
License: MIT
Url: https://projects.kde.org/projects/prison

Source: %name-%version.tar

# Automatically added by buildreq on Wed Oct 12 2011 (-bi)
# optimized out: cmake-modules elfutils fontconfig libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libstdc++-devel
#BuildRequires: cmake gcc-c++ libdmtx-devel libqrencode-devel libqt3-devel libqt4-sql-interbase libqt4-sql-mysql libqt4-sql-odbc libqt4-sql-postgresql libqt4-sql-sqlite2 phonon-devel
BuildRequires: cmake gcc-c++ libdmtx-devel libqrencode-devel libqt4-devel
BuildRequires: kde-common-devel

%description
Prison is a barcode api currently offering a nice Qt api to produce QRCode
barcodes and DataMatrix barcodes, and can easily be made support more.

%package -n lib%name%sover
Summary: Qt api to produce QRCode and DataMatrix barcodes
Group: System/Libraries
%description -n lib%name%sover
Prison is a barcode api currently offering a nice Qt api to produce QRCode
barcodes and DataMatrix barcodes, and can easily be made support more.

%package devel
Group: Development/C++
Summary: Qt api to produce QRCode and DataMatrix barcodes
%description devel
Prison is a barcode api currently offering a nice Qt api to produce QRCode
barcodes and DataMatrix barcodes, and can easily be made support more.

%prep
%setup -q

%build
%Kbuild

%install
%Kinstall

%files -n lib%name%sover
%_libdir/libprison.so.%sover
%_libdir/libprison.so.%sover.*

%files devel
%_includedir/prison/
%_libdir/cmake/Prison/
%_libdir/lib%name.so

%changelog
* Wed Oct 12 2011 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1
- initial build
