%define modulename pylxd

Name: python-module-%modulename
Version: 2.2.10
Release: alt1

%setup_python_module %modulename

Summary: Python library for interacting with the LXD REST API.
License: Apache 2.0
Group: Development/Python
BuildRequires(Pre): python3-devel rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-requests-unixsocket >= 0.1.5
BuildRequires: python3-module-pbr
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-six
BuildRequires: python3-module-ws4py
BuildRequires: python3-module-requests
BuildRequires: python3-module-cryptography


Url: https://github.com/lxc/pylxd
Packager: Denis Pynkin <dans@altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

%description
A Python library for interacting with the LXD REST API.

%package -n python3-module-%modulename
Summary: Python library for interacting with the LXD REST API.
Group: Development/Python3

Requires: python3

%py3_provides %modulename

%description -n python3-module-%modulename
A Python library for interacting with the LXD REST API.

%prep
%setup

%build
export PBR_VERSION=%version
%python3_build

%install
export PBR_VERSION=%version
%python3_install
rm -rf -- %buildroot/%python3_sitelibdir/%modulename/deprecated/tests
rm -rf -- %buildroot/%python3_sitelibdir/%modulename/tests

%files -n python3-module-%modulename
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Tue Sep 24 2019 Anton Farygin <rider@altlinux.ru> 2.2.10-alt1
- 2.2.10
- removed python-2.7 support

* Mon Sep 26 2016 Denis Pynkin <dans@altlinux.org> 2.1-alt1
- Update

* Mon Aug 29 2016 Denis Pynkin <dans@altlinux.org> 2.0.4-alt0.git067340e8
- Initial version
