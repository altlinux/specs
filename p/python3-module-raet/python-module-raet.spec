%define oname raet

Name: python3-module-%oname
Version: 0.6.5.git.f2a25d18
Release: alt2

Summary: RAET (Reliable Asynchronous Event Transport) Protocol
License: ASL 2.0
Group: Development/Python3
Url: https://github.com/saltstack/raet
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setupdocs


%description
Modern large scale distributed application architectures, wherein
components are distributed across the internet on multiple hosts
and multiple CPU cores, are often based on a messaging or event bus
that allows the various distributed components to communicate
asynchronously with each other. Typically the messaging bus is some
form of messaging queue service such as AMQP or ZeroMQ. The message
bus supports what is commonly referred to as a publish/subscribe
methodology for information exchange.

%package tests
Summary: Flow Based Programming Automated Reasoning Engine and Automation Operation System
Group: Development/Python3

%description tests
Test files for %oname

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python3_build


%install
%python3_install

%files
%doc README.md LICENSE ChangeLog.md
%_bindir/%{oname}flo
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/test
%exclude %python3_sitelibdir/%oname/*/test


%files tests
%python3_sitelibdir/%oname/test
%python3_sitelibdir/%oname/*/test


%changelog
* Wed Jan 15 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.6.5.git.f2a25d18-alt2
- porting on python3

* Wed Nov 30 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 0.6.5.git.f2a25d18-alt1
- New version

* Tue Apr 28 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 0.6.1-alt2
- New version

* Sat Feb 14 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 0.5.3-alt2
- Add subpackage tests

* Thu Feb 12 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 0.5.3-alt1
- Initial build for ALT

