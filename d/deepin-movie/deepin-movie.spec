%def_with clang

Name: deepin-movie
Version: 6.5.6
Release: alt1.1

Summary: Deepin movie is Deepin Desktop Environment Movie Player

License: GPL-3.0+ and CC0-1.0 and CC-BY-4.0
Group: Video
Url: https://github.com/linuxdeepin/deepin-movie-reborn
Vcs: git://github.com/linuxdeepin/deepin-movie-reborn.git

Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-reborn-%version.tar
Patch0: %name-6.5.6-alt-cxx-flags.patch
Patch1: %name-6.5.6-alt-pkgconfig-find-requires.patch

#Requires: libdmr libdvdnav libgsettings-qt
# direct dependency because dmr controls mpv via libmpv calls
Requires: libmpv2
Requires: libdqt6-gui = %_dqt6_version

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6
# Automatically added by buildreq on Mon Mar 10 2025
# optimized out: alt-os-release clang19.1 clang19.1-support cmake cmake-modules dqt6-base-devel dqt6-tools glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gstreamer1.0-devel libX11-devel libavcodec-devel libavformat-devel libavutil-devel libclang-cpp19 libdouble-conversion3 libdqt6-concurrent libdqt6-core libdqt6-dbus libdqt6-gui libdqt6-multimedia libdqt6-multimediawidgets libdqt6-network libdqt6-opengl libdqt6-openglwidgets libdqt6-printsupport libdqt6-qml libdqt6-sql libdqt6-svg libdqt6-svgwidgets libdqt6-waylandclient libdqt6-widgets libdqt6-xml libdtk6core-devel libdtk6gui-devel libdtk6log-devel libdvdread-devel libglvnd-devel libgpg-error libgsettings-qt1 libmpris-dqt6-1 libp11-kit libsasl2-3 libssl-devel libstartup-notification libstdc++-devel libva-devel libwayland-client libwayland-cursor libxcb-devel libxkbcommon-devel lld19.1 llvm-common llvm19.1-libs ninja-build pkg-config python3 python3-base sh5 vulkan-headers xorg-proto-devel
BuildRequires: dqt6-multimedia-devel dqt6-svg-devel dqt6-tools-devel gst-plugins1.0-devel libXtst-devel libdtk6widget-devel libdvdnav-devel libffmpegthumbnailer-devel libgsettings-qt-devel libmpris-dqt6-devel libmpv-devel libxcbutil-devel

%if_with clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++
%endif

%description
%summary.

%package -n libdmr
Summary: Library for %name
Group: System/Libraries
Requires: libdqt6-gui = %_dqt6_version

%description -n libdmr
This package provides Library for %name.

%package -n libdmr-devel
Summary: Development files for libdmr
Group: Development/Other

%description -n libdmr-devel
This package provides development files for libdmr.

%prep
%setup -n %name-reborn-%version
%if_with clang
# build: use system opt flags.
# The package isn't built with the patch using gcc.
%patch0 -p1
%endif
%patch1 -p1
# ffmpeg7
sed -i 's|->channels|->ch_layout.nb_channels|g' \
  src/libdmr/playlist_model.{cpp,h} \
  src/libdmr/gstutils.{cpp,h} \
  src/widgets/movieinfo_dialog.cpp

%build
%if_with clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%else
export CC=gcc
export CXX=g++
%endif
export CPLUS_INCLUDE_PATH=%_includedir/qt5:$CPLUS_INCLUDE_PATH
%DQ6build \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DVERSION=%version

%install
%DQ6install
%find_lang %name

%files -f %name.lang
%doc CHANGELOG.md HACKING.md LICENSE LICENSES README.md
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_datadir/dbus-1/services/com.deepin.movie.service
%_datadir/glib-2.0/schemas/com.deepin.deepin-movie.gschema.xml
%_iconsdir/hicolor/scalable/apps/%name.svg
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%name/
%_datadir/deepin-manual/manual-assets/application/%name/movie/

