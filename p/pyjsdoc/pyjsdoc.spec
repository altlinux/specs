Name: pyjsdoc
Version: 0.9.0
Release: alt1.git20120528
Summary: Python port of JSDoc
License: MIT / ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/PyJSDoc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/nostrademons/pyjsdoc.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-cjson

%py_requires cjson

%description
Python port of JSDoc, with some additional features like dependency
analysis and extensibility.

%prep
%setup

%build
%python_build_debug

%install
%python_install

install -p -m644 static/jsdoc.css %buildroot%python_sitelibdir/static/

%check
python setup.py test

%files
%doc *.md
%_bindir/*
%python_sitelibdir/*

%changelog
* Wed Apr 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20120528
- Initial build for Sisyphus

