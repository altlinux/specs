
Name: qt6-phonon-backend-mpv
Version: 0.1.0
Release: alt1

Group: System/Libraries
Summary: MPV phonon backend
License: LGPL-2.1-or-later
Url: https://github.com/OpenProgger/phonon-mpv

Source: phonon-mpv-%version.tar

BuildRequires(pre): qt6-base-devel qt6-phonon-devel
BuildRequires: qt6-tools-devel
BuildRequires: cmake extra-cmake-modules glibc-devel libxml2-devel libGL-devel libEGL-devel
BuildRequires: pkgconfig(mpv) >= 1.101.0
BuildRequires: libxkbcommon-x11-devel
BuildRequires: pkgconfig(xcb-atom)
BuildRequires: pkgconfig(xcb-aux)
BuildRequires: pkgconfig(xcb-cursor)
BuildRequires: pkgconfig(xcb-event)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-renderutil)
BuildRequires: rpm-build-kf5

%description
This is a fork of phonon-vlc, rewritten to work with libmpv instead of
libVLC. libmpv supports less features than VLC but they are only
related to memory streams and audio/video dumps. This backend should be
a lightweight alternative to libVLC with less dependencies.

%package -n qt6-phonon-backend-1-mpv
Group: System/Libraries
Summary: MPV phonon backend
Provides: qt6-phonon-backend = %{get_version qt6-phonon-devel}
Provides: qt6-phonon-backend-mpv = %EVR qt6-phonon-mpv = %EVR
%description -n qt6-phonon-backend-1-mpv
MPV phonon backend.

%prep
%setup -n phonon-mpv-%version

%build
%add_optflags %optflags_shared
# -UPIE -U__PIE__
%K5cmake \
    -DPHONON_BUILD_QT5=OFF \
    -DPHONON_BUILD_QT6=ON \
    -DLOCALE_INSTALL_DIR=%_K5i18n \
    -DINCLUDE_INSTALL_DIR=%_K5inc \
    -DICON_INSTALL_DIR=%_K5icon \
    -DPLUGIN_INSTALL_DIR:PATH=%_qt6_plugindir \
    #
%K5make

%install
%K5install
%K5find_qtlang phonon_mpv_qt

%files -n qt6-phonon-backend-1-mpv -f phonon_mpv_qt.lang
%_qt6_plugindir/phonon4qt6_backend/phonon_mpv_qt6.so
#%_K5icon/hicolor/*/apps/phonon-mpv.*

%changelog
* Thu May 02 2024 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt1
- initial build
