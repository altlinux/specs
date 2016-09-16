%global pypi_name parallax

%def_with python3

Name: python-module-%pypi_name
Version: 1.0.1
Release: alt1
Summary: Execute commands and copy files over SSH to multiple machines at once

Group: Development/Python
License: ASL 2.0
URL: https://launchpad.net/pycadf
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr
BuildRequires: python-module-sphinx >= 1.1.2
BuildRequires: python-module-oslosphinx >= 2.5.0
BuildRequires: python-module-oslo.config >= 2.1.0
BuildRequires: python-module-oslo.serialization >= 1.4.0
BuildRequires: python-module-pytz
BuildRequires: python-module-six >= 1.9.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-sphinx >= 1.1.2
BuildRequires: python3-module-oslosphinx >= 2.5.0
BuildRequires: python3-module-oslo.config >= 2.1.0
BuildRequires: python3-module-oslo.serialization >= 1.4.0
BuildRequires: python3-module-pytz
BuildRequires: python3-module-six >= 1.9.0
%endif

%description
Execute commands and copy files over SSH to multiple machines at once.

%if_with python3
%package -n python3-module-%pypi_name
Summary: Execute commands and copy files over SSH to multiple machines at once
Group: Development/Python3

%description -n python3-module-%pypi_name
Execute commands and copy files over SSH to multiple machines at once.
%endif


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
mv %buildroot%_bindir/parallax-askpass %buildroot%_bindir/python3-parallax-askpass
popd
%endif
%python_install

%files
%doc README.md COPYING
%_bindir/parallax-askpass
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%pypi_name
%_bindir/python3-parallax-askpass
%python3_sitelibdir/*
%endif

%changelog
* Mon Sep 19 2016 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt1
- initial build
