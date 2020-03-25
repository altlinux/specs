%define _unpackaged_files_terminate_build 1

%define oname PLTable

Name: python-module-%oname
Version: 1.0.1
Release: alt1
Summary: Easily displaying tabular data in a visually appealing ASCII table format

Group: Development/Python
License: BSD
Source: %name-%version.tar
# vcs-git: https://github.com/platomav/PLTable.git
Url: https://github.com/platomav/PLTable

BuildArch: noarch
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools
Provides: python-module-prettytable = %EVR
Obsoletes: python-module-prettytable < %EVR

%py_provides %oname

%description
PLTable is a Python library designed to make it quick and easy
to represent tabular data in visually appealing ASCII tables.
PLTable is a fork of PTable which was in turn originally forked from PrettyTable.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc README.md LICENSE
%python_sitelibdir/*

%changelog
* Wed Mar 25 2020 Alexey Shabalin <shaba@altlinux.org> 1.0.1-alt1
- Initial build
