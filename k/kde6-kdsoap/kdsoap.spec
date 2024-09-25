%define rname kdsoap
%define sover 2
%define libkdsoap libkdsoap-qt6_%sover
%define libkdsoap_server libkdsoap-server-qt6_%sover

Name: kde6-%rname
Version: 2.2.0
Release: alt1
%K6init

Group: System/Libraries
Summary: Qt-based client-side and server-side SOAP component
Url: https://www.kdab.com/products/kd-soap
Vcs: https://github.com/KDAB/KDSoap
License: MIT

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: boost-devel cmake qt6-base-devel

%description
KD Soap is a Qt-based client-side and server-side SOAP component.
It can be used to create client applications for web services and also provides
the means to create web services without the need for any further component
such as a dedicated web server.
KD Soap targets C++ programmers who use Qt in their applications.

%package common
BuildArch: noarch
Summary: Common %name files
Group: System/Configuration/Other
%description common
Common %name files

%package -n %libkdsoap
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
%description -n %libkdsoap
%name library

%package -n %libkdsoap_server
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
%description -n %libkdsoap_server
%name library

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: libgcrypt-devel libqca-qt6-devel
%description devel
This package contains the development files for %name.


%prep
%setup -qn %rname-%version

%ifarch %e2k
sed -i "/-Wl,--fatal-warnings/d" cmake/KDAB/modules/KDCompilerFlags.cmake
%endif

%build
%K6build \
    -DCMAKE_INSTALL_INCLUDEDIR=%_K6inc \
    -DKDSoap_QT6:BOOL=ON \
    -DKDSoap_EXAMPLES:BOOL=OFF \
    #

%install
%K6install
%find_lang --with-kde --all-name %name

#mkdir -p %buildroot/%_K6archdata/mkspecs/features/
#mv %buildroot/%_datadir/mkspecs/features/* %buildroot/%_K6archdata/mkspecs/features/

%files common -f %name.lang
%doc LICENSES/*

%files -n %libkdsoap
%_libdir/libkdsoap-qt6.so.%sover
%_libdir/libkdsoap-qt6.so.*
%files -n %libkdsoap_server
%_libdir/libkdsoap-server-qt6.so.%sover
%_libdir/libkdsoap-server-qt6.so.*

%files devel
%doc kdsoap.pri kdwsdl2cpp.pri
%_K6bin/kdwsdl2cpp*
%_K6lib/cmake/KDSoap*/
%_K6inc/KDSoap*/
%_K6link/lib*.so
%_K6archdata/mkspecs/modules/*oap*.pri

%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 2.2.0-alt1
- initial build
