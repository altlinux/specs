%define _unpackaged_files_terminate_build 1

Name: vogl
Version: 1.0
Release: alt1

Summary: OpenGL capture / playback debugger.
License: MIT
Group: Development/Debuggers

Url: https://github.com/ValveSoftware/vogl

Source:%name-%version.tar

Patch:%name-alt-build.patch
Patch2:%name-223-upstream-issue.patch
Patch3:%name-build-for-sisyphus.patch
ExclusiveArch: x86_64

BuildRequires: /usr/bin/clang /usr/bin/clang++
BuildRequires: cmake
BuildRequires: libX11-devel
BuildRequires: libtinyxml2-devel
BuildRequires: liblzma-devel
BuildRequires: libunwind-devel
BuildRequires: libturbojpeg-devel
BuildRequires: libGLES-devel
BuildRequires: freeglut-devel
BuildRequires: libSDL2_gfx-devel
BuildRequires: libSDL2_image-devel
BuildRequires: libSDL2_ttf-devel
BuildRequires: libjpeg-devel
BuildRequires: libdrm-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXdamage-devel
BuildRequires: libXxf86vm-devel
BuildRequires: qt5-base-devel
BuildRequires: tinyxml-devel
BuildRequires: libdwarf-devel

%description
VOGL is a debugger for the OpenGL rendering API intended to be used
in the development of video games.
VOGL was originally written at RAD Game Tools and Valve Corporation.
VOGL is free and open-source software subject to the terms of the MIT License.

There is a graphical front-end implementing Qt5-based GUI widgets.

VOGL was initially released with support for Linux operating systems only,
but on April 23, 2014, additional support for Microsoft Windows was released.

Goals included:

--Free and open-source
--Steam integration
--Vendor and driver version neutral
--No special app builds needed
--Frame capturing, full stream tracing, trace trimming
--Optimized replayer
--OpenGL usage validation
--Regression testing, benchmarking
--Robust API support: OpenGL v3/4.x, core or compatibility contexts
--UI to edit captures, inspect state, diff snapshots, control tracing
--VOGLperf is a benchmarking tool for Linux OpenGL games.

%package tests
Summary: Vogl tests apps
Group: Development/Debuggers
Requires: %name = %EVR

%description tests
Tests for vogl

%prep
%setup -q -n %name-%version
%patch -p1
%patch2 -p1
%patch3 -p1

find . -type f | xargs sed -i -e "s:@LIBDIR@:%_libdir:g"

%build
%remove_optflags -frecord-gcc-switches 
export CC=clang
export CXX=clang++

%cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_X64=On

%cmake_build

%install
cd vogl_build
mkdir -m 755 -p %buildroot%_bindir
mkdir -m 755 -p %buildroot%_libdir

install  glxspheres64                %buildroot%_bindir
install  ktxtool64                   %buildroot%_bindir
install  libbacktrace_test64         %buildroot%_bindir
install  vogl64                      %buildroot%_bindir
install  voglbench64                 %buildroot%_bindir
install  vogleditor64                %buildroot%_bindir
install  voglgen64                   %buildroot%_bindir
install  vogltest64                  %buildroot%_bindir
install  libbacktrace_testlib64.so   %buildroot%_libdir
install  libvogltrace64.so           %buildroot%_libdir

%files
%_bindir/glxspheres64
%_bindir/ktxtool64
%_bindir/vogl64
%_bindir/voglbench64
%_bindir/vogleditor64
%_bindir/voglgen64
%_libdir/libvogltrace64.so

%files tests
%_bindir/vogltest64
%_libdir/libbacktrace_testlib64.so
%_bindir/libbacktrace_test64

%changelog
* Tue Oct 23 2018 Alexey Melyashinsky <bip@altlinux.org> 1.0-alt1
- Initial build for ALT
