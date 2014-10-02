%define oname jmbo-sitemap

%def_with python3

Name: python-module-%oname
Version: 0.1.2
Release: alt1.git20130724
Summary: XML and HTML sitemap product for Jmbo
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jmbo-sitemap/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/jmbo-sitemap.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
XML and HTML sitemap product for Jmbo.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
XML and HTML sitemap product for Jmbo.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: XML and HTML sitemap product for Jmbo
Group: Development/Python3

%description -n python3-module-%oname
XML and HTML sitemap product for Jmbo.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
XML and HTML sitemap product for Jmbo.

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
* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20130724
- Initial build for Sisyphus

