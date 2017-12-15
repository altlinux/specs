%define _unpackaged_files_terminate_build 1
%define oname equals

%def_with python3

Name: python-module-%oname
Version: 0.0.25
Release: alt2
Summary: Fuzzy equality test objects for testing
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/equals/

# https://github.com/toddsifleet/equals.git
Source: %{oname}-%{version}.tar.gz

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-flake8 python-module-mock
BuildRequires: python-module-doubles python-module-coverage
BuildRequires: python-module-z4r-coveralls
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-flake8 python3-module-mock
BuildRequires: python3-module-doubles python3-module-coverage
BuildRequires: python3-module-coveralls python3-module-html5lib
%endif

%py_provides %oname

%description
Equals is a stricter version of Mock.Any.

Equals allows you to assert certain equality constraints between python
objects during testing. There are times where we don't want to assert
absolute equality, e.g. we need to ensure two lists have the same
elements, but don't care about order. This was designed specifically for
usage with Mock and doubles.

%if_with python3
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
* Fri Dec 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.25-alt2
- Fixed build.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.25-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.22-alt1.git20150210.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.22-alt1.git20150210.1
- NMU: Use buildreq for BR.

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.22-alt1.git20150210
- Initial build for Sisyphus

