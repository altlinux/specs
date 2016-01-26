%define mname pyannote
%define oname %mname.metrics
%def_disable check

Name: python-module-%oname
Version: 0.4.1
Release: alt3.git20141120
Summary: PyAnnote metrics
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyannote.metrics/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pyannote/pyannote-metrics.git
Source: %name-%version.tar
BuildRequires: python-module-notebook python-module-pyannote.algorithms

#BuildPreReq: python-module-setuptools-tests python-module-%mname.core
#BuildPreReq: python-module-pyannote.algorithms python-module-scipy
#BuildPreReq: python-module-munkres python-module-docopt

%py_provides %oname
#%py_requires %mname pyannote.core pyannote.algorithms

%description
PyAnnote is a Python module for collaborative annotation of multimodal
documents.

This package provides evaluation metrics.

%prep
%setup

sed -i 's|@VERSION@|%version|' %mname/metrics/_version.py

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
%doc *.md
%_bindir/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%changelog
* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 0.4.1-alt3.git20141120
- Rebuild with "def_disable check"
- Cleanup buildreq

* Thu Mar 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt2.git20141120
- Fixed build

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20141120
- Version 0.4.1

* Sat Nov 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20141031
- Initial build for Sisyphus

