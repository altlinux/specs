%define oname traitlets

%def_with python3

Name: python-module-%oname
Version: 4.3.2
Release: alt1
Summary: Traitlets Python config system
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/traitlets

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: time python-module-alabaster python-module-decorator python-module-docutils python-module-html5lib
BuildRequires: python-module-ipython_genutils-tests python-module-objects.inv python-module-pytest
BuildRequires: python-module-sphinx_rtd_theme python-module-enum34 python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-decorator python3-module-ipython_genutils-tests python3-module-pytest
BuildRequires: python3-module-sphinx_rtd_theme python3-module-enum34 python3-module-mock
%endif

%py_provides %oname
%py_requires ipython_genutils decorator

%description
A configuration system for Python applications.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A configuration system for Python applications.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Traitlets Python config system
Group: Development/Python3
%py3_provides %oname
%py3_requires ipython_genutils decorator

%description -n python3-module-%oname
A configuration system for Python applications.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A configuration system for Python applications.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A configuration system for Python applications.

This package contains pickles for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
rm -fR build
py.test -vv
%if_with python3
pushd ../python3
rm -fR build
py.test3 -vv
popd
%endif

%files
%doc examples docs/build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc examples docs/build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Wed Aug 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.3.2-alt1
- Updated to upstream version 4.3.2.

* Thu Jul 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.0-alt1.1.2
- Fixed build spec with py.test3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.0.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Aug 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus

