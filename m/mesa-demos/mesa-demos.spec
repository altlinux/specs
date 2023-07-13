Name: mesa-demos
Version: 9.0.0
Release: alt1
Epoch: 5
Summary: Miscellaneous Mesa GL utilities
License: MIT
Group: Development/Other
Url: http://www.mesa3d.org

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: meson gcc-c++ glslang-devel libGLES-devel libGLEW-devel libGLUT-devel libOSMesa-devel libcairo-devel libdecor-devel
BuildRequires: libdrm-devel libgbm-devel libvulkan-devel libwayland-egl-devel libxkbcommon-x11-devel pkgconfig(wayland-protocols)

%description
This package provides several basic GL utilities built by Mesa

%package -n glxinfo
Summary: display info about a GLX extension and OpenGL renderer
Group: System/X11

%description -n glxinfo
glxinfo lists information about the GLX extension, OpenGL capable visu-
als, and the OpenGL renderer on an X server. The GLX and renderer  info
includes  the  version  and extension attributes. The visual info lists
the GLX visual attributes available  for  each  OpenGL  capable  visual
(e.g.  whether  the  visual is double buffered, the component sizes, Z-
buffering depth, etc)

%package -n glxgears
Summary: GLX version of the infamous "gears" GL demo
Group: System/X11

%description -n glxgears
glxgears  is a GLX demo that draws three rotating gears, and prints out
framerate information to stdout

%prep
%setup -q
%patch -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%exclude %_bindir/line
%exclude %_bindir/glxgears
%exclude %_bindir/glxinfo
%_bindir/*
%_datadir/%name

%files -n glxinfo
%_bindir/glxinfo

%files -n glxgears
%_bindir/glxgears

%changelog
* Wed Jul 12 2023 Valery Inozemtsev <shrek@altlinux.ru> 5:9.0.0-alt1
- 9.0.0

* Tue Jul 17 2018 Valery Inozemtsev <shrek@altlinux.ru> 5:8.4.0-alt1
- initial release

