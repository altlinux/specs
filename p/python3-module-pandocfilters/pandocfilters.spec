%define oname pandocfilters

Name: python3-module-%oname
Version: 1.5.1
Release: alt1
Summary: Utilities for writing pandoc filters in python
License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/pandocfilters
VCS: https://github.com/jgm/pandocfilters

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
A python module for writing pandoc filters.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE *.md *.rst
%python3_sitelibdir/*.py
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Sun May 19 2024 Grigory Ustinov <grenka@altlinux.org> 1.5.1-alt1
- Automatically updated to 1.5.1.

* Mon Jun 21 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.3-alt1
- Updated to upstream version 1.4.3.
- Disabled build for python-2.

* Thu Nov 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.2-alt1
- Initial build for ALT.
