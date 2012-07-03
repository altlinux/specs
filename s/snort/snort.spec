Summary:   An intrusion detection system
Name:      snort
Version:   2.8.6.1
Release: alt3
License: %gpl2only
Group:     Security/Networking
Url:       http://www.snort.org
Packager: Ilya Mashkin <oddity@altlinux.ru>

# You can omit building some target packages via 'rpmbuild --without xxx'
%def_with    mysql
%def_with    postgresql
%def_with    odbc
%def_without prelude
%def_with    inline
%def_without libpq3
# You can omit this feature via 'rpmbuild --disable flexresp'
%def_enable flexresp

%define dbhints_dir  %_datadir/%name-dbhints
%define dbhints_path %dbhints_dir/%name-dbhints.sql

Source0:   %name-%version.tar
Source5:   snortdb-extra.bz2

Source10:  snort.sysconfig.m4
Source20:  README-ALT.ru.m4
Source21:  README-ALT.uk.m4
Source30:  snort.logrotate.m4
Source99:  snortd

Patch0:    %name-%version-%release.patch

Requires:  libpcap >= 0.4
Requires:  service >= 0.5.6
Requires:  snort-base, snort-rules
PreReq:    alternatives >= 0.2.0-alt0.7
BuildPreReq: libltdl-devel, m4, bzip2
BuildRequires: rpm-build-licenses

# Automatically added by buildreq on Fri Jan 14 2005, explicit versions added manually
BuildRequires: libnet1-devel >= 1.0.2a, libpcap-devel >= 0.4, libpcre-devel
BuildRequires: zlib-devel

Conflicts: snort-rules < 2.8

%if_with postgresql
BuildRequires: postgresql-devel
%if_with libpq3
BuildRequires: libpq3-devel
%else
BuildRequires: libpq-devel
%endif
%endif

%if_with prelude
Requires:  libprelude
%endif
%if_with mysql
BuildRequires: libMySQL-devel
%endif
%if_with prelude
BuildRequires: libprelude-devel
%endif
%if_with odbc
BuildRequires: libunixODBC-devel
%endif
%if_with inline
BuildRequires: iptables-devel
%endif

%if_with mysql
%if_with postgresql
%if_with odbc
%if_with inline
%def_with bloat
%endif
%endif
%endif
%endif
%def_without bloat

Summary(ru_RU.KOI8-R): Автоматический анализатор/блокировщик сетевых пакетов

%description
Snort is a libpcap-based packet sniffer/logger which can be used as a
lightweight network intrusion detection system.  It features rules
based logging and can perform protocol analysis, content
searching/matching and can be used to detect a variety of attacks and
probes, such as buffer overflows, stealth port scans, CGI attacks, SMB
probes, OS fingerprinting attempts, and much more.  Snort has a
real-time alerting capabilty, with alerts being sent to syslog, a
seperate "alert" file, or as a WinPopup message via Samba's smbclient.

Please see the documentation in %_docdir/%name-%version

%description -l ru_RU.KOI8-R
Snort -- это мощный прослушиватель и перехватчик сетевых пакетов,
основанный на библиотеке libpcap. При работе Snort использует набор
предварительно подготовленных правил, которые содержат условия срабатывания
по значениям служебных и прикладных данных.

Snort может использоваться в качестве системы обнаружения вторжения в сеть,
а также разнообразных атак и попыток предпринятия таковых (переполнение буфера,
сканирование портов и SMB, стелс-сканирование, атаки CGI, определение
операционных систем и многое другое).

Snort имеет возможность оповещения в реальном масштабе времени через сообщения,
отправленные в системный лог-файл, альтернативный файл "тревоги"
или как WinPopup-сообщение, отправленное с помощью smbclient.

Базовая версия не блокирует опасные соединения. Если вам требуется эта функция,
инсталлируйте один из пакетов snort с суффиксом flexresp или bloat в названии.

Пожалуйста, обязательно ознакомьтесь с документацией,
которая размещена в %_docdir/%name-%version

%description -l uk_UA.KOI8-U
Snort -- це потужний зас╕б прослуховування та перехвату мережевих
пакет╕в, оснований на б╕бл╕отец╕ libpcap. В╕н базу╓ться на попередньо
сформованих правилах та вм╕╓ виконувати анал╕з зм╕сту протоколу.

Даний пакет може використовуватися в якост╕ системи виявлення
вторгнень в мереж╕, а також допомага╓ виявляти р╕зноман╕тн╕ атаки та
╖х спроби (переповнення буфера, сканування порт╕в, невидим╕
сканування, атаки CGI, SMB, спроби визначення типу операц╕йно╖ системи
та багато ╕нших).

Snort ма╓ можлив╕сть опов╕щення в реальному масштаб╕ часу через
пов╕домлення, в╕дправлен╕ в системний лог-файл, альтернативний файл
"тривоги" або як WinPopup-пов╕домлення, в╕дправлене за допомогою
програми smbclient.

Будь-ласка, обов'язково ознайомтеся з документац╕╓ю, що розм╕щена в
%_docdir/%name-%version

%package plain+flexresp
Summary: Snort (plain) with Flexible Response
Summary(ru_RU.KOI8-R): Snort с поддержкой автоматического блокирования соединений
Group: Security/Networking
Requires: %name = %version
Requires: libnet1
%description plain+flexresp
Snort compiled with flexresp support.
Flexible Response allows snort to actively close offending connections.
Requires snort libnet rpm.
%description -l ru_RU.KOI8-R plain+flexresp
Snort, скомпилированный с поддержкой flexresp. Flexible Responses означает
возможность автоматически блокировать соединения, признанные злонамеренными
на основании соответствующих правил. Требует библиотеку libnet.
%description -l uk_UA.KOI8-U plain+flexresp
Snort, скомп╕льований з п╕дтримкою flexresp.
Вимага╓ б╕бл╕отеку libnet.

%package mysql
Summary: Snort with MySQL support
Summary(ru_RU.KOI8-R): Snort с отправкой статистики в базу MySQL
Group: Security/Networking
Requires: %name = %version
%description mysql
Snort compiled with mysql support.
%description -l ru_RU.KOI8-R mysql
Snort, скомпилированный с поддержкой MySQL в качестве хранилища статистики.
%description -l uk_UA.KOI8-U mysql
Snort, скомп╕льований з п╕дтримкою MySQL.

%package mysql+flexresp
Summary: Snort with MySQL support and Flexible Response
Summary(ru_RU.KOI8-R): Snort с отправкой статистики в базу MySQL и автоблокировкой
Group: Security/Networking
Requires: %name = %version
Requires: libnet1
%description mysql+flexresp
Snort compiled with mysql support and flexresp support.
Requires snort libnet rpm.
%description -l ru_RU.KOI8-R mysql+flexresp
Snort, скомпилированный с поддержкой MySQL в качестве хранилища статистики
и flexresp - автоматическим блокированием соединений на основании правил.
Требует библиотеку libnet.
%description -l uk_UA.KOI8-U mysql+flexresp
Snort, скомп╕льований з п╕дтримкою MySQL та flexresp.
Вимага╓ б╕бл╕отеку libnet.

%package postgresql
Summary: Snort with PostgreSQL support
Summary(ru_RU.KOI8-R): Snort с отправкой статистики в базу PostgreSQL
Group: Security/Networking
Requires: %name = %version
%description postgresql
Snort compiled with postgresql support. 
%description -l ru_RU.KOI8-R postgresql
Snort, скомпилированный с поддержкой PostgreSQL в качестве хранилища статистики.
%description -l uk_UA.KOI8-U postgresql
Snort, скомп╕льований з п╕дтримкою PostgreSQL.

%package postgresql+flexresp
Summary: Snort with PostgreSQL support and Flexible Response
Summary(ru_RU.KOI8-R): Snort с отправкой статистики в базу PostgreSQL и автоблокировкой
Group: Security/Networking
Requires: %name = %version
Requires: libnet1
%description postgresql+flexresp
Snort compiled with postgresql support and flexresp support.
Requires snort libnet rpm.
%description -l ru_RU.KOI8-R postgresql+flexresp
Snort, скомпилированный с поддержкой PostgreSQL в качестве хранилища статистики
и flexresp - автоматическим блокированием соединений на основании правил.
Требует библиотеку libnet.
%description -l uk_UA.KOI8-U postgresql+flexresp
Snort, скомп╕льований з п╕дтримкою PostgreSQL та flexresp.
Вимага╓ б╕бл╕отеку libnet.

