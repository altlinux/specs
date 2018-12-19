%define oname freezegun

Name: python-module-%oname
Version: 0.3.9
Release: alt1
Summary: Let your Python tests travel through time
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/freezegun/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/spulec/freezegun.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-six python-module-dateutil
BuildRequires: python-module-nose python-module-coverage
BuildRequires: python-module-coveralls
BuildRequires: python-module-mock
BuildRequires: python-modules-sqlite3

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-six python3-module-dateutil
BuildRequires: python3-module-nose python3-module-coverage
BuildRequires: python3-module-coveralls
BuildRequires: python3-module-mock
BuildRequires: python3-modules-sqlite3

%py_provides %oname
%py_requires six dateutil sqlite3

%description
FreezeGun is a library that allows your python tests to travel through
time by mocking the datetime module.

%package -n python3-module-%oname
Summary: Let your Python tests travel through time
Group: Development/Python3
%py3_provides %oname
%py3_requires six dateutil sqlite3

%description -n python3-module-%oname
FreezeGun is a library that allows your python tests to travel through
time by mocking the datetime module.

%prep
%setup

cp -fR . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
python setup.py test
sed -i 's|nosetests|nosetests -v|' Makefile
%make test


pushd ../python3
python3 setup.py test
sed -i 's|nosetests|nosetests3 -v|' Makefile
%make test
popd

%files
%doc *.rst
%python_sitelibdir/*

%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*

%changelog
* Wed Dec 19 2018 Alexey Shabalin <shaba@altlinux.org> 0.3.9-alt1
- 0.3.9

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.8-alt1.git20141231.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.8-alt1.git20141231.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.8-alt1.git20141231.1
- NMU: Use buildreq for BR.

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.8-alt1.git20141231
- Initial build for Sisyphus

