%define rname ksanecore

%define sover 1
%define libksanecore libksanecore%sover

Name: kde5-%rname
Version: 24.02.2
Release: alt3
%K5init

Group: Graphical desktop/KDE
Summary: Qt interface for the SANE library
Url: http://www.kde.org
License: LGPL-2.1-only OR LGPL-3.0-only

Source: %rname-%version.tar
Patch1: alt-headers-place.patch

#BuildRequires: extra-cmake-modules qt5-base-devel
#BuildRequires: libsane-devel
#BuildRequires: kf5-kconfig-devel kf5-ki18n-devel kf5-ktextwidgets-devel kf5-kwallet-devel
#BuildRequires: kf5-kwidgetsaddons-devel kf5-sonnet-devel

# Automatically added by buildreq on Fri Sep 16 2022 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libctf-nobfd0 libglvnd-devel libgpg-error libldap2.4-compat libqt5-core libqt5-gui libsasl2-3 libssl-devel libstdc++-devel python-modules python2-base python3 python3-base python3-dev python3-module-paste qt5-base-devel rpm-build-file rpm-build-python3 sh4 tzdata
#BuildRequires: appstream clang-tools extra-cmake-modules kf5-ki18n-devel libsane-devel lua5.3 python3-module-setuptools python3-module-zope qt5-imageformats qt5-svg-devel qt5-wayland-devel qt5-webengine-devel rpm-build-lua tbb-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: libsane-devel
BuildRequires: kf5-ki18n-devel

%description
KSaneCore is a library that provides a Qt interface for the SANE library for scanner hardware.

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

%package -n %libksanecore
Group: System/Libraries
Summary: KF5 library
Requires: %name-common >= %EVR
%description -n %libksanecore
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    #

%install
%K5install
%K5install_move data locale
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*

%files devel
#%_K5inc/ksane_version.h
%_K5inc/KSaneCore/
%_K5link/lib*.so
%_K5lib/cmake/KSaneCore/
#%_K5archdata/mkspecs/modules/qt_ksane.pri

%files -n %libksanecore
%_K5lib/libKSaneCore.so.%sover
%_K5lib/libKSaneCore.so.*

%changelog
* Thu Oct 10 2024 Sergey V Turchin <zerg@altlinux.org> 24.02.2-alt3
- relax requires

* Tue May 28 2024 Sergey V Turchin <zerg@altlinux.org> 24.02.2-alt2
- fix headers placement

* Thu May 02 2024 Sergey V Turchin <zerg@altlinux.org> 24.02.2-alt1
- new version

* Thu Apr 11 2024 Sergey V Turchin <zerg@altlinux.org> 24.02.1-alt1
- new version

* Fri Feb 16 2024 Sergey V Turchin <zerg@altlinux.org> 23.08.5-alt1
- new version

* Mon Dec 11 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.4-alt1
- new version

* Fri Nov 10 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.3-alt1
- new version

* Fri Oct 13 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.2-alt1
- new version

* Thu Oct 05 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.1-alt1
- new version

* Fri Jul 14 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.3-alt1
- new version

* Fri Jun 09 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.2-alt1
- new version

* Thu Jun 01 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.1-alt1
- new version

* Mon Mar 06 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.3-alt1
- new version

* Mon Feb 06 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.2-alt1
- new version

* Wed Jan 11 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.1-alt1
- new version

* Mon Nov 07 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt1
- new version

* Tue Oct 18 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.2-alt1
- new version

* Fri Sep 16 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.1-alt1
- initial build
