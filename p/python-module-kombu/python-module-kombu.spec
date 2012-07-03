%define module_name kombu

Name: python-module-%module_name
Version: 2.1.7
Release: alt1
Group: System/Base
License: BSD License
Summary: Kombu is an AMQP messaging framework for Python
URL: http://github.com/ask/kombu/
Packager: Viacheslav Dubrovskyi <dubrsl@altlinux.org>
Source: %name-%version.tar

BuildRequires: python-module-distribute

%description
AMQP is the Advanced Message Queuing Protocol, an open standard protocol
for message orientation, queuing, routing, reliability and security.

One of the most popular implementations of AMQP is `RabbitMQ`_.

The aim of `Kombu` is to make messaging in Python as easy as possible by
providing an idiomatic high-level interface for the AMQP protocol, and also
provide proven and tested solutions to common messaging problems.

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

%files
%doc AUTHORS Changelog FAQ LICENSE README.rst THANKS TODO
%python_sitelibdir/kombu*

%changelog
* Fri May 04 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.1.7-alt1
- build for ALT
