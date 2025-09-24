%global aname Quotient
%global appname libQuotient
%global sover 0.9
%global libname libquotientqt6_%sover
%global _description %{expand:
The Quotient project aims to produce a Qt-based SDK to develop applications
for Matrix. libQuotient is a library that enables client applications. It is
the backbone of Quaternion, Spectral and other projects. Versions 0.5.x and
older use the previous name - libQMatrixClient.}
%global _K6link %_libdir
%global optflags_lto %optflags_lto -ffat-lto-objects

Name: libquotient-qt6
Version: 0.9.5
Release: alt1

Group: System/Libraries
Summary: Qt library to write cross-platform clients for Matrix
Url: https://github.com/quotient-im/libQuotient
License: BSD-3-Clause AND LGPL-2.1-or-later

Source0: %appname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: qt6-base-devel qt6-tools-devel qt6-multimedia-devel
BuildRequires: libolm-devel
BuildRequires: libqtkeychain-qt6-devel
BuildRequires: pkgconfig(openssl)

%description %_description

%package -n %libname
Group: System/Libraries
Summary: Qt Matrix clients library
%description -n %libname %_description

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel %_description
%prep
%setup -n %appname-%version

%build
%K6build \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_INSTALL_INCLUDEDIR=%_includedir/%{aname}Qt6 \
    -DQuotient_ENABLE_E2EE:BOOL=ON \
    -DQuotient_INSTALL_TESTS:BOOL=OFF \
    -DQuotient_INSTALL_EXAMPLE:BOOL=OFF \
    -DBUILD_WITH_QT6=ON

%install
%K6install
rm -rf %buildroot/%_datadir/ndk-modules

%files -n %libname
%doc COPYING README.md CONTRIBUTING.md SECURITY.md
%_libdir/libQuotientQt6.so.%sover
%_libdir/libQuotientQt6.so.*

%files devel
%_includedir/%{aname}Qt?/
%_libdir/cmake/%{aname}Qt?/
%_libdir/lib*.so
%_libdir/pkgconfig/%{aname}Qt?.pc

%changelog
* Wed Sep 24 2025 Sergey V Turchin <zerg@altlinux.org> 0.9.5-alt1
- new version

* Wed Apr 23 2025 Sergey V Turchin <zerg@altlinux.org> 0.9.3-alt1
- initial build
