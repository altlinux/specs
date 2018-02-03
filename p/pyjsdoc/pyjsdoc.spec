Name: pyjsdoc
Version: 0.9.1
Release: alt1.1
Summary: Python port of JSDoc
License: MIT / ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/PyJSDoc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/nostrademons/pyjsdoc.git
Source0: https://pypi.python.org/packages/3f/f9/6c418982612418f7740bbe72659275ffe47da3d3c608aad804cdc5b776a2/PyJSDoc-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-cjson

%py_requires cjson

%description
Python port of JSDoc, with some additional features like dependency
analysis and extensibility.

%prep
%setup -q -n PyJSDoc-%{version}

%build
%python_build_debug

%install
%python_install

install -p -m644 static/jsdoc.css %buildroot%python_sitelibdir/static/

%check
python setup.py test

%files
%doc README*
%_bindir/*
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1
- automated PyPI update

* Wed Apr 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20120528
- Initial build for Sisyphus

