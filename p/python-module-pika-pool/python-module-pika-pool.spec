%define modulename pika-pool

%def_with python3

Name: python-module-%modulename
Version: 0.1.3
Release: alt1

%setup_python_module %modulename

Summary: Pika connection pooling
License: BSD
Group: Development/Python

Url: https://github.com/bninja/pika-pool
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: python-devel
BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
%summary

%package -n python3-module-%modulename
Summary: Pika connection pooling
Group: Development/Python3

%description -n python3-module-%modulename
%summary

%prep
%setup

%if_with python3
cp -fR . ../python3
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
%doc README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%modulename
%doc README.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 0.1.3-alt1
- initial build
