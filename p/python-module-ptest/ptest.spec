%define _unpackaged_files_terminate_build 1
%define oname ptest

%def_with python3

Name: python-module-%oname
Version: 1.7.4
Release: alt1.1
Summary: Light testing framework for Python
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/ptest
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/KarlGong/ptest.git
Source0: https://pypi.python.org/packages/60/ba/c8b04e9bb9ca7fe92acf369c2004fa1cf20f3c0c5ece62b8a36abee431e4/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
ptest is a light testing framework for Python. Using decorator to tag
test classes and test cases, executing test cases by command line, and
generating clear report.

%if_with python3
%package -n python3-module-%oname
Summary: Light testing framework for Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
ptest is a light testing framework for Python. Using decorator to tag
test classes and test cases, executing test cases by command line, and
generating clear report.
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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ${i}3
done
popd
%endif

%python_install

%check
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.7.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.7.4-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.0-alt1.git20150813.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20150813
- Initial build for Sisyphus

