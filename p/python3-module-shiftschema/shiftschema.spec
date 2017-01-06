%define oname shiftschema
Name: python3-module-%oname
Version: 0.0.10
Release: alt1
Summary: Python3 filtering and validation library
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/shiftschema/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/projectshift/shift-schema.git
Source0: https://pypi.python.org/packages/5e/0f/314203a0e909e8780f94c9b3d91465020031b082a890baf4c70abe2ffea6/shiftschema-%{version}.tar.gz
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
%setup -q -n shiftschema-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test
nosetests3 -v

%files
%python3_sitelibdir/*

%changelog
* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.10-alt1
- automated PyPI update

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.9-alt1.git20150218.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.9-alt1.git20150218
- Version 0.0.9

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1.git20150211
- Version 0.0.7

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1.git20150205
- Initial build for Sisyphus

