%def_with check

%define pypi_name jupyter_cache

Name: python3-module-%pypi_name
Version: 1.0.1
Release: alt1

Summary: A defined interface for working with a cache of executed jupyter notebooks
License: MIT
Group: Development/Python3
Url: https://jupyter-cache.readthedocs.io/en/latest/
Vcs: https://github.com/executablebooks/jupyter-cache.git

Source: %name-%version.tar
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-attrs
BuildRequires: python3-module-click
BuildRequires: python3-module-importlib-metadata
BuildRequires: python3-module-nbclient
BuildRequires: python3-module-nbformat
BuildRequires: python3-module-pyyaml-ft
BuildRequires: python3-module-sqlalchemy
BuildRequires: python3-module-tabulate
BuildRequires: python3-module-flit-core

BuildArch: noarch

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%_bindir/jcache
%python3_sitelibdir_noarch/%pypi_name
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Mar 31 2026 Ulysses Apokin <ulysses@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
