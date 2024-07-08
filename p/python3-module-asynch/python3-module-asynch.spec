%define _unpackaged_files_terminate_build 1
%define pypi_name asynch
%define mod_name %pypi_name

# tests require running clickhouse server
%def_without check

Name: python3-module-%pypi_name
Version: 0.2.4
Release: alt1

Summary: An asyncio ClickHouse Python Driver with native (TCP) interface support
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/asynch/
Vcs: https://github.com/long2ice/asynch

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

%package -n %name+compression
Summary: %summary
Group: %group
Requires: %name
%pyproject_runtimedeps_metadata -- --extra compression
%description -n %name+compression
Extra 'compression' for %pypi_name.

%description
Asynch is an asyncio ClickHouse Python Driver with native (TCP) interface
support, which reuse most of clickhouse-driver and comply with PEP249.

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

# remove wrong-installed docs
rm %buildroot%python3_sitelibdir/{CHANGELOG.md,README.md,LICENSE}

%check
%pyproject_run_pytest -vra

%files
%doc CHANGELOG.md README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%files -n %name+compression

%changelog
* Mon Jul 08 2024 Anton Zhukharev <ancieg@altlinux.org> 0.2.4-alt1
- Updated to 0.2.4.

* Thu Mar 07 2024 Anton Zhukharev <ancieg@altlinux.org> 0.2.3-alt1
- Built for ALT Sisyphus.

