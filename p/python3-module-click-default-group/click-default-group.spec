%define modulename click-default-group
%define pypi_name click_default_group

%def_with check

Name:    python3-module-%modulename
Version: 1.2.4
Release: alt1

Summary: Extends click.Group to invoke a command without explicit subcommand name

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/click-default-group
VCS:     https://github.com/click-contrib/click-default-group

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-click
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
python3 test.py

%files
%doc LICENSE *.md
%python3_sitelibdir/%pypi_name.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Thu Dec 28 2023 Grigory Ustinov <grenka@altlinux.org> 1.2.4-alt1
- Initial build for Sisyphus.
