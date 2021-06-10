%define _unpackaged_files_terminate_build 1

%define oname monetdb

Name: python3-module-%oname
Epoch: 1
Version: 1.4.1
Release: alt1
Summary: MonetDB is an open source column-oriented database management system
License: MPL-2.0-no-copyleft-exception
Group: Development/Python3
BuildArch: noarch
URL: http://monetdb.org

# https://github.com/gijzelaerr/pymonetdb.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: monetdb
BuildRequires: python3-devel python3-module-setuptools

%description
MonetDB is an open source column-oriented database management system. It was
designed to provide high performance on complex queries against large databases,
e.g. combining tables with hundreds of columns and multi-million rows.

This package contains MonetDB python3 interface.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files -n python3-module-%oname
%doc LICENSE
%doc CHANGES README.rst
%python3_sitelibdir/pymonetdb
%python3_sitelibdir/pymonetdb-%version-py*.egg-info

%changelog
* Thu Jun 10 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.4.1-alt1
- Updated to upstream version 1.4.1.
- Rebuilt without python-2.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:1.1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jan 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.1.1-alt1
- Initial build for ALT.
