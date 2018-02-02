%define oname ripozo-tests

%def_with python3

Name: python-module-%oname
Version: 0.1.16
Release: alt1.dev0.git20150414.2.1
Summary: A helper package for creating tests for ripozo and its extensions
License: UNKNOWN
Group: Development/Python
Url: https://pypi.python.org/pypi/ripozo-tests/

# https://github.com/vertical-knowledge/ripozo-tests.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-module-setuptools
BuildRequires: python-module-ripozo
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-ripozo
%endif

%py_provides ripozo_tests
%py_requires six logging
%py_requires ripozo

%description
These are the common tests that can be used for various common
extensions such as managers and adapters.

%if_with python3
%package -n python3-module-%oname
Summary: A helper package for creating tests for ripozo and its extensions
Group: Development/Python3
%py3_provides ripozo_tests
%py3_requires six logging
%py3_requires ripozo

%description -n python3-module-%oname
These are the common tests that can be used for various common
extensions such as managers and adapters.
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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.16-alt1.dev0.git20150414.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Aug 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.16-alt1.dev0.git20150414.2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.16-alt1.dev0.git20150414.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.16-alt1.dev0.git20150414.1
- NMU: Use buildreq for BR.

* Fri Apr 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.16-alt1.dev0.git20150414
- Version 0.1.16.dev0

* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.13-alt2.dev0.git20150323
- Added necessary requirements

* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.13-alt1.dev0.git20150323
- Initial build for Sisyphus

