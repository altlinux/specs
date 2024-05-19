%define oname monetdb

Name: python3-module-%oname
Epoch: 1
Version: 1.8.1
Release: alt1
Summary: MonetDB is an open source column-oriented database management system
License: MPL-2.0-no-copyleft-exception
Group: Development/Python3
BuildArch: noarch
URL: https://pypi.org/project/pymonetdb
VCS: https://github.com/MonetDB/pymonetdb

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: monetdb
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
MonetDB is an open source column-oriented database management system. It was
designed to provide high performance on complex queries against large databases,
e.g. combining tables with hundreds of columns and multi-million rows.

This package contains MonetDB python3 interface.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

rm -rv %buildroot%python3_sitelibdir/tests

%files
%doc LICENSE CHANGES.md README.rst
%python3_sitelibdir/pymonetdb
%python3_sitelibdir/pymonetdb-%version.dist-info

%changelog
* Sun May 19 2024 Grigory Ustinov <grenka@altlinux.org> 1:1.8.1-alt1
- Automatically updated to 1.8.1.

* Thu Jun 10 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.4.1-alt1
- Updated to upstream version 1.4.1.
- Rebuilt without python-2.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:1.1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jan 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.1.1-alt1
- Initial build for ALT.
