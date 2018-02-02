%define oname Levenshtein

%def_with python3

Name: python-module-%oname
Version: 0.11.2
Release: alt1.git20140923.1.1
Summary: Python extension for computing string edit distances and similarities
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/python-Levenshtein/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ztane/python-Levenshtein.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
The Levenshtein Python C extension module contains functions for fast
computation of

* Levenshtein (edit) distance, and edit operations
* string similarity
* approximate median strings, and generally string averaging
* string sequence and set similarity

It supports both normal and Unicode strings.

%package -n python3-module-%oname
Summary: Python extension for computing string edit distances and similarities
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
The Levenshtein Python C extension module contains functions for fast
computation of

* Levenshtein (edit) distance, and edit operations
* string similarity
* approximate median strings, and generally string averaging
* string sequence and set similarity

It supports both normal and Unicode strings.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
./gendoc.sh

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt NEWS* *.rst Levenshtein.html
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt NEWS* *.rst Levenshtein.html
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.11.2-alt1.git20140923.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11.2-alt1.git20140923.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Oct 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.2-alt1.git20140923
- Initial build for Sisyphus

