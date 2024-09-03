# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%add_python3_path %_libdir/obs-scripting/
%add_python3_path %_datadir/obs/obs-plugins/frontend-tools/scripts/

Name: obs-studio
Summary: Free and open source software for video recording and live streaming
Summary(ru_RU.UTF-8): Свободная программа для записи и трансляции видеопотока
Version: 30.2.3
Release: alt1
License: GPL-2.0-or-later
Group: Video
Url: https://github.com/jp9000/obs-studio
Source: %name-%version.tar
Patch1: obs-studio-27.2.4-alt-cert-bundle.patch

# https://bugzilla.altlinux.org/47318
Requires: qt6-svg

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-luajit
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: libjansson-devel
BuildRequires: cmake gcc-c++
BuildRequires: libGL-devel libGLU-devel
BuildRequires: libX11-devel libxcb-devel
BuildRequires: libalsa-devel
BuildRequires: libjack-devel
BuildRequires: libpulseaudio-devel 
BuildRequires: qt6-base-devel
BuildRequires: qt6-svg-devel qt6-svg
BuildRequires: pkgconfig(MagickCore)
BuildRequires: texlive-latex-base
BuildRequires: zlib-devel
BuildRequires: libcurl-devel
BuildRequires: libx264-devel
BuildRequires: libv4l-devel
BuildRequires: libswscale-devel libswresample-devel
BuildRequires: libavutil-devel libavformat-devel libavdevice-devel libavfilter-devel libavcodec-devel
BuildRequires: libvlc-devel
BuildRequires: libpostproc-devel
BuildRequires: fontconfig-devel libfreetype-devel libpng-devel libexpat-devel
BuildRequires: systemd-devel libudev-devel
BuildRequires: pkgconfig(dbus-1)
BuildRequires: swig
BuildRequires: libspeexdsp-devel
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(libpci)
BuildRequires: pipewire-libs-devel
BuildRequires: libdrm-devel
BuildRequires: libmbedtls-compat-devel
BuildRequires: libuuid-devel
BuildRequires: libfdk-aac-devel
BuildRequires: libdatachannel-devel
BuildRequires: libuthash-devel
BuildRequires: nv-codec-headers
BuildRequires: nlohmann-json-devel
%ifarch %luajit_arches
BuildRequires: pkgconfig(luajit)
%endif

%add_python3_req_skip obspython

Obsoletes: %name-plugin-frontend-tools <= 0.26.0
Obsoletes: %name-plugin-image-source <= 0.26.0
Obsoletes: %name-plugin-alsa <= 0.26.0
Obsoletes: %name-plugin-capture <= 0.26.0
Obsoletes: %name-plugin-decklink <= 0.26.0
Obsoletes: %name-plugin-v4l2 <= 0.26.0
Obsoletes: %name-plugin-ffmpeg <= 0.26.0
Obsoletes: %name-plugin-filters <= 0.26.0
Obsoletes: %name-plugin-outputs <= 0.26.0
Obsoletes: %name-plugin-transitions <= 0.26.0
Obsoletes: %name-plugin-rtmp-services <= 0.26.0
Obsoletes: %name-plugin-freetype2 <= 0.26.0
Obsoletes: %name-plugin-vlc-video <= 0.26.0
Obsoletes: %name-plugin-x264 <= 0.26.0
Obsoletes: %name-plugin-jack <= 29.1.0
Obsoletes: %name-plugin-pulseaudio <= 29.1.0
Obsoletes: %name-plugin-pipewire <= 29.1.0
Obsoletes: %name-base <= 29.1.0

Provides: %name-base = %EVR

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
Requires: libobs = %EVR

%description -n libobs-devel
Development files for %name.

%prep
%setup
%patch1 -p0
%ifarch %e2k
# someone added this poorly written code to upstream
sed -i '/MATCHES "e2k"/c if(false)' cmake/Modules/CompilerConfig.cmake
%add_optflags -DSIMDE_ARCH_AMD64=1000 -mno-sse4.2
%endif
touch plugins/obs-{browser,websocket}/CMakeLists.txt

# rpmlint reports E: hardcoded-library-path
# replace OBS_MULTIARCH_SUFFIX by LIB_SUFFIX
sed -i 's|OBS_MULTIARCH_SUFFIX|LIB_SUFFIX|g' cmake/Modules/ObsHelpers.cmake

# remove -Werror flag to mitigate FTBFS with ffmpeg 5.1
sed -e 's|-Werror-implicit-function-declaration||g' -i cmake/Modules/CompilerConfig.cmake
sed -e '/-Werror/d' -i cmake/Modules/CompilerConfig.cmake

# disable unusable qsv plugin
mv plugins/obs-qsv11/CMakeLists.txt plugins/obs-qsv11/CMakeLists.txt.disabled
touch plugins/obs-qsv11/CMakeLists.txt

%build
%cmake \
	-DOBS_VERSION_OVERRIDE=%version \
	-DUNIX_STRUCTURE=1 \
	-DCMAKE_SKIP_RPATH=1 \
	-DWITH_RTMPS=ON \
	-DBUILD_BROWSER=OFF \
	-DBUILD_VST=OFF \
	-DENABLE_NEW_MPEGTS_OUTPUT=OFF \
	-DENABLE_AJA=OFF \
	-DENABLE_JACK=ON \
	-DENABLE_LIBFDK=ON \
