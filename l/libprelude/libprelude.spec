Summary: Prelude Hybrid Intrusion Detection System Library
Name: libprelude
Version: 1.0.0
Release: alt1.6
License: GPLv2
Group: System/Libraries
Url: http://www.prelude-ids.org/
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Source: %name-%version.tar
Patch0: libprelude-1.0.0-alt-extern-libltdl.patch
Patch1: libprelude-1.0.0-alt-DSO.patch

%def_enable static
%{?_enable_static:BuildPreReq: glibc-devel-static}
%def_enable gtk_doc
%define _gtk_docdir %_datadir/gtk-doc/html
%{?_enable_gtk_doc:BuildPreReq: gtk-doc}

# Automatically added by buildreq on Mon Oct 17 2011
BuildRequires: gcc-c++ libgcrypt-devel libgnutls-extra-devel libltdl7-devel liblua5-devel perl-devel python-devel swig glib2-devel

%description
The Prelude Library is a collection of generic functions providing
communication between the Prelude Hybrid IDS suite components. It
provides a convenient interface for sending alerts to Prelude Manager
with transparent SSL, failover and replication support, asynchronous
events and timer interfaces, an abstracted configuration API (hooking
at the commandline, the configuration line, or wide configuration,
available from the Manager), and a generic plugin API. It allows you
to easily turn your favorite security program into a Prelude sensor.

%description -l ru_RU.UTF-8
Библиотека Prelude содержит коллекцию общих функций, обеспечивающих
коммуникацию между компонентами Prelude Hybrid IDS. Она обеспечивает
интерфейс для пересылки предупреждений менеджеру Prelude используя
SSL, отказоустойчивость и поддержку репликаций, асинхронные события и
интерфейсы таймера, абстрактный конфигурационный API и общий API для
дополнений. Это позволит вам легко интегрировать вашу программу
безопасности в датчик Prelude.

%description -l uk_UA.UTF-8
Бібліотека Prelude містить колекцію спільних функцій, що забезпечують
комунікацію між компонентами Prelude Hybrid IDS. Вона забезпечує
інтерфейс для надсилання попереджень менеджеру Prelude використовуючи
SSL, відмовостійкість і підтримку реплікацій, асинхронні події та
інтерфейси таймера, абстрактний конфігураційний API та загальний API
для доповнень. Це дозволить вам легко інтегрувати вашу програму
безпеки в датчик Prelude.

%package devel
Summary: Libraries, includes, etc. to develop Prelude IDS sensors
Group: Development/C
Requires: %name = %version-%release

%description devel
Libraries, include files, etc you can use to develop Prelude IDS sensors using
the Prelude Library. The Prelude Library is a collection of generic functions
providing communication between the Prelude Hybrid IDS suite componentst
It provides a convenient interface for sending alerts to Prelude Manager with
transparent SSL, failover and replication support, asynchronous events and
timer interfaces, an abstracted configuration API (hooking at the commandline,
the configuration line, or wide configuration, available from the Manager), and
a generic plugin API. It allows you to easily turn your favorite security
program into a Prelude sensor.

%description -l ru_RU.UTF-8 devel
Библиотеки, заголовочные файлы и т.п вы можете использовать для
разработки датчиков Prelude IDS. Библиотека Prelude содержит коллекцию
общих функций, обеспечивающих коммуникацию между компонентами Prelude
Hybrid IDS. Она обеспечивает интерфейс для пересылки предупреждений
менеджеру Prelude используя SSL, отказоустойчивость и поддержку
репликаций, асинхронные события и интерфейсы таймера, абстрактный
конфигурационный API и общий API для дополнений. Это позволит вам
легко интегрировать вашу программу безопасности в датчик Prelude.

%description -l uk_UA.UTF-8 devel
Бібліотеки, файли заголовків і т.п ви можете використовувати для
розробки датчиків Prelude IDS. Бібліотека Prelude містить колекцію
спільних функцій, що забезпечують комунікацію між компонентами Prelude
Hybrid IDS. Вона забезпечує інтерфейс для надсилання попереджень
менеджеру Prelude використовуючи SSL, відмовостійкість і підтримку
реплікацій, асинхронні події та інтерфейси таймера, абстрактний
конфігураційний API та загальний API для доповнень. Це дозволить вам
легко інтегрувати вашу програму безпеки в датчик Prelude.

%if_enabled static
%package devel-static
Summary: Static libraries to develop Prelude IDS sensors
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static libraries to develop Prelude IDS sensors using the Prelude Library.
%endif

%package devel-doc
Summary: Development documentation for %name
Group: Development/GNOME and GTK+
Conflicts: %name-devel < %version-%release
BuildArch: noarch

%description devel-doc
Libraries, include files, etc you can use to develop Prelude IDS sensors using
the Prelude Library. The Prelude Library is a collection of generic functions
providing communication between the Prelude Hybrid IDS suite componentst
It provides a convenient interface for sending alerts to Prelude Manager with
transparent SSL, failover and replication support, asynchronous events and
timer interfaces, an abstracted configuration API (hooking at the commandline,
the configuration line, or wide configuration, available from the Manager), and
a generic plugin API. It allows you to easily turn your favorite security
program into a Prelude sensor.

This package contains development documentation for the library.

