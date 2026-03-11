%define _unpackaged_files_terminate_build 1
%define pypi_name cmap
%define mod_name cmap

%def_with check

Name: python3-module-%pypi_name
Version: 0.7.2
Release: alt1

Summary: Scientific colormaps for python, with only numpy dependency
License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/cmap
VCS: https://github.com/jtauber/cmap
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs

%if_with check
BuildRequires: python3-module-numpy-testing
%endif

%description
%summary.

%prep
%setup
%pyproject_scm_init

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.md
%doc LICENSES/LicenseRef-Battelle.txt
%doc LICENSES/LicenseRef-ColorBrewer.txt
%doc LICENSES/LicenseRef-Yorick.txt
%doc LICENSES/LicenseRef-gnuplot.txt
%python3_sitelibdir_noarch/%mod_name
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Mar 03 2026 Aleksandr Dovydenkov <asd@altlinux.org> 0.7.2-alt1
- Initial build for Sisyphus.