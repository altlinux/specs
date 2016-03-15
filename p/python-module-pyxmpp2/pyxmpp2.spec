%define oname pyxmpp2

%def_with python3

Name: python-module-%oname
Version: 2.0.0
Release: alt2.git20130922.1
Summary: The new and shiny XMPP implementation for Python
License: LGPLv2.1
Group: Development/Python
Url: https://github.com/Jajcus/pyxmpp2
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Jajcus/pyxmpp2.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
The new and shiny XMPP implementation for Python.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The new and shiny XMPP implementation for Python.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: The new and shiny XMPP implementation for Python
Group: Development/Python3

%description -n python3-module-%oname
The new and shiny XMPP implementation for Python.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
The new and shiny XMPP implementation for Python.

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
%doc CHANGES README TODO doc/*.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files tests
%python_sitelibdir/*/test

%if_with python3
%files -n python3-module-%oname
%doc CHANGES README TODO doc/*.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt2.git20130922.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.git20130922
- Enabled requirement on python3-module-libxml2

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20130922
- Initial build for Sisyphus

