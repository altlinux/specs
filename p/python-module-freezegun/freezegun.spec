%define _unpackaged_files_terminate_build 1

%define oname freezegun
%def_with check

Name: python-module-%oname
Version: 0.3.11
Release: alt1
Summary: Let your Python tests travel through time
License: ASLv2.0
Group: Development/Python
Url: https://pypi.org/project/freezegun/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/spulec/freezegun.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python-module-dateutil
BuildRequires: python-module-mock
BuildRequires: python-module-nose
BuildRequires: python-module-tox
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-mock
BuildRequires: python3-module-nose
BuildRequires: python3-module-tox
%endif

%description
FreezeGun is a library that allows your python tests to travel through
time by mocking the datetime module.

%package -n python3-module-%oname
Summary: Let your Python tests travel through time
Group: Development/Python3

%description -n python3-module-%oname
FreezeGun is a library that allows your python tests to travel through
time by mocking the datetime module.

%prep
%setup
# unnecessary requirements
sed -i '/coverage==3\.7\.1/d' requirements.txt
sed -i '/coveralls/d' requirements.txt
sed -i '/maya/d' requirements.txt

rm -rf ../python3
cp -fR . ../python3

# asyncio is Python3.4+ only module
rm freezegun/_async.py

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
export PIP_INDEX_URL=http://host.invalid./
sed -i 's|nosetests|nosetests -v|' Makefile
%_bindir/tox --sitepackages -e py%{python_version_nodots python} -v


pushd ../python3
sed -i 's|nosetests|nosetests3 -v|' Makefile
%_bindir/tox.py3 --sitepackages -e py%{python_version_nodots python3} -v
popd

%files
%doc *.rst
%python_sitelibdir/freezegun/
%python_sitelibdir/freezegun-*.egg-info/

%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/freezegun/
%python3_sitelibdir/freezegun-*.egg-info/

%changelog
* Mon Jan 14 2019 Stanislav Levin <slev@altlinux.org> 0.3.11-alt1
- 0.3.9 -> 0.3.11.

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

