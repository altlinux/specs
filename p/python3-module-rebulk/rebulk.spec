%define _unpackaged_files_terminate_build 1
%define oname rebulk

Name: python3-module-%oname
Version: 2.0.1
Release: alt1
Summary: Rebulk - define simple search patterns in bulk to perform advanced matching on any string
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/rebulk

# https://github.com/Toilal/rebulk.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest-runner
BuildRequires: python3-module-six
BuildRequires: python3-module-pytest

%description
ReBulk is a python library that performs advanced searches in strings
that would be hard to implement using re module or String methods only.

It includes some features like Patterns, Match, Rule that allows developers
to build a custom and complex string matcher using a readable and extendable API.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
ReBulk is a python library that performs advanced searches in strings
that would be hard to implement using re module or String methods only.

It includes some features like Patterns, Match, Rule that allows developers
to build a custom and complex string matcher using a readable and extendable API.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files tests
%python3_sitelibdir/*/test

%changelog
* Fri Jul 31 2020 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt1
- Automatically updated to 2.0.1.
- Drop python2 support.

* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- new version 2.0.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.0-alt1
- Initial build for ALT.
