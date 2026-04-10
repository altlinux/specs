%define _unpackaged_files_terminate_build 1

Name: nheko
Version: 0.12.1
Release: alt4

Summary: Desktop client (QT) for the Matrix protocol

Group: Development/Other
License: GPLv3
Url: https://nheko.im/nheko-reborn/nheko

Source: %name-%version.tar
Source2: nheko_ru.ts
Patch2: alt-qt-6.10.patch
Patch3: fix_reply_rendering.patch
Patch4: fix_calls.patch
Patch5: fix_screen_capture_on_wayland.patch

BuildRequires: cmake gcc-c++
BuildRequires: qt6-tools-devel qt6-multimedia-devel qt6-svg-devel
BuildRequires: qt6-declarative-devel libkdsingleapplication-qt6-devel
BuildRequires: libqtkeychain-qt6-devel
BuildRequires: boost-asio-devel boost-devel-headers boost-signals-devel
BuildRequires: libssl-devel zlib-devel libtweeny-devel liblmdbxx-devel
BuildRequires: libmtxclient-devel >= 0.10.1
BuildRequires: liblmdb-devel cmark-devel
BuildRequires: nlohmann-json-devel libfmt-devel
BuildRequires: libolm-devel libsodium-devel libspdlog-devel
BuildRequires: gst-plugins-bad-devel gst-plugins-devel
BuildRequires: libpcre-devel
BuildRequires: libmount-devel
BuildRequires: libblkid-devel
BuildRequires: libuuid-devel
BuildRequires: libselinux-devel
BuildRequires: libxcbutil-icccm-devel
BuildRequires: asciidoc-a2x
BuildRequires: libre2-devel
%ifarch %e2k
BuildRequires: clang llvm-devel
%endif

# Additional (runtime) dependencies
Requires: qt6-multimedia qt6-declarative

# Additional dependencies for call
Requires: gstreamer1.0
Requires: gst-plugins-base1.0
Requires: gst-plugins-good1.0
Requires: gst-plugins-bad1.0
Requires: gst-plugins-nice1.0

# Additional dependencies for get rid of errors
Requires: gst-plugins-good1.0-qt6

%description
The motivation behind the project is to provide a native desktop app
for Matrix that feels more like a mainstream chat app (Riot, Telegram etc)
and less like an IRC client.

%prep
%setup
%autopatch -p1
cp %SOURCE2 resources/langs/nheko_ru.ts

%build
%cmake -DUSE_BUNDLED_SPDLOG=OFF    \
       -DUSE_BUNDLED_OLM=OFF       \
       -DUSE_BUNDLED_GTEST=OFF     \
       -DUSE_BUNDLED_CMARK=OFF     \
       -DUSE_BUNDLED_JSON=OFF      \
       -DUSE_BUNDLED_OPENSSL=OFF   \
       -DUSE_BUNDLED_MTXCLIENT=OFF \
       -DUSE_BUNDLED_LMDB=OFF      \
       -DUSE_BUNDLED_LMDBXX=OFF    \
       -DUSE_BUNDLED_COEURL=OFF    \
       -DUSE_BUNDLED_LIBCURL=OFF   \
       -DUSE_BUNDLED_LIBEVENT=OFF  \
%ifarch %e2k
       -DCMAKE_CXX_COMPILER=clang++ \
       -DCMAKE_CXX_FLAGS_RELEASE="-O2 -DNDEBUG" \
%endif
       -DCMAKE_BUILD_TYPE=Release

# Adjust nprocs for git.alt
[ ${NPROCS:-%__nprocs} -le 16 ] || NPROCS=16
%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md COPYING
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/metainfo/*.appdata.xml
%_man1dir/nheko*
%_datadir/zsh/site-functions/*

%changelog
* Thu Apr 09 2026 Paul Wolneykien <manowar@altlinux.org> 0.12.1-alt4
- Require qt6-declarative and remove libqt6-* from runtime dependencies
  (closes: 50671).

* Mon Mar 23 2026 Arseniy Romenskiy <romenskiy@altlinux.org> 0.12.1-alt3
- Add OpenSUSE patch to fix reply rendering.
- Add patch to fix call support.
- Add patch to fix screen capture on wayland.
- Add dependencies to call support.
- Add dependencies to get rid of errors messages.
- Update russian translation from upstream.

* Mon Mar 16 2026 Anton Midyukov <antohami@altlinux.org> 0.12.1-alt2
- NMU: Add missing runtime dependencies on libqt6-quickdialogs2 (closes: 58253).

* Tue Mar 10 2026 Arseniy Romenskiy <romenskiy@altlinux.org> 0.12.1-alt1
- New version 0.12.1.

* Sat Feb 14 2026 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.12.0-alt5
- e2k build fix

* Thu Jan 22 2026 Sergey V Turchin <zerg@altlinux.org> 0.12.0-alt4
- Fix to build with Qt-6.10 .

* Mon Sep 01 2025 Paul Wolneykien <manowar@altlinux.org> 0.12.0-alt3
- Fix: Add runtime dependency on libqt6-quickparticles (closes: 49690, 50671).

* Sat Mar 08 2025 Paul Wolneykien <manowar@altlinux.org> 0.12.0-alt2
- Drop explicit qt6-graphicaleffects and qt6-quickcontrols2
  dependencies.

* Sat Mar 08 2025 Paul Wolneykien <manowar@altlinux.org> 0.12.0-alt1
- New version 0.12.0.

* Sun Oct 20 2024 Nazarov Denis <nenderus@altlinux.org> 0.11.3-alt1.1
- NMU: Fix build with fmt 11

* Wed Feb 07 2024 Paul Wolneykien <manowar@altlinux.org> 0.11.3-alt1
- New version 0.11.3.
- Added ZSH site-functions.
- Build with libre2.

* Sun Oct 15 2023 Nazarov Denis <nenderus@altlinux.org> 0.9.3-alt1.1
- NMU: Fix build with fmt 10

* Tue Jul 19 2022 Vladimir Didenko <cow@altlinux.org> 0.9.3-alt1
- Updated to v0.9.3.

* Mon Jan 10 2022 Paul Wolneykien <manowar@altlinux.org> 0.9.1-alt1
- Switch to https://nheko.im/nheko-reborn/nheko.git.
- Updated to v0.9.1.

* Tue Sep 14 2021 Paul Wolneykien <manowar@altlinux.org> 0.8.2-alt1
- Updated to v0.8.2.

* Sun Feb 14 2021 Paul Wolneykien <manowar@altlinux.org> 0.8.1-alt1
- Fixed build requirements for new version.
- Fresh up to v0.8.1.

* Fri Jul 10 2020 Paul Wolneykien <manowar@altlinux.org> 0.7.2-alt2
- Fix: Additional (runtime) QT dependencies.

* Wed Jul 08 2020 Paul Wolneykien <manowar@altlinux.org> 0.7.2-alt1
- Fresh up to v0.7.2.
- Package the SVG icon.

* Tue Mar 31 2020 Paul Wolneykien <manowar@altlinux.org> 0.6.4-alt1
- New upstream: https://github.com/Nheko-Reborn/nheko.git
- Added -DCMAKE_BUILD_TYPE=Release
- New upstream version 0.6.4.

* Wed Dec 05 2018 Paul Wolneykien <manowar@altlinux.org> 0.6.2-alt2
- Adjust nprocs for git.alt (<= 16).

* Mon Dec 03 2018 Paul Wolneykien <manowar@altlinux.org> 0.6.2-alt1
- Initial release.
