%define oname guppy
Name: python-module-%oname
Version: 0.1.10
Release: alt1.svn20110524
Summary: Guppy-PE -- A Python Programming Environment
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/guppy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Patch1: python-guppy-0001-Work-with-big-endian-archs.patch
Patch2: python-guppy-0002-Preliminary-changes-to-cope-with-Python-version-2.7-.patch

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%description
Guppy-PE is a library and programming environment for Python, currently
providing in particular the Heapy subsystem, which supports object and
heap memory sizing, profiling and debugging. It also includes a
prototypical specification language, the Guppy Specification Language
(GSL), which can be used to formally specify aspects of Python programs
and generate tests and documentation from a common source.

%package tests
Summary: Tests for guppy
Group: Development/Python
Requires: %name = %version-%release

%description tests
Guppy-PE is a library and programming environment for Python, currently
providing in particular the Heapy subsystem, which supports object and
heap memory sizing, profiling and debugging. It also includes a
prototypical specification language, the Guppy Specification Language
(GSL), which can be used to formally specify aspects of Python programs
and generate tests and documentation from a common source.

This package contains tests for guppy.

%prep
%setup
#patch1 -p1
#patch2 -p1

%build
%python_build

%install
%python_install

%files
%doc ANNOUNCE* ChangeLog README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.10-alt1.svn20110524
- Version 0.1.10

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.9-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.9-alt1.1
- Rebuild with Python-2.7

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.9-alt1
- Initial build for Sisyphus

