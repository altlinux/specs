%define _unpackaged_files_terminate_build 1
%define pypi_name pydocstyle
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 6.3.0
Release: alt1
Summary: Python docstring style checker
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pydocstyle/
Vcs: https://github.com/PyCQA/pydocstyle
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# Conflicts due to binaries in /usr/bin
Conflicts: python-module-%pypi_name
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter types-
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
pydocstyle is a static analysis tool for checking
compliance with Python docstring conventions.

pydocstyle supports most of PEP 257 out of the box,
but it should not be considered a reference implementation.

%prep
%setup
%autopatch -p1
# upstream uses dev version for git tree
sed -i 's/^version = "@VERSION@"$/version = "%version"/' pyproject.toml
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements/tests.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore \
    --ignore=src/tests/test_integration.py \
    src/tests

%files
%doc README.rst
%_bindir/pydocstyle
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed May 17 2023 Stanislav Levin <slev@altlinux.org> 6.3.0-alt1
- 6.2.3 -> 6.3.0.

* Tue Jan 31 2023 Ivan A. Melnikov <iv@altlinux.org> 6.2.3-alt1
- Updated to upstream version 6.2.3.
- Switch to %%pyproject_* macros.

* Thu Jun 10 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.1-alt1
- Updated to upstream version 6.1.1.
- Rebuilt without python-2.

* Fri Aug 31 2018 Stanislav Levin <slev@altlinux.org> 2.1.1-alt4
- Fix build.

* Wed May 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.1-alt3
- Fixed build dependencies.

* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.1-alt2
- Upstream renamed package to pydocstyle from pep257.

* Thu Oct 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.1-alt1
- Updated to upstream version 2.1.1.

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt1
- Updated to upstream version 2.0.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.alpha.git20150226.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.alpha.git20150226.1
- NMU: Use buildreq for BR.

* Thu Mar 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.alpha.git20150226
- Version 0.5.0-alpha
- Added docs

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20150109
- Initial build for Sisyphus

