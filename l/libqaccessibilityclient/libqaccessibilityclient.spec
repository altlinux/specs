
Name: libqaccessibilityclient
Version: 0.1.1
Release: alt2

Group: System/Libraries
Summary: Accessibility client library for Qt
Url: https://projects.kde.org/projects/playground/accessibility/libkdeaccessibilityclient
# KDE e.V. may determine that future LGPL versions are accepted
License: LGPLv2 / LGPLv3

Source0: %name-%version.tar
# FC
Patch50: qaccessibilityclient-0.1.0-dso.patch
# ALT
Patch100: alt-qt4.patch
Patch101: alt-version.patch
Patch102: alt-gcc8.patch

# Automatically added by buildreq on Wed May 15 2013 (-bi)
# optimized out: cmake-modules elfutils fontconfig libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-test libqt4-xml libstdc++-devel python-base ruby ruby-stdlibs
#BuildRequires: cmake gcc-c++ libqt3-devel libqt4-sql-interbase libqt4-sql-mysql libqt4-sql-odbc libqt4-sql-postgresql libqt4-sql-sqlite2 phonon-devel rpm-build-ruby
BuildRequires: cmake gcc-c++ libqt4-devel phonon-devel
BuildRequires: kde-common-devel

%description
%summary.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: libqt4-devel
%description devel
%summary.

%prep
%setup
%patch50 -p1
%patch100 -p1
%patch102 -p1

%build
%Kbuild \
    -DKDE4_BUILD_TESTS=OFF \
    #

%install
%Kinstall

%files
%doc AUTHORS ChangeLog README
%_libdir/libqaccessibilityclient.so.*

%files devel
%_includedir/qaccessibilityclient/
%_libdir/cmake/QAccessibilityClient/
%_libdir/libqaccessibilityclient.so

%changelog
* Thu Feb 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1-alt2
- NMU: fixed build with gcc-8.

* Tue Feb 18 2014 Sergey V Turchin <zerg@altlinux.org> 0.1.1-alt1
- new version

* Tue May 14 2013 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt0.1
- initial build
