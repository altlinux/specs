%define _unpackaged_files_terminate_build 1

Name: python3-module-pyexcel
Version: 0.7.4
Release: alt1

Summary: One API to read and write data in various excel file formats
Group: Development/Python3
License: BSD-3-Clause
URL: https://github.com/pyexcel/pyexcel
VCS: https://github.com/pyexcel/pyexcel.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-lml
BuildRequires: python3-module-pyexcel-io
BuildRequires: python3-module-texttable
BuildRequires: python3-module-pyexcel-xls
BuildRequires: python3-module-pyexcel-xlsx

%description
One application programming interface(API) to handle multiple data sources:
physical file
memory file
SQLAlchemy table
Django Model
Python data structures: dictionary, records and array
One API to read and write data in various excel file formats.
For large data sets, data streaming are supported. A genenerator can be
returned to you. Checkout iget_records, iget_array, isave_as and isave_book_as.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst LICENSE
%python3_sitelibdir_noarch/%{pyproject_distinfo pyexcel}
%python3_sitelibdir_noarch/pyexcel

%changelog
* Tue Apr 07 2026 Ilya Muhamadeev <nicourced@altlinux.org> 0.7.4-alt1
- Initial build.
