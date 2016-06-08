%define oname xlutils

Name:	  python-module-%oname
Version:  1.7.1
Release:  alt1

Summary:  Utilities for working with Excel files that require both xlrd and xlwt

License:  MIT
Group:    Development/Python
URL: 	  http://www.python-excel.org/
BuildArch: noarch

Packager: Andrey Cherepanov <cas@altlinux.org>
Source:   %oname-%version.tar
#VCS:	  https://github.com/python-excel/xlutils

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute
BuildRequires: python-module-xlrd
BuildRequires: python-module-xlwt
BuildRequires: python-module-testfixtures

%description
This package collects utilities that require both xlrd and xlwt,
including the ability to copy and modify or filter existing excel files.

%prep
%setup -q -n %oname-%version

%build
%python_build

%install
%python_install

%files
%doc README.txt docs/*
%_bindir/*
%python_sitelibdir/xlutils/
%python_sitelibdir/xlutils*.egg-info/

%changelog
* Tue Jun 07 2016 Andrey Cherepanov <cas@altlinux.org> 1.7.1-alt1
- new version 1.7.1

* Thu Mar 27 2014 Andrey Cherepanov <cas@altlinux.org> 1.7.0-alt1
- Initial build for ALT Linux

