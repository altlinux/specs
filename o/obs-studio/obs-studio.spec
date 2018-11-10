# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define _libexecdir %prefix/libexec

%add_python3_path %_libdir/obs-scripting/
%add_python3_path %_datadir/obs/obs-plugins/frontend-tools/scripts/

Name: obs-studio
Summary: Free and open source software for video recording and live streaming
Summary(ru_RU.UTF-8): Свободная программа для записи и трансляции видеопотока
Version: 22.0.2
Release: alt1
License: GPLv2+
Group: Video
Url: https://github.com/jp9000/obs-studio.git
Packager: Anton Midyukov <antohami@altlinux.org>
Source: %name-%version.tar
Patch: obs-ffmpeg-mux.patch

# Arm gcc has no xmmintrin.h file
ExclusiveArch: %ix86 x86_64

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: libjansson-devel
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libGL-devel libGLU-devel
BuildRequires: libX11-devel libxcb-devel
BuildRequires: libalsa-devel
BuildRequires: libjack-devel
BuildRequires: libpulseaudio-devel 
BuildRequires: qt5-base-devel qt5-x11extras-devel
BuildRequires: pkgconfig(MagickCore)
BuildRequires: texlive-latex-base
BuildRequires: zlib-devel
BuildRequires: libcurl-devel
BuildRequires: libx264-devel
BuildRequires: libv4l-devel
BuildRequires: libswscale-devel libswresample-devel libavresample-devel
BuildRequires: libavutil-devel libavformat-devel libavdevice-devel libavfilter-devel libavcodec-devel
BuildRequires: libvlc-devel
BuildRequires: libpostproc-devel
BuildRequires: fontconfig-devel libfreetype-devel libpng-devel libexpat-devel
BuildRequires: systemd-devel libudev-devel
BuildRequires: pkgconfig(dbus-1)
BuildRequires: swig
BuildRequires: libspeexdsp-devel
BuildRequires: libluajit-devel

Requires: %name-base = %EVR
Requires: %name-plugin-frontend-tools = %EVR
Requires: %name-plugin-image-source = %EVR
Requires: %name-plugin-alsa = %EVR
Requires: %name-plugin-capture = %EVR
Requires: %name-plugin-decklink = %EVR
Requires: %name-plugin-jack = %EVR
Requires: %name-plugin-pulseaudio = %EVR
Requires: %name-plugin-v4l2 = %EVR
Requires: %name-plugin-ffmpeg = %EVR
Requires: %name-plugin-filters = %EVR
Requires: %name-plugin-outputs = %EVR
Requires: %name-plugin-transitions = %EVR
Requires: %name-plugin-x264 = %EVR
Requires: %name-plugin-rtmp-services = %EVR
Requires: %name-plugin-freetype2 = %EVR
Requires: %name-plugin-vlc-video = %EVR

%description
Free and open source software for video recording and live streaming.

%description -l ru_RU.UTF-8
Свободная программа для записи и трансляции видеопотока.

%package base
Summary: Free and open source software for video recording and live streaming
Summary(ru_RU.UTF-8): Свободная программа для записи и трансляции видеопотока
Group: Video
Requires: libobs = %EVR

%description base
Free and open source software for video recording and live streaming.
Base application without plugins. Some of the plugins are required to run.

%description -l ru_RU.UTF-8
Свободная программа для записи и трансляции видеопотока.
Базовое приложение без плагинов. Для запуска потребуются некоторые из плагинов.

%package -n libobs
Summary: Open Broadcaster Software Studio libraries
Group: Video

%description -n libobs
Library files for Open Broadcaster Software.

%package -n libobs-devel
Summary: Development files for %name
Group: Development/C
Requires: libobs = %EVR

%description -n libobs-devel
Development files for %name

%package plugin-frontend-tools
Summary: frontend-tools plugin for Open Broadcaster Software.
Group: Video
Requires: %name-base = %EVR
%add_python3_req_skip obspython

