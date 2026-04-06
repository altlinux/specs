%define _name wlroots
%define soversion 0.20

Name: lib%_name-%soversion
Version: 0.20.0
Release: alt1

Summary: Modular Wayland compositor library
License: MIT
Group: System/Libraries
Url: https://gitlab.freedesktop.org/wlroots/wlroots

Vcs: https://gitlab.freedesktop.org/wlroots/wlroots.git

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Source: https://gitlab.freedesktop.org/wlroots/wlroots/-/releases/%version/downloads/%_name-%version.tar.gz
#Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson cmake
BuildRequires: ctags
BuildRequires: glslang
BuildRequires: pkgconfig(hwdata)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libdisplay-info)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libseat)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(vulkan)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(x11-xcb)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-composite)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-render)
BuildRequires: pkgconfig(xcb-renderutil)
BuildRequires: pkgconfig(xcb-xfixes)
BuildRequires: pkgconfig(xcb-xinput)
BuildRequires: pkgconfig(xcb-errors)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xwayland)
BuildRequires: pkgconfig(libliftoff)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(cairo)

%description
%summary.

%package -n libwlroots%soversion
Summary: Modular Wayland compositor library
Group: System/Libraries

%description -n libwlroots%soversion
%summary.

%package -n libwlroots%soversion-devel
Summary: Development files for libwlroots
Group: Development/C
Requires: libwlroots%soversion = %EVR
Provides: libwlroots-devel

%description -n libwlroots%soversion-devel
This package provides development files for libwlroots library.

%prep
%setup -n %_name-%version

%build
%meson \
  "-Dbackends=[
    'drm',
	'libinput',
    'x11',
  ]" \
  -Dxwayland=enabled \
  -Dxcb-errors=enabled

%meson_build

%install
%meson_install

%check
%__meson_test

%files -n libwlroots%soversion
%_libdir/libwlroots-%soversion.so
%doc README.md LICENSE

%files -n libwlroots%soversion-devel
%_includedir/wlroots-%soversion/
%_pkgconfigdir/wlroots-%soversion.pc

%changelog
* Mon Apr 06 2026 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt1
- 0.20.0

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- first build for Sisyphus

