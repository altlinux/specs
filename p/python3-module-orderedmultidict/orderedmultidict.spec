%define _unpackaged_files_terminate_build 1
%define pypi_name orderedmultidict
%define mod_name %pypi_name

%def_with check

Name:    python3-module-%pypi_name
Version: 1.0.1
Release: alt2

Summary: Ordered Multivalue Dictionary. Helps power furl.

License: Unlicense
Group:   Development/Python3
URL:     https://github.com/gruns/orderedmultidict

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-six
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
A multivalue dictionary is a dictionary that can store multiple values for the
same key. An ordered multivalue dictionary is a multivalue dictionary that
retains the order of insertions and deletions.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest discover -v tests

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 14 2024 Stanislav Levin <slev@altlinux.org> 1.0.1-alt2
- migrated from removed setuptools' test command (see #50996).

* Fri Jun 24 2022 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
