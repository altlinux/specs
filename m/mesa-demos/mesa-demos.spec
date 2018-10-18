Name: mesa-demos
Version: 8.4.0
Release: alt1
Epoch: 5
Summary: Miscellaneous Mesa GL utilities
License: MIT
Group: Development/Other
Url: http://www.mesa3d.org

Source: %name-%version.tar
#Patch: %name-%version.patch

BuildRequires: gcc-c++ libGLES-devel libGLEW-devel libGLUT-devel libXext-devel libdrm-devel libgbm-devel libfreetype-devel libwayland-egl-devel

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

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

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
* Tue Jul 17 2018 Valery Inozemtsev <shrek@altlinux.ru> 5:8.4.0-alt1
- initial release

