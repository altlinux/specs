%define modulename Geraldo

Name:       python3-module-%modulename
Version:    0.4.17
Release:    alt2

Summary:    Geraldo is a reports engine for Python and Django applications
License:    LGPL
Group:      Development/Python3
URL:        http://www.geraldoreports.org

BuildArch:  noarch

Source: %modulename-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
Geraldo is a Python and Django pluggable application
that works with ReportLab to generate complex reports.

%prep
%setup -n %modulename-%version

sed -i 's|, new||' geraldo/base.py

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%files
%doc README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests


%changelog
* Mon Feb 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.4.17-alt2
- Porting to python3.

* Fri Aug 09 2019 Alexey Shabalin <shaba@altlinux.org> 0.4.17-alt1
- Initial build for ALT
