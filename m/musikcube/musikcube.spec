%global __find_debuginfo_files %nil

Name: musikcube
Version: 3.0.4
Release: alt1

Summary: a cross-platform, terminal-based audio engine, library, player and server written in c++

License: BSD-3-Clause
Group: Sound
URL: https://musikcube.com
VCS: https://github.com/clangen/musikcube

Source: %name-%version.tar

BuildRequires: asio-devel cmake gcc-c++ libavformat-devel libcurl-devel
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

%build
rm -rv src/3rdparty/{asio,bin}
sed -i 's/share/%_lib/' src/musikcube*/musikcube*.in
sed -i 's|share/%name|%_lib/%name|g' .cmake/InstallFiles.cmake
cmake \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DCMAKE_BUILD_TYPE=Release \
    -DENABLE_PCH=true \
    .
%make_build

%install
%makeinstall_std

%files
%doc CHANGELOG.txt CONTRIBUTORS.txt LICENSE.txt README.md
%_bindir/musikcube
%_bindir/musikcubed
%_libdir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Fri Jan 24 2025 Alexander Kovalev <alexvk@altlinux.org> 3.0.4-alt1
- Initial build for ALT.
