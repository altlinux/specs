Name: plasma-wallpaper-engine-kde-plugin
Version:0.5.4
Release: alt1.gited58dd8

Summary: A kde wallpaper plugin integrating wallpaper engine
License: GPL-2.0
Group: Graphical desktop/KDE
Url: https://github.com/catsout/wallpaper-engine-kde-plugin

# Source-url: https://github.com/catsout/wallpaper-engine-kde-plugin.git
Source: %name-%version.tar

ExcludeArch: i586

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ extra-cmake-modules
BuildRequires: libvulkan-devel
BuildRequires: plasma-workspace-devel plasma-workspace-qml glslang-devel glslc
BuildRequires: kf6-kpackage-devel kf6-kcoreaddons-devel kf6-kservice-devel plasma6-lib-devel kf6-kwindowsystem-devel
BuildRequires: gstreamer1.0-devel
BuildRequires: gst-libav
BuildRequires: liblz4-devel
BuildRequires: libmpv-devel
BuildRequires: python3-module-websockets
BuildRequires: qt6-base-devel qt6-webchannel-devel qt6-websockets-devel

Requires: python3-module-websockets

%description
A wallpaper plugin integrating wallpaper engine into kde wallpaper setting.

%prep
%setup

%build
%cmake -DUSE_PLASMAPKG=OFF
%cmake_build

%install
%cmake_install

%files
%_libdir/qt6/qml/com/github/catsout/wallpaperEngineKde/libWallpaperEngineKde.so
%_libdir/qt6/qml/com/github/catsout/wallpaperEngineKde/qmldir
%_datadir/plasma/wallpapers/com.github.catsout.wallpaperEngineKde
%_datadir/metainfo/com.github.catsout.wallpaperEngineKde.appdata.xml


%changelog
* Tue Nov 19 2024 Ivan Mazhukin <vanomj@altlinux.org> 0.5.4-alt1.gited58dd8
- Initial build for ALT Sisyphus

