%define modulename pika

Name: python-module-%modulename
Version: 0.9.5
Release: alt1.git20120106

%setup_python_module %modulename

Summary: Pika is a pure-Python implementation of the AMQP 0-9-1 protocol.
License: GPL
Group: Development/Python

Url: http://github.com/pika/pika
Packager: Alexey Morsov <swi@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

BuildPreReq: %py_dependencies setuptools

%description
Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that
tries to stay fairly independent of the underlying network support library.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Tue Jan 17 2012 Alexey Morsov <swi@altlinux.ru> 0.9.5-alt1.git20120106
- initial build

