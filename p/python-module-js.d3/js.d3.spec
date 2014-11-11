%define oname js.d3

%def_with python3

Name: python-module-%oname
Version: 3.3.13
Release: alt1.git20140104
Summary: Fanstatic package for D3.js
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.d3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mgood/js.d3.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-fanstatic python-module-shutilwhich
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-fanstatic python3-module-shutilwhich
%endif

%py_provides %oname
%py_requires js

%description
Fanstatic package for D3.js.

%package -n python3-module-%oname
Summary: Fanstatic package for D3.js
Group: Development/Python3
%py3_provides %oname
%py3_requires js

%description -n python3-module-%oname
Fanstatic package for D3.js.

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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

cp -fR js/d3/resources %buildroot%python_sitelibdir/js/d3/
%if_with python3
pushd ../python3
cp -fR js/d3/resources %buildroot%python3_sitelibdir/js/d3/
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
%doc *.txt
%python_sitelibdir/js/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/js/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.13-alt1.git20140104
- Initial build for Sisyphus

