%define  modulename restructuredtext_lint

Name:    python3-module-%modulename
Version: 1.4.0
Release: alt2

Summary: reStructuredText linter
License: Unlicense
Group:   Development/Python3
URL:     https://github.com/twolfson/restructuredtext-lint

# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %modulename} = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-docutils >= 0.11

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%_bindir/*
%python3_sitelibdir/*

%changelog
* Mon Dec 25 2023 Ajrat Makhmutov <rauty@altlinux.org> 1.4.0-alt2
- Mapped PyPI name to distro's one.

* Sat May 28 2022 Grigory Ustinov <grenka@altlinux.org> 1.4.0-alt1
- Build new version.

* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 1.2.1-alt2
- Drop python2 support.

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus
