%define _unpackaged_files_terminate_build 1
%define pypi_name py-key-value-aio
%define mod_name key_value

# tests require running docker with a lot of images
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
Version: 0.4.5
Release: alt1

Summary: Async Key-Value Store - A pluggable interface for KV Stores
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/py-key-value-aio/
Vcs: https://github.com/strawgate/py-key-value

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
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%add_python_extra memory
%add_python_extra disk
%add_python_extra filetree
%add_python_extra redis
%add_python_extra mongodb
# %%add_python_extra valkey -- lack of 'valkey-glide' in repo
# %%add_python_extra vault -- lack of 'types-hvac' in repo
%add_python_extra memcached
%add_python_extra elasticsearch
%add_python_extra opensearch
# %%add_python_extra dynamodb -- lack of 'aioboto3' and 'types-aiobotocore-dynamodb' in repo
# %%add_python_extra s3 -- lack of 'aioboto3' and 'types-aiobotocore-s3' in repo
# %%add_python_extra azure-tables -- lack of 'azure-data-tables' in repo
%add_python_extra keyring
# %%add_python_extra keyring-linux -- python3-module-dbus must be python3-module-dbus-python
%add_python_extra pydantic
# %%add_python_extra aerospike -- lack of 'aerospike' in repo
# %%add_python_extra rocksdb -- lack of 'rockdsdict' in repo
# %%add_python_extra duckdb -- no 'duckdb' for i586
# %%add_python_extra chdb -- lack of 'chdb' in repo
%add_python_extra postgresql
# %%add_python_extra firestore -- lack of 'google-cloud-firestore' and 'google-auth' in repo
%add_python_extra wrappers-encryption
# %%add_python_extra docs -- disable due to common sense

%prep
%setup
%autopatch -p1
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
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Aug 19 2026 Anton Zhukharev <ancieg@altlinux.org> 0.4.5-alt1
- Packaged for ALT Sisyphus.
