%define  modulename bandit

Name:    python3-module-%modulename
Version: 1.7.0
Release: alt1

Summary: Bandit is a tool designed to find common security issues in Python code.

License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/PyCQA/bandit

Packager: Grigory Ustinov <grenka@altlinux.org>

Requires: python3-module-yaml

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr

BuildArch: noarch

Source:  %modulename-%version.tar

%description
Bandit is a tool designed to find common security issues in Python code.
To do this Bandit processes each file, builds an AST from it, and runs
appropriate plugins against the AST nodes. Once Bandit has finished scanning
all the files it generates a report.

Bandit was originally developed within the OpenStack Security Project and later
rehomed to PyCQA.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%_bindir/bandit
%_bindir/bandit-baseline
%_bindir/bandit-config-generator
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Fri Mar 19 2021 Grigory Ustinov <grenka@altlinux.org> 1.7.0-alt1
- Build new version.

* Tue Nov 12 2019 Grigory Ustinov <grenka@altlinux.org> 1.6.2-alt1
- Initial build for Sisyphus.
