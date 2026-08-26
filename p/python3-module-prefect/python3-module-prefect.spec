%define _unpackaged_files_terminate_build 1
%define pypi_name prefect
%define mod_name prefect

# really hard to run properly
%def_without check

%define add_python_extra() \
%{expand:%%package -n %%name+%1 \
Summary: %%summary \
Group: Development/Python3 \
Requires: %%name \
%%pyproject_runtimedeps_metadata_extra %1 \
%%description -n %%name+%1' \
Extra "%1" for %%pypi_name. \
%%files -n %%name+%1 \
}

Name: python3-module-%pypi_name
Version: 3.8.4
Release: alt1

Summary: Workflow orchestration and management
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/prefect/
Vcs: https://github.com/PrefectHQ/prefect

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
# python3-module-ruamel-yaml.clib doesn't provide 'ruamel-yaml-clib'
%add_pyproject_deps_runtime_filter ruamel-yaml-clib
Requires: python3-module-ruamel-yaml.clib
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# python3-module-ruamel-yaml.clib doesn't provide 'ruamel-yaml-clib'
%add_pyproject_deps_check_filter ruamel-yaml-clib
BuildRequires: python3-module-ruamel-yaml.clib
# 'codespell' is provided by 'codespell' package, not 'python3-module-codespell'
%add_pyproject_deps_check_filter codespell
BuildRequires: codespell
%add_pyproject_deps_check_filter pytest-flakefinder
%add_pyproject_deps_check_filter typsht
%add_pyproject_deps_check_filter vale
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Prefect is a workflow orchestration framework for building data pipelines
in Python. It's the simplest way to elevate a script into a production workflow.
With Prefect, you can build resilient, dynamic data pipelines that react to the
world around them and recover from unexpected changes.

With just a few lines of code, data teams can confidently automate any data
process with features such as scheduling, caching, retries, and event-based
automations.

%add_python_extra otel

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
export TZ=UTC
%pyproject_run_pytest -vra -o=addopts= -n %_smp_build_ncpus \
    --ignore tests/deployment \
    --ignore tests/cli/deployment \
    --ignore tests/cli/test_deploy.py \
    --ignore tests/docker

%files
%_bindir/prefect
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Aug 26 2026 Anton Zhukharev <ancieg@altlinux.org> 3.8.4-alt1
- Updated to 3.8.4.

* Thu Aug 20 2026 Anton Zhukharev <ancieg@altlinux.org> 3.8.3-alt1
- Packaged for ALT Sisyphus.
