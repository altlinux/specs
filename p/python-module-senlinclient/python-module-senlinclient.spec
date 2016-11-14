%def_with python3

Name: python-module-senlinclient
Version: 1.0.0
Release: alt1
Source: %name-%version.tar
Summary: OpenStack Clustering API Client Library
Group: Development/Tools
License: Apache-2.0
BuildArch: noarch

BuildRequires: python-module-yaml python-module-sphinx python-module-openstacksdk
BuildRequires: python-module-oslosphinx python-module-oslotest python-module-pbr
BuildRequires: python-module-pip python-module-heatclient python-module-mock
BuildRequires: python-module-requests python-module-setuptools python-module-six
BuildRequires: python-module-testtools python-module-tox python-module-traceback2
BuildRequires: python-module-virtualenv

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-yaml python3-module-sphinx python3-module-openstacksdk
BuildRequires: python3-module-oslosphinx python3-module-oslotest python3-module-pbr
BuildRequires: python3-module-pip python3-module-heatclient python3-module-mock
BuildRequires: python3-module-requests python3-module-setuptools python3-module-six
BuildRequires: python3-module-testtools python3-module-tox python3-module-traceback2
BuildRequires: python3-module-virtualenv
%endif

%if_with python3
%package -n python3-module-senlinclient
Summary: OpenStack Clustering API Client Library
Group: Development/Tools

%description -n python3-module-senlinclient
Python bindings to the Senlin Clustering API
============================================
%endif

%description
Python bindings to the Senlin Clustering API
============================================

%prep
%setup

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
%if_with python3
pushd ../python3
%python3_install
mv %buildroot%_bindir/senlin %buildroot%_bindir/senlin.py3
popd
%endif

%python_install

%files
%_bindir/senlin
%python_sitelibdir/*

%if_with python3
%files -n python3-module-senlinclient
%_bindir/senlin.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Nov 11 2016 Lenar Shakirov <snejok@altlinux.ru> 1.0.0-alt1
- First build for ALT (based on ClearLinux)

