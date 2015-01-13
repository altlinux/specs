%define oname hgtools

%def_with python3

Name: python-module-%oname
Version: 6.2.1
Release: alt1
Summary: Classes and setuptools plugin for Mercurial repositories
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/hgtools/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
hgtools builds on the setuptools_hg plugin for setuptools. hgtools
provides classes for inspecting and working with repositories in the
Mercurial and Git version control systems (VCS).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
hgtools builds on the setuptools_hg plugin for setuptools. hgtools
provides classes for inspecting and working with repositories in the
Mercurial and Git version control systems (VCS).

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Classes and setuptools plugin for Mercurial repositories
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
hgtools builds on the setuptools_hg plugin for setuptools. hgtools
provides classes for inspecting and working with repositories in the
Mercurial and Git version control systems (VCS).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
hgtools builds on the setuptools_hg plugin for setuptools. hgtools
provides classes for inspecting and working with repositories in the
Mercurial and Git version control systems (VCS).

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
* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.2.1-alt1
- Version 6.2.1

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.1.1-alt1
- Initial build for Sisyphus

