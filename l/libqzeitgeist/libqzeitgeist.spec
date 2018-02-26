
Name: libqzeitgeist
Version: 0.7.0
Release: alt1

Group: System/Libraries
Summary: Qt Zeitgeist Library
Url: http://projects.kde.org/projects/kdesupport/libqzeitgeist
License: LGPLv2+

Source: %name-%version.tar

# upstream
Patch1: libqzeitgeist-0.7.0-libsuffix.patch
# FC
Patch50: libqzeitgeist-0.7.0-pkgconfig_version.patch

BuildRequires: cmake gcc-c++ libqt4-devel kde-common-devel

%description
Qt Zeitgeist Library

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
%description devel
Development files for %name

%prep
%setup
%patch1 -p1 -b .libsuffix
%patch50 -p1 -b .pkgconfig_version


%build
%Kbuild


%install
%Kinstall


%files
%doc README
%_libdir/libqzeitgeist.so.*

%files devel
%dir %_datadir/qzeitgeist/
%_datadir/qzeitgeist/cmake/
%_includedir/QtZeitgeist/
%_libdir/libqzeitgeist.so
%_pkgconfigdir/QtZeitgeist.pc

%changelog
* Fri Sep 09 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.0-alt1
- initial build
