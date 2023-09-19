%define _unpackaged_files_terminate_build 1
%define pypi_name publicsuffix2

Name: python3-module-%pypi_name
Version: 2.20191221
Release: alt1

Summary: Get a public suffix for a domain name using the Public Suffix List
License: MIT and MPL-2.0
Group: Development/Python3
Url: https://pypi.org/project/publicsuffix2
Vcs: https://github.com/nexB/python-publicsuffix2
BuildArch: noarch
Source: %name-%version.tar

Provides: python3-module-%{pep503_name %pypi_name} = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: publicsuffix-list

%description
Get a public suffix for a domain name using the Public Suffix List.
Forked from and using the same API as the publicsuffix package.

%prep
%setup

# Remove bundled publicsuffix data
rm -f %{pypi_name}/public_suffix_list.dat
# Using system psl
cp %_datadir/publicsuffix/public_suffix_list.dat src/%pypi_name/public_suffix_list.dat

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Sep 07 2023 Anton Vyatkin <toni@altlinux.org> 2.20191221-alt1
- Initial build for Sisyphus
