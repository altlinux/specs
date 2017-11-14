%define rname okteta

%define okteta2gui_sover 2
%define libokteta2gui libokteta2gui%okteta2gui_sover
%define kasten3controllers_sover 3
%define libkasten3controllers libkasten3controllers%kasten3controllers_sover
%define kasten3okteta1controllers_sover 1
%define libkasten3okteta1controllers libkasten3okteta1controllers%kasten3okteta1controllers_sover
%define kasten3okteta1gui_sover 1
%define libkasten3okteta1gui libkasten3okteta1gui%kasten3okteta1gui_sover
%define okteta2core_sover 2
%define libokteta2core libokteta2core%kasten3okteta1gui_sover
%define kasten3okteta1core_sover 1
%define libkasten3okteta1core libkasten3okteta1core%kasten3okteta1core_sover
%define kasten3core_sover 3
%define libkasten3core libkasten3core%kasten3core_sover
%define kasten3gui_sover 3
%define libkasten3gui libkasten3gui%kasten3gui_sover


Name: kde5-%rname
Version: 17.08.3
Release: alt1%ubt
%K5init altplace

Group: Development/Tools
Summary: Viewing and editing of data on the byte level
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Patch1: %rname-alt-castxml-compat.patch

# Remove 'gccxml' from 'Requires'
%define __find_provides sh -c '/usr/lib/rpm/find-provides | sort | uniq'
%define __find_requires sh -c '/usr/lib/rpm/find-requires | sort | uniq | sed "/^gccxml$/d"'

# Automatically added by buildreq on Thu Oct 01 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ kf5-attica-devel kf5-kdoctools-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libjson-c libqca-qt5 libqt5-core libqt5-dbus libqt5-designer libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-script libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base python3 python3-base qt5-base-devel qt5-script-devel rpm-build-gir ruby ruby-stdlibs shared-mime-info xml-common xml-utils
#BuildRequires: extra-cmake-modules gccxml kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libqca-qt5-devel python-module-google qt5-quick1-devel qt5-tools-devel rpm-build-python3 rpm-build-ruby xsltproc
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel qt5-declarative-devel qt5-tools-devel qt5-script-devel
BuildRequires: libqca-qt5-devel xsltproc
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel
BuildRequires: kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel
BuildRequires: kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel
BuildRequires: kf5-solid-devel kf5-sonnet-devel kf5-kcrash-devel

%description
%summary.

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

%package -n %libokteta2gui
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libokteta2gui
KF5 library

%package -n %libkasten3controllers
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkasten3controllers
KF5 library

%package -n %libkasten3okteta1controllers
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkasten3okteta1controllers
KF5 library

%package -n %libkasten3okteta1gui
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkasten3okteta1gui
KF5 library

%package -n %libokteta2core
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libokteta2core
KF5 library

%package -n %libkasten3okteta1core
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkasten3okteta1core
KF5 library

%package -n %libkasten3core
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkasten3core
KF5 library

%package -n %libkasten3gui
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkasten3gui
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build \
    -DINCLUDE_INSTALL_DIR=%_K5inc \
    #

%install
%K5install
%K5install_move data okteta
%find_lang %name --with-kde --all-name
mv %buildroot/%_K5xdgmime/okteta{,5}.xml

%files common -f %name.lang
%doc COPYING*

%files
%config(noreplace) %_K5xdgconf/*.knsrc
%_K5bin/*
%_K5plug/*.so
%_K5plug/designer/*.so
%_K5data/okteta/
%_K5xmlgui/*/
%_K5xdgmime/*.xml
%_K5xdgapp/*.desktop
%_K5icon/*/*/apps/*.*
%_K5cfg/*.kcfg

%files devel
#%_K5inc/okteta_version.h
%_K5inc/*/
%_K5link/lib*.so
%_K5lib/cmake/*/
#%_K5archdata/mkspecs/modules/qt_okteta.pri

%files -n %libokteta2gui
%_K5lib/libokteta2gui.so.%okteta2gui_sover
%_K5lib/libokteta2gui.so.*
%files -n %libkasten3controllers
%_K5lib/libkasten3controllers.so.%kasten3controllers_sover
%_K5lib/libkasten3controllers.so.*
%files -n %libkasten3okteta1controllers
%_K5lib/libkasten3okteta1controllers.so.%kasten3okteta1controllers_sover
%_K5lib/libkasten3okteta1controllers.so.*
%files -n %libkasten3okteta1gui
%_K5lib/libkasten3okteta1gui.so.%kasten3okteta1gui_sover
%_K5lib/libkasten3okteta1gui.so.*
%files -n %libokteta2core
%_K5lib/libokteta2core.so.%okteta2core_sover
%_K5lib/libokteta2core.so.*
%files -n %libkasten3okteta1core
%_K5lib/libkasten3okteta1core.so.%kasten3okteta1core_sover
%_K5lib/libkasten3okteta1core.so.*
%files -n %libkasten3core
%_K5lib/libkasten3core.so.%kasten3core_sover
%_K5lib/libkasten3core.so.*
%files -n %libkasten3gui
%_K5lib/libkasten3gui.so.%kasten3gui_sover
%_K5lib/libkasten3gui.so.*


%changelog
* Tue Nov 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Mon Sep 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 17.04.3-alt2%ubt
- Patched struct2osd script to work with castxml.

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Fri Jun 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Thu May 04 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- new version

* Tue Apr 04 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Mon Dec 05 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1%ubt
- new version

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Thu Jul 14 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt1
- new version

* Mon Jul 04 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Fri Apr 01 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt1
- new version

* Fri Feb 26 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Wed Jan 20 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Tue Dec 22 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- new version

* Thu Nov 12 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version

* Wed Oct 14 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Wed Sep 30 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- initial build
