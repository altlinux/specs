%define oname seaborn

Name: python3-module-seaborn
Version: 0.9.0
Release: alt1

Summary: Seaborn: statistical data visualization
License: BSD-3-Clause
Group: Sciences/Other
URL: https://github.com/mwaskom/seaborn
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flake8 python3-module-pytest-runner


%description
Seaborn is a library for making attractive and informative statistical graphics in Python. It is built on top of matplotlib and tightly integrated with the PyData stack, including support for numpy and pandas data structures and statistical routines from scipy and statsmodels.

Some of the features that seaborn offers are

- Several built-in themes that improve on the default matplotlib aesthetics
- Tools for choosing color palettes to make beautiful plots that reveal patterns in your data
- Functions for visualizing univariate and bivariate distributions or for comparing them between subsets of data
- Tools that fit and visualize linear regression models for different kinds of independent and dependent variables
- Functions that visualize matrices of data and use clustering algorithms to discover structure in those matrices
- A function to plot statistical timeseries data with flexible estimation and representation of uncertainty around the estimate
- High-level abstractions for structuring grids of plots that let you easily build complex visualizations


%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir_noarch/seaborn
%python3_sitelibdir_noarch/seaborn-%{version}*


%changelog
* Mon Jan 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.9.0-alt1
- Version updated to 0.9.0
- porting on python3.

* Thu Dec 12 2019 Grigory Ustinov <grenka@altlinux.org> 0.7.1-alt2
- NMU: Fix license.

* Wed Jun 21 2017 Terechkov Evgenii <evg@altlinux.org> 0.7.1-alt1
- Initial build for ALT Linux Sisyphus
