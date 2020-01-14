%define oname OpenGL

%def_with python3

Name: python-module-%oname
Version: 3.1.5
Release: alt1

Summary: A Python module for interfacing with the OpenGL library
Summary(ru_RU.UTF-8): Расширение языка Python для работы с библиотекой OpenGL

Group: Development/Python
License: see license.txt
Url: http://pyopengl.sourceforge.net

Source: PyOpenGL-%version.tar.gz
Patch: PyOpenGL-swig.patch
Patch1: %name.patch

BuildArch: noarch

%setup_python_module OpenGL

%py_requires OpenGL_accelerate

BuildPreReq: python-module-setuptools python-devel
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools python3-devel

%description
OpenGL bindings for Python including support for GL extensions,
GLU, WGL, GLUT, GLE, and Tk

%package -n python3-module-%oname
Summary: A Python module for interfacing with the OpenGL library
Group: Development/Python3
%py3_requires OpenGL_accelerate
%add_python3_req_skip OpenGL.GLES3.OES
%add_python3_req_skip OpenGL.raw.DISABLED
%add_python3_req_skip OpenGL.raw.DISABLED._types
%add_python3_req_skip OpenGL.raw.GLSC2
%add_python3_req_skip OpenGL.raw.GLSC2._types

%description -n python3-module-%oname
OpenGL bindings for Python including support for GL extensions,
GLU, WGL, GLUT, GLE, and Tk

%package -n python3-module-%oname-tests
Summary: PyOpenGL tests
Group: Development/Python3
Requires: python3-module-%oname =  %EVR
###add_python3_req_skip pygame

%description -n python3-module-%oname-tests
PyOpenGL tests.

%package demo
Summary: PyOpenGL demo files
Group: Development/Python
Requires: %name = %EVR
%add_python_req_skip items win32ui

%description demo
Demo for PyOpenGL

%package doc
Summary: PyOpenGL documentation
Group: Development/Python
Requires: %name = %EVR

%description doc
PyOpenGL documentation

%package tests
Summary: PyOpenGL tests
Group: Development/Python
Requires: %name = %EVR

%description tests
PyOpenGL tests.

%package tk
Summary: %oname Python 2.x Tk widget
Group: Development/Python
Requires: %name = %EVR
%py_requires tkinter

%description tk
%oname Togl (Tk OpenGL widget) 1.6 support for Python 2.x.

%package -n python3-module-%oname-tk
Summary: %oname Python 3.x Tk widget
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires tkinter

%description -n python3-module-%oname-tk
%oname Togl (Tk OpenGL widget) 1.6 support for Python 3.x.

%prep
%setup -n PyOpenGL-%version


cp -a tests tests3
find tests -type f -name '*.py' -exec \
	sed -i 's|#! %_bindir/env python|#!%_bindir/python2|' '{}' +

find tests3 -type f -name '*.py' -exec \
	sed -i 's|#! %_bindir/env python|#!%_bindir/python3|' '{}' +

%build
%python_build_debug -b build2
sed -i '/import itertools/afrom __future__ import print_function' build2/lib/OpenGL/EGL/debug.py
%python3_build_debug -b build3

%install
rm -f build && ln -s build2 build
%python_install
touch tests/__init__.py
cp -fR tests %buildroot/%python_sitelibdir/%modulename/

rm -f build && ln -s build3 build
%python3_install
touch tests3/__init__.py
cp -fR tests3 %buildroot/%python3_sitelibdir/%modulename/tests

%files
%python_sitelibdir/*.egg-info
%python_sitelibdir/%modulename/
%exclude %python_sitelibdir/%modulename/tests
%exclude %python_sitelibdir/OpenGL/Tk

%files tests
%python_sitelibdir/%modulename/tests

%files tk
%python_sitelibdir/OpenGL/Tk

%files -n python3-module-%oname
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/%modulename/
%exclude %python3_sitelibdir/%modulename/tests
%exclude %python3_sitelibdir/OpenGL/Tk

%files -n python3-module-%oname-tests
%python3_sitelibdir/%modulename/tests

%files -n python3-module-%oname-tk
%python3_sitelibdir/OpenGL/Tk

%changelog
* Tue Jan 14 2020 Fr. Br. George <george@altlinux.ru> 3.1.5-alt1
- Version up

* Sat Apr 20 2019 Anton Midyukov <antohami@altlinux.org> 3.1.1a1-alt2
- Fix build with python-3.7

* Sat Jan 27 2018 Anton Midyukov <antohami@altlinux.org> 3.1.1a1-alt1
- New version 3.1.1a1 (Closes: 34485)
- New subpackages python-module-tk and python3-module-tk

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.1.0-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.1.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt2
- Added requirement on 'OpenGL_accelerate'

* Sun Aug 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1
- Version 3.1.0
- Added module for Python 3

* Fri Dec 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.2-alt1
- Version 3.0.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.1-alt1.1
- Rebuild with Python-2.7

* Sat Nov 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1
- Version 3.0.1
- Added tests subpackage

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt3.1
- Rebuilt with python 2.6

* Mon Feb 16 2009 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt3
- new version 3.0.0c1
- build package as noarch

* Sun Dec 28 2008 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt2
- new version 3.0.0b8
- remove tests packing (fix bug #18378)

* Sat Nov 29 2008 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- new version (3.0.0)
- cleanup spec, update buildreqs

* Sun Nov 13 2005 Vitaly Lipatov <lav@altlinux.ru> 2.0.2.01-alt2
- fix Source tag

* Tue Jul 19 2005 Vitaly Lipatov <lav@altlinux.ru> 2.0.2.01-alt1
- first build for ALT Linux Sisyphus
