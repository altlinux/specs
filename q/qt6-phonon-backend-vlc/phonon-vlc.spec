
Name: qt6-phonon-backend-vlc
Version: 0.12.0
Release: alt1

Group: Sound
Summary: VLC plugin for Phonon
Url: http://phonon.kde.org/
License: LGPL-2.1-or-later

Source: phonon-backend-vlc-%version.tar

BuildRequires(pre): qt6-base-devel qt6-phonon-devel
BuildRequires: qt6-tools-devel
BuildRequires: cmake extra-cmake-modules libEGL-devel
BuildRequires: libvlc-devel >= 1.1
BuildRequires: rpm-build-kf5



%description
Phonon-VLC is a backend for KDE5 Multimedia Framework

%package -n qt6-phonon-backend-3-vlc
Group: System/Libraries
Summary: VLC Phonon backend
Provides: qt6-phonon-backend = %{get_version qt6-phonon-devel}
Provides: qt6-phonon-backend-vlc = %EVR qt6-phonon-vlc = %EVR
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
Requires: vlc-plugin-smb
Requires: vlc-plugin-xml
Requires: vlc-plugin-dbus
Requires: vlc-plugin-taglib
%description -n qt6-phonon-backend-3-vlc
Phonon-VLC is a backend for KDE5 Multimedia Framework

%prep
%setup -n phonon-backend-vlc-%version

%build
%add_optflags %optflags_shared
# -UPIE -U__PIE__
%K5build \
    -DPHONON_BUILD_QT5=OFF \
    -DPHONON_BUILD_QT6=ON \
    -DLOCALE_INSTALL_DIR=%_K5i18n \
    -DINCLUDE_INSTALL_DIR=%_K5inc \
    -DICON_INSTALL_DIR=%_K5icon \
    -DPLUGIN_INSTALL_DIR=%_qt6_archdatadir \
    #

%install
%K5install

%K5find_qtlang phonon_vlc_qt

%files -n qt6-phonon-backend-3-vlc -f phonon_vlc_qt.lang
%_qt6_plugindir/phonon4qt6_backend/phonon_vlc_qt6.so

%changelog
* Thu May 02 2024 Sergey V Turchin <zerg@altlinux.org> 0.12.0-alt1
- initial build

