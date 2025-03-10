%define pypi_name setuptools-git-versioning

%def_without check

Name:    python3-module-%pypi_name
Version: 2.1.0
Release: alt1

Summary: Use git repo data (latest tag, current commit hash, etc) for building a version number according PEP-440
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/setuptools-git-versioning/
Vcs:     https://github.com/dolfinus/setuptools-git-versioning

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel git-core
Requires: git-core

BuildArch: noarch

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE MANIFEST.* README.*
%_bindir/%pypi_name
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/setuptools*

%changelog
* Sat Jan 25 2025 Sergey Palcheh <minergenon@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus
