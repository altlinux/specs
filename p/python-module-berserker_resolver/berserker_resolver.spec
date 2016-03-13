%define oname berserker_resolver

%def_with python3

Name: python-module-%oname
Version: 1.0.3
Release: alt1.git20141125.1
Summary: Fast mass dns resolver which can bypass loadbalancers
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/berserker_resolver/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/DmitryFillo/berserker_resolver.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-dns
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-dns
%endif

%py_provides %oname
%py_requires dns

%description
Berserker Resolver is fast mass dns resolver which can bypass
loadbalancers.

%package -n python3-module-%oname
Summary: Fast mass dns resolver which can bypass loadbalancers
Group: Development/Python3
%py3_provides %oname
%py3_requires dns

%description -n python3-module-%oname
Berserker Resolver is fast mass dns resolver which can bypass
loadbalancers.

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md TODO examples.py
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md TODO examples.py
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.3-alt1.git20141125.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.git20141125
- Initial build for Sisyphus

