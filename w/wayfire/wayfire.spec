# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%set_verify_elf_method relaxed

Name: wayfire
Summary: A modular and extensible wayland compositor
Version: 0.9.0
Release: alt1
License: MIT
Url: https://wayfire.org
Group: Graphical desktop/Other

Source: %name-%version.tar
# Source1-url: https://github.com/WayfireWM/wf-config
Source1: wf-utils.tar
# Source2-url: https://github.com/WayfireWM/wf-touch
Source2: wf-touch.tar

Patch: %name-%version-%release.patch

BuildRequires: cmake
BuildRequires: gcc-c++ libgomp-devel
BuildRequires: inotify-tools-devel
BuildRequires: libevdev-devel
BuildRequires: meson >= 0.63.0

BuildRequires: doctest-devel
BuildRequires: libglm-devel

BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libinput) >= 1.7.0
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(nlohmann_json) >= 3.11.2
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-protocols) >= 1.12
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wf-config) >= 0.9.0
BuildRequires: pkgconfig(wlroots) >= 0.17.0
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xcb-ewmh)	

# Recommends:
#Requires: wayfire-config-manager
#Requires: wf-shell

%description
Wayfire is a 3D Wayland compositor, inspired by Compiz and based on wlroots.
It aims to create a customizable, extendable and lightweight environment
without sacrificing its appearance.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %EVR

%description devel
Development files for %name.

%prep
%setup
tar -xvf %SOURCE1 -C subprojects/
tar -xvf %SOURCE2 -C subprojects/
%patch -p1

%build
%meson                            \
    -Duse_system_wfconfig=enabled \
    -Duse_system_wlroots=enabled  \
%nil
%meson_build

%install
%meson_install
install -D -p -m 0644 %name.desktop %buildroot%_datadir/wayland-sessions/%name.desktop
rm -v %buildroot%_libdir/libwftouch.a

%files
%doc LICENSE
%doc README.md %name.ini
%_bindir/%name
%_datadir/%name/
%_datadir/wayland-sessions/*.desktop
%_libdir/%name/
%_libdir/lib%name-blur-base.so
%_libdir/libwf-utils.so.0*
%_man1dir/*.1*

%files devel
%_includedir/%name/
%_libdir/libwf-utils.so
%_pkgconfigdir/*.pc

%changelog
* Sat Oct 12 2024 Anton Midyukov <antohami@altlinux.org> 0.9.0-alt1
- initial build
