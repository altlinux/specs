%define oname dirty-models
Name: python3-module-%oname
Version: 0.5.0
Release: alt1.git20150420.1
Summary: Dirty models for python 3
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/dirty-models/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/alfred82santa/dirty-models.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
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
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test
nosetests3 -v --with-coverage -d --cover-package=dirty_models

%files
%doc *.rst docs/*.rst performance
%python3_sitelibdir/*

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.git20150420.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Apr 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20150420
- Initial build for Sisyphus

