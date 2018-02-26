%define qt4ver {%get_version libqt4-devel}
%define qt4_docdir %_docdir/qt-%qt4ver

Name: qt4-mobility
Version: 1.2.0
Release: alt2

Group: System/Libraries
Summary: Qt Mobility Framework
License: LGPLv2 with exceptions
Url: http://qt.nokia.com/products/qt-addons/mobility

#Provides: qt-mobility = %version-%release

Source: qt-mobility-opensource-src-1.2.0.tar
# FC
Patch50: qt-mobility-opensource-src-1.2.0-translationsdir.patch
Patch51: qt-mobility-opensource-src-1.2.0-pkgconfig.patch
Patch52: qt-mobility-opensource-src-1.1.0-pulseaudio-lib.patch

# Automatically added by buildreq on Tue Feb 07 2012 (-bi)
# optimized out: elfutils fontconfig glib2-devel gst-plugins-bad gst-plugins-devel gstreamer-devel libGL-devel libX11-devel libXext-devel libXrandr-devel libXrender-devel libXv-devel libgst-plugins libqt4-clucene libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-help libqt4-network libqt4-opengl libqt4-script libqt4-sql libqt4-sql-sqlite libqt4-svg libqt4-xml libqt4-xmlpatterns libstdc++-devel libxml2-devel pkg-config python-base ruby xorg-randrproto-devel xorg-renderproto-devel xorg-videoproto-devel xorg-xextproto-devel xorg-xproto-devel
#BuildRequires: NetworkManager-devel gcc-c++ glibc-devel-static gst-plugins-bad-devel libalsa-devel libblkid-devel libbluez-devel libicu libpulseaudio-devel libqt4-sql-interbase libqt4-sql-mysql libqt4-sql-odbc libqt4-sql-postgresql libqt4-sql-sqlite2 libudev-devel phonon-devel python-module-distribute qt4-mobility-devel rpm-build-ruby
BuildRequires(pre): libqt4-devel
BuildRequires: NetworkManager-devel gcc-c++ glibc-devel
BuildRequires: gst-plugins-bad-devel gst-plugins-devel libalsa-devel
BuildRequires: libblkid-devel libbluez-devel libpulseaudio-devel
BuildRequires: libudev-devel phonon-devel
# BuildRequires: qt4-qmf-devel

%description
Qt Mobility Project delivers a set of new APIs to Qt with features that are well
known from the mobile device world, in particular phones. However, these APIs
allow the developer to use these features with ease from one framework and apply
them to phones, netbooks and non-mobile personal computers. The framework not
only improves many aspects of a mobile experience, because it improves the use
of these technologies, but has applicability beyond the mobile device arena.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
%description common
%name common package

%package devel
Summary: Qt Mobility Framework development files
Group: Development/KDE and QT
Requires: libqt4-devel
#Provides: qt-mobility-devel = %version-%release
Provides: %name-bearer-devel = %version-%release
Provides: libqt4-bearer-devel = %version-%release
Provides: %name-contacts-devel = %version-%release
Provides: libqt4-contacts-devel = %version-%release
Provides: %name-connectivity-devel = %version-%release
Provides: libqt4-connectivity-devel = %version-%release
Provides: %name-feedback-devel = %version-%release
Provides: libqt4-feedback-devel = %version-%release
Provides: %name-gallery-devel = %version-%release
Provides: libqt4-gallery-devel = %version-%release
Provides: %name-location-devel = %version-%release
Provides: libqt4-location-devel = %version-%release
Provides: %name-multimedia-devel = %version-%release
Provides: libqt4-multimedia-devel = %version-%release
Provides: %name-multimediakit-devel = %version-%release
Provides: libqt4-multimediakit-devel = %version-%release
Provides: %name-organizer-devel = %version-%release
Provides: libqt4-organizer-devel = %version-%release
Provides: %name-publishsubscribe-devel = %version-%release
Provides: libqt4-publishsubscribe-devel = %version-%release
Provides: %name-sensors-devel = %version-%release
Provides: libqt4-sensors-devel = %version-%release
Provides: %name-serviceframework-devel = %version-%release
Provides: libqt4-serviceframework-devel = %version-%release
Provides: %name-systeminfo-devel = %version-%release
Provides: libqt4-systeminfo-devel = %version-%release
Provides: %name-versit-devel = %version-%release
Provides: libqt4-versit-devel = %version-%release
Provides: %name-versitorganizer-devel = %version-%release
Provides: libqt4-versitorganizer-devel = %version-%release
#Provides: %name-messaging-devel = %version-%release
#Provides: libqt4-messaging-devel = %version-%release
%description devel
%summary.

