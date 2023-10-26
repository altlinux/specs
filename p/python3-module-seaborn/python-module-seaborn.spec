%define _unpackaged_files_terminate_build 1

%define oname seaborn

%ifnarch i586
%def_with check
%else
%def_without check
%endif

Name: python3-module-seaborn
Version: 0.13.0
Release: alt1
Summary: Seaborn: statistical data visualization
License: BSD-3-Clause
Group: Sciences/Other
URL: https://pypi.org/project/seaborn/

VCS: https://github.com/mwaskom/seaborn
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core
%if_with check
BuildRequires: python3-module-matplotlib
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-pandas
BuildRequires: python3-module-pandas-tests
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-contourpy
BuildRequires: python3-module-statsmodels
%endif

%description
Seaborn is a library for making attractive and informative statistical graphics
in Python. It is built on top of matplotlib and tightly integrated with the
PyData stack, including support for numpy and pandas data structures and
statistical routines from scipy and statsmodels.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

# Remove testing file, that brings numpy.testing
rm -fv %buildroot%python3_sitelibdir/%oname/_testing.py

%check
# need pandas version >=2.0.2
%pyproject_run_pytest -n auto -k "\
not test_kde_singular_data \
and not test_unfilled_marker_edgecolor_warning"

%files
%doc LICENSE.md README.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Thu Oct 26 2023 Anton Vyatkin <toni@altlinux.org> 0.13.0-alt1
- New version 0.13.0.

* Mon Sep 11 2023 Anton Vyatkin <toni@altlinux.org> 0.12.2-alt3
- FTBFS: add patches for numpy-1.25 and matplotlib-3.7 and statsmodels-0.14.

* Wed Mar 01 2023 Grigory Ustinov <grenka@altlinux.org> 0.12.2-alt2
- Removed extra runtime dependency.

* Tue Feb 07 2023 Anton Vyatkin <toni@altlinux.org> 0.12.2-alt1
- new version 0.12.2 (Closes: #44636).

* Wed Aug 26 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.10.1-alt1
- Updated to upstream version 0.10.1.

* Mon Jan 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.9.0-alt1
- Version updated to 0.9.0
- porting on python3.

* Thu Dec 12 2019 Grigory Ustinov <grenka@altlinux.org> 0.7.1-alt2
- NMU: Fix license.

* Wed Jun 21 2017 Terechkov Evgenii <evg@altlinux.org> 0.7.1-alt1
- Initial build for ALT Linux Sisyphus
