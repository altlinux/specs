%define oname dispatcher

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt1.git20131112.1
Summary: A library for event-driven programming
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/dispatcher/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/olivierverdier/dispatch.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-devel rpm-build-python3

%description
Dispatch: signal broadcasting in python.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Dispatch: signal broadcasting in python.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A library for event-driven programming
Group: Development/Python3

%description -n python3-module-%oname
Dispatch: signal broadcasting in python.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Dispatch: signal broadcasting in python.

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
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0-alt1.git20131112.1
- NMU: Use buildreq for BR.

* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20131112
- Initial build for Sisyphus