%package odbc
Summary: Snort with unixODBC support
Summary(ru_RU.KOI8-R): Snort с отправкой статистики в ODBC-базу
Group: Security/Networking
Requires: %name = %version
Requires: libunixODBC
%description odbc
Snort compiled with unixODBC support. 
%description -l ru_RU.KOI8-R odbc
Snort, скомпилированный с поддержкой unixODBC в качестве хранилища статистики.
%description -l uk_UA.KOI8-U odbc
Snort, скомп╕льований з п╕дтримкою unixODBC.

%package odbc+flexresp
Summary: Snort with unixODBC support and Flexible Response
Summary(ru_RU.KOI8-R): Snort с отправкой статистики в ODBC-базу и автоблокировкой
Group: Security/Networking
Requires: %name = %version
Requires: libnet1
Requires: libunixODBC
%description odbc+flexresp
Snort compiled with unixODBC support and flexresp support.
Requires snort libnet rpm.
%description -l ru_RU.KOI8-R odbc+flexresp
Snort, скомпилированный с поддержкой ODBC-СУБД в качестве хранилища статистики
и flexresp - автоматическим блокированием соединений на основании правил.
Требует библиотеку libnet.
%description -l uk_UA.KOI8-U odbc+flexresp
Snort, скомп╕льований з п╕дтримкою unixODBC та flexresp.
Вимага╓ б╕бл╕отеку libnet.

%package inline
Summary: Snort with IPTables support
Summary(ru_RU.KOI8-R): Snort с чтением трафика через IPTables вместо PCAP
Group: Security/Networking
Requires: %name = %version
Requires: iptables
%description inline
Snort-Inline takes packets from iptables instead of libpcap.
It then uses new rule types to help iptables make pass or drop decisions
based on snort rules.
%description -l ru_RU.KOI8-R inline
Snort, использующий для просмотра трафика функции пакетного фильтра IPTables
вместо библиотеки PCAP. Дополнительные типы правил служат для передачи указаний
от Snort'а пакетному фильтру.
%description -l uk_UA.KOI8-U inline
Snort, скомп╕льований з п╕дтримкою IPTables

%package inline+flexresp
Summary: Snort with IPTables and FlexibleResponse support
Summary(ru_RU.KOI8-R): Snort с чтением трафика через IPTables и автоблокировкой
Group: Security/Networking
Requires: %name = %version
Requires: iptables
%description inline+flexresp
Snort-Inline takes packets from iptables instead of libpcap.
It then uses new rule types to help iptables make pass or drop decisions
based on snort rules.
%description -l ru_RU.KOI8-R inline+flexresp
Snort, использующий для просмотра трафика функции пакетного фильтра IPTables
вместо библиотеки PCAP. Дополнительные типы правил служат для передачи указаний
от Snort'а пакетному фильтру. Flexresp означает возможность автоматически
блокировать соединения на основании соответствующих правил.
%description -l uk_UA.KOI8-U inline+flexresp
Snort, скомп╕льований з п╕дтримкою IPTables та flexresp.

%package bloat
Summary: Snort with MySQL, PostgreSQL, ODBC, SNMP, ClamAV, IPTables supports and FlexResp
Group: Security/Networking
Requires: %name = %version
Requires: libnet1
%description bloat
Snort compiled with mysql, postgresql, odbc, iptables supports and flexresp support.
%description -l ru_RU.KOI8-R bloat
Snort, скомпилированный с поддержкой всех возможных функций:
- отправка статистики в базу MySQL, PostgreSQL или ODBC,
- отправка уведомлений на центральную сетевую консоль управления по протоколу SNMP,
- проверка трафика антивирусом ClamAV,
- управление пакетным фильтром IPTables,
- автоматическая блокировака опасных соединений через flexresp
  (требует библиотеку libnet).
Хотя сам пакет незначительно отличается по размеру от базового, он требует большого
количества вспомогательных библиотек, поэтому устанавливать его без необходимости
не следует. Вместо этого попробуйте установить пакеты snort с отдельными функциями,
которые вам действительно нужны.
%description -l uk_UA.KOI8-U bloat
Snort, скомп╕льований з п╕дтримкою MySQL, PostgreSQL, ODBC, SNMP, ClamAV, IPTables та flexresp.

%package doc
Summary: Various documentation from Snort IDS distribution.
Summary(ru_RU.KOI8-R): Документация по анализатору сетевого трафика Snort
Group: Security/Networking
BuildArch: noarch
%description doc
Snort manual, FAQ and tons of detailed textual listings
describing all network intrusions known by Snort.
%description doc -l ru_RU.KOI8-R
Руководство пользователя, FAQ, а также детальная документация
по сигнатурам всех сетевых атак, которые распознаёт Snort.

%package dbhints
Summary: Script for creation human readable descriptions in SQL/ODBC database
Summary(ru_RU.KOI8-R): Сценарий создания описаний в SQL/ODBC-базе со статистикой Snort'a
Group: Security/Networking
BuildArch: noarch
%description dbhints
This package contain script that generates three tables in any SQL92 compliant
database providing information useful when analyzing network data.
These tables are intended to supplement the base tables required
for database support in snort in order to make data more human readable.
%description dbhints -l ru_RU.KOI8-R
В этом пакете находится сценарий на языке SQL92, создающий несколько
информационных таблиц в БД 'snort'. Данные таблицы хранят информативные описания
сетевых протоколов, флагов и служб, полезные для построения различных отчётов.

Примечание: сценарий требуется устанавливать и запускать не на том компьютере,
на котором инсталлирован Snort, а на том, на котором работает СУБД с базой данных,
содержащей поступающую от Snort'a статистику.

%prep
%setup -q

%patch0 -p1

mkdir -p building
%autoreconf -I m4

%build

#export LDFLAGS="$LDFLAGS -Wl,--no-as-needed"

function prepconf() {
    local t=$1
    case $t in
	--without* ) return ;;
    esac
    shift

#   echo DEBUG: Configure args: "$@"
#   return

    local d=$1
    shift
    mkdir -p $d
    pushd $d
    ln -s -f ../configure ./configure
    OPENSSL_LIB_DIR=%_libdir \
     %configure \
	--prefix=%_prefix \
	--sysconfdir=%_sysconfdir/%name \
	--enable-linux-smp-stats \
	--with-oracle=no \
    --enable-dynamicplugin \
	%{subst_with prelude} \
	"$@"
    %make    
    mv src/%name ../building/%name-$d
    case "$d" in
        plain)
        mv src/dynamic-plugins/sf_engine/.libs/libsf_engine.so* ../building/
        mv src/dynamic-preprocessors/build/usr/lib/snort_dynamicpreprocessor ../building/
        ;;
        *);;
    esac
    popd
}

prepconf   xxx                    plain               --with-mysql=no  --with-postgresql=no  --with-odbc=no  --enable-inline=no
prepconf %{subst_with mysql}      mysql               --with-mysql=yes --with-postgresql=no  --with-odbc=no  --enable-inline=no
prepconf %{subst_with postgresql} postgresql          --with-mysql=no  --with-postgresql=yes --with-odbc=no  --enable-inline=no
prepconf %{subst_with odbc}       odbc                --with-mysql=no  --with-postgresql=no  --with-odbc=yes --enable-inline=no
prepconf %{subst_with inline}     inline              --with-mysql=no  --with-postgresql=no  --with-odbc=no  --enable-inline=yes
%if_enabled flexresp
prepconf   xxx                    plain+flexresp      --with-mysql=no  --with-postgresql=no  --with-odbc=no   --enable-inline=no  --enable-flexresp
prepconf %{subst_with mysql}      mysql+flexresp      --with-mysql=yes --with-postgresql=no  --with-odbc=no   --enable-inline=no  --enable-flexresp
prepconf %{subst_with postgresql} postgresql+flexresp --with-mysql=no  --with-postgresql=yes --with-odbc=no   --enable-inline=no  --enable-flexresp
prepconf %{subst_with odbc}       odbc+flexresp       --with-mysql=no  --with-postgresql=no  --with-odbc=yes  --enable-inline=no  --enable-flexresp
prepconf %{subst_with inline}     inline+flexresp     --with-mysql=no  --with-postgresql=no  --with-odbc=no   --enable-inline=yes --enable-flexresp
prepconf %{subst_with bloat}      bloat               --with-mysql=yes --with-postgresql=yes --with-odbc=yes  --enable-inline=yes --enable-flexresp
%endif

