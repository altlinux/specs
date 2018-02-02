%define oname dirty-models
Name: python3-module-%oname
Version: 0.9.2
Release: alt1.1
Summary: Dirty models for python 3
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/dirty-models/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/alfred82santa/dirty-models.git
Source0: https://pypi.python.org/packages/38/e8/03bdc3d80b75f47956581229edd3f5b6380124107a6a151bda5986db9a6a/dirty-models-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-dateutil python3-module-nose
BuildPreReq: python3-module-coverage python3-module-iso8601

%py3_provides dirty_models
%py3_requires dateutil

%description
Dirty models for python 3.


Features:

* Python 3 package.
* Easy to create a model.
* Non destructive modifications.
* Non false positive modifications.
* Able to restore original data for each field or whole model.
* Access to original data.
* Read only fields.
* Alias for fields.
* Custom getters and setters for each fields.
* Automatic cast value.
* Easy import from/export to dict.
* Basic field type implemented.
* HashMap model. It could be used instead of DynamicModel.
* FastDynamicModel. It could be used instead of DynamicModel. Same
  behavior, better performance.
* Pickable models.
* Datetime fields can use any datetime format using parser and formatter
  functions.
* No database dependent.

%prep
%setup -q -n dirty-models-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test
nosetests3 -v --with-coverage -d --cover-package=dirty_models

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt1
- automated PyPI update

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.git20150420.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Apr 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20150420
- Initial build for Sisyphus

