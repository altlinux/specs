%define pre b1
%define oname OpenGLContext

%def_without bootstrap

Name: python-module-%oname
Version: 2.3.0
Release: alt3.1

Summary: Demonstration and testing contexts for PyOpenGL
Group: Development/Python
License: BSD-like
Url: http://pyopengl.sourceforge.net/context
BuildArch: noarch

Source: http://prdownloads.sourceforge.net/pyopengl/%oname-%version%pre.tar.gz

%add_python_req_skip win32con win32ui FXPy

BuildRequires: python-module-html5lib python-module-matplotlib time
BuildRequires: python-tools-2to3 python-module-docutils

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools


%description
Demonstration and Testing Contexts for PyOpenGL

OpenGLContext includes rendering contexts (including navigation)
for wxPython, PyGame and GLUT, as well as a partial context for
Tkinter.  It also includes support for rendering TrueType fonts,
and a significant subset of VRML97.  It provides fairly extensive
VRML97 scenegraph model.  It also includes the bulk of the tests
used to maintain and extend PyOpenGL.

%package -n python3-module-%oname
Summary: Demonstration and testing contexts for PyOpenGL
Group: Development/Python3
%add_python3_req_skip pygame win32con win32ui fontTools
%add_python3_req_skip FXPy.fox wx wx.py ttfquery

%description -n python3-module-%oname
Demonstration and Testing Contexts for PyOpenGL

OpenGLContext includes rendering contexts (including navigation)
for wxPython, PyGame and GLUT, as well as a partial context for
Tkinter.  It also includes support for rendering TrueType fonts,
and a significant subset of VRML97.  It provides fairly extensive
VRML97 scenegraph model.  It also includes the bulk of the tests
used to maintain and extend PyOpenGL.

%package -n python3-module-%oname-tests
Summary: Tests for %name
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Demonstration and Testing Contexts for PyOpenGL

OpenGLContext includes rendering contexts (including navigation)
for wxPython, PyGame and GLUT, as well as a partial context for
Tkinter.  It also includes support for rendering TrueType fonts,
and a significant subset of VRML97.  It provides fairly extensive
VRML97 scenegraph model.  It also includes the bulk of the tests
used to maintain and extend PyOpenGL.

This package contains tests for %name.

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
%setup -n %oname-%version%pre

rm -rf ../python3
cp -fR . ../python3

%build
%python_build

pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc docs
%python_sitelibdir/%oname/
%python_sitelibdir/*egg-info/

%files -n python3-module-%oname
%python3_sitelibdir/%oname/
%python3_sitelibdir/*egg-info/


%changelog
* Thu May 24 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.3.0-alt3.1
- rebuild with all requires

* Sat May 19 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.3.0-alt3
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.0-alt2.b1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Mar 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.3.0-alt2.b1
- NMU: added python-tools-2to3 to BRs.

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 2.3.0-alt1.b1.1
- NMU: Use buildreq for BR.

* Sun Aug 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1.b1
- Version 2.3.0b1
- Added module for Python 3

* Fri Dec 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.a3
- Version 2.2.0a3

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
