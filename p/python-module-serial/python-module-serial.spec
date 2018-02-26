# -*- mode: rpm-spec; coding: utf-8 -*-
%define version 2.7
%define release alt1.pre1.svn20120412
%define source_version 2.7
%define source_name pyserial
%define oname serial
%setup_python_module %oname

%def_without doc_package
%def_without win32
%def_without jython
%def_with python3

Version: %version
Release: %release

Summary: Serial port access for python
Summary(ru_RU.UTF-8): Доступ к последовательному порту из python
Name: %packagename
Source: %source_name-%source_version.tar
License: Python
Group: Development/Python
Prefix: %_prefix
Url: http://pyserial.sf.net
BuildArch: noarch

Provides: %{__python_module_prefix}-pyserial
Obsoletes: %{__python_module_prefix}-pyserial

%add_python_req_skip System clr
%if_without doc_package
Provides: %{__python_module_prefix}-pyserial-doc
Obsoletes: %{__python_module_prefix}-pyserial-doc
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

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

%if_with python3
%package -n python3-module-%oname
Summary: Serial port access for python 3
Group: Development/Python3
%add_python3_req_skip System clr

%description -n python3-module-%oname
pyserial capsulates the access for the serial port. It provides
backends for standard Python running on Windows, Linux, BSD (possibly
any POSIX compilant system) and Jython. The module automaticaly
selects the appropriate backend.

This module contains POSIX compatible serial port access.
It's built for python %_python_version
%endif

%if_with jython
%package jython
Summary: Jython compatible serial port access
Group: Development/Python

%description jython
This module capsulates the access for the serial port. It provides
backends for standard Python running on Windows, Linux, BSD (possibly
any POSIX compilant system) and Jython. The module automaticaly
selects the appropriate backend.

This module contains Jython compatible serial port access.
It's built for python %__python_version
%endif

# Do we really need this?
%if_with win32
%package win32
Summary: Win32-specific serial port access
Group: Development/Python
AutoReqProv: yes, python

%description win32
This module capsulates the access for the serial port. It provides
backends for standard Python running on Windows, Linux, BSD (possibly
any POSIX compilant system) and Jython. The module automaticaly
selects the appropriate backend.

This module contains Win32-specific serial port access.
It's built for python %__python_version
%endif

%if_with doc_package
%package -n python-%modulename-doc
Summary: %modulename documentation and example programs
Summary(ru_RU.UTF-8): Документация по API и примеры программ для %modulename
Group: Development/Python
Prefix: %_prefix
Requires: python-%modulename = %version

%description -n  python-%modulename-doc
%modulename provides portable way to access serial ports in various
systems. Install python-%modulename-doc if you need API documentation
and examples for this module

%description -n  python-%modulename-doc -l ru_RU.UTF-8
%modulename предоставляет унифицированный доступ к последовательному
порту в разных системах. Установите python-%modulename-doc, если Вам
требуется документация по API и примеры программирования с
использованием данного модуля.
%endif

%prep
%setup -n %source_name-%source_version
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
echo "*** Creating package %name ***"
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_build_install --optimize=2
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ${i}3
done
popd
%endif

%python_build_install --optimize=2 \
		--record=INSTALLED_FILES

grep java INSTALLED_FILES > JAVA_INSTALLED_FILES
subst '/java/d' INSTALLED_FILES
grep win32 INSTALLED_FILES > WIN32_INSTALLED_FILES
subst '/win32/d' INSTALLED_FILES

%files -f INSTALLED_FILES
%doc CHANGES.txt README.txt
%if_with python3
%exclude %_bindir/*3
%endif
%python_sitelibdir_noarch/serial/serialcli.py

%if_with doc_package
%files -n python-%modulename-doc
%endif
%doc examples

%if_with jython
%files jython -f JAVA_INSTALLED_FILES
%endif

%if_with win32
%files win32 -f WIN32_INSTALLED_FILES
%endif

%if_with python3
%files -n python3-module-%oname
%doc CHANGES.txt README.txt
%_bindir/*3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/serial/serialjava.py*
%exclude %python3_sitelibdir/serial/__pycache__/serialjava.*
%exclude %python3_sitelibdir/serial/serialwin32.py*
%exclude %python3_sitelibdir/serial/__pycache__/serialwin32.*
%exclude %python3_sitelibdir/serial/win32.py*
%exclude %python3_sitelibdir/serial/__pycache__/win32.*
%endif

%changelog
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
