%define _unpackaged_files_terminate_build 1
%define oname equals

%def_with python3

Name: python-module-%oname
Version: 0.0.25
Release: alt1
Summary: Fuzzy equality test objects for testing
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/equals/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toddsifleet/equals.git
Source0: https://pypi.python.org/packages/bf/97/a1b38b77696e90ceda10e3161f81e2b2dc2f7bb7b33b66163ff54f983f89/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-flake8 python-module-mock
#BuildPreReq: python-module-doubles python-module-coverage
#BuildPreReq: python-module-coveralls
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-flake8 python3-module-mock
#BuildPreReq: python3-module-doubles python3-module-coverage
#BuildPreReq: python3-module-coveralls
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-enum34 python-module-funcsigs python-module-mccabe python-module-ndg-httpsclient python-module-ntlm python-module-pbr python-module-pluggy python-module-py python-module-pyasn1 python-module-pytest python-module-setuptools python-module-six python-module-unittest2 python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-multiprocessing python-modules-unittest python-modules-xml python-tools-pep8 python3 python3-base python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-mccabe python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pluggy python3-module-py python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-sh python3-module-six python3-module-unittest2 python3-module-yaml python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-pyflakes python3-tools-pep8 xz
BuildRequires: python-module-doubles python-module-flake8 python-module-mock python-module-setuptools-tests python-module-z4r-coveralls python3-module-doubles python3-module-flake8 python3-module-html5lib python3-module-mock python3-module-setuptools-tests python3-module-z4r-coveralls rpm-build-python3 time

%description
Equals is a stricter version of Mock.Any.

Equals allows you to assert certain equality constraints between python
objects during testing. There are times where we don't want to assert
absolute equality, e.g. we need to ensure two lists have the same
elements, but don't care about order. This was designed specifically for
usage with Mock and doubles.

%package -n python3-module-%oname
Summary: Fuzzy equality test objects for testing
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Equals is a stricter version of Mock.Any.

Equals allows you to assert certain equality constraints between python
objects during testing. There are times where we don't want to assert
absolute equality, e.g. we need to ensure two lists have the same
elements, but don't care about order. This was designed specifically for
usage with Mock and doubles.

%prep
%setup -q -n %{oname}-%{version}

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
export PYTHONPATH=$PWD
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
py.test-%_python3_version -vv
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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.25-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.22-alt1.git20150210.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.22-alt1.git20150210.1
- NMU: Use buildreq for BR.

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.22-alt1.git20150210
- Initial build for Sisyphus

