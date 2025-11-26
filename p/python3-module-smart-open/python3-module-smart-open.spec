%define pypi_name smart-open
Name:    python3-module-%pypi_name
Version: 7.4.1
Release: alt1
Summary: smart_open - utils for streaming large files in Python
License: MIT
URL:     https://pypi.org/project/smart-open
VCS:     https://github.com/piskvorky/smart_open
Source:  %name-%version.tar
Group:   Development/Python3

BuildArch: noarch

BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-requests_toolbelt
BuildRequires: python3-module-wrapt
BuildRequires: python3-module-azure-core

%description
smart_open is a Python 3 library for efficient streaming
of very large files from/to storages such as S3, GCS, Azure Blob Storage,
HDFS, WebHDFS, HTTP, HTTPS, SFTP, or local filesystem.
It supports transparent, on-the-fly (de-)compression
for a variety of different formats.

%prep
%setup -n %name-%version

%build
%pyproject_build

#Requires azure-storage-blob
#E   ModuleNotFoundError: No module named 'azure.storage'
#%%check
#%%pyproject_run_pytest -q --disable-warnings --maxfail=1 tests

%install
%pyproject_install

%files
%doc README* LICENSE*
%python3_sitelibdir/smart_open-0.0.0.dist-info
%python3_sitelibdir/smart_open

%changelog
* Thu Oct 30 2025 Arseniy Romenskiy <romenskiy@altlinux.org> 7.4.1-alt1
- Initial build.
