%def_disable baloo
%def_disable mysql
%define rname digikam
%define label digiKam

Name: kde5-%rname
%define lname lib%name
Version: 5.0.0
Release: alt1
%K5init

Summary: digiKam is an advanced digital photo management application for linux
License: GPLv2+
Group: Graphics
Url: http://www.digikam.org/

Provides: digikam = %version-%release

Requires: qt5-sql-sqlite
#Requires: kde5-runtime
Requires: %name-data = %version-%release
%if_enabled mysql
Requires: qt5-sql-mysql
%endif

BuildRequires(pre): rpm-build-kf5
# Automatically added by buildreq on Wed Jul 20 2016 (-bi)
# optimized out: boost-devel-headers cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig gcc-c++ glib2-devel glibc-devel-static gtk-update-icon-cache kde5-akonadi-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kguiaddons-devel kf5-kiconthemes-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libEGL-devel libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdb4-devel libdbusmenu-qt52 libdc1394-22 libgdk-pixbuf libgpg-error libgphoto2-6 libgphoto2_port-12 libgst-plugins1.0 libical-devel libjson-c libopencore-amrnb0 libopencore-amrwb0 libp11-kit libpangox-compat libpng-devel libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-multimedia libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-script libqt5-sensors libqt5-sql libqt5-svg libqt5-webchannel libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libraw1394-11 libstdc++-devel libwayland-client libwayland-server libxcbutil-keysyms libxkbfile-devel perl pkg-config python-base python-modules python3 python3-base qt5-base-devel rpm-build-gir rpm-build-python3 ruby ruby-stdlibs xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: doxygen eigen3 extra-cmake-modules flex git-core graphviz kde4-marble-devel kde5-kcalcore-devel kde5-kcontacts-devel kde5-libkipi-devel kde5-libksane-devel kde5-pimlibs-devel kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kfilemetadata-devel kf5-ki18n-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-knotifyconfig-devel kf5-sonnet-devel kf5-threadweaver-devel libXres-devel libexiv2-devel libexpat-devel libgomp-devel libgphoto2-devel libjasper-devel libjpeg-devel liblcms2-devel liblensfun-devel liblqr-devel libopencv-devel libtiff-devel libusb-devel python-module-google python3-dev qt4-dbus qt5-multimedia-devel qt5-webkit-devel qt5-x11extras-devel rpm-build-ruby sqlite3 zlib-devel-static
BuildRequires: doxygen eigen3 extra-cmake-modules flex graphviz
BuildRequires: qt5-dbus qt5-multimedia-devel qt5-webkit-devel qt5-x11extras-devel
BuildRequires: libXres-devel libexiv2-devel libexpat-devel libgomp-devel libgphoto2-devel libjasper-devel libjpeg-devel libpng-devel
BuildRequires: liblcms2-devel liblensfun-devel liblqr-devel libopencv-devel libtiff-devel libusb-devel
BuildRequires: libEGL-devel libGL-devel libGLU-devel
BuildRequires: sqlite3 zlib-devel
BuildRequires: kde5-marble-devel
BuildRequires: kde5-kcalcore-devel kde5-kcontacts-devel kde5-libkipi-devel kde5-libksane-devel kde5-pimlibs-devel
BuildRequires: kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kfilemetadata-devel kf5-ki18n-devel kf5-kinit-devel
BuildRequires: kf5-kio-devel kf5-kitemmodels-devel kf5-knotifyconfig-devel kf5-sonnet-devel kf5-threadweaver-devel
%if_enabled baloo
BuildRequires: kf5-baloo-devel
%endif

Source0: %rname-%version.tar
Source1: po.tar
Source2: doc.tar
Source3: doc-translated.tar

%description
DigiKam is an advanced digital photo management application for KDE.
Photos can be collected into albums which can be sorted chronologically,
by directory layout or by custom collections.
DigiKam also provides tagging functionality. Images can be tagged despite of
their position and digiKam provides fast and intuitive ways to browse them.
User comments and customized meta-information added to images, are stored
into a database and retrieved to make them available into the user interface.
As soon as the camera is plugged in digikam allows you to preview, download,
upload and delete images.
DigiKam also includes tools like Image Editor, to modify photos using plugins
such as red eye correction or Gamma correction, exif management,...
Light Table to make artistic photos and an external image editor such
as Showfoto.
DigiKam also uses KIPI plugins (KDE Image Plugin Interface) to increase
its functionalities.

