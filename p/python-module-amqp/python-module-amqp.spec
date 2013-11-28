%define module_name amqp

Name: python-module-%module_name
Version: 1.0.11
Release: alt1.1
Group: System/Base
License: GPLv2
Summary: fork of amqplib used by Kombu containing additional features and improvements
URL: http://github.com/celery/py-amqp.git
Packager: Viacheslav Dubrovskyi <dubrsl@altlinux.org>
Source: %name-%version.tar

BuildRequires: python-module-setuptools-tests

%description
This is a fork of amqplib_ which was originally written by Barry Pederson.
It is maintained by the Celery_ project, and used by kombu as a pure python
alternative when librabbitmq is not available.

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
%doc AUTHORS Changelog LICENSE README.rst
%python_sitelibdir/*

%changelog
* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.11-alt1.1
- Fixed build

* Sat Apr 13 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.11-alt1
- build for ALT
