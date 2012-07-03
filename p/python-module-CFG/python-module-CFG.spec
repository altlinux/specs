%define version 0.0.9
%define release alt2

%setup_python_module CFG

Name: %packagename
Version: %version
Release: %release.1
License: GPL
Source0: python-CFG-%version.tar
Url: http://www.neural.ru/
Packager: Python Development Team <python at packages.altlinux.org>
BuildArch: noarch

Summary: Python module for use some configurations
Summary(ru_RU.UTF-8): Питоновкий модуль для работы с конфигурационными файами
Group: Development/Python

%description
Python module developed to work with configuration files

%prep
%setup -q -n python-CFG-%version

%install
mkdir -p %buildroot{%python_sitelibdir/%modulename,%_docdir/%packagename-%version}

cp -af CFG/*.py %buildroot/%python_sitelibdir/%modulename
cp -af doc/*.txt %buildroot/%_docdir/%packagename-%version
cp -af scripts/*.py %buildroot/%_docdir/%packagename-%version

%set_python_req_method strict

%files
%defattr(-, root, root)
%python_sitelibdir/%modulename
%_docdir/%packagename-%version

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.9-alt2.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.9-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.0.9-alt1.1
- Rebuilt with python-2.5.

* Fri May 04 2007 Ivan Fedorov <ns@altlinux.ru> 0.0.9-alt1
- 0.0.9
- spec rewritten

* Thu Mar 03 2005 Andrey Orlov <cray@altlinux.ru> 0.0.2-alt6
- Rebuild with python 2.4

* Mon Dec 27 2004 Andrey Orlov <cray@altlinux.ru> 0.0.2-alt5
- Fix descriptions

* Sun May 23 2004 Andrey Orlov <cray@altlinux.ru> 0.0.2-alt4
- Fix python policy compatibility

* Mon Feb 23 2004 Andrey Orlov <cray@altlinux.ru> 0.0.2-alt3
- Rebuild with python 23

* Mon Dec 01 2003 Andrey Orlov <cray@altlinux.ru> 0.0.2-alt1.23
- Check on PY23

* Wed Aug 27 2003 Andrey Orlov <cray@altlinux.ru> 0.0.1-alt1
- Initial release

