%define oname stuf

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.9.16
Release: alt2.git20150404.1
Summary: Normal, default, ordered, chained, restricted, counter, and frozen dictionaries
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/stuf

# https://bitbucket.org/lcrees/stuf.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-parse python-module-Fabric
BuildRequires: python-module-pytest python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-parse
BuildRequires: python3-module-pytest python3-module-coverage
%endif

%py_provides %oname
%py_requires parse fabric

%description
A collection of Python dictionary types that support attribute-style
access. Includes defaultdict, OrderedDict, restricted, ChainMap,
Counter, and frozen implementations plus miscellaneous utilities for
writing Python software.

%if_with python3
%package -n python3-module-%oname
Summary: Normal, default, ordered, chained, restricted, counter, and frozen dictionaries
Group: Development/Python3
%py3_provides %oname
%py3_requires parse

%description -n python3-module-%oname
A collection of Python dictionary types that support attribute-style
access. Includes defaultdict, OrderedDict, restricted, ChainMap,
Counter, and frozen implementations plus miscellaneous utilities for
writing Python software.
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
python setup.py test -v
nosetests -vv --with-coverage --cover-package=%oname
%if_with python3
pushd ../python3
python3 setup.py test -v
nosetests3 -vv --with-coverage --cover-package=%oname
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.16-alt2.git20150404.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Nov 24 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.16-alt2.git20150404
- Updated build and runtime dependencies.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.16-alt1.git20150404.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.16-alt1.git20150404.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.16-alt1.git20150404
- Initial build for Sisyphus

