%define _unpackaged_files_terminate_build 1
%define pypi_name graphql-core
%define mod_name graphql

%def_with check

Name: python3-module-%pypi_name
Version: 3.2.3
Release: alt2

Summary: A Python 3.6+ port of the GraphQL.js reference implementation of GraphQL
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/graphql-core/
Vcs: https://github.com/graphql-python/graphql-core

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%py3_provides %pypi_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%add_pyproject_deps_check_filter bump2version
%add_pyproject_deps_check_filter check-manifest
%add_pyproject_deps_check_filter sphinx-rtd-theme
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_check
%endif

%description
GraphQL-core 3 is a Python 3.6+ port of GraphQL.js, the JavaScript
reference implementation for GraphQL, a query language for APIs
created by Facebook.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# Remove broken test for Python 3.11 (there is not asyncio.coroutine anymore).
%pyproject_run_pytest -vra -k "not recognizes_an_old_style_coroutine"

%files
%doc LICENSE README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Aug 28 2023 Anton Zhukharev <ancieg@altlinux.org> 3.2.3-alt2
- Fixed FTBFS.

* Sat May 13 2023 Anton Zhukharev <ancieg@altlinux.org> 3.2.3-alt1
- Initial build for ALT Sisyphus.

