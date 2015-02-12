%define oname raet
%def_without python3

Summary: RAET (Reliable Asynchronous Event Transport) Protocol
Name: python-module-%oname
Version: 0.5.3
Release: alt1
Url: https://github.com/saltstack/raet
Source: %name-%version.tar
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
License: ASL 2.0
Group: Development/Python

BuildArch: noarch
BuildRequires: python-dev python-module-setupdocs python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setupdocs python3-module-setuptools
%endif

%description
Modern large scale distributed application architectures, wherein
components are distributed across the internet on multiple hosts
and multiple CPU cores, are often based on a messaging or event bus
that allows the various distributed components to communicate
asynchronously with each other. Typically the messaging bus is some
form of messaging queue service such as AMQP or ZeroMQ. The message
bus supports what is commonly referred to as a publish/subscribe
methodology for information exchange.

%package -n python3-module-%oname
Summary: Flow Based Programming Automated Reasoning Engine and Automation Operation System
Group: Development/Python3

%description -n python3-module-%oname
Modern large scale distributed application architectures, wherein
components are distributed across the internet on multiple hosts
and multiple CPU cores, are often based on a messaging or event bus
that allows the various distributed components to communicate
asynchronously with each other. Typically the messaging bus is some
form of messaging queue service such as AMQP or ZeroMQ. The message
bus supports what is commonly referred to as a publish/subscribe
methodology for information exchange.


%prep
%setup

%if_with python3
cp -fR . ../python3
%endif


%build
%add_optflags -fno-strict-aliasing
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif


%install
%python_build_install --prefix=/usr

%if_with python3
pushd ../python3
%python3_install
popd
%endif



%files
%doc README.md LICENSE ChangeLog.md
%python_sitelibdir/*
%_bindir/raetflo

%if_with python3
%files -n python3-module-%oname
%doc README.md LICENSE ChangeLog.md
%python3_sitelibdir/*
%_bindir/raetflo
%endif


%changelog
* Thu Feb 12 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 0.5.3-alt1
- Initial build for ALT