%package doc
Group: Development/Documentation
Summary: API documentation for %name
Requires: qt4-assistant
BuildArch: noarch
%description doc
%summary.

%package examples
Group: Development/KDE and QT
Summary: Qt Mobility Framework examples
%description examples
%summary.

%package -n libqt4-bearer
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libqt4-bearer

%name library
%package -n libqt4-contacts
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libqt4-contacts
%name library

%package -n libqt4-connectivity
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libqt4-connectivity
%name library

%package -n libqt4-feedback
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libqt4-feedback
%name library

%package -n libqt4-gallery
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libqt4-gallery
%name library

%package -n libqt4-location
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libqt4-location
%name library

%package -n libqt4-multimediakit
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libqt4-multimediakit
%name library

%package -n libqt4-organizer
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libqt4-organizer
%name library

%package -n libqt4-publishsubscribe
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libqt4-publishsubscribe
%name library

%package -n libqt4-sensors
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libqt4-sensors
%name library

%package -n libqt4-serviceframework
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libqt4-serviceframework
%name library

%package -n libqt4-systeminfo
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libqt4-systeminfo
%name library

%package -n libqt4-versit
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libqt4-versit
%name library

%package -n libqt4-versitorganizer
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libqt4-versitorganizer
%name library

%package -n libqt4-messaging
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libqt4-messaging
%name library


%prep
%setup -qn qt-mobility-opensource-src-%version

%patch50 -p1 -b .translationsdir
%patch51 -p1 -b .pkgconfig
%patch52 -p1 -b .pulseaudio_lib

QMFCLIENT_FLAGS=
QMFMESSAGESERVER_FLAGS=
pkg-config --exists qmfclient && QMFCLIENT_FLAGS=`pkg-config --cflags qmfclient`
pkg-config --exists qmfmessageserver && QMFMESSAGESERVER_FLAGS=`pkg-config --cflags qmfmessageserver`
cat >> common.pri << __EOF__
linux*-g++*:QMAKE_CFLAGS += %optflags %optflags_shared $QMFCLIENT_FLAGS $QMFMESSAGESERVER_FLAGS
linux*-g++*:QMAKE_CXXFLAGS += %optflags %optflags_shared $QMFCLIENT_FLAGS $QMFMESSAGESERVER_FLAGS
__EOF__

sed -i 's|^[[:space:]]*QMAKE_RPATHDIR.*||' features/mobility.prf.template
find -type f -name '*.pr[oif]' | \
while read f; do
    sed -i 's|^[[:space:]]*QMAKE_RPATHDIR.*||' $f
done

%build
export PATH=%_qt4dir/bin:$PATH
./configure \
    -release \
    -prefix %_qt4dir \
    -bindir %_qt4dir/bin \
    -headerdir %_includedir/qt4 \
    -libdir %_libdir \
    -plugindir %_qt4dir/plugins \
    -qmake-exec qmake-qt4
#	-examples

%make_build
%make_build qch_docs

%install
%make install INSTALL_ROOT=%buildroot

