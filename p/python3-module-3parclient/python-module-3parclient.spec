%define oname 3parclient

%def_without tests

Name:       python3-module-%oname
Version:    4.2.2
Release:    alt3

Summary:    HPE 3PAR REST Python Client
License:    Apache License, Version 2.0
Group:      Development/Python3
Url:        https://pypi.python.org/pypi/python-3parclient

BuildArch:  noarch

Source0:    %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
This is a Client library that can talk to the HPE 3PAR Storage array.
The 3PAR storage array has a REST web service interface and a command
line interface. This client library implements a simple interface
for talking with either interface, as needed. The python Requests
library is used to communicate with the REST interface.
The python paramiko library is used to communicate with
the command line interface over an SSH connection.

The HP 3PAR Rest Client (hp3parclient) is now considered deprecated.

%if_with tests
%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description tests
This is a Client library that can talk to the HPE 3PAR Storage array.
The 3PAR storage array has a REST web service interface and a command
line interface. This client library implements a simple interface
for talking with either interface, as needed. The python Requests
library is used to communicate with the REST interface.
The python paramiko library is used to communicate with
the command line interface over an SSH connection.

This package contains tests for %oname.
%endif

%prep
%setup

%build
%python3_build

%install
%python3_install

mv %buildroot%python3_sitelibdir/test/ \
   %buildroot%python3_sitelibdir/hpe%{oname}/test/

%files
%doc README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/hpe%{oname}/test/

%if_with tests
%files tests
%python3_sitelibdir/hpe%{oname}/test/
%endif


%changelog
* Fri Jan 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.2.2-alt3
- Build for python2 disabled.

* Mon Oct 02 2017 Lenar Shakirov <snejok@altlinux.ru> 4.2.2-alt2
- Remove "test" dir from sources (ALT bug: 33948)

* Tue Nov 29 2016 Lenar Shakirov <snejok@altlinux.ru> 4.2.2-alt1
- Initial build for ALT

