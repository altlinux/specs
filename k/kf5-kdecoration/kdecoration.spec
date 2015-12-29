%define rname kdecoration
%define sover 5
%define libkdecorations libkdecorations2%sover
%define libkdecorationsprivate libkdecorations2private%sover

Name: kf5-%rname
Version: 5.5.2
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Workspace 5 Plugin based library to create window decorations
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Mar 05 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libcloog-isl4 libqt5-core libqt5-gui libqt5-test libstdc++-devel python-base ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ python-module-google qt5-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel

%description
KDecoration2 is a library to create window decorations. These window decorations can be used by
for example an X11 based window manager which re-parents a Client window to a window decoration
frame.

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

%package -n %libkdecorations
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkdecorations
KF5 library

%package -n %libkdecorationsprivate
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkdecorationsprivate
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --all-name

%files common -f %name.lang
%doc COPYING.LIB README.md

%files devel
%_K5inc/kdecoration2_version.h
%_includedir/KDecoration2/
%_K5link/lib*.so
%_K5lib/cmake/KDecoration2
#%_K5archdata/mkspecs/modules/qt_KDecoration.pri

%files -n %libkdecorations
%_K5lib/libkdecorations2.so.%sover
%_K5lib/libkdecorations2.so.%sover.*
%files -n %libkdecorationsprivate
%_K5lib/libkdecorations2private.so.%sover
%_K5lib/libkdecorations2private.so.%sover.*

%changelog
* Tue Dec 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.2-alt1
- new version

* Thu Dec 17 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Wed Dec 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Thu Nov 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt3
- rebuild

* Wed Nov 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt1
- new version

* Wed Oct 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Thu Sep 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Wed Aug 26 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Sat Aug 22 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.95-alt1
- new version

* Wed Jul 01 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri May 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Thu Apr 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Tue Apr 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt0.1
- test

* Thu Apr 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt1
- new version

* Mon Mar 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt0.1
- test

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.1
- initial build
