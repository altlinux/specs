Name: libdnet
Version: 1.12
Release: alt3.1

Summary: A dumb networking library
Group: System/Libraries
License: BSD-style
Url: http://code.google.com/p/libdnet/

# Don't build static library by default,
# can be overridden by 'rpmbuild --enable static ...'
%def_disable static

# Python bindings, may be enabled using 'rpmbuild --with python ...'
%def_with python

# http://libdnet.googlecode.com/files/libdnet-%version.tgz
Source: libdnet-%version.tar
Patch1: libdnet-1.12-alt-warnings.patch
Patch2: libdnet-1.12-alt-fixes.patch

BuildRequires: gcc-c++ libpcap-devel

Summary(ru_RU.UTF-8): Низкоуровневая библиотека работы с сетью

%package devel
Summary: Development libdnet library, header files, documentation and examples
Summary(ru_RU.UTF-8): Средства разработки для libdnet - библиотека, заголовки, документация и примеры
Group: Development/C
Requires: %name = %version-%release

%package devel-static
Summary: Static libdnet library
Summary(ru_RU.UTF-8): Библиотека libdnet для статической компоновки
Group: Development/C
Requires: %name-devel = %version-%release
Requires: glibc-devel-static

%package -n dnet
Summary: A dumb networking library test program
Summary(ru_RU.UTF-8): Утилита для тестирования библиотеки libdnet
Group: Networking/Other
Requires: %name = %version-%release

%description
libdnet provides a simplified, portable interface to several low-level
networking routines, including network address manipulation, kernel
arp(4) cache and route(4) table lookup and manipulation, network
firewalling, network interface lookup and manipulation, and raw IP
packet and Ethernet frame transmission.

%description -l ru_RU.UTF-8
Библиотека libdnet предоставляет понятный и переносимый интерфейс
к низкоуровневым системным вызовам для управления следующими данными:
  * таблица сетевых интерфейсов,
  * кэш arp(4),
  * таблица маршрутизации (man 4 route),
  * правила пакетной фильтрации,
  * передача raw IP- и Ethernet-пакетов.

%description devel
libdnet provides a simplified, portable interface to several low-level
networking routines, including network address manipulation, kernel
arp(4) cache and route(4) table lookup and manipulation, network
firewalling, network interface lookup and manipulation, and raw IP
packet and Ethernet frame transmission.

This package contains the development library, it's header files,
documentation and examples needed to develop libdnet-based applications.

%description devel -l ru_RU.UTF-8
Библиотека libdnet предоставляет понятный и переносимый интерфейс
к низкоуровневым системным вызовам для управления следующими данными:
  * таблица сетевых интерфейсов,
  * кэш arp(4),
  * таблица маршрутизации (man 4 route),
  * правила пакетной фильтрации,
  * передача raw IP- и Ethernet-пакетов.

Данный пакет содержит библиотеку, необходимую для разработки приложений,
заголовочные файлы для неё, документацию и примеры программ.

%description devel-static
libdnet provides a simplified, portable interface to several low-level
networking routines, including network address manipulation, kernel
arp(4) cache and route(4) table lookup and manipulation, network
firewalling, network interface lookup and manipulation, and raw IP
packet and Ethernet frame transmission.

This package contains the static libdnet library required to develop
statically linked libdnet-based applications.

%description devel-static -l ru_RU.UTF-8
Библиотека libdnet предоставляет понятный и переносимый интерфейс
к низкоуровневым системным вызовам для управления следующими данными:
  * таблица сетевых интерфейсов,
  * кэш arp(4),
  * таблица маршрутизации (man 4 route),
  * правила пакетной фильтрации,
  * передача raw IP- и Ethernet-пакетов.

Данный пакет содержит библиотеку, необходимую для разработки приложений,
компонуемых с libdnet статически.

%description -n dnet
dnet is a simple test program for the dnet(3) library. It can be used
to compose and transmit network datagrams as a Unix-style filter (e.g.
reading from or writing to files and pipes) or modify the local system
network configuration (including the ARP cache, firewall ruleset,
network interfaces, and routing table).

%description -n dnet -l ru_RU.UTF-8
dnet является простой утилитой для тестирования одноимённой библиотеки
(см. man 3 dnet). Его можно использовать для генерации и передачи
сетевых датаграмм как обычный Юникс-фильтр (т.е. читая или записывая
данные в файлы и каналы), а также для тонкой настройки сетевых параметров
операционной системы, таких как кэш ARP, правила файрволла, сетевые интерфейсы,
таблица маршрутизации и т.д.

%if_with python

%setup_python_subpackage dnet
%package -n %packagename
Summary: Python bindings for libdnet, a dumb networking library
Summary(ru_RU.UTF-8): Модуль для доступа к функциям библиотеки libdnet из языка Python
Group: Development/Python
Requires: %name = %version-%release
BuildRequires(pre): python
%setup_std_python_package_deps

