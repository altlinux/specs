%define _unpackaged_files_terminate_build 1

Name: python3-module-pyexcel-xls
Version: 0.7.1
Release: alt1

Summary: A tiny wrapper library to read, manipulate and write data in xls
Group: Development/Python3
License: BSD-3-Clause
URL: https://github.com/pyexcel/pyexcel-xls
VCS: https://github.com/pyexcel/pyexcel-xls.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pyexcel-io
BuildRequires: python3-module-xlrd
BuildRequires: python3-module-xlwt

%description
Pyexcel-xls is a tiny wrapper library to read, manipulate and write data in xls
format and it can read xlsx and xlsm fromat. You are likely to use it with
pyexcel.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst LICENSE
%python3_sitelibdir_noarch/%{pyproject_distinfo pyexcel_xls}
%python3_sitelibdir_noarch/pyexcel_xls

%changelog
* Thu Apr 09 2026 Ilya Muhamadeev <nicourced@altlinux.org> 0.7.1-alt1
- Initial build.
