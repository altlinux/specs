%define oname logtool

%define ver1 0
%define ver2 2
%define ver3 11

%def_with python3

Name: python-module-%oname
Version: %ver1.%ver2.%ver3
Release: alt1.git20150224.1.1
Summary: Methods and tools that assist logging
License: GPLv3+
Group: Development/Python
Url: https://pypi.python.org/pypi/logtool/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/clearclaw/logtool.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-wrapt
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-wrapt
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires wrapt

%description
Methods and tools that assist logging.

%package -n python3-module-%oname
Summary: Methods and tools that assist logging
Group: Development/Python3
%py3_provides %oname
%py3_requires wrapt

%description -n python3-module-%oname
Methods and tools that assist logging.

%prep
%setup

sed -i 's|@VERSION@|%version|' %oname/__init__.py
sed -i 's|@V1@|%ver1|' %oname/__init__.py
sed -i 's|@V2@|%ver2|' %oname/__init__.py
sed -i 's|@V3@|%ver3|' %oname/__init__.py

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.11-alt1.git20150224.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.11-alt1.git20150224.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.11-alt1.git20150224
- Version 0.2.11

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1.git20141124
- Initial build for Sisyphus

