%define oname pyramid_mako_starters

%def_with python3

Name: python-module-%oname
Version: 0.1.2
Release: alt1.git20150101
Summary: Pyramid project scaffolds using Mako templates
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_mako_starters/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ronnix/pyramid-mako-starters.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid
%endif

%py_provides %oname

%description
This package provides Pyramid project scaffolds based on Mako templates.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package provides Pyramid project scaffolds based on Mako templates.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Pyramid project scaffolds using Mako templates
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This package provides Pyramid project scaffolds based on Mako templates.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package provides Pyramid project scaffolds based on Mako templates.

This package contains tests for %oname.

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20150101
- Initial build for Sisyphus

