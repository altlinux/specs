%def_disable check

Name: libvdpau-va-gl
Version: 0.3.4
Release: alt2.git20150311
Summary: VDPAU driver with OpenGL/VAAPI backend
License: LGPLv3
Group: System/Libraries
Url: https://github.com/i-rinat/libvdpau-va-gl
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/i-rinat/libvdpau-va-gl.git
Source: %name-%version.tar
Source1: http://ftp.de.debian.org/debian/pool/main/libv/libvdpau-va-gl/libvdpau-va-gl_0.3.4-2.debian.tar.xz

BuildPreReq: libvdpau-devel libva-devel glib2-devel libswscale-devel
BuildPreReq: libGLU-devel doxygen graphviz cmake gcc-c++ libXau-devel
BuildPreReq: libICE-devel libSM-devel libXres-devel libXext-devel ctest
BuildPreReq: libXtst-devel libXcomposite-devel libXcursor-devel
BuildPreReq: libXdamage-devel libXdmcp-devel libXfixes-devel libXft-devel
BuildPreReq: libXi-devel libXinerama-devel libxkbfile-devel libXmu-devel
BuildPreReq: libXpm-devel libXrandr-devel libXrender-devel
BuildPreReq: libXScrnSaver-devel libXt-devel libXv-devel
BuildPreReq: libXxf86misc-devel libXxf86vm-devel libxshmfence-devel

Provides: vdpau-driver = %EVR

%description
Many applications can use VDPAU to accelerate portions of the video
decoding process and video post-processing to the GPU video hardware.
Unfortunately, there is no such library for many graphic chipsets. Some
applications also support VA-API but many of them, including Adobe Flash
Player, don't.

This library proposes a generic VDPAU library. It uses OpenGL under the
hood to accelerate drawing and scaling and VA-API (if available) to
accelerate video decoding.

%prep
%setup

tar -xf %SOURCE1
sed -i '1i\#!/bin/sh\n' debian/20vdpau-va-gl

%build
cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	.
%make_build VERBOSE=1

doxygen

%install
%makeinstall_std

install -d %buildroot%_sysconfdir/profile.d
install -p -m755 debian/20vdpau-va-gl \
	%buildroot%_sysconfdir/profile.d/20vdpau-va-gl.sh
install -d %buildroot%_docdir/libvdpau-va-gl1

%check
%make VERBOSE=1 check
%make VERBOSE=1 test

%files
%doc debian/README.Debian ChangeLog *.md doc/*.md html
%config(noreplace) %_sysconfdir/profile.d/*
%_libdir/vdpau/*

%changelog
* Wed Apr 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt2.git20150311
- Moved 20vdpau-va-gl into %_sysconfdir/profile.d

* Tue Apr 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1.git20150311
- Initial build for Sisyphus (ALT #30921)

