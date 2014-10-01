%define oname django-atlas

%def_with python3

Name: python-module-%oname
Version: 0.0.4
Release: alt1.beta.git20130509
Summary: Geolocation models, data and tools using GeoDjango
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-atlas/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/django-atlas.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
Geolocation models, data and tools using GeoDjango.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Geolocation models, data and tools using GeoDjango.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Geolocation models, data and tools using GeoDjango
Group: Development/Python3

%description -n python3-module-%oname
Geolocation models, data and tools using GeoDjango.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Geolocation models, data and tools using GeoDjango.

This package contains tests for %oname.

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

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Wed Oct 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.beta.git20130509
- Initial build for Sisyphus