%files -n libdmr
%_libdir/libdmr.so.0.1*

%files -n libdmr-devel
%_libdir/libdmr.so
%dir %_includedir/libdmr/
%_includedir/libdmr/*.h
%_pkgconfigdir/libdmr.pc

%changelog
* Tue Mar 11 2025 Ivan A. Melnikov <iv@altlinux.org> 6.5.6-alt1.1
- NMU: Build with clang on loongarch64, too.

* Mon Mar 10 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.6-alt1
- New version 6.5.6.
- Switched to dqt6.
- Built via clang again.

* Thu Dec 05 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.11-alt1
- New version 6.0.11.
- Added vcs tag.

* Thu May 16 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.7-alt1
- New version 6.0.7.
- Built via separate qt5 instead system (ALT #48138).

* Wed Mar 06 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.6-alt1
- New version 6.0.6.

* Wed Nov 01 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.5-alt2
- Fixed build with dtkgui.
- Cleanup spec and BRs.
- Used default compiler versions for easy backporting.

* Tue Oct 31 2023 Ivan A. Melnikov <iv@altlinux.org> 6.0.5-alt1.1
- NMU: Build on loongarch64 with gcc13.

* Fri Mar 24 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.5-alt1
- New version 6.0.5.

* Tue Jan 31 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.1-alt1
- New version (6.0.1).
- Updated libmpv patch.
- Enabled build on armh.

* Fri Nov 18 2022 Leontiy Volodin <lvol@altlinux.org> 5.10.15-alt1
- NMU:
  + 5.9.14 -> 5.10.15 (fix FTBFS).
  + update License (by lakostis@).
  + remove build-fix patch (by lakostis@).
  + BR: added gst deps (by lakostis@).
  + BR: added qt5-multimedia (by lakostis@).
  + Requires: bump libmpv dependency (by lakostis@).
  + build using gcc instead clang.
  + fix underlinked libraries.
- Future improvements:
  + clang build: use system opt flags (by lakostis@).

* Fri May 06 2022 Leontiy Volodin <lvol@altlinux.org> 5.9.14-alt1
- New version (5.9.14).

* Wed Feb 09 2022 Leontiy Volodin <lvol@altlinux.org> 5.9.8-alt1
- New version (5.9.8).

* Thu Jun 10 2021 Leontiy Volodin <lvol@altlinux.org> 5.7.15-alt1.gitfe98519
- New version (5.7.15).
- Updated to git commit fe98519031e8482cba72bfca4ad67269cd98a1de.

* Mon Apr 26 2021 Leontiy Volodin <lvol@altlinux.org> 5.7.11-alt1
- New version (5.7.11) with rpmgs script.

* Thu Mar 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.7.6.165-alt2
- Fixed version tag.

* Mon Jan 11 2021 Leontiy Volodin <lvol@altlinux.org> 5.7.6.165-alt1
- New version (5.7.6.165) with rpmgs script.

* Thu Dec 10 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.6.164-alt1
- New version (5.7.6.164) with rpmgs script.
- Fixed build with mpv (thanks archlinux for the patches).

* Mon Nov 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.6.157-alt1.git1ad288f
- Built from git.

* Fri Nov 13 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.6.88-alt1
- New version (5.7.6.88) with rpmgs script.

* Thu Nov 05 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.6.74-alt1
- New version (5.7.6.74) with rpmgs script.

* Mon Oct 26 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.6.61-alt1
- New version (5.7.6.61) with rpmgs script.

* Mon Oct 19 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.6.51-alt1
- New version (5.7.6.51) with rpmgs script.

* Fri Oct 16 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.6.48-alt1
- New version (5.7.6.48) with rpmgs script.

* Thu Oct 15 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.6.47-alt1
- New version (5.7.6.47) with rpmgs script.

* Sat Oct 03 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.6.37-alt1
- New version (5.7.6.37) with rpmgs script.

* Fri Sep 11 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.6.29-alt1
- Initial build for ALT Sisyphus.
