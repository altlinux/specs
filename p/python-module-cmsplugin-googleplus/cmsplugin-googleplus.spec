%define oname cmsplugin-googleplus

%def_with python3

Name: python-module-%oname
Version: 0.4.1
Release: alt1.dev0.git20140621
Summary: Django-CMS plugin for Google Plus Activities
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/cmsplugin-googleplus/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/itbabu/cmsplugin-googleplus.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Django-cms plugin for fetching Google+ activities.

%package tests
Summary: Tests for Django-CMS plugin for Google Plus Activities
Group: Development/Python
Requires: %name = %EVR

%description tests
Django-cms plugin for fetching Google+ activities.

This package contains tests for %name.

%package -n python3-module-%oname
Summary: Django-CMS plugin for Google Plus Activities
Group: Development/Python3

%description -n python3-module-%oname
Django-cms plugin for fetching Google+ activities.

%package -n python3-module-%oname-tests
Summary: Tests for Django-CMS plugin for Google Plus Activities
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Django-cms plugin for fetching Google+ activities.

This package contains tests for python3-module-%oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8

%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8

%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc AUTHORS *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Mon Sep 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.dev0.git20140621
- Initial build for Sisyphus

