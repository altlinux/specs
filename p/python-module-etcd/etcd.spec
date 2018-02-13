%define _unpackaged_files_terminate_build 1
%define mname etcd

%def_with check

Name: python-module-%mname
Version: 0.4.5
Release: alt3%ubt

Summary: A python client for Etcd https://github.com/coreos/etcd
Group: Development/Python
# Source-git: https://github.com/jplana/python-etcd.git
License: MIT
Url: https://pypi.python.org/pypi/python-etcd

BuildArch: noarch
%py_provides %mname

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3
BuildRequires: python-module-dns
BuildRequires: python3-module-dns
BuildRequires: etcd

%if_with check
BuildRequires: pytest
BuildRequires: python-module-nose
BuildRequires: python-module-pytest-cov
BuildRequires: python-module-pytest-runner
BuildRequires: python-module-urllib3
BuildRequires: python-module-mock
BuildRequires: pytest3
BuildRequires: python3-module-nose
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-runner
BuildRequires: python3-module-urllib3
BuildRequires: python3-module-mock
%endif

%description
Client library for interacting with an etcd service, providing Python
access to the full etcd REST API.  Includes authentication, accessing
and manipulating shared content, managing cluster members, and leader
election.

%package tests
Summary: Tests for %mname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %mname.

%package -n python3-module-%mname
Summary: %summary
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
Client library for interacting with an etcd service, providing Python
access to the full etcd REST API.  Includes authentication, accessing
and manipulating shared content, managing cluster members, and leader
election.

%package -n python3-module-%mname-tests
Summary: Tests for %mname
Group: Development/Python3
Requires:  python3-module-%mname = %EVR

%description -n python3-module-%mname-tests
This package contains tests for %mname.

%prep
%setup
%patch -p1
rm -rfv ../python3
cp -a . ../python3

%build
%python_build_debug
pushd ../python3
%python3_build_debug
popd

%install
%python_install
pushd ../python3
%python3_install
popd

%check
export PATH=$PATH:%_sbindir
#export ETCD_UNSUPPORTED_ARCH for etcd
%if %_arch == "i586"
export ETCD_UNSUPPORTED_ARCH=386
%endif
python -m pytest --cov=etcd --verbose
pushd ../python3
python3 -m pytest --cov=etcd --verbose
popd

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/%mname/tests

%files tests
%python_sitelibdir/%mname/tests

%files -n python3-module-%mname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%mname/tests

%files -n python3-module-%mname-tests
%python3_sitelibdir/%mname/tests

%changelog
* Tue Feb 13 2018 Stanislav Levin <slev@altlinux.org> 0.4.5-alt3%ubt
- Fix build time tests Requires
- Package tests

* Thu Nov 16 2017 Stanislav Levin <slev@altlinux.org> 0.4.5-alt2%ubt
- Add fixes from upstream
- Enable tests

* Thu Oct 26 2017 Stanislav Levin <slev@altlinux.org> 0.4.5-alt1%ubt
- Initial build

