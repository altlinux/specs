%define oname rebulk

%def_with check

Name: python3-module-%oname
Version: 3.3.0
Release: alt1

Summary: Rebulk - define simple search patterns in bulk to perform advanced matching on any string

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/rebulk
VCS: https://github.com/Toilal/rebulk

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

%description
ReBulk is a python library that performs advanced searches in strings
that would be hard to implement using re module or String methods only.

It includes some features like Patterns, Match, Rule that allows developers
to build a custom and complex string matcher using a readable and extendable API.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest rebulk/test

%files
%doc LICENSE *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/*/test

%changelog
* Sat Jan 20 2024 Grigory Ustinov <grenka@altlinux.org> 3.3.0-alt1
- Automatically updated to 3.3.0.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 3.2.0-alt1
- Automatically updated to 3.2.0.

* Wed Feb 09 2022 Stanislav Levin <slev@altlinux.org> 3.1.0-alt1
- 3.0.1 -> 3.1.0.

* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt1
- Automatically updated to 3.0.1.

* Fri Jul 31 2020 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt1
- Automatically updated to 2.0.1.
- Drop python2 support.

* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- new version 2.0.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.0-alt1
- Initial build for ALT.
