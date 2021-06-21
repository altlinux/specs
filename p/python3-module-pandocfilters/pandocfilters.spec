%define _unpackaged_files_terminate_build 1

%define oname pandocfilters

Name: python3-module-%oname
Version: 1.4.3
Release: alt1
Summary: Utilities for writing pandoc filters in python
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/jgm/pandocfilters

BuildArch: noarch

# https://github.com/jgm/pandocfilters.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-fixes.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
A python module for writing pandoc filters.

%prep
%setup
%patch1 -p1

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE
%doc README
%python3_sitelibdir/*.py
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/%oname-%version-py*.egg-info

%changelog
* Mon Jun 21 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.3-alt1
- Updated to upstream version 1.4.3.
- Disabled build for python-2.

* Thu Nov 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.2-alt1
- Initial build for ALT.
