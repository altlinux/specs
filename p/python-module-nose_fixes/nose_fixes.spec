%define oname nose_fixes

%def_with python3

Name: python-module-%oname
Version: 1.3
Release: alt1.git20130214.2.1
Summary: A plugin to make nose behave better
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/nose_fixes/

# https://github.com/cjw296/nose_fixes.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose python-module-pkginfo
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose
BuildPreReq: python3-module-pytest
%endif

%py_provides %oname

%description
A plugin that changes nose to behave better. Hopefully, these changes
will make their way back into nose...

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A plugin that changes nose to behave better. Hopefully, these changes
will make their way back into nose...

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A plugin to make nose behave better
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A plugin that changes nose to behave better. Hopefully, these changes
will make their way back into nose...

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A plugin that changes nose to behave better. Hopefully, these changes
will make their way back into nose...

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A plugin that changes nose to behave better. Hopefully, these changes
will make their way back into nose...

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A plugin that changes nose to behave better. Hopefully, these changes
will make their way back into nose...

This package contains documentation for %oname.

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

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
py.test
%if_with python3
pushd ../python3
py.test3
popd
%endif

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3-alt1.git20130214.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3-alt1.git20130214.2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt1.git20130214.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20130214
- Initial build for Sisyphus