%install
mkdir -p %buildroot/{%_sbindir,%_initdir,%_man8dir,%_logdir/%name,%_altdir}
mkdir -p %buildroot/%_sysconfdir/{%name,logrotate.d,sysconfig}

weight=0

function myinstall() {
    weight=$[10+$weight]
    test -r "$1" || return 0
    install -m 755 "$1" "%buildroot/%_sbindir/$1"

    # Create record file for alterantives
    printf "%_sbindir/%name\t%_sbindir/$1\t$weight\n" > %buildroot%_altdir/$1
}

mkdir -p %buildroot%_libdir/%name/dynamicengine
mkdir -p %buildroot%_libdir/%name/dynamicpreprocessor/
pushd building
for c in %name-{plain,mysql,postgresql,odbc,inline}; do
    myinstall "$c"
    myinstall "$c+flexresp"
done
myinstall "%name-bloat"
cp -P libsf_engine.so* %buildroot%_libdir/%name/dynamicengine/
chmod 0644 %buildroot%_libdir/%name/dynamicengine/libsf_engine.so*
cp -P snort_dynamicpreprocessor/libsf_*_preproc.so* %buildroot%_libdir/%name/dynamicpreprocessor/
chmod 0644 %buildroot%_libdir/%name/dynamicpreprocessor/libsf_*_preproc.so*
popd

# Create symlink for %%ghost, actually not packaged
pushd %buildroot/%_sbindir
ln -s %name-plain %name
popd

