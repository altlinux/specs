%define _unpackaged_files_terminate_build 1
%define oname genty

%def_with python3

Name: python-module-%oname
Version: 1.3.2
Release: alt1.1
Summary: Allows you to run a test with multiple data sets
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/genty/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/box/genty.git
Source0: https://pypi.python.org/packages/c9/bc/eee096fe9ecf1041944f1327cf6a2030fb2c59acd66580b692eb8b540233/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-six python-module-coveralls
#BuildPreReq: python-module-mock python-tools-pep8
#BuildPreReq: python-module-tox pylint
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-six python3-module-coveralls
#BuildPreReq: python3-module-mock python3-tools-pep8
#BuildPreReq: python3-module-tox pylint-py3
%endif

%py_provides %oname
%py_requires six

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-egenix-mx-base python-module-enum34 python-module-funcsigs python-module-kerberos python-module-logilab-common python-module-ndg-httpsclient python-module-ntlm python-module-pbr python-module-pyasn1 python-module-pytest python-module-setuptools python-module-six python-module-unittest2 python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python3 python3-base python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-logilab-common python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-sh python3-module-six python3-module-unittest2 python3-module-yaml python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3
BuildRequires: pylint pylint-py3 python-module-mock python-module-setuptools python-module-tox python-module-z4r-coveralls python-tools-pep8 python3-module-html5lib python3-module-mock python3-module-setuptools python3-module-tox python3-module-z4r-coveralls python3-tools-pep8 rpm-build-python3

%description
Genty, pronounced "gen-tee", stands for "generate tests". It promotes
generative testing, where a single test can execute over a variety of
input.

%package -n python3-module-%oname
Summary: Allows you to run a test with multiple data sets
Group: Development/Python3
%py3_provides %oname
%py3_requires six

%description -n python3-module-%oname
Genty, pronounced "gen-tee", stands for "generate tests". It promotes
generative testing, where a single test can execute over a variety of
input.

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
%if_with python3
pushd ../python3
python3 setup.py test
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt1.git20150223.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1.git20150223.1
- NMU: Use buildreq for BR.

* Tue Feb 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.git20150223
- Initial build for Sisyphus

