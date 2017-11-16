%define _unpackaged_files_terminate_build 1

%define mname etcd

Name: python-module-%mname
Version: 0.4.5
Release: alt2%ubt
Summary: A python client for Etcd https://github.com/coreos/etcd

Group: Development/Python
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
#for tests
BuildRequires: pytest
BuildRequires: python-module-nose
BuildRequires: python-module-pytest-cov
BuildRequires: python-module-pytest-runner
BuildRequires: pytest3
BuildRequires: python3-module-nose
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-runner
#

%description
Client library for interacting with an etcd service, providing Python
access to the full etcd REST API.  Includes authentication, accessing
and manipulating shared content, managing cluster members, and leader
election.

%package -n python3-module-%mname
Summary: %summary
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
Client library for interacting with an etcd service, providing Python
access to the full etcd REST API.  Includes authentication, accessing
and manipulating shared content, managing cluster members, and leader
election.

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
#remove tests
rm -rfv %buildroot%python_sitelibdir/%mname/tests
rm -rfv %buildroot%python3_sitelibdir/%mname/tests

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

%files -n python3-module-%mname
%python3_sitelibdir/*

%changelog
* Thu Nov 16 2017 Stanislav Levin <slev@altlinux.org> 0.4.5-alt2%ubt
- Add fixes from upstream
- Enable tests

* Thu Oct 26 2017 Stanislav Levin <slev@altlinux.org> 0.4.5-alt1%ubt
- Initial build

