%define oname wtforms_extras

%def_with python3

Name: python-module-%oname
Version: 1.1.3
Release: alt1.git20141125
Summary: Provide templates for wtform widgets
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/wtforms_extras/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/vangheem/wtform_extras.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-chameleon.core
BuildPreReq: python-module-wtforms
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-chameleon.core
BuildPreReq: python3-module-wtforms
%endif

%py_provides %oname
%py_requires chameleon wtforms

%description
This package aims to bring some improvements to make working with
wtforms easier.

This package currently allows you to render entire forms.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package aims to bring some improvements to make working with
wtforms easier.

This package currently allows you to render entire forms.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Provide templates for wtform widgets
Group: Development/Python3
%py3_provides %oname
%py3_requires chameleon wtforms

%description -n python3-module-%oname
This package aims to bring some improvements to make working with
wtforms easier.

This package currently allows you to render entire forms.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package aims to bring some improvements to make working with
wtforms easier.

This package currently allows you to render entire forms.

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
cp -fR %oname/templates %buildroot%python_sitelibdir/%oname/

%if_with python3
pushd ../python3
%python3_install
cp -fR %oname/templates %buildroot%python3_sitelibdir/%oname/
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
* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.git20141125
- Initial build for Sisyphus

