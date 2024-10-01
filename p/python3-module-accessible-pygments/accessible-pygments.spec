%define pypi_name accessible-pygments

%def_with check

Name:    python3-module-%pypi_name
Version: 0.0.5
Release: alt1

Summary: Accessible pygments themes

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/accessible-pygments
VCS:     https://github.com/Quansight-Labs/accessible-pygments

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-fancy-pypi-readme
BuildRequires: python3-module-hatch-vcs
BuildRequires: python3-module-setuptools-scm

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-hypothesis
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE *.md
%python3_sitelibdir/a11y_pygments
%python3_sitelibdir/%{pyproject_distinfo accessible_pygments}

%changelog
* Tue Oct 01 2024 Grigory Ustinov <grenka@altlinux.org> 0.0.5-alt1
- Initial build for Sisyphus.
