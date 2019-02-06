%define rname kpkpass

Name: kde5-%rname
Version: 18.12.1
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: Apple Wallet pass files library
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: shared-mime-info
BuildRequires: kf5-karchive-devel

%description
Library to deal with Apple Wallet pass files.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkpimpkpass
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n libkpimpkpass
%name library


%prep
%setup -n %rname-%version

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    #

%install
%K5install
mv %buildroot/%_K5xdgmime/application-vnd-apple-pkpass.xml \
    %buildroot/%_K5xdgmime/kde5-application-vnd-apple-pkpass.xml
%find_lang %name --all-name

%files common -f %name.lang
%doc COPYING.LIB README.md
%config(noreplace) %_K5xdgconf/*.*categories
%_K5xdgmime/*.xml

%files devel
#%_K5inc/kpkpass_version.h
%_K5inc/KPim/KPkPass/
%_K5link/lib*.so
%_K5lib/cmake/KPimPkPass/
#%_K5archdata/mkspecs/modules/qt_kpkpass.pri

%files -n libkpimpkpass
%_K5lib/libKPimPkPass.*

%changelog
* Mon Feb 04 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.1-alt1
- initial build
