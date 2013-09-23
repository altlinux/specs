%define nversion 3.1
%define dversion April2012

Name: nvidia-cg-toolkit
Version: %{nversion}_%dversion
Release: alt1

Summary: NVIDIA Cg Toolkit
License: Proprietary
Group: Development/Tools

URL: https://developer.nvidia.com/cg-toolkit
Packager: Nazarov Denis <nenderus@altlinux.org>
Vendor: NVIDIA Corporation

ExclusiveArch: %ix86 x86_64

%ifarch %ix86
BuildArch:      i586
%else
BuildArch:      x86_64
%endif

Source0: http://developer.download.nvidia.com/cg/Cg_%nversion/Cg-%{version}_x86.tgz
Source1: http://developer.download.nvidia.com/cg/Cg_%nversion/Cg-%{version}_x86_64.tgz

Requires: glibc >= 2.4
Requires: libcg = %version-%release
Requires: libcggl = %version-%release

BuildRequires: libGLUT-devel
BuildRequires: libXi-devel
BuildRequires: libXmu-devel
BuildRequires: libglew-devel
BuildRequires: libstdc++-devel

%description
The NVIDIA Cg Toolkit provides a compiler for the Cg language, runtime libraries for use with both leading graphics APIs, runtime libraries for CgFX, example applications, and extensive documentation. Supporting over 20 different OpenGL and DirectX profile targets, Cg will allow you to incorporate stunning interactive effects into your 3D applications.
The runtime package contains the compiler and runtime libraries only.

%package -n libcg
Summary: Nvidia Cg core runtime library
Group: System/Libraries

%description -n libcg
C for graphics (CG) is a high-level shading language developed by Nvidia in close collaboration with Microsoft for programming vertex and pixel shaders.

%package -n libcg-devel
Summary: Development files for Nvidia Cg core runtime library
Group: Development/C++
BuildArch: noarch
Requires: libcg = %version-%release

%description -n libcg-devel
C for graphics (CG) is a high-level shading language developed by Nvidia in close collaboration with Microsoft for programming vertex and pixel shaders.

%package -n libcggl
Summary: Nvidia Cg OpenGL runtime library
Group: System/Libraries
Requires: libcg = %version-%release

%description -n libcggl
C for graphics (CG) is a high-level shading language developed by Nvidia in close collaboration with Microsoft for programming vertex and pixel shaders.

%package -n libcggl-devel
Summary: Development files for Nvidia Cg OpenGL runtime library
Group: Development/C++
BuildArch: noarch
Requires: libcggl = %version-%release
Requires: libcg-devel = %version-%release

%description -n libcggl-devel
C for graphics (CG) is a high-level shading language developed by Nvidia in close collaboration with Microsoft for programming vertex and pixel shaders.

%prep
%ifarch %ix86
%setup -c %name-%version
%else
%setup -c %name-%version -D -T -a 1
%endif

%__rm usr/bin/{cgfxcat,cginfo}

%build

for b in cgfxcat cginfo ; do
	%__sed -i -e 's/-DGLEW_STATIC//' usr/local/Cg/examples/Tools/${b}/Makefile.${b}
	%__sed -i -e 's/-Wall/%{optflags}/' usr/local/Cg/examples/Tools/${b}/Makefile.${b}
	%make_build -C usr/local/Cg/examples/Tools/${b} \
		GLEW=%prefix \
		CG_INC_PATH=%_builddir/%buildsubdir/usr/include \
		CG_LIB_PATH=%_builddir/%buildsubdir/%_libdir
	%__mv usr/local/Cg/examples/Tools/${b}/${b} usr/bin
	%__strip usr/bin/${b}
done

%install
%__install -Dp -m0755 usr/bin/cgc %buildroot%_bindir/cgc
%__install -Dp -m0755 usr/bin/cgfxcat %buildroot%_bindir/cgfxcat
%__install -Dp -m0755 usr/bin/cginfo %buildroot%_bindir/cginfo
%__install -Dp -m0644 usr/include/Cg/cg.h %buildroot%_includedir/Cg/cg.h
%__install -Dp -m0644 usr/include/Cg/cgGL.h %buildroot%_includedir/Cg/cgGL.h
%ifarch %ix86
%__install -Dp -m0644 usr/lib/libCg.so %buildroot%_libdir/libCg.so
%__install -Dp -m0644 usr/lib/libCgGL.so %buildroot%_libdir/libCgGL.so
%else
%__install -Dp -m0644 usr/lib64/libCg.so %buildroot%_libdir/libCg.so
%__install -Dp -m0644 usr/lib64/libCgGL.so %buildroot%_libdir/libCgGL.so
%endif

%files
%doc usr/local/Cg/docs usr/local/Cg/MANIFEST usr/local/Cg/README
%_bindir/cg*

%files -n libcg
%dir %_includedir/Cg
%_libdir/libCg.so

%files -n libcg-devel
%dir %_includedir/Cg
%_includedir/Cg/cg.h

%files -n libcggl
%dir %_includedir/Cg
%_libdir/libCgGL.so

%files -n libcggl-devel
%dir %_includedir/Cg
%_includedir/Cg/cgGL.h

%changelog
* Mon Sep 23 2013 Nazarov Denis <nenderus@altlinux.org> 3.1_April2012-alt1
- Initial build for ALT Linux
