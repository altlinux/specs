%define _unpackaged_files_terminate_build 1
%define pypi_name graphql-core
%define mod_name graphql

%def_with check

Name: python3-module-%pypi_name
Version: 3.3.0
Release: alt1

Summary: GraphQL-core is a Python port of GraphQL.js, the JavaScript reference implementation for GraphQL
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/graphql-core/
Vcs: https://github.com/graphql-python/graphql-core

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter pytest-
BuildRequires: python3-module-pytest-describe
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
GraphQL-core 3 is a Python 3.10+ port of GraphQL.js, the JavaScript reference
implementation for GraphQL, a query language for APIs created by Facebook.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_depgroup test

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests --ignore=tests/benchmarks -vra -o=addopts=

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Oct 16 2026 Anton Zhukharev <ancieg@altlinux.org> 3.3.0-alt1
- Updated to 3.3.0.

* Tue Jul 21 2026 Anton Zhukharev <ancieg@altlinux.org> 3.2.11-alt1
- Updated to 3.2.11.

* Wed Mar 18 2026 Anton Zhukharev <ancieg@altlinux.org> 3.2.8-alt1
- Updated to 3.2.8.

* Thu Feb 27 2025 Anton Zhukharev <ancieg@altlinux.org> 3.2.6-alt1
- Updated to 3.2.6.

* Tue Oct 15 2024 Anton Zhukharev <ancieg@altlinux.org> 3.2.5-alt1
- Updated to 3.2.5.

* Sun Oct 13 2024 Anton Zhukharev <ancieg@altlinux.org> 3.2.4-alt1
- Updated to 3.2.4.

* Mon Aug 28 2023 Anton Zhukharev <ancieg@altlinux.org> 3.2.3-alt2
- Fixed FTBFS.

* Sat May 13 2023 Anton Zhukharev <ancieg@altlinux.org> 3.2.3-alt1
- Initial build for ALT Sisyphus.
