%define rname kdepimlibs

Name: kde5-pimlibs
Version: 15.12.3
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: Akonadi client access library
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: kde5-akonadi

Source: %rname-%version.tar
Patch1: alt-akonadi-plugins-dir.patch
Patch2: alt-akonadi-resources-dir.patch

# Automatically added by buildreq on Wed Aug 12 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils kf5-kdoctools-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-designer libqt5-gui libqt5-network libqt5-printsupport libqt5-sql libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms libxml2-devel pkg-config python-base python3 python3-base qt5-base-devel ruby ruby-stdlibs shared-mime-info xml-common xml-utils
#BuildRequires: boost-devel-headers extra-cmake-modules gcc-c++ kde5-akonadi-devel kde5-kcalcore-devel kde5-kcontacts-devel kde5-kldap-devel kde5-kmbox-devel kde5-kmime-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libdb4-devel libical-devel libldap-devel libsasl2-devel libxslt-devel python-module-google qt5-phonon-devel qt5-quick1-devel qt5-tools-devel rpm-build-python3 rpm-build-ruby xsltproc
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: boost-devel-headers libical-devel libldap-devel libsasl2-devel libxslt-devel xsltproc
BuildRequires: qt5-phonon-devel qt5-quick1-devel qt5-tools-devel
BuildRequires: kde5-akonadi-devel kde5-kcalcore-devel kde5-kcontacts-devel kde5-kldap-devel kde5-kmbox-devel kde5-kmime-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel
BuildRequires: kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel
BuildRequires: kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel
BuildRequires: kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel

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
Requires: qt5-phonon-devel kde5-akonadi-devel boost-devel-headers
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5akonadiwidgets
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5akonadiwidgets
KF5 library

%package -n libkf5akonadisocialutils
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5akonadisocialutils
KF5 library

%package -n libkf5akonadinotes
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5akonadinotes
KF5 library

%package -n libkf5akonadicontact
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5akonadicontact
KF5 library

%package -n libkf5akonadixml
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5akonadixml
KF5 library

%package -n libkf5akonadimime
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5akonadimime
KF5 library

%package -n libkf5akonadicore
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5akonadicore
KF5 library

%package -n libkf5akonadiagentbase
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5akonadiagentbase
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1

%build
%K5build

%install
%K5install
mkdir %buildroot/%_K5data/akonadi/
for f in %buildroot/%_datadir/akonadi5/*.xs* ; do
    fname=`basename $f`
    dname=`dirname $f`
    ln -s `relative %_datadir/akonadi5/$fname %_K5data/akonadi/$fname` %buildroot/%_K5data/akonadi/$fname
done
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%config(noreplace) %_K5xdgconf/kdepimlibs*
%_K5xdgmime/*.xml
%_K5icon/*/*/apps/*_protocol.*
%dir %_K5data/akonadi/

%files
%_K5bin/akonadi*
%_K5plug/kf5/kio/*.so
%_K5plug/*akonadi*.so
%_K5data/akonadi_knut_resource/
%_datadir/akonadi5/agents/*
%_datadir/akonadi5/contact/*
%_datadir/akonadi5/plugins/*
%_K5cfg/*.kcfg
%_K5srv/akonadi/contact/*.desktop
%_K5srv/akonadi*.desktop
%_K5srv/*.protocol
%_K5srvtyp/*protocol.desktop

%files devel
%_K5plug/designer/akonadi*.so
%_K5data/akonadi/*.xs*
%_datadir/akonadi5/*.xs*
%_K5inc/akonadi_version.h
%_K5inc/Akonadi*/
%_K5inc/akonadi/
%_K5inc/akonadi*.h
%_K5link/lib*.so
%_K5lib/cmake/KF5Akonadi*/
%_K5archdata/mkspecs/modules/qt_Akonadi*.pri

%files -n libkf5akonadiwidgets
%_K5lib/libKF5AkonadiWidgets.so.*
%files -n libkf5akonadisocialutils
%_K5lib/libKF5AkonadiSocialUtils.so.*
%files -n libkf5akonadinotes
%_K5lib/libKF5AkonadiNotes.so.*
%files -n libkf5akonadicontact
%_K5lib/libKF5AkonadiContact.so.*
%files -n libkf5akonadixml
%_K5lib/libKF5AkonadiXml.so.*
%files -n libkf5akonadimime
%_K5lib/libKF5AkonadiMime.so.*
%files -n libkf5akonadicore
%_K5lib/libKF5AkonadiCore.so.*
%files -n libkf5akonadiagentbase
%_K5lib/libKF5AkonadiAgentBase.so.*


%changelog
* Tue Mar 22 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt1
- new version

* Thu Feb 25 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Tue Jan 19 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Mon Dec 21 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- new version

* Thu Nov 12 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version

* Wed Oct 14 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Wed Sep 16 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- new version

* Wed Sep 09 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt4
- add symlinks for devel data

* Wed Sep 09 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt3
- find akonadi resources in alternate place

* Tue Sep 01 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt2
- find akonadi plugins in alternate place

* Thu Aug 20 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Mon Aug 10 2015 Sergey V Turchin <zerg@altlinux.org> 15.7.90-alt1
- initial build
