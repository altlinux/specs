%define _unpackaged_files_terminate_build 1
%define pypi_name pipenv
%define mod_name pipenv

# tests require the Internet connection that is prohibited in hasher
%def_without check

Name: python3-module-%pypi_name
Version: 2026.2.1
Release: alt1

Summary: Python Development Workflow for Humans
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pipenv/
Vcs: https://github.com/pypa/pipenv

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# remove providing vendored packages
%filter_from_provides /^python3(pipenv.vendor./d
%filter_from_provides /^python3(pipenv.patched./d
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter pypiserver
%add_pyproject_deps_check_filter stdeb
%pyproject_builddeps_metadata_extra tests
%pyproject_builddeps_check
# not listed in any dependency source, but required for testing
BuildRequires: python3-module-pytz
%endif

%description
Pipenv is a Python virtualenv management tool that supports a multitude
of systems and nicely bridges the gaps between pip, python (using
system python, pyenv or asdf) and virtualenv.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipenv Pipfile dev-packages
%endif

%build
%pyproject_build

%install
%pyproject_install
rm -rv %buildroot%python3_sitelibdir/benchmarks

%check
export PATH="$PATH:%buildroot%_bindir"
export PYTHONPATH="%buildroot%python3_sitelibdir"
pipenv --site-packages run python3 -m pytest -vra -o=addopts= --import-mode=append

%files
%_bindir/pipenv
%_bindir/pipenv-resolver
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Artem Krasovskiy <aibure@altlinux.org> 2026.2.1-alt1
- Initial build for Sisyphus.
