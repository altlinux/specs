%define _unpackaged_files_terminate_build 1

Name: python3-module-pyexcel-io
Version: 0.6.7.1
Release: alt1

Summary: Provides one API to read and write the data in excel format
License: BSD-3-Clause
Group: Development/Python3
URL: https://github.com/pyexcel/pyexcel-io
VCS: https://github.com/pyexcel/pyexcel-io.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-lml
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
Pyexcel-io provides one application programming interface(API) to read and
write the data in excel format, import the data into and export the data from
database. It provides support for csv(z) format, django database and sqlalchemy
supported databases.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst LICENSE
%python3_sitelibdir_noarch/pyexcel_io
%python3_sitelibdir_noarch/pyexcel_io-0.6.7.dist-info

%changelog
* Tue Apr 07 2026 Ilya Muhamadeev <nicourced@altlinux.org> 0.6.7.1-alt1
- Initial build.
