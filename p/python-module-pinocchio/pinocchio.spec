%define oname pinocchio

%def_with python3

Name: python-module-%oname
Version: 0.4.2
Release: alt2.git20141201.1
Summary: pinocchio plugins for the nose testing framework
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/pinocchio/

# https://github.com/mkwiatkowski/pinocchio.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-nose python-module-colorama
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-nose python3-module-colorama
%endif

%py_provides %oname
%py_requires nose colorama

%description
Extra plugins for the nose testing framework. Provides tools for
flexibly assigning decorator tags to tests, choosing tests based on
their runtime, doing moderately sophisticated code coverage analysis of
your unit tests, and making your test descriptions look like
specifications.

%if_with python3
%package -n python3-module-%oname
Summary: pinocchio plugins for the nose testing framework
Group: Development/Python3
%py3_provides %oname
%py3_requires nose colorama

%description -n python3-module-%oname
Extra plugins for the nose testing framework. Provides tools for
flexibly assigning decorator tags to tests, choosing tests based on
their runtime, doing moderately sophisticated code coverage analysis of
your unit tests, and making your test descriptions look like
specifications.
%endif

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
%doc IDEAS *.rst doc/* examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc IDEAS *.rst doc/* examples
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.2-alt2.git20141201.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.2-alt2.git20141201
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt1.git20141201.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1.git20141201.1
- NMU: Use buildreq for BR.

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20141201
- Initial build for Sisyphus

