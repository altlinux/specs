%define oname pyramid_who

%def_with python3

Name: python-module-%oname
Version: 0.3
Release: alt2
Summary: Pyramid authentication policies based on repoze.who
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_who/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires pyramid repoze.who

%description
pyramid_who is an extension for the pyramid web framework, providing an
authentication policy based on the "new" repoze.who API, as found in
version 2.0 and greater.

%package -n python3-module-%oname
Summary: Pyramid authentication policies based on repoze.who
Group: Development/Python3
%py3_requires pyramid repoze.who

%description -n python3-module-%oname
pyramid_who is an extension for the pyramid web framework, providing an
authentication policy based on the "new" repoze.who API, as found in
version 2.0 and greater.

%package -n python3-module-%oname-tests
Summary: Tests for pyramid_who
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
pyramid_who is an extension for the pyramid web framework, providing an
authentication policy based on the "new" repoze.who API, as found in
version 2.0 and greater.

This package contains tests for pyramid_who.

%package tests
Summary: Tests for pyramid_who
Group: Development/Python
Requires: %name = %version-%release

%description tests
pyramid_who is an extension for the pyramid web framework, providing an
authentication policy based on the "new" repoze.who API, as found in
version 2.0 and greater.

This package contains tests for pyramid_who.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8

%python_build

%if_with python3
pushd ../python3
%python3_build
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
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sat Aug 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Version 0.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt1.1
- Rebuild with Python-2.7

* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

