%define _unpackaged_files_terminate_build 1

%define oname traitlets

Name: python3-module-%oname
Version: 5.3.0
Release: alt1

Summary: Traitlets Python config system

License: BSD-3-Clause
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/traitlets

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3 rpm-macros-sphinx3
BuildRequires: python3-module-decorator python3-module-ipython_genutils-tests python3-module-pytest
BuildRequires: python3-module-sphinx_rtd_theme python3(enum) python3-module-mock
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-flit

%py3_provides %oname
%py3_requires ipython_genutils decorator

%description
A configuration system for Python applications.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
A configuration system for Python applications.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
A configuration system for Python applications.

This package contains pickles for %oname.

%prep
%setup

%prepare_sphinx3 docs
ln -s ../objects.inv docs/source/

%build
%__python3 -m flit build --format wheel
export PYTHONPATH=%buildroot%python3_sitelibdir
%make SPHINXBUILD="sphinx-build-3" -C docs pickle
%make SPHINXBUILD="sphinx-build-3" -C docs html

%install
pip3 install -I dist/%oname-%version-*-none-any.whl --root %buildroot --prefix %prefix --no-deps

cp -fR docs/build/pickle %buildroot%python3_sitelibdir/%oname

%check
rm -fR build
py.test3 -vv

%files
%doc examples docs/build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests

%files pickles
%python3_sitelibdir/*/pickle

%changelog
* Thu Jun 16 2022 Grigory Ustinov <grenka@altlinux.org> 5.3.0-alt1
- Build new version.

* Fri Mar 19 2021 Grigory Ustinov <grenka@altlinux.org> 5.0.5-alt1
- Build new version (Closes: #39489).
- Drop python2 support.

* Wed May 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.3.2-alt2
- Updated build and runtime dependencies.

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

