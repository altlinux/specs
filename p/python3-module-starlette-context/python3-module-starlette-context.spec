%define _unpackaged_files_terminate_build 1
%define pypi_name starlette-context
%define mod_name starlette_context

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.6
Release: alt1.25.gf46610a

Summary: Middleware for Starlette that allows you to store and access the context data of a request
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/starlette-context/
Vcs: https://github.com/tomwojcik/starlette-context

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
Middleware for Starlette that allows you to store and access the context data of
a request. Can be used with logging so logs automatically use request headers
such as x-request-id or x-correlation-id.

%prep
%setup
%autopatch -p1
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
%pyproject_run_pytest -vra

%files
%doc LICENSE README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jul 24 2024 Anton Zhukharev <ancieg@altlinux.org> 0.3.6-alt1.25.gf46610a
- Built for ALT Sisyphus.

