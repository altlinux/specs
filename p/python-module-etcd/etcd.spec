%define unpackaged_files_terminate_build 1

%define mname etcd
#temporarily skip tests https://github.com/jplana/python-etcd/issues/251
%def_disable check

Name: python-module-%mname
Version: 0.4.5
Release: alt1%ubt
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
#for tests
BuildRequires: pytest
BuildRequires: python-module-pytest-runner
BuildRequires: pytest3
BuildRequires: python3-module-pytest-runner
#
BuildRequires: python-module-dns
BuildRequires: python3-module-dns
BuildRequires: python-module-nose
BuildRequires: python3-module-nose
BuildRequires: etcd

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
python -m pytest --verbose
pushd ../python3
python3 -m pytest --verbose
popd

%files
%python_sitelibdir/*

%files -n python3-module-%mname
%python3_sitelibdir/*

%changelog
* Thu Oct 26 2017 Stanislav Levin <slev@altlinux.org> 0.4.5-alt1%ubt
- Initial build