install -m 644 %name.8    %buildroot%_man8dir/
install -m 644 etc/*.{conf,config,map} %buildroot/%_sysconfdir/%name
install -m 744 %SOURCE99  %buildroot/%_initdir/
mkdir -p %buildroot/%_sysconfdir/%name/preproc_rules/
install -m 644 preproc_rules/*.rules %buildroot/%_sysconfdir/%name/preproc_rules/
sed -i 's;^var RULE_PATH \.\./rules;var RULE_PATH \%_sysconfdir/%name/rules;i' %buildroot/%_sysconfdir/%name/%name.conf
sed -i 's;^var PREPROC_RULE_PATH \.\./preproc_rules;var PREPROC_RULE_PATH \%_sysconfdir/%name/preproc_rules;i' \
        %buildroot/%_sysconfdir/%name/%name.conf
sed -i 's;/usr/local/lib/snort_;%_libdir/%name/;' %buildroot/%_sysconfdir/%name/%name.conf

m4 -DSNORT_CONFDIRPATH=%_sysconfdir/%name %SOURCE10 > %buildroot/%_sysconfdir/sysconfig/%name
m4 -DSNORT_LOGPATH=%_logdir/%name %SOURCE30 > %buildroot/%_sysconfdir/logrotate.d/%name
m4 -DSNORT_CONFPATH=%_sysconfdir/%name/%name.conf -DSNORT_BINPATH=%_sbindir/%name %SOURCE20 > README-ALT.ru
m4 -DSNORT_CONFPATH=%_sysconfdir/%name/%name.conf -DSNORT_BINPATH=%_sbindir/%name %SOURCE21 > README-ALT.uk

mkdir -p %buildroot%dbhints_dir
bzcat %SOURCE5 > %buildroot%dbhints_path

%pre
%_sbindir/groupadd -rf %name
%_bindir/id %name > /dev/null 2>&1 \
|| %_sbindir/useradd -c "Snort IDS" -g %name -r -M -d /dev/null -s /dev/null %name

%post
%post_service snortd

%preun
%preun_service snortd

%postun
echo
echo You can delete fakeuser \"%name\" using command:
echo -e "\t%_sbindir/userdel %name"
echo if needed
echo

%files
%doc doc/AUTHORS doc/BUGS doc/CREDITS doc/NEWS doc/PROBLEMS doc/README* doc/TODO doc/USAGE doc/WISHLIST
%doc README-ALT.ru README-ALT.uk
%doc schemas/create_*
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_initdir/snortd
%config(noreplace) %_sysconfdir/logrotate.d/%name
%config(noreplace) %_sysconfdir/%name
%attr(1770,root,snort) %dir %_logdir/%name
%_sbindir/%name-plain
%ghost %_sbindir/%name
%_man8dir/%name.*
%_altdir/%name-plain
%_libdir/%name

%if_with mysql
%files mysql
%_sbindir/%name-mysql
%_altdir/%name-mysql
%endif

%if_with postgresql
%files postgresql
%_sbindir/%name-postgresql
%_altdir/%name-postgresql
%endif

%if_with odbc
%files odbc
%_sbindir/%name-odbc
%_altdir/%name-odbc
%endif

%if_with inline
%files inline
%_sbindir/%name-inline
%_altdir/%name-inline
%endif

%if_enabled flexresp

%files plain+flexresp
%_sbindir/%name-plain+flexresp
%_altdir/%name-plain+flexresp

%if_with mysql
%files mysql+flexresp
%_sbindir/%name-mysql+flexresp
%_altdir/%name-mysql+flexresp
%endif

%if_with postgresql
%files postgresql+flexresp
%_sbindir/%name-postgresql+flexresp
%_altdir/%name-postgresql+flexresp
%endif

%if_with odbc
%files odbc+flexresp
%_sbindir/%name-odbc+flexresp
%_altdir/%name-odbc+flexresp
%endif

%if_with inline
%files inline+flexresp
%_sbindir/%name-inline+flexresp
%_altdir/%name-inline+flexresp
%endif

%if_with bloat
%files bloat
%_sbindir/%name-bloat
%_altdir/%name-bloat
%endif

%endif  # flexresp

%files doc
%doc doc/faq.* doc/snort_manual.* doc/snort_schema_v106.pdf

%files dbhints
%dbhints_dir

%changelog
* Tue Oct 05 2010 Mikhail Efremov <sem@altlinux.org> 2.8.6.1-alt3
- Really rebuild with libmysqlclient.so.16

* Sun Sep 19 2010 Mikhail Efremov <sem@altlinux.org> 2.8.6.1-alt2
- rebuild with libmysqlclient.so.16

* Tue Aug 03 2010 Mikhail Efremov <sem@altlinux.org> 2.8.6.1-alt1
- init script: fix service restart.
- 2.8.6.1
- package snort-dbhints and snort-doc as noarch.

* Mon May 31 2010 Mikhail Efremov <sem@altlinux.org> 2.8.6-alt1
- remove clamav support.
- 2.8.6

* Tue Mar 23 2010 Mikhail Efremov <sem@altlinux.org> 2.8.5.3-alt1
- 2.8.5.3

* Mon Jan 11 2010 Mikhail Efremov <sem@altlinux.org> 2.8.5.2-alt1
- 2.8.5.2

* Tue Nov 10 2009 Mikhail Efremov <sem@altlinux.org> 2.8.5.1-alt2
- drop obsolete configure option '--with-libpcap'.
- enable build with PostgreSQL support.
- disable build with libclamav.
- init script: always use '-D' option.
- fix alternatives files.

* Fri Oct 23 2009 Mikhail Efremov <sem@altlinux.org> 2.8.5.1-alt1
- start snort only for active interfaces.
- init script: display interface for snort.
- not start in chroot in any case.
- completely remove old alternatives.
- spec cleanup.
- removed SNMP support.
- 2.8.5.1 (closes: #11627)

* Sun Dec 14 2008 Ilya Mashkin <oddity@altlinux.ru> 2.4.5-alt4
- enable inline, fix #16686
- fix build with new glibc
- apply repocop patch (remove old alternatives), fix #17620
- remove "-Wl,--no-as-needed" from spec, fix #11147

* Mon Oct 13 2008 Ilya Mashkin <oddity@altlinux.ru> 2.4.5-alt3
- Rebuilt 
- Fixed x86_64 build, thanks to Sergey Y. Afonin
- Brand new version 2.8.3.1 will upload soon

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.4.5-alt2.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Fri Jun 23 2006 Ilya Evseev <evseev@altlinux.ru> 2.4.5-alt2
- fixup ia64 build: assign explicit path for OpenSSL libraries
- suppress warning on 'ghost' macro in comment

* Fri Jun 16 2006 Ilya Evseev <evseev@altlinux.ru> 2.4.5-alt1
- Updated to version 2.4.5 (of course, with SNMP patch renewed..)
- Prelude support is disabled by default because it's no more in Sisyphus
- Re-enable old libraries linking style,
  see http://wiki.sisyphus.ru/devel/UpStream/AsNeeded

* Thu Nov 10 2005 Ilya Evseev <evseev@altlinux.ru> 2.4.3-alt1
- Updated to version 2.4.3, revisite SNMP patch again..
- Replace manually created symlinks from %_sbindir/%name
  to actual snort binaries by modern alternatives
- Bugfix: create %name user/group before install stage, not after

* Tue Sep 20 2005 Ilya Evseev <evseev@altlinux.ru> 2.4.1-alt1
- Updated to version 2.4.1, revisited SNMP patch (#2)

* Mon Aug 15 2005 Ilya Evseev <evseev@altlinux.ru> 2.4.0-alt1
- Updated to version 2.4.0
- Rules and configuration directory skeleton are moved to separate package
  because they're distributed by upstream staff as independent tarball now,
  and updated more frequently than binary core.
- Patchset changes:
   + revisited patchset: SNMP(#2), ClamAV(#13), lib64(#14)
   + removed patch #1 for Prelude support because it is upstream part now!

* Mon Jun 02 2005 Ilya Evseev <evseev@altlinux.ru> 2.3.3-alt2
- changed PostgreSQL requirements: old = libpq3-devel, new = libpq-devel,
  added '--with libpq3' rpmbuild cmdline option for backward compatibility.
  Temporarily disabled because Sisyphus problems.
- small fixes taken from Mandrake Cooker 2.3.1-3mdk build: lib64, timestamp etc.
- use SNMP for sending alerts (mdk)
- use ClamAV for verifying traffic (mdk)
- use IPTables for verifying/managing traffic in addition to PCAP library (mdk)
- provide SQL script for describing flags/proto/services in snort database (mdk)

* Wed Apr 27 2005 Ilya Evseev <evseev@altlinux.ru> 2.3.3-alt1
- Updated to version 2.3.3
- Allow omit building selected targets via 'rpmbuild --without xxx'

* Sun Mar 13 2005 Ilya Evseev <evseev@altlinux.ru> 2.3.2-alt1
- 2.3.2

* Thu Jan 27 2005 Ilya Evseev <evseev@altlinux.ru> 2.3.0-alt1
- 2.3.0
- revisioned prelude patch, use autoreconf instead of autogen.sh
- documentation is packaged separately (including 4MB of signatures descriptions)
- contrib package is obsoleted since upstream does not contain them anymore
- put rules to /etc/snort/rules instead of /etc/snort
- some generated configs are moved from specfile to separate m4-based templates
- specfile cleanups for better reading

* Fri Jan 14 2005 Ilya Evseev <evseev@altlinux.ru> 2.2.0-alt4
- prelude patch is updated to 0.3.6 for snort 2.2.0
- libltdl-devel is explicitly added to BuildPreReq for preventing rebuild failure

* Tue Sep  7 2004 Ilya Evseev <evseev@altlinux.ru> 2.2.0-alt3
- service script improvements:
   + global lockfile for correct shutdown
   + status routine checks per-process lockfiles using new service-0.5.6 feature
   + fixup is_loaded routine

* Sat Aug 28 2004 Ilya Evseev <evseev@altlinux.ru> 2.2.0-alt2
- fixed bug #1272: incorrect /var/log/snort ownership
- fixed bug #4771: snort daemon was not visible by snort service script
- service script is completely rewritten:
   + bugfix feature: when INTERFACES=any,
     all presented network interfaces are enumerated now
   + built-in default options for running daemon
     even sysconfig does not contain ADDPARAM_*
   + bugfix: condstop/condrestart was unusable
   + support virtual interfaces like eth0:1
- bugfix in logrotate: replace "restart" by "condreload"
- sysconfig description updated

* Wed Aug 25 2004 Ilya Evseev <evseev@altlinux.ru> 2.2.0-alt1
- New release
- added "Requires: service" for rejection install under pre-Master 2.4
- Prelude patch is upgraded to 0.3.5 for Snort 2.1.2
- removed separate Prelude README because Prelude patch already includes it.

* Fri Aug  6 2004 Ilya Evseev <evseev@altlinux.ru> 2.1.3-alt1
- New release
- separate Snort version and Prelude patch version because patch may be outdated.
- Prelude patch is upgraded to 0.3.0

* Fri May 14 2004 Serge A. Volkov <vserge@altlinux.ru> 2.1.0-alt2.2
- Add Buildreq: libunixODBC-devel
- Add Requires: libunixODBC for all snort-odbc* packages

* Thu May 13 2004 Serge A. Volkov <vserge@altlinux.ru> 2.1.0-alt2.1
- Rebuild with openssl-0.9.7d

* Fri Feb  6 2004 Serhii Hlodin <hlodin@altlinux.ru> 2.1.0-alt1
- New release
- Enable statistics reporting through proc by default
- Add unixODBC support to bloat package

* Tue Nov 25 2003 Serhii Hlodin <hlodin@altlinux.ru> 2.0.5-alt1
- New release

* Thu Nov  6 2003 Serhii Hlodin <hlodin@altlinux.ru> 2.0.4-alt1
- New release
- Add script for logrotate
- Create new package %name-contrib for all contrib files

* Thu Oct 09 2003 Serhii Hlodin <hlodin@altlinux.ru> 2.0.2-alt1
- New release

* Sat Sep 06 2003 Serhii Hlodin <hlodin@altlinux.ru> 2.0.1-alt3
- Add official Prelude IDS patch from Krzysztof Zaraska
  <kzaraska@student.uci.agh.edu.pl>
- Modify description (russian, ukrainian). Thanks to Michael Shigorin
  <mike@osdn.org.ua>
- Add README-ALT.ru README-ALT.uk files to documentation

* Sat Aug 30 2003 Serhii Hlodin <hlodin@altlinux.ru> 2.0.1-alt2
- Add Prelude IDS patch

* Wed Aug 27 2003 Serhii Hlodin <hlodin@altlinux.ru> 2.0.1-alt1
- fix host endianess problem in udp decoder
- vlan decoding fixes from Michael Pomraning
- add tcp state checking to httpflow
- ignoring bad checksums throughout snort if checksumming is turned on
- config disable_ttcp_alerts is now also config disable_tcpopt_ttcp_alerts
- better initialization handling of low memory conditions pointing to the low memory search engine
- byte_jump / byte_test 2 byte cases handled and unified
- correctly assign port numbers on tcpoption events
- pass rule logic changed to "win" in specific multiple event cases
- named interface support for win32 from the winpcap folks
- spp_bo now also will work with log-only output plugins
- added window detection plugin documentation to manual
- lots of new rules and tons of rule documentation 
- init-script rewrited according to new policy
- remove patch for Prelude IDS

* Wed May 28 2003 Serhii Hlodin <hlodin@altlinux.ru> 2.0.0-alt3
- Fixed spec-file
- Fixed snord startup file

* Tue May 23 2003 Serhii Hlodin <hlodin@altlinux.ru> 2.0.0-alt2
- Update source URL
- Update initscript
- Removed command for delete fakeuser "snort" in %postun section
- Fixed %post section
- Add patch for Prelude IDS

* Sun May 11 2003 Serhii Hlodin <hlodin@altlinux.ru> 2.0.0-alt1
- Initial build based on original SNORT spec-file
