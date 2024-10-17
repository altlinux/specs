%define _unpackaged_files_terminate_build 1
%define pypi_name tarjan
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.4
Release: alt1
Summary: Implementation of Tarjan's algorithm: resolve cyclic deps
License: LGPLv3
Group: Development/Python3
Url: https://pypi.org/project/tarjan/
Vcs: https://github.com/bwesterb/py-tarjan/
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
BuildRequires: python3-module-pytest
%endif

%description
Tarjan's algorithm takes as input a directed (possibly cyclic!) graph
and returns as output its strongly connected components in a topological
order.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%mod_name/tests

%changelog
* Thu Oct 17 2024 Stanislav Levin <slev@altlinux.org> 0.2.4-alt1
- 0.2.1.3 -> 0.2.4.

* Tue Nov 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.1.3-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.1.3-alt1.git20140805.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1.3-alt1.git20140805.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1.3-alt1.git20140805
- Initial build for Sisyphus

