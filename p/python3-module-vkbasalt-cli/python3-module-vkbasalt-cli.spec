%define pypi_name vkbasalt-cli

%def_without check

Name:    python3-module-%pypi_name
Version: 3.1.1
Release: alt1

Summary: Command-line utility for vkBasalt
License: GPL-3.0+ and LGPL-3.0+
Group:   Development/Python3
URL:     https://gitlab.com/TheEvilSkeleton/vkbasalt-cli

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
vkbasalt-cli (filename vkbasalt) is a CLI utility and library in conjunction
with vkBasalt. This makes generating configuration files or running vkBasalt
with games easier. This is mainly convenient in environments where integrating
vkBasalt is wishful, for example a GUI application. Integrating vkbasalt-cli
allows a front-end to easily generate and use specific configurations on the
fly, without asking the user to manually write a configuration file.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/vkbasalt
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Sep 13 2023 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1
- Initial build for Sisyphus.
