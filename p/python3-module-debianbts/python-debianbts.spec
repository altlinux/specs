Summary: Python interface to Debian's Bug Tracking System
Name: python3-module-debianbts
Version: 4.0.1
Release: alt1
Packager: Igor Vlasenko <viy@altlinux.ru>
License: MIT
Group: Development/Python
URL: http://github.com/venthur/python-debianbts
Source: %name-%version.tar
BuildArch: noarch
BuildRequires: python3-module-setuptools python3-module-wheel

%description
This package provides the debianbts module, which allows one to query Debian's
BTS via it's SOAP-interface and returns the answer in Python's native data
types.

%prep
%setup -q

%build
%pyproject_build

%install
%pyproject_install

# disable tests as they require internet connection

%files
%doc README.md
%doc CHANGELOG.md
%doc THANKS.txt
%_bindir/debianbts
%python3_sitelibdir/debianbts
%python3_sitelibdir/python_debianbts-%version.dist-info

%changelog
* Fri Oct 13 2023 Anton Vyatkin <toni@altlinux.org> 4.0.1-alt1
- New version 4.0.1.

* Fri Sep 25 2020 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt1
- new version

