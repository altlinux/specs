Name: musikcube
Version: 3.0.5
Release: alt2

Summary: a cross-platform, terminal-based audio engine, library, player and server written in c++

License: BSD-3-Clause
Group: Sound
URL: https://musikcube.com
VCS: https://github.com/clangen/musikcube

Source: %name-%version.tar
Patch: alt-patch-rpath-script.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: /proc asio-devel cmake gcc-c++
BuildRequires: libavformat-devel libcap-devel libcurl-devel
BuildRequires: libev-devel libgme-devel liblame-devel libmicrohttpd-devel
BuildRequires: libmpg123-devel libncursesw-devel libopenmpt-devel
BuildRequires: libportaudio2-devel libpulseaudio-devel libswresample-devel
BuildRequires: libsystemd-devel libtag-devel patchelf pipewire-libs-devel

%description
a cross-platform, terminal-based audio engine, library, player
and server written in c++.

musikcube compiles and runs easily on windows, macos and linux.
It also runs well on a raspberry pi with raspbian, and can be setup
as a streaming audio server.

%prep
%setup
%autopatch -p1

# remove empty dirs
rm -rv src/3rdparty/{asio,bin}

# fix paths
sed -i 's|share|%_lib|' src/musikcube*/musikcube*.in
sed -i 's|share/%name|%_lib/%name|g' .cmake/InstallFiles.cmake

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DENABLE_PCH=true \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no
%cmake_build

%install
%cmake_install

%files
%doc CHANGELOG.txt CONTRIBUTORS.txt LICENSE.txt README.md
%_bindir/musikcube
%_bindir/musikcubed
%_libdir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Mon Jun 01 2026 Alexander Kovalev <alexvk@altlinux.org> 3.0.5-alt2
- Build with debuginfo.
- Add libcap-devel to BuildRequires.
- Add patch to fix rpath.

* Sun Sep 28 2025 Alexander Kovalev <alexvk@altlinux.org> 3.0.5-alt1
- New version 3.0.5.
- Remove submodule asio.

* Sun Aug 10 2025 Alexander Kovalev <alexvk@altlinux.org> 3.0.4-alt2
- Build with submodule asio to fix FTBFS.

* Fri Jan 24 2025 Alexander Kovalev <alexvk@altlinux.org> 3.0.4-alt1
- Initial build for ALT.
