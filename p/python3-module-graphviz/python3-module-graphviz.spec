%define  modulename graphviz
%def_enable check

Name:    python3-module-%modulename
Version: 0.13.2
Release: alt1

Summary: Simple Python interface for Graphviz
License: MIT
Group:   Development/Python3
URL:     https://github.com/xflr6/graphviz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-tox
BuildRequires: python3-module-mock
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-pytest-cov
BuildRequires: graphviz

BuildArch: noarch
Source:  %name-%version.tar
Patch0: %name-%version-%release.patch

%description
%summary

%prep
%setup
%patch0 -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -v

%files
%python3_sitelibdir/%{modulename}*
%python3_sitelibdir/*.egg-info

%changelog
* Tue Dec 03 2019 Anton Farygin <rider@altlinux.ru> 0.13.2-alt1
- first build for ALT

