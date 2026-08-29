%define rname kimageformats

Name: dkf6-%rname
Version: 6.28.1
Release: alt0.dde.1
%DK6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 plugins to allow QImage to support extra file formats
Url: http://www.kde.org
License: LGPL-2.1-or-later

Requires: %name-common >= %EVR

Source: %name-%version.tar

BuildRequires(pre): rpm-build-dkf6
BuildRequires: deepin-extra-cmake-modules dqt6-tools-devel
BuildRequires: libdqt6-gui libdqt6-printsupport
BuildRequires: zlib-devel
BuildRequires: libcups-devel
BuildRequires: openexr-devel
BuildRequires: libavif-devel
BuildRequires: libraw0-devel
BuildRequires: libheif-devel
BuildRequires: libjasper-devel
BuildRequires: libopenjpeg2.0-devel openjpeg-tools2.0
%ifnarch %arm
BuildRequires: libjxl-devel
%endif
# JXR disabled by default
#BuildRequires: libjxr-devel
BuildRequires: dkf6-karchive-devel

# find libraries
%add_findprov_lib_path %_DK6lib

%description
This framework provides additional image format plugins for QtGui.  As
such it is not required for the compilation of any other software, but
may be a runtime requirement for Qt-based software to support certain
image formats.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
# Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common >= %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n %name-%version

%build
%DK6build \
    -DKIMAGEFORMATS_HEIF=ON \
    #

%install
%DK6install
%find_lang %name --all-name
%DK6find_qtlang %name --all-name

%files common
%doc LICENSES/* README.md

%files
%_DK6plug/imageformats/kimg_*.so
#%_DK6srv/qimageioplugins/

%files devel
%_DK6lib/cmake/KF6ImageFormats/

%changelog
* Wed Aug 26 2026 Leontiy Volodin <lvol@altlinux.org> 6.28.1-alt0.dde.1
- fork for independent deepin build

* Tue Jul 21 2026 Sergey V Turchin <zerg@altlinux.org> 6.28.1-alt1
- new version

* Tue Jul 14 2026 Sergey V Turchin <zerg@altlinux.org> 6.28.0-alt1
- new version

* Tue Jun 16 2026 Sergey V Turchin <zerg@altlinux.org> 6.27.0-alt1
- new version

* Mon May 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.26.0-alt1
- new version

* Thu Apr 30 2026 Sergey V Turchin <zerg@altlinux.org> 6.25.0-alt2
- build with libraw0-devel

* Mon Apr 13 2026 Sergey V Turchin <zerg@altlinux.org> 6.25.0-alt1
- new version

* Fri Mar 20 2026 Sergey V Turchin <zerg@altlinux.org> 6.24.0-alt1
- new version

* Mon Feb 16 2026 Sergey V Turchin <zerg@altlinux.org> 6.23.0-alt1
- new version

* Wed Jan 14 2026 Sergey V Turchin <zerg@altlinux.org> 6.22.0-alt1
- new version

* Mon Dec 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.21.0-alt1
- new version

* Thu Nov 20 2025 Sergey V Turchin <zerg@altlinux.org> 6.20.0-alt1
- new version

* Fri Oct 17 2025 Sergey V Turchin <zerg@altlinux.org> 6.19.0-alt1
- new version

* Mon Sep 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.18.0-alt1
- new version

* Mon Aug 25 2025 Sergey V Turchin <zerg@altlinux.org> 6.17.0-alt1
- new version

* Mon Aug 04 2025 Sergey V Turchin <zerg@altlinux.org> 6.16.0-alt1
- new version

* Mon Jul 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.15.0-alt1
- new version

* Wed May 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.14.0-alt1
- new version

* Mon Apr 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.13.0-alt1
- new version

* Mon Mar 17 2025 Sergey V Turchin <zerg@altlinux.org> 6.12.0-alt1
- new version

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.11.0-alt1
- new version

* Mon Jan 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.10.0-alt1
- new version

* Mon Dec 16 2024 Sergey V Turchin <zerg@altlinux.org> 6.9.0-alt1
- new version

* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.8.0-alt1
- new version

* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.0-alt1
- new version

* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

* Wed Sep 04 2024 Sergey V Turchin <zerg@altlinux.org> 6.5.0-alt1
- new version

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.4.0-alt1
- new version

* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

