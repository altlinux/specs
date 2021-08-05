# -*- mode: rpm-spec; coding: utf-8 -*-
%define oname serial

%def_without doc_package
%def_without jython

Name: python3-module-%oname
Version: 3.5
Release: alt2
Summary: Serial port access for python
Summary(ru_RU.UTF-8): Доступ к последовательному порту из python
# https://github.com/pyserial/pyserial
Source: %name-%version.tar
License: Python
Group: Development/Python3
Prefix: %_prefix
Url: https://github.com/pyserial/pyserial
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
%add_python3_req_skip System clr

Conflicts: python-module-%oname
Obsoletes: python-module-%oname

%description
pyserial capsulates the access for the serial port. It provides
backends for standard Python running on Windows, Linux, BSD (possibly
any POSIX compilant system) and Jython. The module automaticaly
selects the appropriate backend.

This module contains POSIX compatible serial port access.
It's built for python %_python_version

%description -l ru_RU.UTF-8
С помощью модулей pyserial можно работать с последовательным портом в
стандартном Python, запущенном на Windows, Linux, BSD (возможно, любой
POSIX-совместимой системе) или Jython. Модуль автоматически выбирает
подходящий для данной системы механизм доступа.

Этот модуль содержит методы доступа к последовательному порту, пригодные
для POSIX-совместимых систем.
Он собран для Python версии %_python_version

%if_with jython
%package jython
Summary: Jython compatible serial port access
Group: Development/Python3

%description jython
This module capsulates the access for the serial port. It provides
backends for standard Python running on Windows, Linux, BSD (possibly
any POSIX compilant system) and Jython. The module automaticaly
selects the appropriate backend.

This module contains Jython compatible serial port access.
It's built for python %__python_version
%endif

%prep
%setup

%build
echo "*** Creating package %name ***"
%python3_build

%install
%python3_build_install --optimize=2

%files
%doc CHANGES.rst README.rst LICENSE.txt
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/serial/*java.py*
%exclude %python3_sitelibdir/serial/__pycache__/*java.*
%exclude %python3_sitelibdir/serial/*win32.py*
%exclude %python3_sitelibdir/serial/__pycache__/*win32.*
%exclude %python3_sitelibdir/serial/tools/*windows.py*
%exclude %python3_sitelibdir/serial/tools/__pycache__/*windows.*
%exclude %python3_sitelibdir/serial/serialcli.py*
%exclude %python3_sitelibdir/serial/__pycache__/serialcli.*
%doc examples

%if_with jython
%files jython
%python3_sitelibdir/serial/*java.py*
%endif

%changelog
* Thu Aug 05 2021 Grigory Ustinov <grenka@altlinux.org> 3.5-alt2
- Drop python2 support.

* Thu Feb 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.5-alt1
- 3.5 released

* Fri Oct 20 2017 Anton Midyukov <antohami@altlinux.org> 3.4-alt1
- New version 3.4

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.7-alt1.svn20140804.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.7-alt1.svn20140804.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt1.svn20140804
- New snapshot

* Wed Dec 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt1.svn20131120
- Version 2.7

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt1.pre1.svn20120816
- New snapshot

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 2.7-alt1.pre1.svn20120412.1
- Rebuild with Python-3.3

* Mon Jun 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt1.pre1.svn20120412
- Version 2.7-pre1
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5-alt1.1
- Rebuild with Python-2.7

* Mon Aug 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1
- Version 2.5 (ALT #22489)

* Sat Aug 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt3.1.2
- Rebuilt with python 2.6
- Set as noarch package

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2.1-alt3.1.1
- Rebuilt with python-2.5.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.1-alt3.1
- Rebuilt using rpm-build-python-0.29-alt4.

* Mon Nov 14 2005 Igor Zubkov <icesik@altlinux.ru> 2.1-alt3
- jython subpackage is optional and off by default

* Mon Nov 07 2005 Igor Zubkov <icesik@altlinux.ru> 2.1-alt2
- bump release

* Tue Aug 31 2004 Alexey Morozov <morozov@altlinux.org> 2.1-alt1
- new version (2.1)
- separate doc package is optional now (docs put into the main package
  by default)
- win32 package is optional and off by default

* Mon May 31 2004 Alexey Morozov <morozov@altlinux.org> 2.0-alt3
- Examples are splitted into a separate package

* Tue Apr 20 2004 Alexey Morozov <morozov@altlinux.org> 2.0-alt2
- New build scheme first try

* Wed Jan 14 2004 Alexey Morozov <morozov@altlinux.org> 2.0-alt1
- Initial build for ALT Linux
