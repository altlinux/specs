%define pre a2
Name: python-module-OpenGLContext
Version: 2.1.0
Release: alt3.4.1

Summary: Demonstration and testing contexts for PyOpenGL

Group: Development/Python
License: BSD-like
Url: http://pyopengl.sourceforge.net/context

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sourceforge.net/pyopengl/OpenGLContext-%version%pre.tar.gz

BuildArch: noarch

%setup_python_module OpenGLContext
#%define python_includedir %_includedir/python%__python_version

# FIXME:
%add_python_req_skip FXPy win32ui win32con vrml

BuildPreReq: rpm-build-compat >= 1.2

BuildRequires: python-module-setuptools python-devel
BuildPreReq: python-modules-compiler python-modules-encodings
BuildPreReq: libnumpy-devel

%description
Demonstration and Testing Contexts for PyOpenGL

OpenGLContext includes rendering contexts (including navigation)
for wxPython, PyGame and GLUT, as well as a partial context for
Tkinter.  It also includes support for rendering TrueType fonts,
and a significant subset of VRML97.  It provides fairly extensive
VRML97 scenegraph model.  It also includes the bulk of the tests
used to maintain and extend PyOpenGL.

%package tests
Summary: Tests for %name
Group: Development/Python
Requires: %name = %version-%release

%description tests
Demonstration and Testing Contexts for PyOpenGL

OpenGLContext includes rendering contexts (including navigation)
for wxPython, PyGame and GLUT, as well as a partial context for
Tkinter.  It also includes support for rendering TrueType fonts,
and a significant subset of VRML97.  It provides fairly extensive
VRML97 scenegraph model.  It also includes the bulk of the tests
used to maintain and extend PyOpenGL.

This package contains tests for %name.

%prep
%setup -q -n OpenGLContext-%version%pre

%build
%python_build

%install
%python_install

%files
%_bindir/vrml_view
%_bindir/choosecontext
%doc docs
%python_sitelibdir/%modulename/
%exclude %python_sitelibdir/%modulename/tests
%python_sitelibdir/*egg-info/

%files tests
%python_sitelibdir/%modulename/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.0-alt3.4.1
- Rebuild with Python-2.7

* Sun Feb 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt3.4
- Extracted tests into separate package

* Sat Feb 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt3.3
- Rebuilt with reformed NumPy

* Fri Jan 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt3.2
- Rebuilt without python-module-Numeric

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt3.1
- Rebuilt with python 2.6

* Mon Feb 16 2009 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt3
- build as noarch

* Tue Dec 02 2008 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt2
- fix requires

* Sat Nov 29 2008 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- new version (2.1.0)

* Sun Sep 04 2005 Vitaly Lipatov <lav@altlinux.ru> 2.0.0c1-alt0.1
- first build for ALT Linux Sisyphus
