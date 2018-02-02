%define oname purl

%def_with python3

Name: python-module-%oname
Version: 1.0.2
Release: alt1.git20141212.1.1
Summary: An immutable URL class for easy URL-building and manipulation
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/purl/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/codeinthehole/purl.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-six python-module-nose
BuildPreReq: python-module-pip python-module-wheel
BuildPreReq: python-module-tox
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-six python3-module-nose
BuildPreReq: python3-module-pip python3-module-wheel
BuildPreReq: python3-module-tox
%endif

%py_provides %oname

%description
A simple, immutable URL class with a clean API for interrogation and
manipulation. Supports Python 2.6, 2.7, 3.3, 3.4 and pypy.

Also supports template URLs as per RFC 6570.

%package -n python3-module-%oname
Summary: An immutable URL class for easy URL-building and manipulation
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A simple, immutable URL class with a clean API for interrogation and
manipulation. Supports Python 2.6, 2.7, 3.3, 3.4 and pypy.

Also supports template URLs as per RFC 6570.

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
./runtests.sh
%if_with python3
pushd ../python3
python3 setup.py test
#sed -i 's|nosetests|nosetests3|' runtests.sh
#./runtests.sh
popd
%endif

%files
%doc AUTHORS *.rst docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1.git20141212.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt1.git20141212.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20141212
- Initial build for Sisyphus