%package -n %lname
Group: System/Libraries
Summary: %label library

%description -n %lname
%label library.

%package data
Group: Graphics
Summary: A Photo Management Application for KDE
Requires: %name = %version-%release
BuildArch: noarch
Conflicts: digikam-data <= 0.9.6-alt3

%description data
DigiKam is an advanced digital photo management application for KDE.
Photos can be collected into albums which can be sorted chronologically,
by directory layout or by custom collections.
DigiKam also provides tagging functionality. Images can be tagged despite of
their position and digiKam provides fast and intuitive ways to browse them.
User comments and customized meta-information added to images, are stored
into a database and retrieved to make them available into the user interface.
As soon as the camera is plugged in digikam allows you to preview, download,
upload and delete images.
DigiKam also includes tools like Image Editor, to modify photos using plugins
such as red eye correction or Gamma correction, exif management,...
Light Table to make artistic photos and an external image editor such
as Showfoto.
DigiKam also uses KIPI plugins (KDE Image Plugin Interface) to increase
its functionalities.

%package devel
Group: Development/KDE and QT
Summary: Development files for %label
%description devel
Development files for %label.

%prep
%setup -q -n %rname-%version  -a1 -a2 -a3

# change double to qreal for casting on arm
find -type f -name \*.cpp | \
while read f ; do
    sed -i 's|<double>|<qreal>|g' $f
done
find -type f -name \*.h | \
while read f ; do
    sed -i 's|<double>|<qreal>|g' $f
done

sed -i 's|add_subdirectory|ECM_OPTIONAL_ADD_SUBDIRECTORY|' doc-translated/CMakeLists.txt
sed -i 's|add_subdirectory|ECM_OPTIONAL_ADD_SUBDIRECTORY|' doc-translated/digikam/CMakeLists.txt

rm -rf doc-translated/digikam/showfoto

cat >> CMakeLists.txt <<__EOF__
find_package(KF5I18n CONFIG REQUIRED)
ki18n_install(po)
find_package(KF5 ${KF5_MIN_VERSION} REQUIRED COMPONENTS DocTools)
ECM_OPTIONAL_ADD_SUBDIRECTORY(doc)
ECM_OPTIONAL_ADD_SUBDIRECTORY(doc-translated)
__EOF__


%build
%K5build \
    -DENABLE_INTERNALMYSQL=OFF \
    -DENABLE_MYSQLSUPPORT=OFF \
    -DENABLE_KFILEMETADATASUPPORT=%{?_enable_baloo:ON}%{!?_enable_baloo:OFF} \
    -DBUILD_TESTING=OFF \
    #

%install
%K5install
%K5install_move data digikam kconf_update showfoto solid locale

rm -f %buildroot/%_K5i18n/*/*/kipiplugin*
rm -f %buildroot/%_K5i18n/*/*/lib*
rm -rf %buildroot/%_K5doc/*/kipi-plugins
%find_lang --with-kde %rname
%find_lang --with-kde --append --output=%rname.lang showfoto

%files
%_K5bin/%rname
%_K5bin/showfoto
%_K5bin/cleanup_digikamdb
%_K5bin/digitaglinktree
#%_K5plug/kio_%{rname}*.so
%_K5plug/%{rname}imageplugin_*.so
%_K5xdgapp/*.desktop
%_K5srv/%{rname}imageplugin_*.desktop
%_K5srvtyp/*.desktop
%_K5xmlgui/%{rname}/
%_K5xmlgui/showfoto/
%_K5notif/%{rname}.notifyrc

%files -n %lname
%_K5lib/lib%{rname}*.so*

%files data -f %rname.lang
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%_K5data/%rname
%_K5data/showfoto
%_K5data/solid/actions/%{rname}-opencamera.desktop
#%_K5srv/%{rname}*.protocol
%_K5icon/hicolor/*/apps/%rname.*
%_K5icon/hicolor/*/apps/showfoto.*
%_K5icon/hicolor/*/apps/panorama.*
%_K5icon/hicolor/*/apps/expoblending.*
%_K5icon/hicolor/*/actions/tag-*.*
%_K5icon/hicolor/*/actions/albumfolder-*.*
%_K5icon/hicolor/*/actions/tag.*
%_K5icon/hicolor/*/actions/overexposure.*
%_K5icon/hicolor/*/actions/underexposure.*
%_K5conf_up/*


%files devel
%_K5link/*.so

%changelog
* Mon Jul 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt1
- initial build
