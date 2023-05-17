%define _unpackaged_files_terminate_build 1
%define pypi_name taskiq-aio-kafka
%define mod_name taskiq_aio_kafka

# tests require running Kafka broker
%def_without check

Name: python3-module-%pypi_name
Version: 0.1.2
Release: alt1

Summary: Kafka broker for taskiq
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/taskiq-aio-kafka/
Vcs: https://github.com/taskiq-python/taskiq-aio-kafka

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%set_pyproject_deps_check_filter types-
%add_pyproject_deps_check_filter autoflake
%add_pyproject_deps_check_filter wemake-python-styleguide
%add_pyproject_deps_check_filter yesqa
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
This lirary provides you with aiokafka broker for taskiq.

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
%pyproject_run_pytest

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun May 14 2023 Anton Zhukharev <ancieg@altlinux.org> 0.1.2-alt1
- Initial build for ALT Sisyphus.

