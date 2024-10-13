%define _unpackaged_files_terminate_build 1
%define pypi_name graphql-core
%define mod_name graphql

%def_with check

Name: python3-module-%pypi_name
Version: 3.2.4
Release: alt1

Summary: A Python 3.6+ port of the GraphQL.js reference implementation of GraphQL
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/graphql-core/
Vcs: https://github.com/graphql-python/graphql-core

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
GraphQL-core 3 is a Python 3.6+ port of GraphQL.js, the JavaScript
reference implementation for GraphQL, a query language for APIs
created by Facebook.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun Oct 13 2024 Anton Zhukharev <ancieg@altlinux.org> 3.2.4-alt1
- Updated to 3.2.4.

* Mon Aug 28 2023 Anton Zhukharev <ancieg@altlinux.org> 3.2.3-alt2
- Fixed FTBFS.

* Sat May 13 2023 Anton Zhukharev <ancieg@altlinux.org> 3.2.3-alt1
- Initial build for ALT Sisyphus.

