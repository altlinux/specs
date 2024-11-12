%define rname libkeduvocdocument

%define keduvocdocument_sover 5
%define libkeduvocdocument libkeduvocdocument%keduvocdocument_sover

Name: kde6-%rname
Version: 24.08.2
Release: alt1
%K6init

Group: System/Libraries
Summary: KVTML format reading and writing library
Url: http://www.kde.org
License: GPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-ki18n-devel kf6-kio-devel
BuildRequires: kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel
BuildRequires: kf6-solid-devel

%description
Contains KEduVocDocument and its related class for reading from/writing to the
KVTML format (and others too).

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides:  kde5-libkeduvocdocument-common = %EVR
Obsoletes: kde5-libkeduvocdocument-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkeduvocdocument
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkeduvocdocument
%name library


%prep
%setup -n %rname-%version

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%find_lang %name --with-kde --all-name

%files common -f %name.lang

%files devel
%_K6inc/libkeduvocdocument/
%_K6link/lib*.so
%_K6lib/cmake/libkeduvocdocument/

%files -n %libkeduvocdocument
%_K6lib/libKEduVocDocument.so.%keduvocdocument_sover
%_K6lib/libKEduVocDocument.so.*


%changelog
* Thu Nov 07 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

