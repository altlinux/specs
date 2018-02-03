%define oname mangoutils

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt1.git20150317.1.1
Summary: A collection of commonly useful utilities
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/mangoutils/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/amol9/mangoutils.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose
BuildPreReq: python-modules-xml
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires xml

%description
A collection of commonly useful utilities.

Submodules:

* web: utility classes for handling urls, list of well known cdns, top
  level domains
* html: utility class for parsing html and accessing elements via xpath
* system: platform related functions

%if_with python3
%package -n python3-module-%oname
Summary: A collection of commonly useful utilities
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A collection of commonly useful utilities.

Submodules:

* web: utility classes for handling urls, list of well known cdns, top
  level domains
* html: utility class for parsing html and accessing elements via xpath
* system: platform related functions
%endif

%prep
%setup

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
cp -fR %oname/system %buildroot%python_sitelibdir/%oname/

%if_with python3
pushd ../python3
%python3_install
cp -fR %oname/system %buildroot%python3_sitelibdir/%oname/
popd
%endif

%check
python setup.py test
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3 -v
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.git20150317.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.git20150317.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Mar 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20150317
- Initial build for Sisyphus

