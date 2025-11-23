%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: rclone-browser
Version: 1.8.0
Release: alt1

Summary: Simple cross platform GUI for rclone
License: MIT
Group: Networking/File transfer
Url: https://github.com/kapitainsky/RcloneBrowser

Source: %name-%version.tar

# sync with rclone-browser (1.8.0-6) from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5Widgets)

Requires: rclone

%description
This is a GUI for rclone, which is a program to sync files and directories
between the local file system and a variety of commercial cloud storage
providers.

%prep
%setup
%patch -p1
sed -i "s|Categories=.*|Categories=Qt;Network;FileTransfer;|" assets/rclone-browser.desktop

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc CHANGELOG.md LICENSE README.md
%_bindir/rclone-browser
%_desktopdir/rclone-browser.desktop
%_iconsdir/hicolor/128x128/apps/rclone-browser.png
%_iconsdir/hicolor/256x256/apps/rclone-browser.png
%_iconsdir/hicolor/32x32/apps/rclone-browser.png
%_iconsdir/hicolor/512x512/apps/rclone-browser.png
%_iconsdir/hicolor/64x64/apps/rclone-browser.png
%_iconsdir/hicolor/scalable/apps/rclone-browser.svg

%changelog
* Sat Nov 22 2025 Nikolay Strelkov <snk@altlinux.org> 1.8.0-alt1
- Initial build for Sisyphus
