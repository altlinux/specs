%define _unpackaged_files_terminate_build 1
%define pypi_name parse-type
%define mod_name parse_type

%def_with check

Name: python3-module-%mod_name
Version: 0.6.3
Release: alt1
Summary: Simplifies to build parse types based on the parse module
License: MIT
Group: Development/Python
Url: https://pypi.org/project/parse-type/
Vcs: https://github.com/jenisys/parse_type
BuildArch: noarch
Source: %name-%version.tar
Patch0: %name-%version-alt.patch
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile py.requirements/ci.github.testing.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Sep 25 2024 Stanislav Levin <slev@altlinux.org> 0.6.3-alt1
- 0.6.2 -> 0.6.3.

* Tue Mar 05 2024 Stanislav Levin <slev@altlinux.org> 0.6.2-alt1
- 0.5.6 -> 0.6.2.

* Wed Jan 31 2024 Grigory Ustinov <grenka@altlinux.org> 0.5.6-alt3
- Moved on modern pyproject macros.

* Thu Sep 16 2021 Stanislav Levin <slev@altlinux.org> 0.5.6-alt2
- Fixed FTBFS (setuptools 58).

* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 0.5.6-alt1
- 0.4.2 -> 0.5.6.
- Stopped build for Python2.

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 0.4.2-alt3
- Fixed testing against Pytest 5.

* Tue Jan 29 2019 Stanislav Levin <slev@altlinux.org> 0.4.2-alt2
- Dropped BR on argparse.

* Thu May 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.2-alt1
- Updated to upstream version 0.4.2.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.5-alt1.dev.git20140505.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.5-alt1.dev.git20140505.2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.5-alt1.dev.git20140505.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1.dev.git20140505
- Initial build for Sisyphus

