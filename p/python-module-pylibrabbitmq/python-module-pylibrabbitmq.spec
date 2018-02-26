%define module_name pylibrabbitmq

Name: python-module-%module_name
Version: 0.5.0
Release: alt1
Group: System/Base
License: GPLv2
Summary: Experimental Python bindings to the RabbitMQ C-library librabbitmq
URL: https://github.com/ask/pylibrabbitmq.git
Packager: Viacheslav Dubrovskyi <dubrsl@altlinux.org>
Source: %name-%version.tar

BuildRequires: python-module-distribute rabbitmq-server-devel librabbitmq-c-devel

%description
Experimental Python bindings to the RabbitMQ C-library librabbitmq

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc AUTHORS Changelog LICENSE-GPL-2.0 LICENSE-MPL-RabbitMQ README.rst TODO
%python_sitelibdir/pylibrabbitmq*
%python_sitelibdir/_pyrabbitmq*

%changelog
* Fri May 04 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.5.0-alt1
- build for ALT
