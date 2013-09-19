%define modulename pyftpdlib

Name: python-module-%modulename
Version: 1.2.0
Release: %branch_release alt1

%setup_python_module %modulename

Summary: Python FTP server library
Summary(ru_RU.UTF-8): Модуль Python FTP-сервера
License: %mit
Group: Development/Python

Url: http://code.google.com/p/pyftpdlib
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-branch
BuildPreReq: rpm-build-licenses
#BuildPreReq: %py_dependencies setuptools

%description
Python FTP server library provides a high-level portable interface to easily
write asynchronous FTP servers with Python. pyftpdlib is currently the most
complete RFC-959 FTP server implementation available for Python programming
language.

%description -l ru_RU.UTF-8
Модуль Python FTP-сервера беспечивает портативный высокоуровневый интерфейс
для лёгкого написания асинхронного FTP сервера на Python. pyftpdlib сейчас --
наиболее полная реализация RFC-959 FTP-сервера для Python.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc CREDITS HISTORY INSTALL LICENSE README demo/ test/
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Tue Sep 03 2013 Anatoly Kitaykin <cetus@altlinux.org> 1.2.0-alt1
- Release 1.2.0

* Tue Oct 30 2012 Anatoly Kitaykin <cetus@altlinux.org> 0.7.0-alt1
- Release 0.7.0

* Mon Nov 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1.1.1
- Rebuild with Python-2.7

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.1
- Rebuilt with python 2.6

* Fri Aug 21 2009 Aleksey Avdeev <solo@altlinux.ru> 0.5.1-alt1
- initial build
