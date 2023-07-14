%define pypi_name looseversion

%def_with check

Name:    python3-module-%pypi_name
Version: 1.2.0
Release: alt1

Summary: A backwards/forwards-compatible fork of distutils.version.LooseVersion
License: Python-2.0
Group:   Development/Python3
URL:     https://github.com/effigies/looseversion

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Jun 15 2023 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- New version.

* Thu Apr 27 2023 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- Initial build for Sisyphus.
