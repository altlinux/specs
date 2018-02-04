%define mname scikits
%define oname %mname.delaunay
Name: python-module-%oname
Epoch: 1
Version: 0.5
Release: alt2.1
Summary: Delaunay triangulation and interpolation tools
License: BSD
Group: Development/Python
Url: http://scikits.scipy.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# from git://git.altlinux.org/people/real/packages/scikits.git
# which from http://svn.scipy.org/svn/scikits/trunk (don't work now)
Source: %name-%version.tar

BuildPreReq: python-module-setuptools libnumpy-devel gcc-c++
BuildPreReq: python-module-matplotlib python-module-nose

%py_provides %oname
%py_requires %mname numpy

%description
This package provides delaunay triangulation and interpolation tools.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires matplotlib nose
%add_python_req_skip triangulate

%description tests
Delaunay triangulation and interpolation tools.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test
python setup.py build_ext -i
export PYTHONPATH=$PWD
nosetests -v

%files
%python_sitelibdir/%mname/delaunay
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/delaunay/test*

%files tests
%python_sitelibdir/%mname/delaunay/test*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:0.5-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.5-alt2
- Rebuilt with updated NumPy

* Sat Feb 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.5-alt1
- Initial build for Sisyphus

