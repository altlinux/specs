%define oname Alquimia
Name: python-module-%oname
Version: 0.7.1
Release: alt1.git20150718.1
Summary: An API to work with JSON schemas in SQLAlchemy
License: LGPLv3+
Group: Development/Python
Url: https://pypi.python.org/pypi/Alquimia/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dutradda/alquimia.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-pytest
BuildPreReq: python-module-jsonschema python-module-SQLAlchemy

%py_provides alquimia
%py_requires jsonschema sqlalchemy

%description
An API to work with JSON schemas in SQLAlchemy.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test -v

%files
%doc *.md docs/*.rst docs/example.py
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7.1-alt1.git20150718.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.git20150718
- Initial build for Sisyphus

