%define _unpackaged_files_terminate_build 1
%define pypi_name dataset

Name: python3-module-%pypi_name
Version: 2.0.0
Release: alt1

License: MIT
Group: Development/Python3

URL: https://pypi.org/project/dataset
VCS: https://github.com/pudo/dataset

Summary: dataset: databases for lazy people

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
Easy-to-use data handling for SQL data stores with support for
implicit table creation, bulk loading, and transactions.

In short, dataset makes reading and writing data in databases
as simple as reading and writing JSON files.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc LICENSE *.md

%changelog
* Mon Jul 13 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.0.0-alt1
- Initial build for ALT Linux.

