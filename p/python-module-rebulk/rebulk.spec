%define _unpackaged_files_terminate_build 1
%define oname rebulk

%def_with python3

Name: python-module-%oname
Version: 0.9.0
Release: alt1.1
Summary: Rebulk - define simple search patterns in bulk to perform advanced matching on any string
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/rebulk

# https://github.com/Toilal/rebulk.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-pytest-runner
BuildRequires: python-module-six
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest-runner
BuildRequires: python3-module-six
BuildRequires: python3-module-pytest
%endif

%description
ReBulk is a python library that performs advanced searches in strings
that would be hard to implement using re module or String methods only.

It includes some features like Patterns, Match, Rule that allows developers
to build a custom and complex string matcher using a readable and extendable API.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
ReBulk is a python library that performs advanced searches in strings
that would be hard to implement using re module or String methods only.

It includes some features like Patterns, Match, Rule that allows developers
to build a custom and complex string matcher using a readable and extendable API.

This package contains tests for %oname.


%if_with python3
%package -n python3-module-%oname
Summary: Rebulk - define simple search patterns in bulk to perform advanced matching on any string
Group: Development/Python3

%description -n python3-module-%oname
ReBulk is a python library that performs advanced searches in strings
that would be hard to implement using re module or String methods only.

It includes some features like Patterns, Match, Rule that allows developers
to build a custom and complex string matcher using a readable and extendable API.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
ReBulk is a python library that performs advanced searches in strings
that would be hard to implement using re module or String methods only.

It includes some features like Patterns, Match, Rule that allows developers
to build a custom and complex string matcher using a readable and extendable API.

This package contains tests for %oname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%check
python setup.py test

%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files tests
%python_sitelibdir/*/test

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.0-alt1
- Initial build for ALT.
