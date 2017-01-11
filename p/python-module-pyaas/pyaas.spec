%define _unpackaged_files_terminate_build 1
%define oname pyaas

%def_with python3

Name: python-module-%oname
Version: 0.6.1
Release: alt1
Summary: Python-as-a-Service is a set of utilities for creating Tornado applications
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyaas
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/moertle/pyaas.git
Source0: https://pypi.python.org/packages/79/f6/6e3c535a1387e3f0a495568d51921ab65a94fb3a8fe1c79565d82a9c8087/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-tornado
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-tornado
%endif

%py_provides %oname
%py_requires tornado

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-devel python3-module-zope rpm-build-python3

%description
PyaaS, or pyaas, or Python-as-a-Service, is a simple wrapper around
Tornado that makes it quick and easy to rapid deploy new web
applications. It has a settings parser, storage engine, and
authentication modules.

%if_with python3
%package -n python3-module-%oname
Summary: Python-as-a-Service is a set of utilities for creating Tornado applications
Group: Development/Python3
%py3_provides %oname
%py3_requires tornado

%description -n python3-module-%oname
PyaaS, or pyaas, or Python-as-a-Service, is a simple wrapper around
Tornado that makes it quick and easy to rapid deploy new web
applications. It has a settings parser, storage engine, and
authentication modules.
%endif

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

%files
%doc *.txt *.rst docs
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst docs
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.0-alt1.git20150805.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1.git20150805.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.git20150805
- Initial build for Sisyphus

