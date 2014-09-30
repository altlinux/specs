%define oname django-facebook_gallery

%def_with python3

Name: python-module-%oname
Version: 0.9
Release: alt1.git20121030
Summary: Facebook Gallery for Django
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/django-facebook_gallery/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/nagyv/facebook_gallery.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
This is a simple gallery app for django that fetches your Galleries from
facebook, and shows them in your site. This way you don't have to bother
with storage and thumbnail generation, Facebook does it for you. End
it's extremely easy to administer, as you should manage your galleries
(almost) only at facebook.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This is a simple gallery app for django that fetches your Galleries from
facebook, and shows them in your site. This way you don't have to bother
with storage and thumbnail generation, Facebook does it for you. End
it's extremely easy to administer, as you should manage your galleries
(almost) only at facebook.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Facebook Gallery for Django
Group: Development/Python3

%description -n python3-module-%oname
This is a simple gallery app for django that fetches your Galleries from
facebook, and shows them in your site. This way you don't have to bother
with storage and thumbnail generation, Facebook does it for you. End
it's extremely easy to administer, as you should manage your galleries
(almost) only at facebook.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This is a simple gallery app for django that fetches your Galleries from
facebook, and shows them in your site. This way you don't have to bother
with storage and thumbnail generation, Facebook does it for you. End
it's extremely easy to administer, as you should manage your galleries
(almost) only at facebook.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.git20121030
- Initial build for Sisyphus

