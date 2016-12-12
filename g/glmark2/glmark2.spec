%define flavors	x11-gl,drm-gl,x11-glesv2,drm-glesv2,wayland-gl,wayland-glesv2

Name:		glmark2
Version:	0.0.0.0.834.f413c5b
Release:	alt1

Summary:	an OpenGL 2.0 and ES 2.0 benchmark
Url:		https://github.com/glmark2/glmark2
Group:		Graphics
License:	GPLv3

# repacked imported tarball from git
Source:		%name-%version.tar

BuildRequires(pre): gcc-c++ python
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel

# GL support
BuildRequires:	libGL-devel
# GLESv2 support
BuildRequires:	libEGL-devel libGLES-devel
# DRM support
BuildRequires:	libdrm-devel libgbm-devel
# Wayland support
BuildRequires:	libwayland-client-devel libwayland-egl-devel

Requires:	%name-data

%package	es2
Summary:	an OpenGL 2.0 and ES 2.0 benchmark - ES 2.0 flavour
Group:		Graphics
Requires:	%name-data

%package	drm
Summary:	an OpenGL 2.0 and ES 2.0 benchmark - DRM flavor
Group:		Graphics
Requires:	%name-data

%package	es2-drm
Summary:	an OpenGL 2.0 and ES 2.0 benchmark - ES 2.0 DRM flavor
Group:		Graphics
Requires:	%name-data

%package	wayland
Summary:	an OpenGL 2.0 and ES 2.0 benchmark - Wayland flavor
Group:		Graphics
Requires:	%name-data

%package	es2-wayland
Summary:	an OpenGL 2.0 and ES 2.0 benchmark - ES 2.0 Wayland flavor
Group:		Graphics
Requires:	%name-data

%package	data
Summary:	an OpenGL 2.0 and ES 2.0 benchmark
Group:		Graphics
BuildArch:	noarch

%define common_descr \
glmark2 is an OpenGL 2.0 and ES 2.0 benchmark. \
\
glmark2 is developed by Alexandros Frantzis and Jesse Barker based on the \
original glmark benchmark by Ben Smith.


%description
%common_descr

%description	es2
%common_descr

This package contains ES 2.0 flavor.

%description	drm
%common_descr

This package contains DRM flavor.

%description	es2-drm
%common_descr

This package contains ES 2.0 DRM flavor.

%description	wayland
%common_descr

This package contains Wayland flavor.

%description	es2-wayland
%common_descr

This package contains ES 2.0 Wayland flavor.

%description	data
%common_descr

This package contains data files.

%prep
%setup

%build
export CFLAGS="%optflags"
export CXXFLAGS="${CFLAGS}"
./waf configure \
	--with-flavors="%flavors" \
	--data-path=%_datadir/%name \
	--prefix=%prefix \
	#
./waf

%install
./waf install --destdir=%buildroot

%files
%_bindir/%name
%_man1dir/%name.1.*

%files es2
%_bindir/%name-es2
%_man1dir/%name-es2.1.*

%files drm
%_bindir/%name-drm
%_man1dir/%name-drm.1.*

%files es2-drm
%_bindir/%name-es2-drm
%_man1dir/%name-es2-drm.1.*

%files wayland
%_bindir/%name-wayland
%_man1dir/%name-wayland.1.*

%files es2-wayland
%_bindir/%name-es2-wayland
%_man1dir/%name-es2-wayland.1.*

%files data
%_datadir/%name

%changelog
* Mon Dec 12 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.0.0.0.834.f413c5b-alt1
- recent upstream commit
- added URL
- fixed CFLAGS and CXXFLAGS
- rebuilt against libpng15

* Fri Sep 09 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.0.0.0.833.gdc1b7fa-alt1
- Initial build.

