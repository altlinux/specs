%define _unpackaged_files_terminate_build 1

%define oname pytest-testinfra

Name: python3-module-%oname
Version: 6.4.0
Release: alt1
Summary: pytest plugin for infrastructure testing
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/pytest-dev/pytest-testinfra

BuildArch: noarch

# https://github.com/pytest-dev/pytest-testinfra.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools_scm

# Testing requirements
BuildRequires: ansible
BuildRequires: python3(pytest)
BuildRequires: python3(salt)
BuildRequires: python3(winrm)
BuildRequires: /proc

%description
With Testinfra you can write unit tests in Python to test actual state of your
servers configured by management tools like Salt, Ansible, Puppet, Chef and so
on. Testinfra aims to be a Serverspec equivalent in python and is written as a
plugin to the powerful Pytest test engine

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
%__python3 -m pytest test -v

%files
%doc LICENSE
%doc CHANGELOG.rst README.rst
%python3_sitelibdir/testinfra/
%python3_sitelibdir/pytest_testinfra-*.egg-info/


%changelog
* Mon Nov 15 2021 Slava Aseev <ptrnine@altlinux.org> 6.4.0-alt1
- Initial build for ALT

