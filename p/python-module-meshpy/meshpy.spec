%define oname meshpy
Name: python-module-%oname
Version: 2011.1
Release: alt2.git20111128
Summary: Triangular and Tetrahedral Mesh Generator in Python
License: MIT
Group: Development/Python
Url: http://mathema.tician.de/software/meshpy
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://git.tiker.net/trees/meshpy.git
Source: %oname-%version.tar

BuildPreReq: boost-python-devel gcc-c++ python-module-setuptools
BuildPreReq: libnumpy-devel python-module-epydoc
BuildPreReq: doxygen graphviz

%description
MeshPy offers quality triangular and tetrahedral mesh generation for
Python. Meshes of this type are chiefly used in finite-element
simulation codes, but also have many other applications ranging from
computer graphics to robotics.

%package tests
Summary: Tests for MeshPy
Group: Development/Python
Requires: %name = %version-%release

%description tests
MeshPy offers quality triangular and tetrahedral mesh generation for
Python. Meshes of this type are chiefly used in finite-element
simulation codes, but also have many other applications ranging from
computer graphics to robotics.

This package contains tests for MeshPy.

%package docs
Summary: Documentation for MeshPy
Group: Development/Documentation
BuildArch: noarch

%description docs
MeshPy offers quality triangular and tetrahedral mesh generation for
Python. Meshes of this type are chiefly used in finite-element
simulation codes, but also have many other applications ranging from
computer graphics to robotics.

This package contains documentation for MeshPy.

%prep
%setup

%build
%python_build_debug

./configure.py
export PYTHONPATH=$PWD
%make doc

%install
%python_install

touch test/__init__.py
rm -f test/clean.sh
cp -fR test %buildroot%python_sitelibdir/%oname/

%files
%doc LICENSE README
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/test

%files tests
%python_sitelibdir/%oname/test

%files docs
%doc doc/html/*

%changelog
* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt2.git20111128
- Rebuilt with Boost 1.49.0

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt1.git20111128
- Version 2011.1

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.2-alt2.git20101129
- Rebuilt with Boost 1.48.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.91.2-alt1.git20101129.2.1
- Rebuild with Python-2.7

* Mon Jul 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.2-alt1.git20101129.2
- Rebuilt with Boost 1.47.0

* Wed Mar 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.2-alt1.git20101129.1
- Rebuilt for debuginfo

* Tue Dec 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.2-alt1.git20101129
- Initial build for Sisyphus

