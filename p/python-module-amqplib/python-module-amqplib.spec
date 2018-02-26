%define module_name amqplib

Name: python-module-%module_name
Version: 1.0.2
Release: alt1
Group: System/Base
License: GPLv2
Summary: Python AMQP (Advanced Message Queuing Protocol) Client library
URL: http://code.google.com/p/py-amqplib/
Packager: Viacheslav Dubrovskyi <dubrsl@altlinux.org>
Source: %module_name-%version.tgz

BuildRequires: python-module-distribute

%description
Python AMQP (Advanced Message Queuing Protocol) Client library

%prep
%setup -n %module_name-%version

%build
%python_build

%install
%python_install

%ifarch x86_64
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

%files
%doc CHANGES LICENSE README TODO
%python_sitelibdir/amqplib*

%changelog
* Fri May 04 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.2-alt1
- build for ALT
