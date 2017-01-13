%define _unpackaged_files_terminate_build 1
%define oname whois

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.6.4
Release: alt1
Summary: Whois querying and parsing of domain registration information
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/python-whois
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/4e/7d/dafe428145b6e712d12442abef54167e530ba54bf7ae6cf9e654233eabfb/python-%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-simplejson
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-simplejson
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-pytest python3-module-pytest rpm-build-python3

%description
Whois querying and parsing of domain registration information.

Goal:
* Create a simple importable Python module which will produce parsed
  WHOIS data for a given domain.
* Able to extract data for all the popular TLDs (com, org, net, ...)
* Query a WHOIS server directly instead of going through an intermediate
  web service like many others do.
* Works with Python 2.4+ and no external dependencies

%if_with python3
%package -n python3-module-%oname
Summary: Whois querying and parsing of domain registration information
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Whois querying and parsing of domain registration information.

Goal:
* Create a simple importable Python module which will produce parsed
  WHOIS data for a given domain.
* Able to extract data for all the popular TLDs (com, org, net, ...)
* Query a WHOIS server directly instead of going through an intermediate
  web service like many others do.
* Works with Python 2.4+ and no external dependencies
%endif

%prep
%setup -q -n python-%{oname}-%{version}

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
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.1
- NMU: Use buildreq for BR.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Initial build for Sisyphus

