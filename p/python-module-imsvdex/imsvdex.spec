%define oname imsvdex

%def_without python3

Name: python-module-%oname
Version: 2.0
Release: alt2.dev0.svn20140527.1
Summary: Read/write vocabularies in IMS Vocabulary Definition Exchange format
License: D-FSL - German Free Software License
Group: Development/Python
Url: https://pypi.python.org/pypi/imsvdex/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.plone.org/svn/collective/imsvdex/trunk/
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-lxml
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-lxml python-tools-2to3
%endif

%py_provides %oname

%description
API to access and modify XML files in the IMS Vocabulary Definition
Exchange format.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
API to access and modify XML files in the IMS Vocabulary Definition
Exchange format.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Read/write vocabularies in IMS Vocabulary Definition Exchange format
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
API to access and modify XML files in the IMS Vocabulary Definition
Exchange format.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
API to access and modify XML files in the IMS Vocabulary Definition
Exchange format.

This package contains tests for %oname.
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
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0-alt2.dev0.svn20140527.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2.dev0.svn20140527
- Fixed build

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.dev0.svn20140527
- Initial build for Sisyphus

