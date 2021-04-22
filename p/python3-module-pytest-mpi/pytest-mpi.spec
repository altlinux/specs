%define _unpackaged_files_terminate_build 1

%define oname pytest-mpi

Name: python3-module-%oname
Version: 0.5
Release: alt1
Summary: Pytest plugin for working with MPI
License: BSD-3-Clause
Group: Development/Python3
Url: https://pytest-mpi.readthedocs.io/

BuildArch: noarch

# https://github.com/aragilar/pytest-mpi.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(pytest)

%description
pytest_mpi is a plugin for pytest providing some useful tools
when running tests under MPI, and testing MPI-related code.

%prep
%setup

sed -i \
	-e "s/git_refnames\s*=\s*\"[^\"]*\"/git_refnames = \" \(tag: v%version\)\"/" \
	./src/pytest_mpi/_version.py

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE.txt
%doc CONTRIBUTING.md README.md
%python3_sitelibdir/pytest_mpi
%python3_sitelibdir/pytest_mpi-%version-py*.egg-info

%changelog
* Fri Apr 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5-alt1
- Initial build for ALT.
