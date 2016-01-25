%define mname pyannote
%define oname %mname.features
%def_disable check

Name: python-module-%oname
Version: 0.2.1
Release: alt2.git20150107
Summary: PyAnnote feature extraction
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyannote.features/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pyannote/pyannote-features.git
Source: %name-%version.tar
BuildRequires: python-module-nltk python-module-notebook python-module-pyannote.core python-module-scikit-learn

#BuildPreReq: python-module-setuptools-tests python-module-%mname.core
#BuildPreReq: python-module-scikit-learn python-module-nltk
#BuildPreReq: python-module-scipy python-module-progressbar
#BuildPreReq: python-module-docopt python-module-opencv
#BuildPreReq: python-module-yaafelib

%py_provides %oname
#%py_requires %mname cv yaafelib

%description
PyAnnote is a Python module for collaborative annotation of multimodal
documents.

This package provides acoustic, visual and textual feature extraction.

%prep
%setup

sed -i 's|@VERSION@|%version|' %mname/features/_version.py

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
* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 0.2.1-alt2.git20150107
- Rebuild with "def_disable check"
- Cleanup buildreq

* Thu Mar 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20150107
- Version 0.2.1

* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141031
- Initial build for Sisyphus

