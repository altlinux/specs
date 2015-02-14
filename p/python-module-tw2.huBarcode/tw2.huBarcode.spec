%define mname tw2
%define oname %mname.huBarcode

%def_without python3
%def_disable check

Name: python-module-%oname
Version: 2.0
Release: alt1.a5.git20101004
Summary: tw2 huBarcode widget
License: AGPLv3+
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.huBarcode/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/decause/tw2.huBarcode.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tw2.core python-module-huBarcode
BuildPreReq: python-module-Pillow python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tw2.core python3-module-huBarcode
BuildPreReq: python3-module-Pillow python3-module-nose
%endif

%py_provides %oname
%py_requires %mname tw2.core PIL huBarcode

%description
toscawidgets2 wrapper for huBarcode.

%package -n python3-module-%oname
Summary: tw2 huBarcode widget
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname tw2.core PIL huBarcode

%description -n python3-module-%oname
toscawidgets2 wrapper for huBarcode.

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.a5.git20101004
- Initial build for Sisyphus

