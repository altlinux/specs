%define mname pyannote
%define oname %mname.algorithms
Name: python-module-%oname
Version: 0.1
Release: alt1.git20141031
Summary: PyAnnote algorithms
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyannote.algorithms/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pyannote/pyannote-algorithms.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-%mname.core
BuildPreReq: python-module-pyannote.core python-module-pyannote.parser
BuildPreReq: python-module-scikit-learn python-module-scipy
BuildPreReq: python-module-munkres python-module-docopt

%py_provides %oname
%py_requires %mname pyannote.core pyannote.parser sklearn

%description
PyAnnote is a Python module for collaborative annotation of multimodal
documents.

This package provides algorithms for multimedia document processing.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%add_python_req_skip viterbi

%description tests
PyAnnote is a Python module for collaborative annotation of multimodal
documents.

This package provides algorithms for multimedia document processing.

This package contains tests for %oname.

%prep
%setup

sed -i 's|@VERSION@|%version|' %mname/algorithms/_version.py

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.md doc
%_bindir/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/*/test*

%files tests
%python_sitelibdir/%mname/*/*/test*

%changelog
* Sat Nov 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141031
- Initial build for Sisyphus

