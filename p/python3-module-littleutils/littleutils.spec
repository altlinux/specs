%define _unpackaged_files_terminate_build 1
%define pypi_name littleutils
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.4
Release: alt1
Summary: Small personal collection of python utility functions, partly just for fun
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/littleutils/
Vcs: https://github.com/alexmojaki/littleutils
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
Small personal collection of python utility functions, partly just for fun.

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
# .github/workflows/test.yml
%pyproject_run -- python %mod_name/__init__.py -v

%files
%doc LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Oct 23 2024 Stanislav Levin <slev@altlinux.org> 0.2.4-alt1
- 0.2.2 -> 0.2.4.

* Tue Jan 18 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.2-alt1.git.6a3d7b7
- Initial build for ALT.
