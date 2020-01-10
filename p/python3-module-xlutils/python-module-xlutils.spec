%define oname xlutils

Name:     python3-module-%oname
Version:  2.0.0
Release:  alt2

Summary:  Utilities for working with Excel files that require both xlrd and xlwt

License:  MIT
Group:    Development/Python3
URL:      http://www.python-excel.org/
BuildArch: noarch

Packager: Andrey Cherepanov <cas@altlinux.org>
Source:   %oname-%version.tar
#VCS:     https://github.com/python-excel/xlutils

Conflicts: python-module-%oname <= %EVR
Obsoletes: python-module-%oname <= %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-distribute
BuildRequires: python3-module-xlrd
BuildRequires: python3-module-xlwt
BuildRequires: python3-module-testfixtures

%description
This package collects utilities that require both xlrd and xlwt,
including the ability to copy and modify or filter existing excel files.

%prep
%setup -q -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc README* docs/*
%_bindir/*
%python3_sitelibdir/xlutils/
%python3_sitelibdir/xlutils*.egg-info/

%changelog
* Fri Jan 10 2020 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt2
- Transfer to python3.

* Sun Jun 12 2016 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- new version 2.0.0

* Tue Jun 07 2016 Andrey Cherepanov <cas@altlinux.org> 1.7.1-alt1
- new version 1.7.1

* Thu Mar 27 2014 Andrey Cherepanov <cas@altlinux.org> 1.7.0-alt1
- Initial build for ALT Linux

