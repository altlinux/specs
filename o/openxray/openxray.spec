Name: openxray
Version: 1.6.02_2088
Release: alt1

Summary: X-Ray Engine Linux port by OpenXRay team
License: BSD-3-Clause
Group: Games/Other
URL: https://github.com/OpenXRay/xray-16

ExcludeArch: armh ppc64le

Source: %name-%version.tar.xz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libfreeimage-devel
BuildRequires: libfreeimageplus-devel
BuildRequires: libjpeg-devel
BuildRequires: liblzo2-devel
BuildRequires: libpcre-devel
BuildRequires: tbb-devel
BuildRequires: libcryptopp-devel
BuildRequires: libGLEW-devel
BuildRequires: libogg-devel
BuildRequires: libopenal-devel
BuildRequires: libSDL2-devel
BuildRequires: libtheora-devel
BuildRequires: libvorbis-devel
BuildRequires: libmimalloc-devel

%description
OpenXRay is an improved version of the X-Ray Engine, the game engine
used in the world-famous S.T.A.L.K.E.R. game series by GSC Game World.

Currently the following games are supported:
 * S.T.A.L.K.E.R.: Call of Pripyat
 * S.T.A.L.K.E.R.: Clear Sky

To play one of the S.T.A.L.K.E.R. games with OpenXRay you need the
original game files.

%prep
%setup

%build
mkdir build && cd build
cmake .. \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DCMAKE_SKIP_RPATH=ON
%make_build

%install
cd build
%makeinstall_std
rm -v %buildroot%_datadir/openxray/gamedata/*/.gitattributes

%files
%doc License.txt README.md
%_bindir/xr_3da
%_libdir/xrAICore.so
%_libdir/xrAPI.so
%_libdir/xrCDB.so
%_libdir/xrCore.so
%_libdir/xrEngine.so
%_libdir/xrGame.so
%_libdir/xrLuabind.so
%_libdir/xrLuajit.so
%_libdir/xrNetServer.so
%_libdir/xrParticles.so
%_libdir/xrRender_GL.so
%_libdir/xrScriptEngine.so
%_libdir/xrSound.so
%_libdir/xrUICore.so
%dir %_datadir/openxray
%_datadir/openxray/gamedata
%_datadir/openxray/fsgame.ltx
%_datadir/applications/openxray_*.desktop
%_datadir/icons/hicolor/*/apps/openxray_*.png
%exclude %_datadir/pixmaps/openxray_*.png
%_datadir/bash-completion/completions/xr_3da

%changelog
* Mon Sep 11 2023 Anton Kurachenko <srebrov@altlinux.org> 1.6.02_2088-alt1
- Updating to new version 1.6.02_2088.
- Compressing of the %files section in the spec. Cosmetic changes.

* Mon Jun 26 2023 Anton Kurachenko <srebrov@altlinux.org> 1.6.02_1747-alt1
- Updating to new version 1.6.02_1747.

* Fri Jun 23 2023 Anton Kurachenko <srebrov@altlinux.org> 1.6.02_1144-alt2
- Cosmetic changes in the spec file.
- Adding ExclusiveArch due to problems with assembly for other architectures.

* Sat Jun 10 2023 Anton Kurachenko <srebrov@altlinux.org> 1.6.02_1144-alt1
- Initial build for ALT.