%description -n %packagename
Python interface for accessing libdnet-provided functions.

%description -n %packagename -l ru_RU.UTF-8
Интерфейс для доступа к функциям библиотеки libdnet из программ на языке Python.

%define with_python_opt --with-python=%_bindir

%else # without python

%define with_python_opt %nil

%endif # with python

%prep
%setup -q
%patch1 -p1
%patch2 -p1
find config -type f -not -name acinclude.m4 -delete

%build
%autoreconf -I config
export ac_cv_dnet_linux_procfs=yes
%configure %{subst_enable static} %with_python_opt
%make_build

%install
%makeinstall_std

mkdir -p %buildroot/etc/buildreqs/files/ignore.d
cat >%buildroot/etc/buildreqs/files/ignore.d/%name-devel <<EOF
^/usr/lib/libdnet.so\$
^/usr/lib/gcc-lib/.*/libdnet.so\$
EOF

%files
%_libdir/*.so.*
%doc LICENSE README THANKS TODO

%files devel
/etc/buildreqs/files/ignore.d/%name-devel
%_bindir/*
%_libdir/*.so
%_includedir/*
%_man3dir/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%files -n dnet
%_sbindir/*
%_man8dir/*

%if_with python
%files -n %packagename
%_libdir/python*/site-packages/*
%doc python/test.py python/dnet.pyx
%endif

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.12-alt3.1
- Rebuild with Python-2.7

* Sun Apr 24 2011 Dmitry V. Levin <ldv@altlinux.org> 1.12-alt3
- Rebuilt for debuginfo.

* Sat Nov 06 2010 Dmitry V. Levin <ldv@altlinux.org> 1.12-alt2
- Updated to 1.12+ svn revision 665.

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12-alt1.1
- Rebuilt with python 2.6

* Thu Jul 23 2009 Dmitry V. Levin <ldv@altlinux.org> 1.12-alt1
- Updated to 1.12+ svn revision 653.
- Enabled linux /proc support.

* Wed May 06 2009 Dmitry V. Levin <ldv@altlinux.org> 1.11-alt8
- Fixed build with fresh autotools.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 1.11-alt7
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.

* Sat Jan 13 2007 Dmitry V. Levin <ldv@altlinux.org> 1.11-alt6
- Enabled python bindings.

* Thu Jun 01 2006 Dmitry V. Levin <ldv@altlinux.org> 1.11-alt4
- Applied changes from nmap project.
- Fixed compilations warnings.

* Sat May 27 2006 Dmitry V. Levin <ldv@altlinux.org> 1.11-alt3
- Disabled python bindings until python stuff gets fixed.
- Fixed build with gcc-4.1.x (damir@).

* Thu May 11 2006 Ilya Evseev <evseev@altlinux.ru> 1.11-alt2
- bugfix #9548, thanks to Igor Zubkov <icesik@altlinux.ru>

* Wed Jan 25 2006 Ilya Evseev <evseev@altlinux.ru> 1.11-alt1
- updated to new version 1.11
- NOTE: since release 1.10-alt2 this package uses macros
  defined by rpm-build-python >= 0.20-alt1.

* Tue Mar 29 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.10-alt2.1
- Rebuilt with python-2.4.

* Mon Feb 28 2005 Dmitry V. Levin <ldv@altlinux.org> 1.10-alt2
- Fixed python bindings packaging to comply with python policy.

* Mon Feb 28 2005 Ilya Evseev <evseev@altlinux.ru> 1.10-alt1
- version 1.10
- python bindings added

* Fri Jan 14 2005 Ilya Evseev <evseev@altlinux.ru> 1.8-alt2
- spec cleanup: most tricks are not needed more because libdnet supports libtool
- dont build static library except rpmbuild is started with '--enable static'

* Sat Jan  8 2005 Ilya Evseev <evseev@altlinux.ru> 1.8-alt1
- Updated to 1.8
- Specfile: added russian summary and descriptions
- Removed Makefile.am patch and rpmbuild/automake build dependencies

* Sat May 03 2003 Dmitry V. Levin <ldv@altlinux.org> 1.7-alt1
- Updated to 1.7, updated patch and build script.

* Sat Nov 02 2002 Dmitry V. Levin <ldv@altlinux.org> 1.5-alt2
- Fixed build.

* Sat Oct 19 2002 Dmitry V. Levin <ldv@altlinux.org> 1.5-alt1
- Updated to 1.5
- %name-devel: added buildreq ignore rule (aka autoconf sux).

* Sun Sep 01 2002 Dmitry V. Levin <ldv@altlinux.org> 1.4-alt1
- Initial revision.