# install docs
install -p -m644 -D doc/qch/qtmobility.qch %buildroot/%qt4_docdir/qch/qtmobility.qch
mkdir -p %buildroot/%qt4_docdir/html/qtmobility
cp -ar doc/html/* %buildroot/%qt4_docdir/html/qtmobility/

# install tools
mkdir -p %buildroot/%_bindir/
pushd %buildroot/%_qt4dir/bin/
for f in `ls -1`; do
    ln -s `relative %buildroot/%_qt4dir/bin/$f %buildroot/%_bindir/$f-qt4` %buildroot/%_bindir/$f-qt4
done
popd


%files common
%files
%doc LGPL_EXCEPTION.txt
%_qt4dir/imports/QtMobility/
%_qt4dir/imports/QtMultimediaKit/
%_qt4dir/plugins/*

%files -n libqt4-bearer
%_libdir/libQtBearer.so.*
%files -n libqt4-contacts
%_libdir/libQtContacts.so.*
%files -n libqt4-connectivity
%_libdir/libQtConnectivity.so.*
%files -n libqt4-feedback
%_libdir/libQtFeedback.so.*
%files -n libqt4-gallery
%_libdir/libQtGallery.so.*
%files -n libqt4-location
%_libdir/libQtLocation.so.*
%files -n libqt4-multimediakit
%_libdir/libQtMultimediaKit.so.*
%files -n libqt4-organizer
%_libdir/libQtOrganizer.so.*
%files -n libqt4-publishsubscribe
%_libdir/libQtPublishSubscribe.so.*
%files -n libqt4-sensors
%_libdir/libQtSensors.so.*
%files -n libqt4-serviceframework
%_libdir/libQtServiceFramework.so.*
%files -n libqt4-systeminfo
%_libdir/libQtSystemInfo.so.*
%files -n libqt4-versit
%_libdir/libQtVersit.so.*
%files -n libqt4-versitorganizer
%_libdir/libQtVersitOrganizer.so.*
#%files -n libqt4-messaging
#%_libdir/libQtMessaging.so.*

%files devel
%_bindir/icheck-qt4
%_qt4dir/bin/icheck
%_bindir/ndefhandlergen-qt4
%_qt4dir/bin/ndefhandlergen
%_bindir/qcrmlgen-qt4
%_qt4dir/bin/qcrmlgen
%_bindir/servicedbgen-qt4
%_qt4dir/bin/servicedbgen
%_bindir/servicefw-qt4
%_qt4dir/bin/servicefw
%_bindir/servicexmlgen-qt4
%_qt4dir/bin/servicexmlgen
%_bindir/vsexplorer-qt4
%_qt4dir/bin/vsexplorer
%_datadir/qt4/mkspecs/features/mobility.prf
%_datadir/qt4/mkspecs/features/mobilityconfig.prf
%_includedir/qt4/Qt*/
%_libdir/libQt*.prl
%_libdir/libQt*.so
%_pkgconfigdir/Qt*.pc

%files doc
%qt4_docdir/qch/qtmobility.qch
%qt4_docdir/html/qtmobility/

%if 0
%files examples
%_qt4dir/bin/arrowkeys
%_qt4dir/bin/audiodevices
%_qt4dir/bin/audioinput
%_qt4dir/bin/audiooutput
%_qt4dir/bin/audiorecorder
%_qt4dir/bin/battery-publisher
%_qt4dir/bin/battery-subscriber
%_qt4dir/bin/bearercloud
%_qt4dir/bin/bearermonitor
%_qt4dir/bin/cubehouse
%_qt4dir/bin/flickrdemo
%_qt4dir/bin/grueapp
%_qt4dir/bin/logfilepositionsource
%_qt4dir/bin/metadata
%_qt4dir/bin/nmealog.txt
%_qt4dir/bin/orientation
%_qt4dir/bin/publish-subscribe
%_qt4dir/bin/radio
%_qt4dir/bin/samplephonebook
%_qt4dir/bin/satellitedialog
%_qt4dir/bin/sensor_explorer
%_qt4dir/bin/servicebrowser
%_qt4dir/bin/sfw-notes
%_qt4dir/bin/show_acceleration
%_qt4dir/bin/show_als
%_qt4dir/bin/show_compass
%_qt4dir/bin/show_magneticflux
%_qt4dir/bin/show_orientation
%_qt4dir/bin/show_proximity
%_qt4dir/bin/show_rotation
%_qt4dir/bin/show_tap
%_qt4dir/bin/simplelog.txt
%_qt4dir/bin/slideshow
%_qt4dir/bin/videographicsitem
%_qt4dir/bin/videowidget
%_qt4dir/bin/xmldata
%_qt4dir/plugins/serviceframework/libserviceframework_voipdialerservice.so
%_qt4dir/plugins/serviceframework/libserviceframework_landlinedialerservice.so
%_qt4dir/plugins/serviceframework/libserviceframework_filemanagerplugin.so
%_qt4dir/plugins/serviceframework/libserviceframework_bluetoothtransferplugin.so
%_qt4dir/plugins/serviceframework/libserviceframework_notesmanagerplugin.so
%_qt4dir/plugins/sensors/libqtsensors_grueplugin.so
%endif

%changelog
* Tue Jun 26 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt2
- rebuilt with udev-185

* Tue Apr 10 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt0.M60P.2
- rebuild with qt-4.8

* Mon Feb 27 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt0.M60P.1
- built for M60P

* Wed Feb 22 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1.1
- rebuild with libgstphotography-0.10.so.23

* Tue Feb 07 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt1
- initial specfile
