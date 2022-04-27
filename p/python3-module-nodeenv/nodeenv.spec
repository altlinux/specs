%define  modulename nodeenv

%def_with check

Name:    python3-module-%modulename
Version: 1.6.0
Release: alt1

Summary: Virtual environment for Node.js & integrator with virtualenv

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/ekalinin/nodeenv

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-mock
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
nodeenv (node.js virtual environment) is a tool to create isolated node.js
environments.
It creates an environment that has its own installation directories, that
doesn't share libraries with other node.js virtual environments.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%_bindir/%modulename
%python3_sitelibdir/%modulename.py
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/*.egg-info

%changelog
* Tue Apr 26 2022 Grigory Ustinov <grenka@altlinux.org> 1.6.0-alt1
- Initial build for Sisyphus.
