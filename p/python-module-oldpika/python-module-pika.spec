%define modulename pika

Name: python-module-old%modulename
Version: 0.5.2
Release: alt1

%setup_python_module old%modulename

Summary: Pika is a pure-Python implementation of the AMQP 0-9-1 protocol.
License: GPLv2.0
Group: Development/Python

Url: http://github.com/pika/pika
BuildArch: noarch

Source: %name-%version.tar

BuildPreReq: %py_dependencies setuptools
BuildPreReq: python-module-sphinx-devel

%py_provides old%modulename

%description
Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that
tries to stay fairly independent of the underlying network support
library.

%prep
%setup

%build
%python_build

%install
%python_install

mv %buildroot%python_sitelibdir/%modulename \
	%buildroot%python_sitelibdir/old%modulename

%files
%doc *.md
%python_sitelibdir/old%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1
- Initial build for Sisyphus

