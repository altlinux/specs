Summary:        Prelude Hybrid Intrusion Detection System - Log Analyzer Sensor
Name:           prelude-lml
Version:        1.0.0
Release:        alt2
License:        GPLv2
Group:          Networking/Other
URL:            http://www.prelude-ids.org/
Source:		http://www.prelude-ids.org/download/releases/%name-%version.tar.gz
Patch:		%name-%version-%release.patch

Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

%def_disable static
%{?_enable_static:BuildPreReq: glibc-devel-static}

BuildRequires: gcc-c++ libgamin-devel libgnutls-devel libpcre-devel libprelude-devel libltdl-devel libicu-devel libgcrypt-devel

%description
The Prelude Log Monitoring Lackey (LML) is the host-based sensor
program part of the Prelude Hybrid IDS suite. It can act as a
centralized log collector for local or remote systems, or as a simple
log analyzer (such as swatch). It can run as a network server
listening on a syslog port or analyze log files. It supports logfiles
in the BSD syslog format and is able to analyze any logfile by using
the PCRE library. It can apply logfile-specific analysis through
plugins such as PAX. It can send an alert to the Prelude Manager when
a suspicious log entry is detected.

%description -l uk_UA.UTF-8
Лакей Prelude, який контролює реєстраційні журнали, являє собою сенсор
на рівні хоста і є частиною комплекту Prelude Hybrid IDS. Даний модуль
може діяти як централізований збирач подій або як простий аналізатор
(типу swatch) для реєстраційних журналів локальних або віддалених
хостів. Він також може працювати мережевим сервером на порту syslog
або аналізувати реєстраційні журнали. Підтримує системні журнали подій
формату BSD і здатний аналізувати будь-які реєстраційні журнали за
допомогою бібліотеки PCRE. Ця можливість дозволяє використовувати
специфічні аналізатори (типу PAX) реєстраційних журналів через
додаткові плагіни. При виявленні підозрілих записів до менеджера
Prelude надсилається відповідне повідомлення.

%description -l ru_RU.UTF-8
Лакей Prelude, который контролирует регистрационные журналы, являет
собой сенсор на уровне хоста и входит в комплект Prelude Hybrid
IDS. Данный модуль может действовать как централизованный сборщик
событий или как простой анализатор (типа swatch) для регистрационных
журналов локальных или удалённых хостов. Он также может работать в
качестве сетевого сервера на порту syslog или анализировать
регистрационные журналы. Поддерживает системные журналы событий
формата BSD и способный анализировать любые регистрационные журналы с
помощью библиотеки PCRE. Эта возможность позволяет использовать
специфические анализаторы (типа PAX) регистрационных журналов через
дополнительные плагины. При выявлении подозрительных записей менеджеру
Prelude посылается соответствующее уведомление.

%package devel
Summary: Libraries, includes, etc. to develop Prelude IDS sensors
Group: Development/C
Requires: %name = %version


%if_enabled static
%package devel-static
Summary: Libraries, includes, etc. to develop Prelude IDS sensors
Group: Development/C
Requires: %name = %version
Requires: %name-devel
%endif

%description devel
The Prelude Log Monitoring Lackey (LML) is the host-based sensor
program part of the Prelude Hybrid IDS suite.

This package contains headers files, requires for build own plugins
for Prelude LML.

Install this package if you want to build Prelude LML Plugins.

%description -l uk_UA.UTF-8 devel
Лакей Prelude, який контролює реєстраційні журнали, являє собою сенсор
на рівні хоста і є частиною комплекту Prelude Hybrid IDS.

Даний пакет містить в собі файли заголовків, які необхідні для
створення власних плагінів до Prelude LML.

Встановіть даний пакет, якщо Ви хочете збирати власні плагіни до
Prelude LML.

%description -l ru_RU.UTF-8 devel
Лакей Prelude, который контролирует регистрационные журналы, являет
собой сенсор на уровне хоста и входит в комплект Prelude Hybrid
IDS.

Данный пакет содержит заголовочные файлы необходимые для разработки
собственных плагинов для Prelude LML.

Установите данный пакет, если Вы хотите создавать свои плагины к
Prelude LML.

%if_enabled static
%description devel-static
The Prelude Log Monitoring Lackey (LML) is the host-based sensor
program part of the Prelude Hybrid IDS suite.  Install this package if
you want to build Prelude LML Plugins.

This package contains statically builded libraries for Prelude LML.

%description -l uk_UA.UTF-8 devel-static
Лакей Prelude, який контролює реєстраційні журнали, являє собою сенсор
на рівні хоста і є частиною комплекту Prelude Hybrid IDS.

