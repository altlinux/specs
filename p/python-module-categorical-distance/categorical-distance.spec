%define _unpackaged_files_terminate_build 1
%define oname categorical-distance

%def_with python3

Name: python-module-%oname
Version: 1.9
Release: alt1.1
Summary: Compare categorical variables
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/categorical-distance/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/datamade/categorical-distance.git
Source0: https://pypi.python.org/packages/48/5c/fc965dba19378a75936ab27fb44f4e8d4ffe14eff27daf51ced701f423b2/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-numpy python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-numpy python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides categorical
%py_requires numpy

%description
Compare two categorical variables.

%if_with python3
%package -n python3-module-%oname
Summary: Compare categorical variables
Group: Development/Python3
%py3_provides categorical
%py3_requires numpy

%description -n python3-module-%oname
Compare two categorical variables.
%endif

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
nosetests -vv
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3 -vv
popd
%endif

%files
%doc PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.9-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5-alt1.git20150304.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.git20150304
- Version 1.5
- Added module for Python 3

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2.git20141205
- Fixed build

* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.git20141205
- Initial build for Sisyphus

