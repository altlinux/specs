%define sname senlinclient

Name: python3-module-%sname
Version: 1.11.0
Release: alt1
Source: %sname-%version.tar
Summary: OpenStack Clustering API Client Library
Group: Development/Tools
License: Apache-2.0
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-yaml
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstacksdk >= 0.24.0
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-oslotest
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-pip
BuildRequires: python3-module-heatclient
BuildRequires: python3-module-mock
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-testtools
BuildRequires: python3-module-tox
BuildRequires: python3-module-traceback2
BuildRequires: python3-module-virtualenv

%description
Python bindings to the Senlin Clustering API

%prep
%setup -n %sname-%version

%build
%python3_build

%install
%python3_install

%files
#%%_bindir/senlin
%python3_sitelibdir/*

%changelog
* Thu Oct 31 2019 Grigory Ustinov <grenka@altlinux.org> 1.11.0-alt1
- new version 1.11.0
- Build without python2.

* Fri Nov 11 2016 Lenar Shakirov <snejok@altlinux.ru> 1.0.0-alt1
- First build for ALT (bsed on ClearLinux)
