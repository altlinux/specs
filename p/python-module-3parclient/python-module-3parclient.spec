%def_with python3

Name: python-module-3parclient
Version: 4.2.2
Release: alt1
Summary: HPE 3PAR REST Python Client

Group: Development/Python
License: Apache License, Version 2.0
Url: https://pypi.python.org/pypi/python-3parclient
Source0: %name-%version.tar


BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
%endif

%description
This is a Client library that can talk to the HPE 3PAR Storage array.
The 3PAR storage array has a REST web service interface and a command
line interface. This client library implements a simple interface
for talking with either interface, as needed. The python Requests
library is used to communicate with the REST interface.
The python paramiko library is used to communicate with
the command line interface over an SSH connection.

The HP 3PAR Rest Client (hp3parclient) is now considered deprecated.

%if_with python3
%package -n python3-module-3parclient
Summary: HPE 3PAR REST Python Client
Group: Development/Python3

%description -n python3-module-3parclient
This is a Client library that can talk to the HPE 3PAR Storage array.
The 3PAR storage array has a REST web service interface and a command
line interface. This client library implements a simple interface
for talking with either interface, as needed. The python Requests
library is used to communicate with the REST interface.
The python paramiko library is used to communicate with
the command line interface over an SSH connection.

The HP 3PAR Rest Client (hp3parclient) is now considered deprecated.
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
%files -n python3-module-3parclient
%doc README.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Nov 29 2016 Lenar Shakirov <snejok@altlinux.ru> 4.2.2-alt1
- Initial build for ALT

