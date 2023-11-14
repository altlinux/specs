%define pypi_name ordered-set
%define mod_name ordered_set

%def_with check

Name: python3-module-%pypi_name
Version: 4.1.0
Release: alt1

Summary: A mutable set that remembers the order of its entries
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/ordered-set
VCS: https://github.com/rspeer/ordered-set
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core
%if_with check
BuildRequires: python3-module-pytest
%endif

%description
An OrderedSet is a mutable data structure that is a hybrid of a list and a set.
It remembers the order of its entries, and every entry has an index number that
can be looked up.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Nov 14 2023 Anton Vyatkin <toni@altlinux.org> 4.1.0-alt1
- Initial build for Sisyphus
