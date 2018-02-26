Name: ipfm
Version: 0.11.5
Release: alt1

Summary: IP Flow Meter - bandwidth analysis tool
License: GPL
Group: Monitoring
Url: http://robert.cheramy.net/%name
Source0: %url/archive/%name-%version.tgz
Source1: %name.service
Source2: %name.cron
Source3: %name.conf

%define crondir %_sysconfdir/cron.weekly

BuildPreReq: libpcap-devel, flex, byacc
#uildPreReq: %crondir

Summary(ru_RU.KOI8-R): IP Flow Meter - анализатор загрузки сетевых интерфейсов

%description
ipfm is a bandwidth analysis tool that starts as system service and counts
how much data was send and received by specified hosts through an Internet link.
ipfm uses PCAP library in normal or promiscuous mode.

%description -l ru_RU.KOI8-R
IP Flow Meter запускается в качестве системного сервиса и подсчитывает
количество байт, принятых и переданных по сети. Накопленные данные
упорядочиваются по IP-адресам компьютеров и с заданной периодичностью
записываются в текстовые файлы в каталоге %_logdir/%name.

IPFM способен одновременно способен вести несколько отчётов
с разными периодами записи и очистки,инкрементными или сбрасываемыми счётчиками,
диапазонами отслеживаемых IP-адресов и направлением данных, и т.д.
К ограничениям IPFM относится невозможность наблюдать
несколько сетевых интерфейсов одновременно.

Для получения сведений из ядра операционной системы IPFM использует
библиотеку PCAP в нормальном или т.н. promiscuous ("подслушивающем") режиме,
в котором анализируется трафик, проходящий не только через локальный компьютер,
но и через все остальные компьютеры в том же физическом сегменте сети.

%prep
%setup -q
%__subst s,@localstatedir@/log,%_logdir,g  Makefile.common.in
%__subst s,@localstatedir@/run,%_var/run,g Makefile.common.in
%configure

%build
%make_build

%install
%make ROOT=%buildroot install
install -pD       %SOURCE1 %buildroot%_initdir/%name
#nstall -pD       %SOURCE2 %buildroot%crondir/%name
install -pD -m600 %SOURCE3 %buildroot%_sysconfdir/%name.conf

%files
%config(noreplace) %_sysconfdir/%name.conf
%_sbindir/%name
%_mandir/*/%name.*
%_logdir/%name
%exclude %_var/run
%_initdir/%name
#crondir/%name

%post                                                                                                                         
%post_service %name

%preun
%preun_service %name

%changelog
* Sat Jul 16 2005 Ilya G. Evseev <evseev@altlinux.ru> 0.11.5-alt1
- Initial build

## EOF ##
