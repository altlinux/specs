%define _unpackaged_files_terminate_build 1

%define oname freezegun
%def_with check

Name: python3-module-%oname
Version: 0.3.15
Release: alt2
Summary: Let your Python tests travel through time
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/freezegun/

# https://github.com/spulec/freezegun.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(dateutil)
BuildRequires: python3(mock)
BuildRequires: python3(pytest)
BuildRequires: python3(sqlite3)
%endif

%description
FreezeGun is a library that allows your python tests to travel through
time by mocking the datetime module.

%prep
%setup
# unnecessary requirements
sed -i -e '/.*cover.*/d' \
       -e '/maya/d' \
       -e 's/pytest==.*/pytest/' \
       requirements.txt

%build
%python3_build

%install
%python3_install
# not used in Python3.6+, causes problems
rm %buildroot%python3_sitelibdir/%oname/_async_coroutine.py

%check
py.test3 -vra

%files
%doc *.rst
%python3_sitelibdir/freezegun/
%python3_sitelibdir/freezegun-*.egg-info/

%changelog
* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 0.3.15-alt2
- Drop python2 support.

* Thu Apr 09 2020 Ivan A. Melnikov <iv@altlinux.org> 0.3.15-alt1
- 0.3.12 -> 0.3.15.

* Wed Oct 02 2019 Stanislav Levin <slev@altlinux.org> 0.3.12-alt1
- 0.3.11 -> 0.3.12.

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

