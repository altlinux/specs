%global pypi_name ansible-runner
%def_disable check

Name: %pypi_name
Version: 2.3.4
Release: alt1
Summary: A tool and python library to interface with Ansible

License: Apache-2.0
Group: Development/Python3
Url: https://github.com/ansible/ansible-runner
Source: %name-%version.tar
BuildArch: noarch

# Requires: (ansible-core or ansible)

BuildRequires(pre): rpm-build-python3 rpm-build-pyproject
BuildRequires: python3-devel
%pyproject_builddeps_build
%pyproject_runtimedeps_metadata

BuildRequires: ansible-core
BuildRequires: python3(mock)
BuildRequires: python3(pbr)
BuildRequires: python3(pip)
BuildRequires: python3(psutil)
BuildRequires: python3(pexpect)
BuildRequires: python3(yaml)
BuildRequires: python3(setuptools)
BuildRequires: python3(six)
BuildRequires: python3(daemon)
BuildRequires: python3(wheel)
%if_enabled check
# For tests
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-cov)
BuildRequires: python3(pytest-mock)
BuildRequires: python3(pytest-timeout)
BuildRequires: python3(pytest-xdist)
BuildRequires: python3(yamllint)
BuildRequires: python3(cryptography)
%endif

%description
Ansible Runner is a tool and python library that helps when interfacing with
Ansible from other systems whether through a container image interface, as a
standalone tool, or imported into a python project.

%package -n python3-module-%pypi_name
Summary: %summary
Group: Development/Python3
Provides: %name = %EVR
%py3_requires daemon

%description -n python3-module-%pypi_name
Ansible Runner is a tool and python library that helps when interfacing with
Ansible from other systems whether through a container image interface, as a
standalone tool, or imported into a python project.

%prep
%setup

%build
export PBR_VERSION=%version
%pyproject_build

%install
export PBR_VERSION=%version
%pyproject_install

%check
%pyproject_run_pytest ||:

%files -n python3-module-%pypi_name
%doc README.md LICENSE.md
%_bindir/*
%python3_sitelibdir/*
%_datadir/%name/utils

%changelog
* Wed Sep 13 2023 Alexey Shabalin <shaba@altlinux.org> 2.3.4-alt1
- Initial build.

