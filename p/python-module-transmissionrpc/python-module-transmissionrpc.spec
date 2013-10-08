%define modulename transmissionrpc

Name: python-module-%modulename
Version: 0.10
Release: alt1

Summary: Python module that implements the Transmission bittorent client RPC protocol

Group: Development/Python
License: MIT license
Url: http://pypi.python.org/pypi/%modulename/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pypi.python.org/packages/source/t/%modulename/%modulename-%version.tar

BuildArch: noarch

%setup_python_module %modulename

BuildRequires: python-dev python-module-distribute python-module-six

%description
This is transmissionrpc. This module helps using Python to connect to a Transmission JSON-RPC service.
transmissionrpc is compatible with Transmission 1.31 and later.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/%modulename-%version-*.egg-info

%changelog
* Tue Oct 08 2013 Vitaly Lipatov <lav@altlinux.ru> 0.10-alt1
- initial build for ALT Linux Sisyphus
