%define _unpackaged_files_terminate_build 1
%define pypi_name receptorctl

%def_without check

Name: python3-module-%pypi_name
Version: 1.6.5
Release: alt1
Summary: Receptorctl is a front-end CLI and importable Python library that interacts with Receptor over its control socket interface
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/receptorctl
BuildArch: noarch
Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-click
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-yaml
%endif

%description
%summary.

%prep
%setup -n %pypi_name-%version
# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM.
if [ ! -d .git ]; then
     git init
     git config user.email author@example.com
     git config user.name author
     git add .
     git commit -m 'release'
     git tag '%version'
fi


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%files
%doc README.*
%_bindir/receptorctl
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jun 16 2026 Nikita Panov <nexxy@altlinux.org> 1.6.5-alt1
- new version 1.6.5

* Thu Feb 20 2025 Anton Vyatkin <toni@altlinux.org> 1.5.3-alt1
- new version 1.5.3

* Tue Dec 17 2024 Anton Vyatkin <toni@altlinux.org> 1.5.2-alt1
- new version 1.5.2

* Thu Dec 05 2024 Anton Vyatkin <toni@altlinux.org> 1.5.1-alt1
- new version 1.5.1

* Thu Nov 21 2024 Anton Vyatkin <toni@altlinux.org> 1.4.11-alt1
- new version 1.4.11

* Tue Nov 19 2024 Anton Vyatkin <toni@altlinux.org> 1.4.10-alt1
- new version 1.4.10

* Thu Oct 17 2024 Anton Vyatkin <toni@altlinux.org> 1.4.9-alt1
- new version 1.4.9

* Tue Jul 23 2024 Anton Vyatkin <toni@altlinux.org> 1.4.8-alt1
- Initial build for Sisyphus.