%package -n python-module-%name
Summary: Development package that includes the %name header files
Group: Development/Python
Requires: %name = %version-%release

%description -n python-module-%name
The devel package contains the %name library and the include files

%package -n perl-%name
Summary: Libraries and modules for access to %name from perl
Group: Development/Perl
Requires: %name = %version-%release

%description -n perl-%name
Perl bindings to %name.
Install perl-%name if you want to use any perl scripts that use %name.

%prep
%setup
%patch0 -p0
%patch1 -p0

%build
%autoreconf
%configure %{subst_enable static} \
	--localstatedir=%_var \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	--with-perl-installdirs=vendor

rm -fR libltdl
%make

%install
%makeinstall_std

# Fix time stamp for both 32 and 64 bit libraries
touch -r ./configure.in %buildroot%_sysconfdir/prelude/default/*

%files
%doc README LICENSE.README AUTHORS COPYING NEWS HACKING.README
%_bindir/prelude-adduser
%_bindir/prelude-admin
%_libdir/%{name}*.so.*
%_libdir/PreludeEasy.so
%config(noreplace) %_sysconfdir/prelude
%_man1dir/*
%dir %_spooldir/*

%if_enabled static
%files devel-static
%_libdir/%{name}*.a
%_libdir/PreludeEasy.a
%endif

%files devel
%_bindir/%name-config
%_libdir/%{name}*.so
%_includedir/%name
%_datadir/aclocal/*
%_libdir/pkgconfig/%name.pc

%files devel-doc
%_gtk_docdir/*

%files -n python-module-%name
%python_sitelibdir/*

%files -n perl-%name
%perl_vendor_autolib/Prelude*
%perl_vendor_archlib/Prelude*

%changelog
* Sat Jun 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.6
- Fixed build

* Sat Oct 29 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt1.5
- Rebuild with Python-2.7

* Mon Oct 17 2011 Alexey Tourbin <at@altlinux.ru> 1.0.0-alt1.4
- Rebuilt for perl-5.14

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.3
- Fixed build

* Fri Feb 25 2011 Dmitry V. Levin <ldv@altlinux.org> 1.0.0-alt1.2
- Rebuilt for debuginfo.

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 1.0.0-alt1.1
- rebuilt with perl 5.12

* Tue Jul 27 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt1
- Update to new version 1.0.0

* Wed Jan 13 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.25-alt1
- Update to new version 0.9.25
- Enable build static lib

* Tue Aug 11 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.24.1-alt1
- Update to new version 0.9.24.1

* Tue Jun 16 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.23-alt2
- Fix dir %_includedir/%name owner (thanks at@)

* Sat Jun 13 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.23-alt1
- Update to new version 0.9.23
- Rename python-modules-libprelude to python-module-libprelude

* Fri Jan 16 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.21.3-alt1
- Update to new version 0.9.21.3

* Fri Dec 26 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.21.2-alt3
- Rebuild with new gnutls
- Enable build documentation and move it to %_gtk_docdir

* Sat Nov 29 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.21.2-alt2
- Remmove depricated ldconfig call in post

* Fri Oct 17 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.21.2-alt1
- Update to new version 0.9.21.2
- Convert spec to UTF-8
- Add lua support

* Sat Jun 28 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.17.2-alt1
- Recovery from orfaned
- Update to new version 0.9.17.2
- Update BuildRequires
- Remove ltdl patch
- Add subpackage python-modules-%name and perl-%name
- Update spec

* Sun Dec 19 2004 Serge A. Volkov <vserge at altlinux.ru> 0.8.10-alt1
- Update to new version 0.8.10
- Update BuildRequires
- Reworked ltdl patch - now we try detect ltdl lib

* Thu May 13 2004 Serge A. Volkov <vserge@altlinux.ru> 0.8.8-alt5.1
- Rebuild with openssl-0.9.7d
- Remove configure options "--enable-gtk-doc"

* Mon Feb  2 2004 Serhii Hlodin <hlodin@altlinux.ru> 0.8.8-alt4
- Minor fixes for Sisyphus
- Add patch for remove and use built-in libltdl

* Sat Dec 20 2003 Serhii Hlodin <hlodin@altlinux.ru> 0.8.8-alt3
- Remove .la files

* Thu Nov  6 2003 Serhii Hlodin <hlodin@altlinux.ru> 0.8.8-alt2
- Minor fixes: %name.so transposed to devel package

* Wed Nov  5 2003 Serhii Hlodin <hlodin@altlinux.ru> 0.8.8-alt1
- New release

* Mon Nov 03 2003 Serhii Hlodin <hlodin@altlinux.ru> 0.8.7-alt3
- Minor build fixes in spec

* Sun Oct 12 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.8.7-alt2
- Minor fixes in spec

* Wed Oct 08 2003 Serhii Hlodin <hlodin@altlinux.ru> 0.8.7-alt1
- New release

* Mon Jun 16 2003 Serhii Hlodin <hlodin@altlinux.ru> 0.8.5-alt2
- Fixed dependence for directories in spec-file

* Sun May 18 2003 Serhii Hlodin <hlodin@altlinux.ru> 0.8.5-alt1
- Initial build based on original .spec-file
  by Sylvain GIL <prelude-packaging@tootella.org>
