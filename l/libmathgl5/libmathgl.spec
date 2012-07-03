%define oname mathgl
Name: lib%{oname}5
Version: 1.11.0.1
Release: alt1.4

Summary: Library of fast C++ routines for the plotting of the data

License: LGPL
Group: System/Legacy libraries
Url: http://www.sf.net/projects/mathgl/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%oname/%oname-%version.tar

# Automatically added by buildreq on Fri Jan 08 2010
BuildRequires: gcc-c++ glibc-devel libGL-devel libfreeglut-devel libgif-devel libgsl-devel libhdf5-devel libjpeg-devel libpng-devel python-devel libnumpy-devel swig

BuildPreReq: chrpath

%description
MathGL is a free library of fast C++ routines for the plotting of the data
varied in one or more dimensions. It uses OpenGL (www.opengl.org)
for the plotting. Also there is a simple window interface based on
GLUT. This provides high compatibility with any operating system
(really any which has OpenGL-like libraries).

%package devel
Summary: Header files for %name
Group: Development/Other
Requires: %name = %version-%release
Conflicts: libmathgl-devel

%description devel
Header files for %name library.

%package -n python-module-mathgl
Summary: Python module for %name
Group: System/Libraries
Requires: %name = %version-%release

%description -n python-module-mathgl
Python module for %name.

%prep
%setup -n %oname-%version

%build
%add_optflags `pkg-config --cflags hdf5`
%configure --enable-tiff --enable-jpeg --enable-python \
	--enable-hdf5 \
	--disable-static
# TODO:  --enable-fltk
%make_build

%install
%makeinstall_std

for i in %buildroot%_bindir/* %buildroot%python_sitelibdir/*.so
do
	chrpath -d $i ||:
done

%ifarch x86_64
mv %buildroot%python_sitelibdir_noarch/*.py* \
	%buildroot%python_sitelibdir/
%endif

%files
%_bindir/mgl2*
%doc AUTHORS README NEWS
%_libdir/libmgl.so.5.0.0
%_libdir/libmgl.so.5
#_datadir/mathgl/

%files devel
#_bindir/mgl_example
%_libdir/libmgl.so
%_includedir/mgl/

#files -n python-module-mathgl
#python_sitelibdir/*

%changelog
* Sun May 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.0.1-alt1.4
- Restored devel subpackage

* Thu May 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.0.1-alt1.3
- Moved this version into System/Legacy libraries

* Wed Feb 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.0.1-alt1.2
- Removed bad RPATH

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.11.0.1-alt1.1.1
- Rebuild with Python-2.7

* Thu Sep 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.0.1-alt1.1
- Rebuilt with libhdf5-7

* Mon Jan 24 2011 Vitaly Lipatov <lav@altlinux.ru> 1.11.0.1-alt1
- new version 1.11.0.1 (with rpmrb script)

* Tue Nov 09 2010 Vitaly Lipatov <lav@altlinux.ru> 1.11-alt1
- new version 1.11 (with rpmrb script) (ALT bug #24481)

* Mon Feb 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10-alt2.1
- Rebuilt with reformed NumPy

* Fri Jan 08 2010 Vitaly Lipatov <lav@altlinux.ru> 1.10-alt2
- cleanup spec, update buildreqs
- build with hdf5 support

* Sun Jan 03 2010 Vitaly Lipatov <lav@altlinux.ru> 1.10-alt1
- new version 1.10 (with rpmrb script)

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9-alt1.1
- Rebuilt with python 2.6

* Thu Jul 09 2009 Vitaly Lipatov <lav@altlinux.ru> 1.9-alt1
- new version (1.9) import in git

* Wed Jun 03 2009 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt2
- rebuild with libhdf5 v1.8.3

* Thu Apr 23 2009 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- new version 1.8.1 (with rpmrb script)
- enable python module build

* Wed Dec 24 2008 Vitaly Lipatov <lav@altlinux.ru> 1.8-alt1
- new version 1.8 (with rpmrb script)
- update buildreq, cleanup spec

* Wed Oct 31 2007 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt1
- new version 1.4 (with rpmrb script)
- soname changed

* Mon Oct 08 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- new version 1.2.2 (with rpmrb script)

* Sun Sep 16 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- initial build for ALT Linux Sisyphus
