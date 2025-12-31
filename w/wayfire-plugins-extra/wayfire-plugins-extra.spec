%define _unpackaged_files_terminate_build 1

Name: wayfire-plugins-extra
Version: 0.10.0
Release: alt1

Summary: Additional plugins for Wayfire
License: MIT
Group: Graphical desktop/Other
Url: https://github.com/WayfireWM/wayfire-plugins-extra

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(wayfire)
BuildRequires: pkgconfig(giomm-2.4)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(libevdev)
BuildRequires: boost-devel
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: vulkan-headers
BuildRequires: pkgconfig(xcb-ewmh)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(libinput)
BuildRequires: boost-polygon-devel

%description
%summary.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc LICENSE README.md
%_libdir/wayfire/libannotate.so
%_libdir/wayfire/libautorotate-iio.so
%_libdir/wayfire/libbench.so
%_libdir/wayfire/libcrosshair.so
%_libdir/wayfire/libextra-animations.so
%_libdir/wayfire/libfocus-change.so
%_libdir/wayfire/libfocus-steal-prevent.so
%_libdir/wayfire/libfollow-focus.so
%_libdir/wayfire/libforce-fullscreen.so
%_libdir/wayfire/libghost.so
%_libdir/wayfire/libglib-main-loop.so
%_libdir/wayfire/libhide-cursor.so
%_libdir/wayfire/libjoin-views.so
%_libdir/wayfire/libkeycolor.so
%_libdir/wayfire/libmag.so
%_libdir/wayfire/libobs.so
%_libdir/wayfire/libpin-view.so
%_libdir/wayfire/libshowrepaint.so
%_libdir/wayfire/libshowtouch.so
%_libdir/wayfire/libview-shot.so
%_libdir/wayfire/libwater.so
%_libdir/wayfire/libwinzoom.so
%_libdir/wayfire/libworkspace-names.so
%_datadir/wayfire/metadata/annotate.xml
%_datadir/wayfire/metadata/autorotate-iio.xml
%_datadir/wayfire/metadata/bench.xml
%_datadir/wayfire/metadata/crosshair.xml
%_datadir/wayfire/metadata/extra-animations.xml
%_datadir/wayfire/metadata/focus-change.xml
%_datadir/wayfire/metadata/focus-steal-prevent.xml
%_datadir/wayfire/metadata/follow-focus.xml
%_datadir/wayfire/metadata/force-fullscreen.xml
%_datadir/wayfire/metadata/ghost.xml
%_datadir/wayfire/metadata/hide-cursor.xml
%_datadir/wayfire/metadata/join-views.xml
%_datadir/wayfire/metadata/keycolor.xml
%_datadir/wayfire/metadata/mag.xml
%_datadir/wayfire/metadata/obs.xml
%_datadir/wayfire/metadata/pin-view.xml
%_datadir/wayfire/metadata/showrepaint.xml
%_datadir/wayfire/metadata/showtouch.xml
%_datadir/wayfire/metadata/view-shot.xml
%_datadir/wayfire/metadata/water.xml
%_datadir/wayfire/metadata/window-zoom.xml
%_datadir/wayfire/metadata/workspace-names.xml

%changelog
* Mon Dec 29 2025 Nikolay Strelkov <snk@altlinux.org> 0.10.0-alt1
- Initial build for Sisyphus
