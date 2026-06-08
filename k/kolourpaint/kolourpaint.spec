%define rname kolourpaint

%define sover 5
%define libkolourpaint libkolourpaint_lgpl%sover

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Graphics
Summary: Paint program
Url: http://www.kde.org
License: GPL-2.0-or-later or LGPL-2.0-only

Provides: kde5-kolourpaint = %EVR
Obsoletes: kde5-kolourpaint < %EVR

Requires: kde6-runtime

Source: %rname-%version.tar
Source1: colors.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-kdoctools-devel kf6-kio-devel kf6-ki18n-devel kf6-ktextwidgets-devel
BuildRequires: kde6-libkexiv2-devel ksanecore-devel kde6-libksane-devel

%description
An easy-to-use paint program designed for everyday tasks like drawing
simple diagrams/logos/icons and editing screenshots.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: kde5-kolourpaint-common = %EVR
Obsoletes: kde5-kolourpaint-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkolourpaint
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n %libkolourpaint
KF6 library


%prep
%setup -n %rname-%version -a1

%build
%K6build

%install
%K6install
%K6install_move data kolourpaint
mkdir -p %buildroot/%_K6xdgconf/colors/
for f in colors/*.colors ; do
    fname=`basename "$f" | sed 's|.colors$||'`
    install -m 0644 "$f" %buildroot/%_K6xdgconf/colors/"$fname"-%{name}.colors
done
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*

%files
%_K6xdgconf/colors/*.colors
%_K6bin/kolourpaint
%_K6bin/kolourpaint
%_K6data/kolourpaint/
%_K6xdgapp/org.kde.kolourpaint.desktop
%_K6icon/*/*/apps/kolourpaint.*
%_datadir/metainfo/*.xml

#%files devel
#%_K6inc/kolourpaint_version.h
#%_K6inc/kolourpaint/
#%_K6link/lib*.so
#%_K6lib/cmake/kolourpaint

%files -n %libkolourpaint
%_K6lib/libkolourpaint_lgpl.so.%sover
%_K6lib/libkolourpaint_lgpl.so.*

%changelog
* Fri Jun 05 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Sun May 10 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Fri Feb 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Mon Jan 19 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Nov 19 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Mon Oct 13 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Tue Sep 23 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- new version

* Fri Jul 25 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Wed Jun 11 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt1
- new version

* Wed May 14 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Tue Mar 11 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt2
- package color palettes (closes: 53282)

* Tue Mar 11 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt1
- new version

* Thu Mar 06 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Wed Jan 29 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt1
- new version

* Mon Nov 18 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

