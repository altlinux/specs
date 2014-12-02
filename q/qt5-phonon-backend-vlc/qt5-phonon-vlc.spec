
Name: qt5-phonon-backend-vlc
Version: 0.8.1
Release: alt1

Group: Sound
Summary: VLC plugin for Phonon
Url: http://phonon.kde.org/
License: LGPLv2+

Source: %name-%version.tar

BuildRequires(pre): qt5-base-devel qt5-phonon-devel
BuildRequires: cmake gcc-c++ automoc libEGL-devel
BuildRequires: libvlc-devel >= 1.1
BuildRequires: kde-common-devel



%description
Phonon-VLC is a backend for KDE4 Multimedia Framework

%package -n qt5-phonon-backend-3-vlc
Group: System/Libraries
Summary: VLC Phonon backend
Provides: qt5-phonon-backend = %{get_version qt5-phonon-devel}
Provides: qt5-phonon-backend-gstreamer = %EVR qt5-phonon-vlc = %EVR
#
Requires: vlc-mini
#
Requires: vlc-plugin-alsa
Requires: vlc-plugin-pulseaudio
#
Requires: vlc-plugin-ffmpeg
Requires: vlc-plugin-flac
Requires: vlc-plugin-mpeg2
Requires: vlc-plugin-ogg
#
Requires: vlc-plugin-dvdnav
Requires: vlc-plugin-dvdread
Requires: vlc-plugin-audiocd
#
Requires: vlc-plugin-v4l
Requires: vlc-plugin-xcb
Requires: vlc-plugin-ts
Requires: vlc-plugin-live555
Requires: vlc-plugin-xml
Requires: vlc-plugin-dbus
Requires: vlc-plugin-taglib
%description -n qt5-phonon-backend-3-vlc
Phonon-VLC is a backend for KDE4 Multimedia Framework

%prep
%setup -q

%build
%K4build \
    -DPHONON_BUILD_PHONON4QT5=ON \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DPLUGIN_INSTALL_DIR=%_qt5_archdatadir \
    -DINCLUDE_INSTALL_DIR=%_includedir/kde5 \
    -DICON_INSTALL_DIR=%_datadir/kde5/share/icons \
    #

%install
%K4install

%files -n qt5-phonon-backend-3-vlc
%_qt5_plugindir/phonon4qt5_backend/phonon_vlc.so
#%_K5srv/phononbackends/vlc.desktop

%changelog
* Tue Dec 02 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt1
- new version

* Fri Sep 12 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt1
- new version

* Mon Sep 01 2014 Sergey V Turchin <zerg@altlinux.org> 0.7.80-alt0.M70P.1
- build for M70P

* Tue Aug 26 2014 Sergey V Turchin <zerg@altlinux.org> 0.7.80-alt1
- new version

* Wed Jul 02 2014 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt1
- initial build
