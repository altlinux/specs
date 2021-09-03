# Error: invalid attempt to declare external version name as default in symbol `comedi_set_buffer_size@@v0.7.18'
# FIXME: #define EXPORT_ALIAS_DEFAULT(a,b,c) __asm__(".symver " #a "," #b "@@v" #c )
%define optflags_lto %nil

%def_with doc
%def_enable python
%def_disable static

%define oname comedilib
%define oversion %(echo "%version" | sed -e "s|\\.|_|g")

Name: libcomedi
Version: 0.12.0
Release: alt2

Summary: Data Acquisition library for the Comedi DAQ driver
Summary(ru_RU.UTF-8): Библиотека получения данных для драйвера Comedi DAQ

License: LGPLv2
Group: Development/Other
Url: http://www.comedi.org

Packager: Vitaly Lipatov <lav@altlinux.ru>
AutoReq: noshell

# Source-url: https://github.com/Linux-Comedi/comedilib/archive/r%oversion.tar.gz
Source: %name-%version.tar

# for correct _localstatedir
BuildRequires: rpm-macros-intro-conflicts

BuildRequires: flex gcc-c++ libstdc++-devel swig
%if_enabled python
BuildRequires: python3-devel
%endif

%if_with doc
BuildRequires: xmlto
%endif

%description
The Linux Control and Measurement Device Interface Library.
Comedilib is the library for the Comedi data acquisition driver
for Linux.  It allows Linux processes to acquire data from
supported DAQ cards, such as those from National Instruments.

%description -l ru_RU.UTF-8
Comedilib -- это библиотека для драйвера получения данных Comedi под Linux.
Она позволяет пользовательским процессам получать данные от поддерживаемых
карт DAQ, например, производимых National Instruments.

%package devel
Summary: The files needed for %name application development
Summary(ru_RU.UTF-8): Файлы, требующиеся для разработки приложений с использованием %name
Group: Development/C
Requires: %name = %EVR
# https://bugzilla.altlinux.org/show_bug.cgi?id=19191
#Requires: kernel-headers-comedi

%description devel
The %name-devel package contains the necessary include files
for developing applications with %name.

See demo dir in the source repository for examples.

%description devel -l ru_RU.UTF-8
Пакет %name-devel содержит необходимые заголовочные файлы
для разработки приложений, которые используют %name.

Посмотрите в каталог demo в исходниках проекта, там есть примеры.

%if_with python-bindings
%package -n python3-module-comedi
Summary: Python interface for %name
Group: Development/Python3
Requires: %name = %EVR

%description -n python3-module-comedi
Python interface for %name.

%endif

%package devel-static
Summary: Static library for %name application development
Summary(ru_RU.UTF-8): Статическая библиотека для разработки приложений с использованием %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
The %name-devel-static package contains the static library
for developing applications with %name
%description devel-static -l ru_RU.UTF-8
Пакет %name-devel-static содержит статическую библиотеку
для разработки приложений, которые используют %name.

%prep
%setup

%build
%autoreconf
%configure --disable-ruby-binding \
           %{subst_enable static} \
%if_enabled python
           --enable-python-binding
%endif
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS README ChangeLog NEWS doc/FAQ
%_libdir/%name.so.*
%_sbindir/comedi_config
%_bindir/comedi_board_info
%_bindir/comedi_test
%dir %_sysconfdir/pcmcia
%config(noreplace) %_sysconfdir/pcmcia/*
%_man1dir/*
%_man7dir/*
%_man8dir/*


%if_enabled python-bindings
%files -n python3-module-comedi
%python3_sitelibdir/*.so
%python3_sitelibdir/comedi.py*
%endif

%files devel
%_includedir/comedi*
%_libdir/%name.so
%_docdir/%oname/
%_pkgconfigdir/*
%if_with doc
%_man3dir/*
%endif

%if_enabled static
%files devel-static
%_libdir/%name.a
%endif

%changelog
* Fri Sep 03 2021 Vitaly Lipatov <lav@altlinux.ru> 0.12.0-alt2
- cleanup spec, fix build
- disable lto (have no idea)
- disable pack devel-static subpackage
- enable man3 packing
- switch to python3

* Sun Jan 24 2021 Pavel Vainerman <pv@altlinux.ru> 0.12.0-alt1
- new version (0.12.0) with rpmgs script

* Fri May 25 2018 Pavel Vainerman <pv@altlinux.ru> 0.11.0-alt3
- disabled build documentations (man3)

* Sat Oct 28 2017 Vitaly Lipatov <lav@altlinux.ru> 0.11.0-alt2
- drop demo with binaries from devel subpackage

* Sat Oct 28 2017 Vitaly Lipatov <lav@altlinux.ru> 0.11.0-alt1
- build new version
- cleanup spec

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt1.1
- Fixed build

* Thu Aug 23 2012 Roman Savochenko <rom_as@altlinux.ru> 0.10.0-alt1
- new version 0.10.0
- all available files included
- spec translated to UTF-8

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

* Thu Feb 21 2002 Tim Ousley <tim.ousley@ni.com>
- initial build of comedilib RPM

