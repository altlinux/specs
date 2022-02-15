%define _unpackaged_files_terminate_build 1

%define oname fsspec

Name: python3-module-%oname
Version: 2022.01.0
Release: alt1
Summary: A specification that python filesystems should adhere to
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/intake/filesystem_spec

BuildArch: noarch

# https://github.com/intake/filesystem_spec.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: pytest3 python3-module-numpy-testing

# not all optional dependencies are available
%add_python3_req_skip distributed.client distributed.worker dvc.repo panel pyarrow.hdfs pygit2 smbclient

%description
A specification for pythonic filesystems.

%prep
%setup

sed -i -e 's/\(^\s\+git_refnames = \).*$/\1"%version"/' %oname/_version.py

%build
%python3_build

%install
%python3_install

%check
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS='-p no:cacheprovider'
export PYTHONPATH=%buildroot%python3_sitelibdir
pytest-3 -v \
	--deselect=fsspec/implementations/tests/test_dbfs.py::test_dbfs_file_listing \
	--deselect=fsspec/implementations/tests/test_dbfs.py::test_dbfs_mkdir \
	--deselect=fsspec/implementations/tests/test_dbfs.py::test_dbfs_write_and_read \
	--deselect=fsspec/tests/test_spec.py::test_find \
	%nil

%files
%doc LICENSE
%doc README.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-*-py3*.egg-info

%changelog
* Tue Feb 15 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 2022.01.0-alt1
- Updated to upstream version 2022.01.0.

* Fri Aug 20 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2021.7.0-alt1
- Initial build for ALT.
