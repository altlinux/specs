%define modulename pyftpdlib

%def_with python3

Name: python-module-%modulename
Version: 1.5.2
Release: alt1

%setup_python_module %modulename

Summary: Python FTP server library
Summary(ru_RU.UTF-8): Модуль Python FTP-сервера
License: %mit
Group: Development/Python
BuildArch: noarch
Url: https://github.com/giampaolo/pyftpdlib

# https://github.com/giampaolo/pyftpdlib.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-branch rpm-build-licenses
BuildRequires: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%py_provides %modulename

%description
Python FTP server library provides a high-level portable interface to easily
write asynchronous FTP servers with Python. pyftpdlib is currently the most
complete RFC-959 FTP server implementation available for Python programming
language.

%description -l ru_RU.UTF-8
Модуль Python FTP-сервера беспечивает портативный высокоуровневый интерфейс
для лёгкого написания асинхронного FTP сервера на Python. pyftpdlib сейчас --
наиболее полная реализация RFC-959 FTP-сервера для Python.

%package pickles
Summary: Pickles for %modulename
Group: Development/Python

%description pickles
Python FTP server library provides a high-level portable interface to easily
write asynchronous FTP servers with Python. pyftpdlib is currently the most
complete RFC-959 FTP server implementation available for Python programming
language.

This package contains pickles for %modulename.

%package docs
Summary: Documentation for %modulename
Group: Development/Documentation
BuildArch: noarch

%description docs
Python FTP server library provides a high-level portable interface to easily
write asynchronous FTP servers with Python. pyftpdlib is currently the most
complete RFC-959 FTP server implementation available for Python programming
language.

This package contains documentation for %modulename.

%package tests
Summary: Documentation for %modulename
Group: Development/Python
%py_requires %modulename

%description tests
Python FTP server library provides a high-level portable interface to easily
write asynchronous FTP servers with Python. pyftpdlib is currently the most
complete RFC-959 FTP server implementation available for Python programming
language.

This package contains tests for %modulename.

%if_with python3
%package -n python3-module-%modulename
Summary: Python FTP server library
Group: Development/Python3
%py3_provides %modulename

%description -n python3-module-%modulename
Python FTP server library provides a high-level portable interface to easily
write asynchronous FTP servers with Python. pyftpdlib is currently the most
complete RFC-959 FTP server implementation available for Python programming
language.

%package -n python3-module-%modulename-tests
Summary: Documentation for %modulename
Group: Development/Python3
%py3_requires %modulename

%description -n python3-module-%modulename-tests
Python FTP server library provides a high-level portable interface to easily
write asynchronous FTP servers with Python. pyftpdlib is currently the most
complete RFC-959 FTP server implementation available for Python programming
language.

This package contains tests for %modulename.
%endif

%prep
%setup

# correct version
sed -i -e "s|^__ver__ = '[^']*'|__ver__ = '%version'|" pyftpdlib/__init__.py

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%modulename/

%files
%doc CREDITS LICENSE *.rst demo/
%python_sitelibdir/%modulename/
%python_sitelibdir/%modulename-%version-py2*.egg-info
%exclude %python_sitelibdir/%modulename/pickle
%exclude %python_sitelibdir/%modulename/test

%files tests
%python_sitelibdir/%modulename/test
%exclude %python_sitelibdir/%modulename/test/README

%files pickles
%python_sitelibdir/%modulename/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%modulename
%doc CREDITS LICENSE *.rst demo/
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%modulename-%version-py3*.egg-info
%exclude %python3_sitelibdir/%modulename/test

%files -n python3-module-%modulename-tests
%python3_sitelibdir/%modulename/test
%exclude %python3_sitelibdir/%modulename/test/README
%endif

%changelog
* Thu Nov 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.2-alt1
- Updated to upstream version 1.5.2.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1
- Version 1.4.0
- Added module for Python 3

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
