BuildRequires(pre): rpm-build-python3
%define oldname python-module-amqplib
%define module_name amqplib

Name: python3-module-%module_name
Version: 1.0.2
Release: alt1
Group: System/Base
License: GPLv2
Summary: Python AMQP (Advanced Message Queuing Protocol) Client library
URL: http://code.google.com/p/py-amqplib/
Packager: Viacheslav Dubrovskyi <dubrsl@altlinux.org>
Source: %module_name-%version.tgz

BuildRequires: python3-module-distribute

%description
Python AMQP (Advanced Message Queuing Protocol) Client library

%prep
%setup -n %module_name-%version

%build
%python3_build

%install
%python3_install

%ifarch x86_64
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

%files
%doc CHANGES LICENSE README TODO
%python3_sitelibdir/amqplib*

%changelog
* Thu May 23 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1
- python3 copycat test run

