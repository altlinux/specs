%define rname signon-kwallet-extension

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: System/Libraries
Summary: Sign-on KWallet extension
Url: http://www.kde.org
License: GPL-2.0-only

Provides: kde5-signon-kwallet-extension = %EVR
Obsoletes: kde5-signon-kwallet-extension < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel
BuildRequires: kf6-kwallet-devel signon-devel

%description
%summary

%prep
%setup -n %rname-%version

%build
%K6build \
    -DBUILD_WITH_QT6:BOOL=ON \
    #

%install
%K6install
#%find_lang %name --with-kde --all-name

%files
%_libdir/signon/extensions/*kwallet*.so*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

