%define oname shiftschema
Name: python3-module-%oname
Version: 0.0.6
Release: alt1.git20150205
Summary: Python3 filtering and validation library
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/shiftschema/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/projectshift/shift-schema.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-rednose
BuildPreReq: python3-module-coveralls

%py3_provides %oname

%description
Filtering and validation library for Python3. Can filter and validate
data in model objects and simple dictionaries with flexible schemas.

Main idea: decouple filtering and validation rules from web forms into
flexible schemas, then reuse those schemas in forms as well as apis and
cli. Model validation and filtering rules should be part of the model
and your domain logic, not your views or forms logic.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test
nosetests3 -v

%files
%doc *.md
%python3_sitelibdir/*

%changelog
* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1.git20150205
- Initial build for Sisyphus