Даний пакет містить в собі статичні файли бібліотек Prelude LML.

%description -l ru_RU.UTF-8 devel-static
Лакей Prelude, который контролирует регистрационные журналы, являет
собой сенсор на уровне хоста и входит в комплект Prelude Hybrid
IDS.

Данный пакет содержит статические файлы библиотек Prelude LML.
%endif

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure %{subst_enable static} \
	--localstatedir=%_var \
	--sysconfdir=%_sysconfdir/prelude \
	--enable-unsupported-rulesets

# Fix undefined symbol
%__subst "s|(LDFLAGS)|(LDFLAGS) \$(LIBPRELUDE_LIBS) |g" plugins/debug/Makefile
%__subst "s|(LDFLAGS)|(LDFLAGS) \$(LIBPRELUDE_LIBS) \$(PCRE_LIBS) |g" plugins/pcre/Makefile

%make

%install
%make DESTDIR=%buildroot install
%__mkdir_p %buildroot%_localstatedir/%name/
%__mkdir_p %buildroot%_initdir/
install -m 755 %name-initd %buildroot%_initdir/%name
%__mkdir_p %buildroot%_sysconfdir/sysconfig
%__cat > %buildroot%_sysconfdir/sysconfig/%name <<EOF
# Additional command line parameters for %name:
#
OPTIONS=""
EOF

%post
%post_service %name

%preun
%preun_service %name

%files
%doc AUTHORS COPYING ChangeLog HACKING.README NEWS README
%config %dir %_sysconfdir/prelude/%name/
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %attr(0644,root,root) %_sysconfdir/prelude/%name/*.conf
%config(noreplace) %attr(0644,root,root) %_sysconfdir/prelude/%name/*.rules
%config %dir %_sysconfdir/prelude/%name/ruleset/
%config(noreplace) %attr(0644,root,root)%_sysconfdir/prelude/%name/ruleset/*
%_initdir/%name
%_bindir/prelude-lml
%dir %_libdir/%name/
%_libdir/%name/debug.so
%_libdir/%name/pcre.so
%dir %_localstatedir/%name/

%if_enabled static
%_libdir/%name/*.a
%endif

%files devel
%dir %_includedir/%name/
%_includedir/%name/*.h

%if_enabled static
%files devel-static
%_libdir/%name/*.la
%endif

%changelog
* Wed Mar 30 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt2
- Add libgcrypt-devel to BuildRequires

* Thu Dec 16 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1.1
- rebuild with new icu44 and/or boost by request of git.alt administrator

* Tue Jul 27 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt1
- Update to new version 0.0.0

* Fri Jan 15 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.15-alt1
- Update to new version 0.9.15

* Fri Jan 16 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.14-alt1
- Update to new version 0.9.14
- Add patch from https://dev.prelude-ids.com/issues/show/294

* Mon Jan 12 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.13-alt3
- Cleanup init script

* Tue Dec 23 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.13-alt2
- Remove depricated postun_ldconfig
- Convert spec to UTF8

* Sun Oct 19 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.13-alt1
- New version

* Sun Jun 29 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.12.2-alt1
- Recovery from orfaned
- Update to new version 0.9.12.2
- Update BuildRequires
- Remove %name-conf.patch
- Update /etc/init.d/%name
- Update spec

* Fri Jan 14 2005 Serge A. Volkov <vserge at altlinux.ru> 0.8.6-alt6
- Remove libpcre requires and update buildreq

* Mon Dec 20 2004 Serge A. Volkov <vserge at altlinux.ru> 0.8.6-alt5
- Rebuild with libprelude-0.8.10
- Update BuildRequires

* Thu May 13 2004 Serge A. Volkov <vserge@altlinux.ru> 0.8.6-alt4.1
- Rebuild with openssl-0.9.7d
- Remove configure options "--enable-gtk-doc"

* Mon Feb  2 2004 Serhii Hlodin <hlodin@altlinux.ru> 0.8.6-alt3
- Minor fixes for Sisyphus
- Add initscript
- Add additional sysconfig file

* Thu Nov  6 2003 Serhii Hlodin <hlodin@altlinux.ru> 0.8.6-alt2
- Minor fixes in dependencies

* Wed Nov  5 2003 Serhii Hlodin <hlodin@altlinux.ru> 0.8.6-alt1
- New release

* Sun Oct 12 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.8.5-alt2
- Minor fixes in spec

* Wed Oct 08 2003 Serhii Hlodin <hlodin@altlinux.ru> 0.8.5-alt1
- New release

* Sun May 18 2003 Serhii Hlodin <hlodin@altlinux.ru> 0.8.3-alt1
- Initial build based on original spec-file