%description plugin-frontend-tools
frontend-tools plugin for Open Broadcaster Software.

%package plugin-image-source
Summary: image-source plugin for Open Broadcaster Software.
Group: Video
Requires: %name-base = %EVR

%description plugin-image-source
image-source plugin for Open Broadcaster Software.

%package plugin-alsa
Summary: ALSA plugin for Open Broadcaster Software.
Group: Video
Requires: %name-base = %EVR

%description plugin-alsa
ALSA plugin for Open Broadcaster Software.

%package plugin-capture
Summary: Capture plugin for Open Broadcaster Software.
Group: Video
Requires: %name-base = %EVR

%description plugin-capture
Capture plugin for Open Broadcaster Software.

%package plugin-decklink
Summary: decklink plugin for Open Broadcaster Software.
Group: Video
Requires: %name-base = %EVR

%description plugin-decklink
decklink plugin for Open Broadcaster Software.

%package plugin-jack
Summary: JACK plugin for Open Broadcaster Software.
Group: Video
Requires: %name-base = %EVR

%description plugin-jack
JACK plugin for Open Broadcaster Software.

%package plugin-pulseaudio
Summary: PulseAudio plugin for Open Broadcaster Software.
Group: Video
Requires: %name-base = %EVR

%description plugin-pulseaudio
PulseAudio plugin for Open Broadcaster Software.

%package plugin-v4l2
Summary: v4l2 plugin for Open Broadcaster Software.
Group: Video
Requires: %name-base = %EVR

%description plugin-v4l2
v4l2 plugin for Open Broadcaster Software.

%package plugin-ffmpeg
Summary: FFMPEG plugin for Open Broadcaster Software.
Group: Video
Requires: %name-base = %EVR
Requires: ffmpeg

%description plugin-ffmpeg
FFMPEG plugin for Open Broadcaster Software.

%package plugin-filters
Summary: Filters plugin for Open Broadcaster Software.
Group: Video
Requires: %name-base = %EVR

%description plugin-filters
Filters plugin for Open Broadcaster Software.

%package plugin-outputs
Summary: Ouputs plugin for Open Broadcaster Software.
Group: Video
Requires: %name-base = %EVR

%description plugin-outputs
Ouputs plugin for Open Broadcaster Software.

%package plugin-transitions
Summary: transitions plugin for Open Broadcaster Software.
Group: Video
Requires: %name-base = %EVR

%description plugin-transitions
transitions plugin for Open Broadcaster Software.

%package plugin-x264
Summary: x264 plugin for Open Broadcaster Software.
Group: Video
Requires: %name-base = %EVR
Requires: x264

%description plugin-x264
x264 plugin for Open Broadcaster Software.

%package plugin-rtmp-services
Summary: RTMP-services plugin for Open Broadcaster Software.
Group: Video
Requires: %name-base = %EVR

%description plugin-rtmp-services
RTMP-services plugin for Open Broadcaster Software.

%package plugin-freetype2
Summary: freetype2 plugin for Open Broadcaster Software.
Group: Video
Requires: %name-base = %EVR

%description plugin-freetype2
freetype2 plugin for Open Broadcaster Software.

%package plugin-vlc-video
Summary: VLC video plugin for Open Broadcaster Software.
Group: Video
Requires: %name-base = %EVR

%description plugin-vlc-video
VLC video plugin for Open Broadcaster Software.

%prep
%setup
%patch -p0

# rpmlint reports E: hardcoded-library-path
# replace OBS_MULTIARCH_SUFFIX by LIB_SUFFIX
sed -i 's|OBS_MULTIARCH_SUFFIX|LIB_SUFFIX|g' cmake/Modules/ObsHelpers.cmake

%build
%cmake \
    -DOBS_VERSION_OVERRIDE=%version \
    -DUNIX_STRUCTURE=1

%cmake_build

%install
%cmakeinstall_std

