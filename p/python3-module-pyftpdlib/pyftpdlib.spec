%define oname pyftpdlib
%define descr \
Python FTP server library provides a high-level portable interface to easily \
write asynchronous FTP servers with Python. pyftpdlib is currently the most \
complete RFC-959 FTP server implementation available for Python programming \
language.

%def_with docs

Name: python3-module-%oname
Version: 1.5.8
Release: alt1

Summary: Python FTP server library
Summary(ru_RU.UTF-8): Модуль Python FTP-сервера

Group: Development/Python3
License: MIT and BSD
Url: https://github.com/giampaolo/pyftpdlib

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with docs
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx python3-module-sphinx_rtd_theme
%endif

BuildArch: noarch

%py3_provides %oname
%py3_requires sendfile

%description -l ru_RU.UTF-8
Модуль Python FTP-сервера беспечивает портативный высокоуровневый интерфейс
для лёгкого написания асинхронного FTP сервера на Python. pyftpdlib сейчас --
наиболее полная реализация RFC-959 FTP-сервера для Python.

%description
%descr

%package tests
Summary: Documentation for %oname
Group: Development/Python3
%py3_requires %oname

%description tests
%descr

This package contains tests for %oname.

%if_with docs
%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
%descr

This package contains documentation for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
%descr

This package contains pickles for %oname.
%endif

%prep
%setup

sed -i -e "s|^__ver__ = '[^']*'|__ver__ = '%version'|" pyftpdlib/__init__.py

%if_with docs
%prepare_sphinx3 .
ln -s ../objects.inv docs/
%endif

%build
%pyproject_build

%if_with docs
export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs pickle
%make -C docs html
%make -C docs man
%endif

%install
%pyproject_install

%if_with docs
mkdir -p %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname
mkdir -p %buildroot%_man1dir
cp -fR docs/_build/man/* %buildroot%_man1dir
%endif

%files
%doc CREDITS LICENSE *.rst demo/
%_bindir/*
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/%oname/test
%if_with docs
%_man1dir/*
%exclude %python3_sitelibdir/%oname/pickle
%endif

%files tests
%python3_sitelibdir/%oname/test
%exclude %python3_sitelibdir/%oname/test/README

%if_with docs
%files docs
%doc docs/_build/html/*

%files pickles
%python3_sitelibdir/%oname/pickle
%endif

%changelog
* Mon Oct 02 2023 Grigory Ustinov <grenka@altlinux.org> 1.5.8-alt1
- Automatically updated to 1.5.8.

* Wed May 17 2023 Grigory Ustinov <grenka@altlinux.org> 1.5.7-alt1
- Automatically updated to 1.5.7.

* Tue Aug 25 2020 Grigory Ustinov <grenka@altlinux.org> 1.5.6-alt2
- Fix obsoletes tag.

* Thu Feb 27 2020 Grigory Ustinov <grenka@altlinux.org> 1.5.6-alt1
- Build new version.
- Remove python2 support.
- Add docs knob.
- Build with man page.
- Fix license.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 1.5.5-alt1
- Build new version.

* Mon Sep 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.4-alt3
- Updated runtime dependencies.

* Wed Aug 08 2018 Grigory Ustinov <grenka@altlinux.org> 1.5.4-alt2
- Rebuild with resolving file conflict between modules.

* Wed May 30 2018 Grigory Ustinov <grenka@altlinux.org> 1.5.4-alt1
- Build new version.

* Fri Mar 30 2018 Grigory Ustinov <grenka@altlinux.org> 1.5.2-alt2
- Transfer package to subst-packaging system.

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
