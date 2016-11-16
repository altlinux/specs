
Name: qt5-phonon-backend-gstreamer
Version: 4.9.0
Release: alt1

Group: System/Libraries
Summary: Gstreamer phonon backend
License: LGPLv2+
Url: http://phonon.kde.org/

Source: %name-%version.tar

BuildRequires(pre): qt5-base-devel qt5-phonon-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: automoc cmake extra-cmake-modules glibc-devel gst-plugins1.0-devel libalsa-devel libxml2-devel libGL-devel libEGL-devel
BuildRequires: kde-common-devel

%description
Gstreamer phonon backend

%package -n qt5-phonon-backend-5-gstreamer
Group: System/Libraries
Summary: Gstreamer phonon backend
Provides: qt5-phonon-backend = %{get_version qt5-phonon-devel}
Provides: qt5-phonon-backend-gstreamer = %EVR qt5-phonon-gstreamer = %EVR
Requires: gst-plugins-base1.0 gst-plugins-good1.0 gst-plugins-bad1.0 gst-plugins-ugly1.0
%description -n qt5-phonon-backend-5-gstreamer
Gstreamer phonon backend

%prep
%setup -q

%build
%add_optflags %optflags_shared -UPIE -U__PIE__
%K4cmake \
    -DPHONON_BUILD_PHONON4QT5=ON \
    -DINCLUDE_INSTALL_DIR=%_includedir/kde5 \
    -DICON_INSTALL_DIR=%_datadir/kf5/icons \
    -DPLUGIN_INSTALL_DIR:PATH=%_qt5_plugindir
pushd BUILD-*/gstreamer
if [ ! -e %_includedir/gstreamer-1.0/gst/gstconfig.h -a -e %_libdir/gstreamer-1.0/include/gst/gstconfig.h ]
then
    mkdir -p gst
    [ -e gst/gstconfig.h ] || \
       ln -s %_libdir/gstreamer-1.0/include/gst/gstconfig.h gst/gstconfig.h
fi
if [ ! -e %_includedir/gstreamer-1.0/gst/gl/gstglconfig.h -a -e %_libdir/gstreamer-1.0/include/gst/gl/gstglconfig.h ]
then
    mkdir -p gst/gl
    [ -e gst/gl/gstglconfig.h ] || \
       ln -s %_libdir/gstreamer-1.0/include/gst/gl/gstglconfig.h gst/gl/gstglconfig.h
fi
popd
%K4make

%install
%K4install

%files -n qt5-phonon-backend-5-gstreamer
%_qt5_plugindir/phonon4qt5_backend/phonon_gstreamer.so
#%_K5srv/phononbackends/gstreamer.desktop
%_datadir/kf5/icons/hicolor/*/apps/phonon-gstreamer.*

%changelog
* Mon Nov 14 2016 Sergey V Turchin <zerg@altlinux.org> 4.9.0-alt1
- new version

* Wed Jul 01 2015 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Tue Mar 24 2015 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt2
- fix icon paths

* Fri Dec 19 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Fri Sep 12 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Mon Sep 01 2014 Sergey V Turchin <zerg@altlinux.org> 4.7.80-alt0.M70P.1
- build for M70P

* Mon Aug 25 2014 Sergey V Turchin <zerg@altlinux.org> 4.7.80-alt1
- new version

* Tue Jul 01 2014 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- initial build
