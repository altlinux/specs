%define _unpackaged_files_terminate_build 1
%define oname doxx

%def_with python3

Name: python-module-%oname
Version: 0.9.4
Release: alt1.1
Summary: Simple, flexible text file templating engine
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/doxx/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/chrissimpkins/doxx.git
Source0: https://pypi.python.org/packages/79/67/8ced67baf183fd8c8beb03983aff4d17a757fc748cab69a907b41a0a66f8/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-Naked python-modules-json
#BuildPreReq: python-module-requests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-Naked
#BuildPreReq: python3-module-requests
%endif

%py_provides %oname
%py_requires Naked

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-chardet python-module-cryptography python-module-enum34 python-module-ndg-httpsclient python-module-ntlm python-module-pyasn1 python-module-pytest python-module-requests python-module-setuptools python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-enum34 python3-module-ndg-httpsclient python3-module-ntlm python3-module-pycparser python3-module-pytest python3-module-requests python3-module-setuptools python3-module-urllib3 python3-module-yaml python3-module-yieldfrom.http.client
BuildRequires: python-module-Naked python-module-setuptools python3-module-Naked python3-module-setuptools python3-module-yieldfrom.urllib3 rpm-build-python3

%description
Simple, flexible text file templating engine.

%package -n python3-module-%oname
Summary: Simple, flexible text file templating engine
Group: Development/Python3
%py3_provides %oname
%py3_requires Naked

%description -n python3-module-%oname
Simple, flexible text file templating engine.

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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc docs/* PKG-INFO
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc docs/* PKG-INFO
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.git20150112.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1.git20150112.1
- NMU: Use buildreq for BR.

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20150112
- Initial build for Sisyphus

