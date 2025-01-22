%define pypi_name kdtree

Name: python3-module-%pypi_name
Version: 0.16
Release: alt1

Summary: A Python implementation of a kd-tree
License: ISC
Group: Development/Python3

Url: https://pypi.org/project/kdtree/
Vcs: https://github.com/stefankoegl/kdtree

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

# Conflicts: python3-module-libkdtree++

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md LICENSE
%python3_sitelibdir/*

%changelog
* Tue Jan 21 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.16-alt1
- Initial build for Sisyphus
