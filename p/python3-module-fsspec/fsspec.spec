%define _unpackaged_files_terminate_build 1

%define oname fsspec

Name: python3-module-%oname
Version: 2026.7.0
Release: alt1
Summary: A specification that python filesystems should adhere to
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/intake/filesystem_spec

BuildArch: noarch

# https://github.com/intake/filesystem_spec.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-pyproject-installer
BuildRequires: python3-module-hatchling python3-module-hatch-vcs
BuildRequires: pytest3 python3-module-pytest-asyncio python3-module-pytest-mock
BuildRequires: python3-module-numpy-testing python3-module-tqdm
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-requests

# not all optional dependencies are available
%add_python3_req_skip distributed.client distributed.worker dvc.repo panel pyarrow.hdfs pygit2 smbclient

%description
A specification for pythonic filesystems.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS='-p no:cacheprovider'
export PYTHONPATH=%buildroot%python3_sitelibdir
pytest-3 -v \
	--ignore=fsspec/implementations/tests/test_http.py \
	--ignore=fsspec/implementations/tests/test_http_sync.py \
	--deselect=fsspec/implementations/tests/test_dbfs.py::test_dbfs_file_listing \
	--deselect=fsspec/implementations/tests/test_dbfs.py::test_dbfs_mkdir \
	--deselect=fsspec/implementations/tests/test_dbfs.py::test_dbfs_write_and_read \
	--deselect=fsspec/implementations/tests/test_reference.py::test_simple \
	--deselect=fsspec/implementations/tests/test_reference.py::test_simple_ver1 \
	--deselect=fsspec/implementations/tests/test_reference.py::test_info \
	--deselect=fsspec/implementations/tests/test_reference.py::test_defaults \
	--deselect=fsspec/implementations/tests/test_reference.py::test_async_cat_file_ranges \
	--deselect=fsspec/tests/test_caches.py::test_background \
	--deselect=fsspec/tests/test_generic.py::test_remote_async_ops \
	--deselect=fsspec/tests/test_generic.py::test_cp_async_to_sync \
	--deselect=fsspec/tests/test_generic.py::test_cat_async \
	--deselect=fsspec/tests/test_generic.py::test_cp_one \
	--deselect=fsspec/tests/test_spec.py::test_cache_not_pickled \
	--deselect=fsspec/tests/test_spec.py::test_find \
	%nil

%files
%doc LICENSE
%doc README.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Thu Aug 13 2026 Anton Farygin <rider@altlinux.org> 2026.7.0-alt1
- 2022.01.0 -> 2026.7.0

* Tue Feb 06 2024 Grigory Ustinov <grenka@altlinux.org> 2022.01.0-alt2
- Fixed FTBFS.

* Tue Feb 15 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 2022.01.0-alt1
- Updated to upstream version 2022.01.0.

* Fri Aug 20 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2021.7.0-alt1
- Initial build for ALT.
