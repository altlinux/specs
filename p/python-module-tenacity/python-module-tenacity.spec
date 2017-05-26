%define oname tenacity
%def_with python3

# asyncio for python3 only
%add_python_req_skip asyncio
%add_findreq_skiplist %python_sitelibdir/%oname/async.py
%add_findreq_skiplist %python_sitelibdir/%oname/tests/test_async.py

Name: python-module-%oname
Version: 4.1.0
Release: alt1
Summary: Retrying library
Group: Development/Python
License: ASL 2.0
Url: https://github.com/jd/tenacity
Source: %oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-pbr
BuildRequires: python-module-futures >= 3.0
BuildRequires: python-module-monotonic >= 0.6

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-pbr
BuildRequires: python3-module-monotonic >= 0.6
%endif

%description
Tenacity is an Apache 2.0 licensed general-purpose
retrying library, written in Python, to simplify the task
of adding retry behavior to just about anything.
It originates from a fork of Retrying

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Retrying library
Group: Development/Python3

%description -n python3-module-%oname
Tenacity is an Apache 2.0 licensed general-purpose
retrying library, written in Python, to simplify the task
of adding retry behavior to just about anything.
It originates from a fork of Retrying

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.


%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rf %oname.egg-info
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif


%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif


%files
%doc README.rst LICENSE AUTHORS ChangeLog
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Thu May 25 2017 Alexey Shabalin <shaba@altlinux.ru> 4.1.0-alt1
- initial build

