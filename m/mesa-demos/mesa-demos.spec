Name: mesa-demos
Version: 9.0.0
Release: alt2
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

%package -n mesa-info
Summary: display info about a GLX/EGL extension and OpenGL renderer
Group: System/X11
Provides: glxinfo = %epoch:%version-%release
Obsoletes: glxinfo < %epoch:%version-%release

%description -n mesa-info
lists information about the GLX/EGL extension

%package -n mesa-gears
Summary: GLX/EGL/VK version of the infamous "gears" GL demo
Group: System/X11
Provides: glxgears = %epoch:%version-%release
Obsoletes: glxgears < %epoch:%version-%release

%description -n mesa-gears
GLX/EGL/VK demo that draws three rotating gears, and prints out
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
%exclude %_bindir/eglgears
%exclude %_bindir/es2gears
%exclude %_bindir/glxgears
%exclude %_bindir/vkgears
%exclude %_bindir/eglinfo
%exclude %_bindir/es2_info
%exclude %_bindir/glxinfo
%_bindir/*
%_datadir/%name

%files -n mesa-info
%_bindir/eglinfo
%_bindir/es2_info
%_bindir/glxinfo

%files -n mesa-gears
%_bindir/eglgears
%_bindir/es2gears
%_bindir/glxgears
%_bindir/vkgears

%changelog
* Wed Oct 04 2023 Valery Inozemtsev <shrek@altlinux.ru> 5:9.0.0-alt2
- another division into subpackages (closes: #47829)

* Wed Jul 12 2023 Valery Inozemtsev <shrek@altlinux.ru> 5:9.0.0-alt1
- 9.0.0

* Tue Jul 17 2018 Valery Inozemtsev <shrek@altlinux.ru> 5:8.4.0-alt1
- initial release

