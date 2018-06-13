%define  modulename backports.functools_lru_cache

Name:    python-module-backports-functools-lru-cache
Version: 1.5
Release: alt1

Summary: Backport of functools.lru_cache from Python 3.3 as published at ActiveState
License: MIT
Group:   Development/Python
URL:     https://github.com/jaraco/backports.functools_lru_cache

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-setuptools_scm

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python_install

%files
%python_sitelibdir/backports
%python_sitelibdir/*.egg-info

%changelog
* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 1.5-alt1
- Initial build for Sisyphus
