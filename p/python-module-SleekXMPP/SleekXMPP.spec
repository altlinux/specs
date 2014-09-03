%define oname SleekXMPP

%def_with python3

Name: python-module-%oname
Version: 1.3.1
Release: alt1.git20140609
Summary: Python 2.6+/3.1+ XMPP Library
License: MIT
Group: Development/Python
Url: http://sleekxmpp.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/fritzy/SleekXMPP.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
SleekXMPP is an MIT licensed XMPP library for Python 2.6/3.1+.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
SleekXMPP is an MIT licensed XMPP library for Python 2.6/3.1+.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
SleekXMPP is an MIT licensed XMPP library for Python 2.6/3.1+.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
SleekXMPP is an MIT licensed XMPP library for Python 2.6/3.1+.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: Python 2.6+/3.1+ XMPP Library
Group: Development/Python3

%description -n python3-module-%oname
SleekXMPP is an MIT licensed XMPP library for Python 2.6/3.1+.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
SleekXMPP is an MIT licensed XMPP library for Python 2.6/3.1+.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files tests
%python_sitelibdir/*/test

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%endif

%changelog
* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.git20140609
- Initial build for Sisyphus

