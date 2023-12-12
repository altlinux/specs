%define  modulename bandit

%def_with check

Name:    python3-module-%modulename
Version: 1.7.6
Release: alt1

Summary: Bandit is a tool designed to find common security issues in Python code.

License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/PyCQA/bandit

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:  %name-%version.tar

Requires: python3-module-yaml

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr

%if_with check
BuildRequires: python3-module-GitPython
BuildRequires: python3-module-yaml
BuildRequires: python3-module-stevedore
BuildRequires: python3-module-rich
BuildRequires: python3-module-stestr
BuildRequires: python3-module-beautifulsoup4
%endif

BuildArch: noarch

%description
Bandit is a tool designed to find common security issues in Python code.
To do this Bandit processes each file, builds an AST from it, and runs
appropriate plugins against the AST nodes. Once Bandit has finished scanning
all the files it generates a report.

Bandit was originally developed within the OpenStack Security Project and later
rehomed to PyCQA.

%prep
%setup

%build
export PBR_VERSION=%version
%pyproject_build

%install
export PBR_VERSION=%version
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE *.rst *.md
%_bindir/bandit
%_bindir/bandit-baseline
%_bindir/bandit-config-generator
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info

%changelog
* Tue Dec 12 2023 Grigory Ustinov <grenka@altlinux.org> 1.7.6-alt1
- Automatically updated to 1.7.6.
- Build with check.

* Fri Mar 10 2023 Grigory Ustinov <grenka@altlinux.org> 1.7.5-alt1
- Automatically updated to 1.7.5.

* Thu Jun 02 2022 Grigory Ustinov <grenka@altlinux.org> 1.7.4-alt1
- Build new version.

* Fri Mar 19 2021 Grigory Ustinov <grenka@altlinux.org> 1.7.0-alt1
- Build new version.

* Tue Nov 12 2019 Grigory Ustinov <grenka@altlinux.org> 1.6.2-alt1
- Initial build for Sisyphus.
