%define oname freezegun

%def_with python3

Name: python-module-%oname
Version: 0.2.8
Release: alt1.git20141231.1.1.1
Summary: Let your Python tests travel through time
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/freezegun/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/spulec/freezegun.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-six python-module-dateutil
#BuildPreReq: python-module-nose python-module-coverage
#BuildPreReq: python-module-coveralls python-module-sure
#BuildPreReq: python-module-mock
#BuildPreReq: python-modules-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-six python3-module-dateutil
#BuildPreReq: python3-module-nose python3-module-coverage
#BuildPreReq: python3-module-coveralls python3-module-sure
#BuildPreReq: python3-module-mock
#BuildPreReq: python3-modules-sqlite3
%endif

%py_provides %oname
%py_requires six dateutil sqlite3

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-enum34 python-module-funcsigs python-module-mock python-module-ndg-httpsclient python-module-ntlm python-module-pbr python-module-pyasn1 python-module-pytest python-module-setuptools python-module-six python-module-unittest2 python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-sh python3-module-six python3-module-unittest2 python3-module-yaml python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 xz
BuildRequires: python-module-dateutil python-module-nose python-module-setuptools python-module-sure python-module-z4r-coveralls python-modules-sqlite3 python3-module-dateutil python3-module-html5lib python3-module-mock python3-module-nose python3-module-setuptools python3-module-sure python3-module-z4r-coveralls python3-modules-sqlite3 rpm-build-python3 time

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

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
sed -i 's|nosetests|nosetests -v|' Makefile
%make test
%if_with python3
pushd ../python3
python3 setup.py test
sed -i 's|nosetests|nosetests3 -v|' Makefile
%make test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.8-alt1.git20141231.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.8-alt1.git20141231.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.8-alt1.git20141231.1
- NMU: Use buildreq for BR.

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.8-alt1.git20141231
- Initial build for Sisyphus

