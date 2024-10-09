%define soname 11

# undefined references
%def_without bcg729

Name: mediastreamer2
Version: 5.3.74
Release: alt6

Summary: Mediastreamer2 is a powerful and lightweight streaming engine for voice/video telephony applications
License: AGPL-3.0
Group: System/Libraries
Url: https://gitlab.linphone.org/BC/public/mediastreamer2

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

Provides: libmediastreamer = %version-%release
Obsoletes: libmediastreamer < %version-%release

%if "%(rpmquery --qf '%%{VERSION}' libavcodec-devel)" >= "5"
Patch: mediastreamer2-5.3.74-opensuse-fix-build-ffmpeg5.patch
%endif
Patch1: mediastreamer2-5.3.74-opensuse-fix-pkgconfig.patch
Patch2: mediastreamer2-5.3.74-mageia-cmake-config-location.patch
Patch3: mediastreamer2-5.3.74-mageia-soname.patch
Patch4: mediastreamer2-5.3.74-mageia-system-OpenGL.patch
Patch5: mediastreamer2-5.3.74-alt-pkgconfig-dav1d-aom.patch

# fix mediastreamer2-mkvstream
Requires: libglvnd-devel libGLEW-devel

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: libortp-devel
BuildRequires: libsrtp2-devel
BuildRequires: libzrtp-devel
BuildRequires: libsqlite3-devel
BuildRequires: libopus-devel
BuildRequires: libspeex-devel
BuildRequires: libspeexdsp-devel
BuildRequires: libalsa-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libavcodec-devel
BuildRequires: libavutil-devel
BuildRequires: libswscale-devel
BuildRequires: libgsm-devel
BuildRequires: libv4l-devel
BuildRequires: libGLEW-devel
BuildRequires: libzxing-cpp-devel
BuildRequires: libyuv-devel
BuildRequires: libvpx-devel
BuildRequires: libtheora-devel
BuildRequires: libturbojpeg-devel
BuildRequires: libbcmatroska2-devel
BuildRequires: libdav1d-devel
BuildRequires: libaom-devel
%if_with bcg729
BuildRequires: libbcg729-devel
%endif

%description
Mediastreamer2 is a powerful and lightweight streaming engine for voice/video
telephony applications. This media processing and streaming toolkit is
responsible for receiving and sending all multimedia streams in Linphone,
including voice/video capture, encoding and decoding, and rendering.

%package tester
Summary: Test data for %name
Group: Development/Other

%description tester
%summary

%package -n lib%name-%soname
Summary: Library of %name
Group: System/Libraries

%description -n lib%name-%soname
%summary

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++
Provides: libmediastreamer-devel = %version-%release
Obsoletes: libmediastreamer-devel < %version-%release

%description -n lib%name-devel
%summary

%prep
%setup
%autopatch -p1

# fix version
sed -i -e '/project/s/\(VERSION\)\s\+[0-9]\+\(\.[0-9]\+\)\+/\1 %version/' CMakeLists.txt

# drop bundled OpenGL includes
rm -rf include/OpenGL

%if_with bcg729
# find BCG729
sed -i '/find_package/s|BCG729|Bcg729|' CMakeLists.txt
%endif

# fix mediastreamer2-tester startup
sed -i '/MEDIASTREAMER_LOCAL_RESOURCE_LOCATION/s|${CMAKE_CURRENT_SOURCE_DIR}/tester|%_datadir/%name-tester|' \
  mediastreamer-config.h.cmake
sed -i '/MEDIASTREAMER_LOCAL_PLUGINS_LOCATION/s|${CMAKE_BINARY_DIR}/lib|%_libdir|' \
  mediastreamer-config.h.cmake

%build
export CPLUS_INCLUDE_PATH=%_includedir/bcmatroska2:$CPLUS_INCLUDE_PATH
%if_with bcg729
export CMAKE_PREFIX_PATH=%_datadir/Bcg729/cmake:$CMAKE_PREFIX_PATH
%endif
%cmake \
  -GNinja \
  -Wno-dev \
  -DBUILD_SHARED_LIBS=TRUE \
  -DENABLE_STRICT=NO \
  -DCMAKE_INSTALL_LIBDIR=%_libdir \
  -DPACKAGE_MS2_PLUGINS_DIR=%_libdir/mediastreamer/plugins/
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"

%files
%doc LICENSE* CHANGELOG* README*
%_bindir/%name-mediastream
%_bindir/%name-mkvstream
%dir %_datadir/images/
%_datadir/images/nowebcamCIF.jpg
%dir %_libdir/mediastreamer/
%dir %_libdir/mediastreamer/plugins/

%files tester
%_bindir/%name-tester
%_datadir/%name-tester/

%files -n lib%name-%soname
%_libdir/lib%name.so.%soname
%_libdir/lib%name.so.%version

%files -n lib%name-devel
%_libdir/lib%name.so
%dir %_includedir/%name/
%_includedir/%name/*.h
%_libdir/pkgconfig/%name.pc
%dir %_libdir/cmake/Mediastreamer2/
%_libdir/cmake/Mediastreamer2/*.cmake

%changelog
* Tue Oct 08 2024 Leontiy Volodin <lvol@altlinux.org> 5.3.74-alt6
- Fixed mediastreamer2-mkvstream and mediastream2-tester startup.

* Thu Sep 19 2024 Leontiy Volodin <lvol@altlinux.org> 5.3.74-alt5
- Built with AV1 support.

* Fri Sep 13 2024 Leontiy Volodin <lvol@altlinux.org> 5.3.74-alt4
- Built with matroska support (ALT #51472).

* Thu Aug 29 2024 Leontiy Volodin <lvol@altlinux.org> 5.3.74-alt3
- Obsoleted libmediastreamer.

* Tue Aug 20 2024 Leontiy Volodin <lvol@altlinux.org> 5.3.74-alt2
- Easy backporting to older branches.

* Mon Aug 19 2024 Leontiy Volodin <lvol@altlinux.org> 5.3.74-alt1
- Initial build for Sisyphus (thanks mageia and opensuse for the patches).
