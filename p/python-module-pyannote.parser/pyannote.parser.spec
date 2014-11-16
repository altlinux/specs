%define mname pyannote
%define oname %mname.parser
Name: python-module-%oname
Version: 0.2.3
Release: alt1.git20141114
Summary: PyAnnote parsers
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyannote.parser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pyannote/pyannote-parser.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-%mname.core
BuildPreReq: python-module-pysrt git

%py_provides %oname
%py_requires %mname

%description
PyAnnote is a Python module for collaborative annotation of multimodal
documents.

This package provides annotation file parsers.

%prep
%setup

sed -i 's|@VERSION@|%version|' %mname/parser/_version.py
git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag %version -m "%version"

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%changelog
* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt1.git20141114
- Version 0.2.3

* Fri Nov 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20141113
- Initial build for Sisyphus

