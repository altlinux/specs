%define oname comedilib
Name: libcomedi
Version: 0.8.1
Release: alt2.2.1

Summary: Data Acquisition library for the Comedi DAQ driver
Summary(ru_RU.KOI8-R): Библиотека получения данных для драйвера Comedi DAQ.

License: LGPL
Group: Development/Other
Url: http://www.comedi.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.comedi.org/download/%oname-%version.tar.bz2
Source1: http://www.comedi.org/download/comedi_examples.tar.gz
Patch: %name-as-needed.patch

# manually removed: hostinfo eric gcc-g77
# Automatically added by buildreq on Sun Nov 07 2004
BuildRequires: docbook-utils-print flex gcc-c++ libstdc++-devel python-devel python-modules-encodings swig

%description
The Linux Control and Measurement Device Interface Library.
Comedilib is the library for the Comedi data acquisition driver
for Linux.  It allows Linux processes to acquire data from
supported DAQ cards, such as those from National Instruments.

%description -l ru_RU.KOI8-R
Comedilib -- это библиотека для драйвера получения данных Comedi под Linux.
Она позволяет пользовательским процессам получать данные от поддерживаемых
карт DAQ, например, производимых National Instruments.

%package devel
Summary: The files needed for %name application development
Summary(ru_RU.KOI8-R): Файлы, требующиеся для разработки приложений с использованием %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains the necessary include files
for developing applications with %name

%description devel -l ru_RU.KOI8-R
Пакет %name-devel содержит необходимые заголовочные файлы
для разработки приложений, которые используют %name.

%package -n python-module-comedi
Summary: Python interface for %name
Group: Development/Python
Requires: %name = %version-%release
Provides: %name-python
Obsoletes: %name-python
%setup_python_module comedi

%description -n python-module-comedi
Python interface for %name

%package devel-static
Summary: Static library for %name application development
Summary(ru_RU.KOI8-R): Статическая библиотека для разработки приложений с использованием %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
The %name-devel-static package contains the static library
for developing applications with %name
%description devel-static -l ru_RU.KOI8-R
Пакет %name-devel-static содержит статическую библиотеку
для разработки приложений, которые используют %name.

%prep
%setup -q -n comedilib-%version
%patch
# unpack examples
#tar xfz %SOURCE1
#%__subst 's|comedi_data_read_n|comedi_data_read_n_obsolete|' ./comedi_examples/monitor/sv.c
#%__subst 's|demo doc|demo|' Makefile.in

%build
%autoreconf
%configure --localstatedir=%buildroot%_localstatedir --disable-ruby-binding
%make_build
#cd comedi_examples/monitor
#	make
#cd -

%install
%makeinstall_std
#install -d %buildroot%_datadir/%name/examples
#install -s -D -m 755 comedi_examples/monitor/monitor %buildroot%_bindir/comedi_monitor
#mv %buildroot%_datadir/comedilib %buildroot%_datadir/%name

#cd comedi_examples
#cp --target-directory %buildroot%_datadir/%name/examples/$i * -R
#cd -
#install -d %buildroot%_datadir/%name/demo/perl
#cd demo
#cp --target-directory %buildroot%_datadir/%name/demo/$i $(ls | grep -v \\.o) -R
#cd -

%files
%doc AUTHORS README ChangeLog NEWS doc/FAQ
%_libdir/%name.so.*
%_sbindir/comedi_config
#%exclude %_bindir/%{name}_monitor
%_bindir/comedi_test
#%_sysconfdir/hotplug/usb/*
#%_sysconfdir/pcmcia/*
%_man7dir/*
%_man8dir/*

%files -n python-module-comedi
%python_sitelibdir/*.so
%python_sitelibdir/comedi.py

%files devel
%doc demo
#%_bindir/comedi_monitor
%_includedir/comedi*
%_libdir/%name.so
%_docdir/%oname/
%_man3dir/*
%_pkgconfigdir/*

%files devel-static
%_libdir/%name.a

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.1-alt2.2.1
- Rebuild with Python-2.7

* Thu Jan 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt2.2
- rebuild for set:provides by request of mithraen

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt2.1
- Rebuilt with python 2.6

* Mon Apr 27 2009 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt2
- build python module as python-module-comedi

* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt1
- new version 0.8.1 (with rpmrb script)

* Wed May 24 2006 Vitaly Lipatov <lav@altlinux.ru> 0.7.22-alt3
- fixes for as-needed
- disable pcmcia support

* Mon Mar 21 2005 Vitaly Lipatov <lav@altlinux.ru> 0.7.22-alt2
- split python module
- rebuild with python 2.4

* Sun Nov 07 2004 Vitaly Lipatov <lav@altlinux.ru> 0.7.22-alt1
- use a macro for ldconfig
- new version
- enable doc, disable ruby, usbdux

* Wed Jun 09 2004 Vitaly Lipatov <lav@altlinux.ru> 0.7.21-alt4
- disable docs build (for incompatible docbook version)

* Sun Feb 29 2004 Vitaly Lipatov <lav@altlinux.ru> 0.7.21-alt3
- change python entries in spec to universal way
- remove COPYING from doc
- correct license in spec to GPL
- disable example build
- add URL to spec

* Mon Jan 05 2004 Vitaly Lipatov <lav@altlinux.ru> 0.7.21-alt2
- build with gcc 3.3
- cleanup spec

* Wed Oct 01 2003 Vitaly Lipatov <lav@altlinux.ru> 0.7.21-alt1
- new version
- disable all docs for problem with docbook utils

* Sat Nov 30 2002 Vitaly Lipatov <lav@altlinux.ru> 0.7.19-alt1
- add install forget libcomedi.so link to devel package
- add comedi_monitor build for examples
- use install in Makefile

* Mon Nov 11 2002 Vitaly Lipatov <lav@altlinux.ru> 0.7.19-alt0.3
- cleanup spec
- main package split in devel and devel-static packages

* Sun Nov 03 2002 Vitaly Lipatov <lav@altlinux.ru> 0.7.19-alt0.1
- initial build for Sisyphus

* Wed Feb 21 2002 Tim Ousley <tim.ousley@ni.com>
- initial build of comedilib RPM

