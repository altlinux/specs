%define _libexecdir %prefix/libexec

Name: obs-studio
Summary: Free and open source software for video recording and live streaming
Summary(ru_RU.UTF-8): Свободная программа для записи и трансляции видеопотока
Version: 19.0.3
Release: alt1
License: GPLv2+
Group: Video
Url: https://github.com/jp9000/obs-studio.git
Packager: Anton Midyukov <antohami@altlinux.org>
Source: %name-%version.tar
Patch: obs-ffmpeg-mux.patch

BuildPreReq: cmake rpm-macros-cmake gcc-c++
BuildRequires: fontconfig-devel libGL-devel libGLU-devel libX11-devel libalsa-devel libfreetype-devel libjack-devel libpulseaudio-devel libxcb-devel pkgconfig(MagickCore) pkgconfig(dbus-1) qt5-base-devel qt5-x11extras-devel texlive-latex-base zlib-devel libcurl-devel libx264-devel libv4l-devel libswscale-devel libswresample-devel libavresample-devel libpostproc-devel libavutil-devel libavformat-devel libavdevice-devel libavfilter-devel libavcodec-devel libvlc-devel
BuildRequires: systemd-devel

Requires: libobs = %version-%release
Requires: ffmpeg x264

%description
Free and open source software for video recording and live streaming.

%description -l ru_RU.UTF-8
Свободная программа для записи и трансляции видеопотока.

%package -n libobs
Summary: Open Broadcaster Software Studio libraries
Group: Video

%description -n libobs
Library files for Open Broadcaster Software.

%package -n libobs-devel
Summary: Development files for %name
Group: Development/C
Requires: libobs = %version-%release

%description -n libobs-devel
Development files for %name

%prep
%setup
%patch -p0

# rpmlint reports E: hardcoded-library-path
# replace OBS_MULTIARCH_SUFFIX by LIB_SUFFIX
sed -i 's|OBS_MULTIARCH_SUFFIX|LIB_SUFFIX|g' cmake/Modules/ObsHelpers.cmake

%build
%cmake_insource -DOBS_VERSION_OVERRIDE=%version -DUNIX_STRUCTURE=1
		
%make_build

%install
%makeinstall_std

mkdir -p %buildroot/%_libexecdir/obs-plugins/obs-ffmpeg/
mv -f %buildroot/%_datadir/obs/obs-plugins/obs-ffmpeg/ffmpeg-mux \
      %buildroot/%_libexecdir/obs-plugins/obs-ffmpeg/ffmpeg-mux

%files
%doc COPYING README.rst
%_bindir/obs
%_datadir/obs
%_desktopdir/obs.desktop
%_iconsdir/hicolor/*/apps/obs.png
%_libdir/obs-plugins
%_libexecdir/obs-plugins
%exclude %_datadir/obs/libobs

%files -n libobs
%_datadir/obs/libobs
%_libdir/*.so.*

%files -n libobs-devel
%_includedir/obs
%_libdir/*.so
%_libdir/cmake/LibObs

%changelog
* Wed Jul 12 2017 Anton Midyukov <antohami@altlinux.org> 19.0.3-alt1
- Initial build for ALT Linux Sisyphus (Closes: 30989).
