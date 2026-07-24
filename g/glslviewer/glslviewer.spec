%define _unpackage_files_terminate_build 1

Name: glslviewer
Version: 3.5.2
Release: alt1

Summary: OpenGL Sandbox for GLSL shaders
Group: Graphics
License: BSD-3-Clause
URL: https://github.com/patriciogonzalezvivo/glslViewer

Source: %name-%version.tar
Source1: modules-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libX11-devel
BuildRequires: libglfw3-devel
BuildRequires: libglm-devel
BuildRequires: libGLEW-devel
BuildRequires: libcurl-devel
BuildRequires: libncurses-devel
BuildRequires: liblo-devel
BuildRequires: python3
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: libXi-devel
BuildRequires: rpm-build-python3

%description
OpenGL Sandbox to display 2D/3D GLSL shaders.

%prep
%setup -a1

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
%_bindir/glslViewer
%_bindir/glslThumbnailer
%_bindir/glslScreenSaver
%_datadir/pixmaps/glslViewer.png
%_datadir/applications/glslViewer.desktop
%_datadir/mime/packages/glslViewer-types.xml
%_datadir/thumbnailers/glslViewer.thumbnailer
%dir %_datadir/thumbnailers
%dir %_datadir/glslViewer
%_datadir/glslViewer/*

%changelog
* Wed Jul 22 2026 Anton Osipov <radiolamp@altlinux.org> 3.5.2-alt1
- Initial build for ALT Linux
