%define _unpackaged_files_terminate_build 1
%define ns_root svg
%define pypi_name %ns_root.charts
%define mod_name charts

%def_with check

Name: python3-module-%pypi_name
Version: 7.3.1
Release: alt1

Summary: Python SVG Charting Library

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/svg.charts/
Vcs: https://github.com/jaraco/svg.charts
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
Requires: python3-module-%ns_root-alt-namespace
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra testing
%endif

%description
svg.charts is a pure-python library for generating charts and graphs in
SVG, originally based on the SVG::Graph Ruby package by Sean E. Russel.

%prep
%setup
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%ns_root/%mod_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Thu Oct 17 2024 Stanislav Levin <slev@altlinux.org> 7.3.1-alt1
- 6.1 -> 7.3.1.

* Sun Oct 16 2022 Grigory Ustinov <grenka@altlinux.org> 6.1-alt4
- Updated build dependencies.

* Sun May 08 2022 Grigory Ustinov <grenka@altlinux.org> 6.1-alt3
- Build without docs.

* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 6.1-alt2
- Rename package, spec cleanup.

* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 6.1-alt1
- new version 6.1 (with rpmrb script)
- python3 only

* Wed May 08 2019 Vitaly Lipatov <lav@altlinux.ru> 6.0-alt1
- new version (6.0) with rpmgs script
- separate doc packing
- disable check section (wait for jaraco.*)

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.0-alt2.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 26 2016 Denis Medvedev <nbr@altlinux.org> 3.0-alt2
- Fixed build by removing mercurial version check.

* Fri Apr 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1
- Initial build for Sisyphus

