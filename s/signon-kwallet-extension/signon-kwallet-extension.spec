%define rname signon-kwallet-extension

Name: %rname
Version: 25.08.3
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
* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Fri Oct 10 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Tue Sep 16 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- new version

* Thu Jul 24 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Fri Jun 06 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt1
- new version

* Mon May 12 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Thu Apr 17 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.0-alt1
- new version

* Fri Mar 07 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt1
- new version

* Wed Feb 12 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Thu Jan 09 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt1
- new version

* Thu Nov 14 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Fri Oct 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- new version

* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

