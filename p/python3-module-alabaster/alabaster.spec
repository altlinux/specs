%define _unpackaged_files_terminate_build 1
%define pypi_name alabaster
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.7.16
Release: alt1
Summary: A light, configurable Sphinx theme
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/alabaster/
Vcs: https://github.com/sphinx-doc/alabaster
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
BuildRequires: /usr/bin/sphinx-build
%endif

%description
%pypi_name is a visually (c)lean, responsive, configurable theme for the Sphinx
documentation system. It requires Python 3.9 or newer and Sphinx 3.4 or newer.

It began as a third-party theme, and is still maintained separately, but as of
Sphinx 1.3, Alabaster is an install-time dependency of Sphinx and is selected as
the default theme.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# see .github/workflows/test.yml
%pyproject_run -- sphinx-build -M html ./docs ./build -j=auto -T -W --keep-going

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue May 28 2024 Stanislav Levin <slev@altlinux.org> 0.7.16-alt1
- 0.7.6 -> 0.7.16.

* Mon Aug 02 2021 Grigory Ustinov <grenka@altlinux.org> 0.7.6-alt4
- Drop python2 support.

* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.7.6-alt3
- rebuild with python3.6

* Fri Apr 22 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.6-alt2.git20150703
- correct XHTML (sphinx 1.4.1 tests failed because of this!)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.6-alt1.git20150703.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.6-alt1.git20150703
- Snapshot from git

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.6-alt1
- Version 0.7.6
- Added module for Python 3

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1
- Version 0.6.2

* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus

