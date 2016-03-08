%define oname meshpy

%def_with python3

Name: python-module-%oname
Version: 2014.1
Release: alt3.git20140706
Summary: Triangular and Tetrahedral Mesh Generator in Python
License: MIT
Group: Development/Python
Url: http://mathema.tician.de/software/meshpy
Packager: Python Development Team <python@packages.altlinux.org>

# http://git.tiker.net/trees/meshpy.git
Source: %oname-%version.tar
# git://github.com/inducer/bpl-subset
Source1: bpl-subset.tar

#BuildPreReq: boost-python-devel gcc-c++ python-module-setuptools
#BuildPreReq: libnumpy-devel python-module-epydoc
#BuildPreReq: doxygen graphviz
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: boost-python3-devel python3-module-setuptools
#BuildPreReq: libnumpy-py3-devel
%endif

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils libboost_python3-1.58.0 libstdc++-devel python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-docutils python-module-genshi python-module-jinja2 python-module-numpy python-module-pyparsing python-module-pytz python-module-snowballstemmer python-module-sphinx python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python3 python3-base python3-dev python3-module-numpy
BuildRequires: boost-python-devel boost-python3-devel gcc-c++ python-module-epydoc python-module-html5lib python-module-matplotlib python-module-numpy-testing python-module-setuptools python3-module-setuptools rpm-build-python3 time

%description
MeshPy offers quality triangular and tetrahedral mesh generation for
Python. Meshes of this type are chiefly used in finite-element
simulation codes, but also have many other applications ranging from
computer graphics to robotics.

%package -n python3-module-%oname
Summary: Triangular and Tetrahedral Mesh Generator in Python
Group: Development/Python3

%description -n python3-module-%oname
MeshPy offers quality triangular and tetrahedral mesh generation for
Python. Meshes of this type are chiefly used in finite-element
simulation codes, but also have many other applications ranging from
computer graphics to robotics.

%package -n python3-module-%oname-tests
Summary: Tests for MeshPy
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
MeshPy offers quality triangular and tetrahedral mesh generation for
Python. Meshes of this type are chiefly used in finite-element
simulation codes, but also have many other applications ranging from
computer graphics to robotics.

This package contains tests for MeshPy.

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

rm -fR bpl-subset
tar -xf %SOURCE1

%if_with python3
rm -rf ../python3
cp -fR . ../python3
sed -i 's|boost_python|boost_python3|' ../python3/setup.py
%endif

%build
./configure.py
%python_build_debug

%if_with python3
pushd ../python3
./configure.py
%python3_build_debug
popd
%endif

export PYTHONPATH=$PWD
%make doc

%install
%python_install

touch test/__init__.py
rm -f test/clean.sh
cp -fR test %buildroot%python_sitelibdir/%oname/

%if_with python3
pushd ../python3
%python3_install
touch test/__init__.py
rm -f test/clean.sh
cp -fR test %buildroot%python3_sitelibdir/%oname/
popd
%endif

%files
%doc LICENSE README
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/test

%files tests
%python_sitelibdir/%oname/test

%files docs
%doc doc/html/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/test
%endif

%changelog
* Mon Mar 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2014.1-alt3.git20140706
- NMU: added python-module-setuptools to BRs.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2014.1-alt2.git20140706.1
- NMU: Use buildreq for BR.

* Sat Aug 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.1-alt2.git20140706
- Added module for Python 3

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.1-alt1.git20140706
- Version 2014.1

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.1.2-alt1.git20131122
- New snapshot

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.1.2-alt1.git20130916
- Version 2013.1.2

* Sun Feb 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt2.git20130121
- New snapshot

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt2.git20121113
- New snapshot

* Thu Sep 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt2.git20120902
- New snapshot

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