mkdir -p %buildroot/%_libexecdir/obs-plugins/obs-ffmpeg/
mv -f %buildroot/%_datadir/obs/obs-plugins/obs-ffmpeg/ffmpeg-mux \
      %buildroot/%_libexecdir/obs-plugins/obs-ffmpeg/ffmpeg-mux

%files

%files base
%doc COPYING README.rst
%_bindir/obs
%_datadir/obs/
%exclude %_datadir/obs/obs-plugins/*
%_desktopdir/obs.desktop
%_iconsdir/hicolor/*/apps/obs.png
%dir %_libdir/obs-plugins/
%_libdir/obs-scripting/
%dir %_libexecdir/obs-plugins/
%exclude %_datadir/obs/libobs/

%files -n libobs
%dir %_datadir/obs
%_datadir/obs/libobs/
%_libdir/*.so.*
%_libdir/libobs-scripting.so

%files -n libobs-devel
%_includedir/obs/
%_libdir/*.so
%exclude %_libdir/libobs-scripting.so
%_libdir/cmake/LibObs/

%files plugin-frontend-tools
%_libdir/obs-plugins/frontend-tools.so
%_datadir/obs/obs-plugins/frontend-tools/

%files plugin-image-source
%_libdir/obs-plugins/image-source.so
%_datadir/obs/obs-plugins/image-source/

%files plugin-alsa
%_libdir/obs-plugins/linux-alsa.so
%_datadir/obs/obs-plugins/linux-alsa/

%files plugin-capture
%_libdir/obs-plugins/linux-capture.so
%_datadir/obs/obs-plugins/linux-capture/

%files plugin-decklink
%_libdir/obs-plugins/linux-decklink.so
%_datadir/obs/obs-plugins/linux-decklink/

%files plugin-jack
%_libdir/obs-plugins/linux-jack.so
%_datadir/obs/obs-plugins/linux-jack/

%files plugin-pulseaudio
%_libdir/obs-plugins/linux-pulseaudio.so
%_datadir/obs/obs-plugins/linux-pulseaudio/

%files plugin-v4l2
%_libdir/obs-plugins/linux-v4l2.so
%_datadir/obs/obs-plugins/linux-v4l2/

%files plugin-ffmpeg
%_libdir/obs-plugins/obs-ffmpeg.so
%_libexecdir/obs-plugins/obs-ffmpeg/
%_datadir/obs/obs-plugins/obs-ffmpeg/

%files plugin-filters
%_libdir/obs-plugins/obs-filters.so
%_datadir/obs/obs-plugins/obs-filters/

%files plugin-outputs
%_libdir/obs-plugins/obs-outputs.so
%_datadir/obs/obs-plugins/obs-outputs/

%files plugin-transitions
%_libdir/obs-plugins/obs-transitions.so
%_datadir/obs/obs-plugins/obs-transitions/

%files plugin-x264
%_libdir/obs-plugins/obs-x264.so
%_datadir/obs/obs-plugins/obs-x264/

%files plugin-rtmp-services
%_libdir/obs-plugins/rtmp-services.so
%_datadir/obs/obs-plugins/rtmp-services/

%files plugin-freetype2
%_libdir/obs-plugins/text-freetype2.so
%_datadir/obs/obs-plugins/text-freetype2/

%files plugin-vlc-video
%_libdir/obs-plugins/vlc-video.so
%_datadir/obs/obs-plugins/vlc-video/

%changelog
* Sat Nov 10 2018 Anton Midyukov <antohami@altlinux.org> 22.0.2-alt1
- new version 22.0.2

* Tue Sep 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 21.1.1-alt2
- NMU: fixed build with Qt-5.11.

* Fri Jul 06 2018 Anton Midyukov <antohami@altlinux.org> 21.1.1-alt1
- new version 21.1.1

* Fri Oct 06 2017 Anton Midyukov <antohami@altlinux.org> 20.0.1-alt1
- new version 20.0.1

* Wed Jul 12 2017 Anton Midyukov <antohami@altlinux.org> 19.0.3-alt1
- Initial build for ALT Linux Sisyphus (Closes: 30989).
