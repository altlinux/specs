%define pypi_name rich-argparse

%def_with check

Name:    python3-module-%pypi_name
Version: 1.7.2
Release: alt1

Summary: A rich help formatter for argparse

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/rich-argparse
VCS:     https://github.com/hamdanal/rich-argparse

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-rich
%endif

BuildArch: noarch

Source: %name-%version.tar

Patch: 1b4430d1d56fb1b1e6246925d651b4202da55ed1.patch

%description
%summary

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE *.md
%python3_sitelibdir/rich_argparse
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Feb 05 2026 Grigory Ustinov <grenka@altlinux.org> 1.7.2-alt1
- Initial build for Sisyphus.
