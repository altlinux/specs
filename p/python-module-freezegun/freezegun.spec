%define _unpackaged_files_terminate_build 1

%define oname freezegun
%def_with check

Name: python-module-%oname
Version: 0.3.12
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
BuildRequires: python2.7(dateutil)
BuildRequires: python2.7(mock)
BuildRequires: python2.7(pytest)
BuildRequires: python2.7(tox)
BuildRequires: python3(dateutil)
BuildRequires: python3(mock)
BuildRequires: python3(pytest)
BuildRequires: python3(sqlite3)
BuildRequires: python3(tox)
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
sed -i -e '/.*cover.*/d' \
       -e '/maya/d' \
       -e 's/pytest==.*/pytest/' \
       requirements.txt

rm -rf ../python3
cp -fR . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install
# asyncio is Python3.4+ only module
rm %buildroot%python_sitelibdir/%oname/_async.py

pushd ../python3
%python3_install
popd

%check
cat > tox.ini <<EOF
[testenv]
commands =
    {envpython} -m pytest {posargs:-vra}
EOF
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v

%files
%doc *.rst
%python_sitelibdir/freezegun/
%python_sitelibdir/freezegun-*.egg-info/

%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/freezegun/
%python3_sitelibdir/freezegun-*.egg-info/

%changelog
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

