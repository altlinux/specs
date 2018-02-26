%define pre c1
Name: python-module-OpenGL
Version: 3.0.1
Release: alt1.1

Summary: A Python module for interfacing with the OpenGL library
Summary(ru_RU.KOI8-R): Расширение языка Python для работы с библиотекой OpenGL

Group: Development/Python
License: see license.txt
Url: http://pyopengl.sourceforge.net

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/pyopengl/PyOpenGL-%version%pre.tar.gz
Patch: PyOpenGL-swig.patch
Patch1: %name.patch

BuildArch: noarch

%setup_python_module OpenGL

%add_python_req_skip WGL__init__

BuildPreReq: python-module-setuptools python-devel

%description
OpenGL bindings for Python including support for GL extensions,
GLU, WGL, GLUT, GLE, and Tk

%package demo
Summary: PyOpenGL demo files
Group: Development/Python
Requires: %name = %version-%release
%add_python_req_skip items win32ui

%description demo
Demo for PyOpenGL

%package doc
Summary: PyOpenGL documentation
Group: Development/Python
Requires: %name = %version-%release

%description doc
PyOpenGL documentation

%package tests
Summary: PyOpenGL tests
Group: Development/Python
Requires: %name = %version-%release

%description tests
PyOpenGL documentation

%prep
%setup -q -n PyOpenGL-%version%pre
#%patch1

%build
%python_build

%install
%python_install

touch tests/__init__.py
cp -fR tests %buildroot/%python_sitelibdir/%modulename/

%files
%python_sitelibdir/*.egg-info
%python_sitelibdir/%modulename/
%exclude %python_sitelibdir/%modulename/tests
#%exclude %python_sitelibdir/%modulename/Demo
#%exclude %python_sitelibdir/%modulename/doc

%files tests
%python_sitelibdir/%modulename/tests

#%files demo
#%python_sitelibdir/%modulename/Demo

#%files doc
#%python_sitelibdir/%modulename/doc

%changelog
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
