%define _unpackaged_files_terminate_build 1

Name: libGLUT
Epoch: 5
Version: 8.0.1
Release: alt4
License: Distributable
Summary: Mesa OpenGL Utility Toolkit library
Group: System/Libraries
Url: https://www.mesa3d.org/

Source: %name-%version.tar

BuildRequires: gcc-c++ libGL-devel libGLU-devel libXi-devel libXmu-devel

%description
Mesa OpenGL Utility Toolkit library

%package -n libmesaglut-devel
Summary: Mesa OpenGL Utility Toolkit development package
Group: Development/C
Requires: libGLUT = %EVR
Conflicts: libfreeglut-devel, libGLUT-devel

%description -n libmesaglut-devel
Mesa OpenGL Utility Toolkit development package

%prep
%setup

%build
%autoreconf
%configure \
	--enable-texture-float \
	--disable-static

%make_build

%install
%makeinstall_std
ln -snf libGLUT.so.3 %buildroot%_libdir/libglut.so

install -m644 include/GL/glutf90.h %buildroot%_includedir/GL

%files
%_libdir/*.so.*

%files -n libmesaglut-devel
%_includedir/GL/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc


%changelog
* Thu Oct 18 2018 Dmitry V. Levin <ldv@altlinux.org> 5:8.0.1-alt4
- Fixed License tag.
- Removed provides for libglut and libglut-devel.
- Reintroduced conflict with libfreeglut-devel.
- Renamed libGLUT-devel to libmesaglut-devel.
- Renamed libglut.so.3 to libGLUT.so.3.

* Wed Oct 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5:8.0.1-alt3
- Removed conflicts to freeglut.

* Tue Feb 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5:8.0.1-alt2
- Added GL/glutf90.h (ALT #26955)

* Tue Feb 14 2012 Valery Inozemtsev <shrek@altlinux.ru> 5:8.0.1-alt1
- 8.0.1

