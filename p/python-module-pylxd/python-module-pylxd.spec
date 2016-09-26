%define modulename pylxd
%define devver dev27

%def_with python3

Name: python-module-%modulename
Version: 2.1
Release: alt1

%setup_python_module %modulename

Summary: Python library for interacting with the LXD REST API.
License: Apache 2.0
Group: Development/Python

Url: https://github.com/lxc/pylxd
Packager: Denis Pynkin <dans@altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

Requires: python
BuildRequires(Pre): python-devel rpm-build-python

BuildRequires: python-module-setuptools
BuildRequires: python-module-requests-unixsocket >= 0.1.5
BuildRequires: python-module-pbr
BuildRequires: python-module-dateutil
BuildRequires: python-module-six
BuildRequires: python-module-ws4py
BuildRequires: python-module-requests
BuildRequires: python-module-cryptography

%py_provides %modulename

%description
A Python library for interacting with the LXD REST API.

%if_with python3
%package -n python3-module-%modulename
Summary: Python library for interacting with the LXD REST API.
Group: Development/Python3

Requires: python3
BuildRequires(Pre): python3-devel rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-requests-unixsocket >= 0.1.5
BuildRequires: python3-module-pbr
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-six
BuildRequires: python3-module-ws4py
BuildRequires: python3-module-requests
BuildRequires: python3-module-cryptography

%py3_provides %modulename

%description -n python3-module-%modulename
A Python library for interacting with the LXD REST API.
%endif

%prep
%setup

%build
export PBR_VERSION=%version.%devver
%python_build

%if_with python3
%python3_build
%endif

%install
export PBR_VERSION=%version.%devver
%python_install

# Remove tests and deprecated parts
rm -rf -- %buildroot/%python_sitelibdir/%modulename/deprecated/tests
rm -rf -- %buildroot/%python_sitelibdir/%modulename/tests

%if_with python3
%python3_install
rm -rf -- %buildroot/%python3_sitelibdir/%modulename/deprecated/tests
rm -rf -- %buildroot/%python3_sitelibdir/%modulename/tests
%endif

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Mon Sep 26 2016 Denis Pynkin <dans@altlinux.org> 2.1-alt1
- Update

* Mon Aug 29 2016 Denis Pynkin <dans@altlinux.org> 2.0.4-alt0.git067340e8
- Initial version
