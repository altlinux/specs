%define oname pyramid_orb

%def_with python3

Name: python-module-%oname
Version: 1.1.2
Release: alt1.git20141118
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
BuildPreReq: python-module-projex
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid python3-module-webhelpers
BuildPreReq: python3-module-projex
%endif

%py_provides %oname
%py_requires webhelpers projex

%description
The pyramid_orb project is aimed at providing an integration layer
between the ORB database mapping system and the pyramid web framework.

%package -n python3-module-%oname
Summary: Bindings for the pyramid webframework and the ORB database ORM library
Group: Development/Python3
%py3_provides %oname
%py3_requires webhelpers projex
%add_python3_req_skip orb

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
%if_with python3
pushd ../python3
python3 setup.py test
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
* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.git20141118
- Version 1.1.2

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.git20141110
- Initial build for Sisyphus

