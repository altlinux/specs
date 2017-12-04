%define oname berserker_resolver

%def_with python3

Name: python-module-%oname
Version: 2.0.1
Release: alt1
Summary: Fast mass dns resolver which can bypass loadbalancers
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/berserker_resolver/

# https://github.com/DmitryFillo/berserker_resolver.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-dns
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-dns
%endif

%py_provides %oname
%py_requires dns

%description
Berserker Resolver is fast mass dns resolver which can bypass
loadbalancers.

%if_with python3
%package -n python3-module-%oname
Summary: Fast mass dns resolver which can bypass loadbalancers
Group: Development/Python3
%py3_provides %oname
%py3_requires dns

%description -n python3-module-%oname
Berserker Resolver is fast mass dns resolver which can bypass
loadbalancers.
%endif

%prep
%setup
%patch1 -p1

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
%doc *.rst TODO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst TODO
%python3_sitelibdir/*
%endif

%changelog
* Mon Dec 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.1-alt1
- Updated to upstream version 2.0.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.3-alt1.git20141125.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.git20141125
- Initial build for Sisyphus

