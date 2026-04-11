%define _unpackaged_files_terminate_build 1

Name: python3-module-pyexcel-xlsx
Version: 0.6.1
Release: alt1

Summary: A tiny wrapper library to manipulate data in xlsx and xlsm
Group: Development/Python3
License: BSD-3-Clause
URL: https://github.com/pyexcel/pyexcel-xlsx
VCS: https://github.com/pyexcel/pyexcel-xlsx.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-openpyxl
BuildRequires: python3-module-pyexcel-io

%description
Pyexcel-xlsx is a tiny wrapper library to read, manipulate and write data in
xlsx and xlsm format using read_only mode reader, write_only mode writer from
openpyxl. You are likely to use it with pyexcel.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst LICENSE
%python3_sitelibdir_noarch/%{pyproject_distinfo pyexcel_xlsx}
%python3_sitelibdir_noarch/pyexcel_xlsx

%changelog
* Thu Apr 09 2026 Ilya Muhamadeev <nicourced@altlinux.org> 0.6.1-alt1
- Initial build.
