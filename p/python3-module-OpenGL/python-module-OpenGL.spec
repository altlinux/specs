%define oname OpenGL

Name: python3-module-%oname
Version: 3.1.5
Release: alt3

Summary: A Python module for interfacing with the OpenGL library
Summary(ru_RU.UTF-8): Расширение языка Python для работы с библиотекой OpenGL

Group: Development/Python3
License: see license.txt
Url: http://pyopengl.sourceforge.net

Source: PyOpenGL-%version.tar.gz
Patch: PyOpenGL-swig.patch
Patch1: %name.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_requires OpenGL_accelerate
%add_python3_req_skip OpenGL.GLES3.OES
%add_python3_req_skip OpenGL.raw.DISABLED
%add_python3_req_skip OpenGL.raw.DISABLED._types
%add_python3_req_skip OpenGL.raw.GLSC2
%add_python3_req_skip OpenGL.raw.GLSC2._types

%description
OpenGL bindings for Python including support for GL extensions,
GLU, WGL, GLUT, GLE, and Tk

%package tk
Summary: %oname Python 2.x Tk widget
Group: Development/Python3
Requires: %name = %EVR
%py3_requires tkinter

%description tk
%oname Togl (Tk OpenGL widget) 1.6 support for Python 2.x.

%prep
%setup -n PyOpenGL-%version

find tests -type f -name '*.py' -exec \
	sed -i 's|#! %_bindir/env python|#!%_bindir/python3|' '{}' +

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/%oname/
%exclude %python3_sitelibdir/OpenGL/Tk

%files tk
%python3_sitelibdir/OpenGL/Tk

%changelog
* Mon Aug 02 2021 Grigory Ustinov <grenka@altlinux.org> 3.1.5-alt3
- Drop python2 support.

* Thu Jul 22 2021 Stanislav Levin <slev@altlinux.org> 3.1.5-alt2
- Stopped shipping of tests for Python2.

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
