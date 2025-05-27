%define _unpackaged_files_terminate_build 1
%define pypi_name sgtk-menu

Name: %pypi_name
Version: 1.4.1
Release: alt1

Summary: GTK launchers for sway & other WMs w/ menu, dmenu, application grid and button bar
License: GPL-3.0
Group: Other
Url: https://github.com/nwg-piotr/sgtk-menu

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
This project is an attempt to create a launcher, that behaves decently on **sway**, but also works on other window
managers.

%package -n python3-module-%pypi_name
Summary: Module for %pypi_name
Group: Development/Python3

%description -n python3-module-%pypi_name
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md
%_bindir/*

%files -n python3-module-%pypi_name
%python3_sitelibdir/sgtk_menu
%python3_sitelibdir/sgtk_menu-%version.dist-info

%changelog
* Mon Jan 27 2025 Artem Semenov <savoptik@altlinux.org> 1.4.1-alt1
- Initial build for Sisyphus.