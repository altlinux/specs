%define sover 2
%define libqoauth libqoauth%sover

Name:          qoauth-qt5
Version:       2.0.1
Release:       alt0.3%ubt

Group:         System/Libraries
Summary:       Qt-based C++ library for OAuth authorization scheme
License:       GPL
URL:           https://github.com/ayoy/qoauth.git
Packager: Sergey V Turchin <zerg@altlinux.org>

Source0:       %name-%version.tar
Patch1: alt-pcfile-qt5.patch
Patch2: alt-linstall-lib.patch

# Automatically added by buildreq on Fri Nov 18 2016 (-bi)
# optimized out: ca-certificates elfutils gcc-c++ kde5-kcalcore-devel kde5-kcontacts-devel kde5-kmime-devel kde5-libkleo-devel kf5-attica-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjs-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libgpg-error libqca-qt5 libqt4-devel libqt5-core libqt5-dbus libqt5-network libqt5-test libssl-devel libstdc++-devel perl pkg-config python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-script-devel qt5-webchannel-devel qt5-webkit-devel qt5-xmlpatterns-devel rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: doxygen kde5-akonadi-calendar-devel kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-akonadi-notes-devel kde5-calendarsupport-devel kde5-eventviews-devel kde5-gpgmepp-devel kde5-incidenceeditor-devel kde5-kalarmcal-devel kde5-kblog-devel kde5-kcalutils-devel kde5-kdgantt2-devel kde5-kholidays-devel kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kldap-devel kde5-kmailtransport-devel kde5-kmbox-devel kde5-kontactinterface-devel kde5-kpimtextedit-devel kde5-ktnef-devel kde5-libgravatar-devel kde5-libkcddb-devel kde5-libkdepim-devel kde5-libksieve-devel kde5-mailcommon-devel kde5-mailimporter-devel kde5-messagelib-devel kde5-pim-apps-libs-devel kde5-pimcommon-devel kde5-syndication-devel kf5-bluez-qt-devel kf5-kactivities-devel kf5-kactivities-stats-devel kf5-karchive-devel kf5-kcmutils-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdesu-devel kf5-kdewebkit-devel kf5-kdnssd-devel kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-khtml-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kjsembed-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kpeople-devel kf5-kplotting-devel kf5-kpty-devel kf5-kross-devel kf5-krunner-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwayland-devel kf5-kwindowsystem-devel kf5-kxmlrpcclient-devel kf5-libkgapi-devel kf5-libkscreen-devel kf5-modemmanager-qt-devel kf5-networkmanager-qt-devel kf5-threadweaver-devel libqca-qt5-devel libqca2-devel python-module-google python3-dev qca-qt5-ossl qt5-connectivity-devel qt5-multimedia-devel qt5-phonon-devel qt5-quick1-devel qt5-sensors-devel qt5-serialport-devel qt5-svg-devel qt5-tools-devel qt5-webengine-devel qt5-websockets-devel qt5-x11extras-devel rpm-build-ruby
BuildRequires(pre): rpm-build-ubt
BuildRequires: doxygen glibc-devel libqca-qt5-devel qt5-base-devel

%description 
QOAuth is an attempt to support interaction with OAuth-powered network 
services in a Qt way, i.e. simply, clearly and efficiently. It gives 
the application developer no more than 4 methods, namely:

* requestToken() to obtain an unauthorized Request Token,
* accessToken() to exchange Request Token for the Access Token,
* createParametersString() to construct a request according to OAuth
  authorization scheme,
* inlineParemeters() - to construct a query string basing on given 
  parameters (provided only for convenience).

%package -n %libqoauth
Summary: %name core library
Group: System/Libraries
Requires: qca-qt5-ossl
%description -n %libqoauth
%name core library.

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and QT
Conflicts: qoauth-devel
Requires: qt5-base-devel
%description  devel
This package contains header files needed if you wish to build applications
based on %{name} .


%prep
%setup -q
%patch1 -p1
%patch2 -p1
sed -i -e 's|/lib|/%{_lib}|g' src/pcfile.sh
%qmake_qt5 qoauth.pro

%build
%make_build


%install
%installqt5
doxygen Doxyfile

# fix the time stamp
for file in doc/html/*; do
     touch -r Doxyfile $file
done
make check || :


%files -n %libqoauth
%_libdir/libqoauth.so.%sover
%_libdir/libqoauth.so.%sover.*

%files devel
%doc doc/html doc/examples
%_libdir/libqoauth.so
%_includedir/QtOAuth/
%_libdir/libqoauth.prl
%_libdir/libqoauth.so
%_pkgconfigdir/qoauth.pc
%_qt5_archdatadir/mkspecs/features/oauth.prf

%changelog
* Thu Dec 21 2017 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt0.3%ubt
- fix library install path

* Tue Dec 19 2017 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt0.2%ubt
- fix requires, url

* Mon Nov 21 2016 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt0.0.M80P.1
- build for M80P

* Fri Nov 18 2016 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt0.1
- git snapshot
- initial build
