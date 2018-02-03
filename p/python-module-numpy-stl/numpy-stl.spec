%define oname numpy-stl
%def_disable check

Name: python-module-%oname
Version: 1.3.6
Release: alt2.git20141210.1
Summary: Library to make reading, writing and modifying both binary and ascii STL files easy
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/numpy-stl/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/WoLpH/numpy-stl.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-module-docutils python-module-html5lib python-module-matplotlib python-module-objects.inv python-module-pytest-cov python-module-pytest-flakes python-module-pytest-pep8 python-module-setuptools
BuildRequires: python-module-sphinx-devel

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-pytest libnumpy-devel
#BuildPreReq: python-module-argparse python-module-cov-core
#BuildPreReq: python-module-coverage python-module-docutils
#BuildPreReq: python-module-execnet python-tools-pep8 pyflakes
#BuildPreReq: python-module-pytest-cache python-module-pytest-cov
#BuildPreReq: python-module-pytest-flakes python-module-pytest-pep8
#BuildPreReq: python-module-sphinx-devel python-module-python_utils

%py_provides stl

%description
Simple library to make working with STL files (and 3D objects in
general) fast and easy.

Due to all operations heavily relying on numpy this is one of the
fastest STL editing libraries for Python available.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%install
%python_install

%make -C docs html

%check
rm -fR build conf.py*
python setup.py test

%files
%doc *.rst docs/_build/html
%_bindir/*
%python_sitelibdir/stl
%python_sitelibdir/*.egg-info

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.6-alt2.git20141210.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 1.3.6-alt2.git20141210
- Rebuild with "def_disable check"
- Cleanup buildreq

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.6-alt1.git20141210
- Version 1.3.6

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.5-alt1.git20141127
- Version 1.3.5

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1.git20141104
- Version 1.3.4

* Mon Oct 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.3-alt1.git20141024
- Initial build for Sisyphus

