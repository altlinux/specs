%define pypi_name sphinx-theme-builder

%def_with check

Name:    python3-module-%pypi_name
Version: 0.2.0b2
Release: alt1

Summary: Streamline the Sphinx theme development workflow

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/sphinx-theme-builder
VCS:     https://github.com/pradyunsg/sphinx-theme-builder

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit

%if_with check
BuildRequires: python3-module-pyproject-metadata
BuildRequires: python3-module-rich
BuildRequires: python3-module-nodeenv
BuildRequires: python3-module-click
BuildRequires: python3-module-build
BuildRequires: python3-module-sphinx-autobuild
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
Streamline the Sphinx theme development workflow, by building upon existing
standardised tools.
- simplified packaging experience
- simplified JavaScript tooling setup
- development server, with rebuild-on-save and automagical browser reloading
- consistent repository structure across themes

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE *.md
%_bindir/stb
%python3_sitelibdir/sphinx_theme_builder
%python3_sitelibdir/%{pyproject_distinfo sphinx_theme_builder}

%changelog
* Tue Sep 19 2023 Grigory Ustinov <grenka@altlinux.org> 0.2.0b2-alt1
- Initial build for Sisyphus.
