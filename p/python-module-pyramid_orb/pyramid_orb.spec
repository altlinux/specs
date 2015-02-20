%define oname pyramid_orb

%def_with python3

Name: python-module-%oname
Version: 1.1.11
Release: alt1.git20150219
Summary: Bindings for the pyramid webframework and the ORB database ORM library
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_orb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ProjexSoftware/pyramid_orb.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid python-module-webhelpers
BuildPreReq: python-module-projex python-module-requests
BuildPreReq: python-module-projex_orb python-modules-compiler
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid python3-module-webhelpers
BuildPreReq: python3-module-projex python3-module-requests
BuildPreReq: python3-module-projex_orb
%endif

%py_provides %oname
%py_requires webhelpers projex requests pyramid orb inspect

%description
The pyramid_orb project is aimed at providing an integration layer
between the ORB database mapping system and the pyramid web framework.

%package -n python3-module-%oname
Summary: Bindings for the pyramid webframework and the ORB database ORM library
Group: Development/Python3
%py3_provides %oname
%py3_requires webhelpers projex requests pyramid orb

%description -n python3-module-%oname
The pyramid_orb project is aimed at providing an integration layer
between the ORB database mapping system and the pyramid web framework.

%prep
%setup

mv src/* ./

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
py.test -vv $(find src/ -name '*.py')
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version -vv $(find src/ -name '*.py')
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.11-alt1.git20150219
- Version 1.1.11

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.5-alt1.git20141121
- Version 1.1.5

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.git20141119
- Version 1.1.3

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.git20141118
- Version 1.1.2

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.git20141110
- Initial build for Sisyphus