%ifarch %luajit_arches
	-DENABLE_SCRIPTING_LUA=ON \
%else
	-DENABLE_SCRIPTING_LUA=OFF \
%endif
	-DOpenGL_GL_PREFERENCE=GLVND

%cmake_build

%install
%cmake_install

%files
%doc COPYING README.rst
%_bindir/*
%_datadir/obs/*
%exclude %_datadir/obs/libobs/
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*.*
%_libdir/obs-scripting/
%_libdir/obs-plugins
%_datadir/metainfo/*

%files -n libobs
%dir %_datadir/obs
%_datadir/obs/libobs/
%_libdir/*.so.*
%_libdir/libobs-scripting.so

%files -n libobs-devel
%_includedir/obs/
%_libdir/*.so
%exclude %_libdir/libobs-scripting.so
%_libdir/cmake/libobs/
%_libdir/cmake/obs-frontend-api/
%_libdir/pkgconfig/libobs.pc

%changelog
* Tue Sep 03 2024 Anton Midyukov <antohami@altlinux.org> 30.2.3-alt1
- New version 30.2.3.

* Wed Aug 28 2024 Anton Midyukov <antohami@altlinux.org> 30.1.2-alt2
- rebuild with libmbedtls-compat-devel (Closes: 51229)

* Sat Apr 20 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 30.1.2-alt1.1
- Fixed build for Elbrus.

* Tue Apr 09 2024 Anton Midyukov <antohami@altlinux.org> 30.1.2-alt1
- New version 30.1.2.

* Tue Mar 26 2024 Anton Midyukov <antohami@altlinux.org> 30.1.1-alt1
- New version 30.1.1.

* Wed Mar 13 2024 Anton Midyukov <antohami@altlinux.org> 30.1.0-alt1
- New version 30.1.0.

* Mon Dec 25 2023 Anton Midyukov <antohami@altlinux.org> 30.0.2-alt1
- New version 30.0.2.

* Sun Nov 26 2023 Anton Midyukov <antohami@altlinux.org> 30.0.0-alt1
- New version 30.0.0.

* Sun Oct 01 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 29.1.3-alt6
- explicitly disabled lua scripting on architectures where
  luajit is not available. Fixes FTBFS on LoongArch.

* Sat Sep 09 2023 Anton Midyukov <antohami@altlinux.org> 29.1.3-alt5
- update BR for build with ffmpeg-6.0

* Wed Aug 30 2023 Anton Midyukov <antohami@altlinux.org> 29.1.3-alt4
- update BR

* Tue Aug 29 2023 Anton Midyukov <antohami@altlinux.org> 29.1.3-alt3
- Requires: qt6-svg (See: ALT bug 47318)

* Tue Aug 22 2023 Anton Midyukov <antohami@altlinux.org> 29.1.3-alt2
- rebuild with qt6

* Thu Aug 17 2023 Nazarov Denis <nenderus@altlinux.org> 29.0.0-alt1.1
- Build with mbedTLS 2.28.4

* Tue Aug 15 2023 Anton Midyukov <antohami@altlinux.org> 29.1.3-alt1
- New version 29.1.3.

* Wed May 10 2023 Anton Midyukov <antohami@altlinux.org> 29.1.0-alt1
- new version 29.1.0
- include plugin packages and obs-studio-base in obs-studio package
- ENABLE_LIBFDK=ON, OpenGL_GL_PREFERENCE=GLVND

* Sun Jan 08 2023 Anton Midyukov <antohami@altlinux.org> 29.0.0-alt1
- new version 29.0.0

* Tue Nov 01 2022 Anton Midyukov <antohami@altlinux.org> 28.1.0-alt1
- new version 28.1.0

* Tue Oct 11 2022 Anton Midyukov <antohami@altlinux.org> 28.0.3-alt1
- new version 28.0.3
- new subpackage plugin-pipewire
- obs-studio: remove Requires: %name-plugin-jack

* Tue May 24 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 27.2.4-alt2
- NMU: Fixed certificate bundle path (Closes: 42827).

* Tue Apr 19 2022 Evgeny Sinelnikov <sin@altlinux.org> 27.2.4-alt1
- new version 27.2.4
- build with rtmps support

* Tue Mar 08 2022 Anton Midyukov <antohami@altlinux.org> 27.2.3-alt1
- new version 27.2.3

* Sat Oct 02 2021 Anton Midyukov <antohami@altlinux.org> 27.1.1-alt1
- new version 27.1.1

* Sun Jun 27 2021 Anton Midyukov <antohami@altlinux.org> 27.0.1-alt2
- fix build on ppc64le

* Sun Jun 27 2021 Anton Midyukov <antohami@altlinux.org> 27.0.1-alt1
- new version 27.0.1

* Mon Apr 26 2021 Anton Midyukov <antohami@altlinux.org> 26.1.2-alt1
- new version 26.1.2

* Tue Dec 15 2020 Anton Midyukov <antohami@altlinux.org> 26.1.0-alt1
- new version 26.1.0

* Sat Oct 10 2020 Anton Midyukov <antohami@altlinux.org> 26.0.2-alt1
- new version 26.0.2

* Fri Oct 02 2020 Anton Midyukov <antohami@altlinux.org> 26.0.0-alt1
- new version 26.0.0
- basic plugins included in the package obs-studio-base
- allowed for all architectures
- avoid luajit where unavailable

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
