%define _unpackaged_files_terminate_build 1

%define oname traitlets

%def_with check

Name: python3-module-%oname
Version: 5.3.0
Release: alt2

Summary: Traitlets Python config system

License: BSD-3-Clause
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/traitlets

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3 rpm-macros-sphinx3

# build backend and its deps
BuildRequires: python3(hatchling)

# docs build
BuildRequires: python3(sphinx)
BuildRequires: python3(sphinx_rtd_theme)

%if_with check
BuildRequires: python3(pytest)
%endif

%py3_provides %oname

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
%pyproject_build

export PYTHONPATH=$(pwd)
%make SPHINXBUILD="sphinx-build-3" -C docs pickle
%make SPHINXBUILD="sphinx-build-3" -C docs html

%install
%pyproject_install

cp -fR docs/build/pickle %buildroot%python3_sitelibdir/%oname

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc examples docs/build/html
%python3_sitelibdir/traitlets/
%python3_sitelibdir/%{pyproject_distinfo %oname}/
%exclude %python3_sitelibdir/*/pickle
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests

%files pickles
%python3_sitelibdir/*/pickle

%changelog
* Thu Nov 10 2022 Stanislav Levin <slev@altlinux.org> 5.3.0-alt2
- Fixed FTBFS (flit_core 3.7.1).

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

