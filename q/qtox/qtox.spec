%define _unpackaged_files_terminate_build 1

Name: qtox
Version: 1.18.5
Release: alt1

Summary: Powerful Tox client that follows the Tox design guidelines

License: GPL-3.0-or-later
Group: Networking/Instant messaging
Url: https://qtox.github.io/
VCS: https://github.com/TokTok/qTox.git

Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libavdevice-devel
BuildRequires: libavformat-devel
BuildRequires: libexif-devel
BuildRequires: libfilteraudio-devel
BuildRequires: libopenal-devel
BuildRequires: libqrencode-devel
BuildRequires: libsodium-devel
BuildRequires: libsqlcipher-devel
BuildRequires: libswresample-devel
BuildRequires: libswscale-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: qt6-base-devel
BuildRequires: qt6-svg-devel
BuildRequires: qt6-tools-devel
BuildRequires: toxcore-devel

%description
Powerful Tox Qt6 client that follows the Tox design guidelines.

%prep
%setup
%ifarch %e2k
# lcc: error: option "-ftrapv" is not supported
sed -i '/^ *-ftrapv;/d' cmake/warnings/CMakeLists.txt
%endif

%build
%add_optflags -fpermissive
%if_with ffmpeg_static
export PKG_CONFIG_PATH=%_libdir/ffmpeg-static/%_lib/pkgconfig/
%endif
%cmake_insource
%make_build VERBOSE=1

%install
%makeinstall_std

%files
%_bindir/%name
%_desktopdir/io.github.qtox.qTox.desktop
%_datadir/metainfo/io.github.qtox.qTox.appdata.xml
%_iconsdir/hicolor/*/apps/*

%changelog
* Thu Jun 11 2026 Anton Farygin <rider@altlinux.org> 1.18.5-alt1
- 1.18.4 -> 1.18.5

* Tue Apr 07 2026 Anton Farygin <rider@altlinux.org> 1.18.4-alt1
- 1.18.3 -> 1.18.4

* Mon Nov 17 2025 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.18.3-alt2
- e2k build fix

* Mon Mar 10 2025 Constantin Sunzow <protvin@altlinux.org> 1.18.3-alt1
- New version.

* Thu Jan 23 2025 Constantin Sunzow <protvin@altlinux.org> 1.18.2-alt1
- New version.

* Sat Sep 16 2023 Vitaly Chikunov <vt@altlinux.org> 1.16.3-alt4
- NMU: Fix FTBFS adding -fpermissive to CMAKE_CXX_FLAGS for this old codebase
  to compile on modern toolchain. This is required for libsodium update.
- NOTE: This project is unmaintained upstream since 2023-02-12.

* Wed Jul 10 2019 Vitaly Lipatov <lav@altlinux.ru> 1.16.3-alt3
- drop ubt macro

* Tue Feb 26 2019 Vitaly Lipatov <lav@altlinux.ru> 1.16.3-alt2
- rebuild with libqrencode4

* Thu Aug 30 2018 Vitaly Lipatov <lav@altlinux.ru> 1.16.3-alt1
- new version 1.16.3 (with rpmrb script)

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 1.15.0-alt2
- rebuild with ffmpeg 4.0

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 1.15.0-alt1
- new version 1.15.0 (with rpmrb script)

* Tue Mar 20 2018 Vitaly Lipatov <lav@altlinux.ru> 1.14.0-alt1
- new version 1.14.0 (with rpmrb script)

* Mon Feb 12 2018 Vitaly Lipatov <lav@altlinux.ru> 1.13.0-alt1.1
- NMU: autorebuild with libsodium-1.0.16

* Sun Dec 10 2017 Vitaly Lipatov <lav@altlinux.ru> 1.13.0-alt1
- new version 1.13.0 (with rpmrb script)

* Fri Oct 06 2017 Vitaly Lipatov <lav@altlinux.ru> 1.12.0-alt1
- new version 1.12.0 (with rpmrb script)
- switched to cmake
- rebuild with ffmpeg really

* Sat Jun 17 2017 Vitaly Lipatov <lav@altlinux.ru> 1.10.2-alt1
- new version 1.10.2 (with rpmrb script)
- build with new toxcore-devel 0.1.9

* Fri Jun 09 2017 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- new version (1.6.0) with rpmgs script
- rebuild with ffmpeg

* Mon Mar 27 2017 Denis Smirnov <mithraen@altlinux.ru> 1.4.1.1-alt2
- rebuild with new toxcore and libsodium

* Mon Jul 25 2016 Vitaly Lipatov <lav@altlinux.ru> 1.4.1.1-alt1
- build new version with toxcore 0.0.1-alt1.20160725
_ still incompatible with libav (a fork of ffmpeg) (see alt bug #32310)

* Sat Jun 13 2015 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- initial build for ALT Linux Sisyphus
