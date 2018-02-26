# -*- coding: utf-8 -*-
Name: python-module-sqlanydb
Version: 1.0.2
Release: alt1.1
Epoch: 1
License: Apache
BuildArch: noarch
Packager: Alexey Morsov <swi@altlinux.ru>
Group: Databases
Summary: Python interface for Sybase Anywhere DB
Summary(ru_RU.UTF-8): Интерфейс к БД Sybase Anywhere для Python

Url: http://code.google.com/p/sqlanydb/

Source: %name-%version.tar

Requires: python >= 2.4
Requires: libfreetds >= 0.64
Requires: python-module-egenix-mx-base

BuildPreReq: python-module-setuptools

%description
This a Google Code project providing a python interface to the
SQL Anywhere Database. This interface conforms to PEP 249.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=%buildroot --optimize=2

%files
%doc
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:1.0.2-alt1.1
- Rebuild with Python-2.7

* Sat Dec 18 2010 Alexey Morsov <swi@altlinux.ru> 1:1.0.2-alt1
- initial build for Sisyphus


