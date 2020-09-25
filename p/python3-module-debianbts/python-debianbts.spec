Summary: Python interface to Debian's Bug Tracking System
Name: python3-module-debianbts
Version: 3.0.2
Release: alt1
Packager: Igor Vlasenko <viy@altlinux.ru>
License: MIT
Group: Development/Python
URL: http://github.com/venthur/python-debianbts
Source: %name-%version.tar
BuildArch: noarch
BuildRequires: python3-devel python3-module-setuptools python3-module-pysimplesoap

%description
This package provides the debianbts module, which allows one to query Debian's
BTS via it's SOAP-interface and returns the answer in Python's native data
types.

%prep
%setup -q

%build
%python3_build_debug

%install
%python3_install

# disable tests as they require internet connection

%files
%doc README.md
%doc CHANGELOG.md
%doc THANKS.txt
%_bindir/debianbts
%python3_sitelibdir_noarch/*

%changelog
* Fri Sep 25 2020 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt1
- new version

