%define _unpackaged_files_terminate_build 1
%define oname nosexcover

%def_with python3

Name: python-module-%oname
Version: 1.0.11
Release: alt1.1
Summary: Extends nose.plugins.cover to add Cobertura-style XML reports
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/nosexcover/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/cmheisel/nose-xcover.git
Source0: https://pypi.python.org/packages/11/b3/2b9e812eb9cb7e60bbfff0a1f581bf411d5b55156e211a4e3580560c8902/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose python3-module-coverage
%endif

%py_provides %oname

%description
A companion to the built-in nose.plugins.cover, this plugin will write
out an XML coverage report to a file named coverage.xml.

It will honor all the options you pass to the Nose coverage plugin,
especially --cover-package.

%package -n python3-module-%oname
Summary: Extends nose.plugins.cover to add Cobertura-style XML reports
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A companion to the built-in nose.plugins.cover, this plugin will write
out an XML coverage report to a file named coverage.xml.

It will honor all the options you pass to the Nose coverage plugin,
especially --cover-package.

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
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.11-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.11-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.10-alt1.git20140325.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.10-alt1.git20140325
- Initial build for Sisyphus

