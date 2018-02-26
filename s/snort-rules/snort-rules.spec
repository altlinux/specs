Name:     snort-rules
Version:  2.8.5
Release:  alt2

Summary:  Rules for Snort, popular network intrusion detection system
License:  GPL
Group:    Security/Networking
Url:      http://www.snort.org
Source0:  %url/pub-bin/downloads.cgi/Download/vrt_pr/snortrules-pr-2.4.tar.gz
Source1:  Community-Rules-2.8.tar.gz
Source2:  snort-mergesidmaps

BuildArch: noarch
Requires: snort-base

Summary(ru_RU.KOI8-R): Настроечные сигнатуры для системы обнаружения сетевых вторжений Snort

%define   myconfdir   %_sysconfdir/snort
%define   myrulesdir  %myconfdir/rules

%description
Rules for Snort, popular network intrusion detection system.
Standard pack distributed under GNU GPL license.

%description -l ru_RU.KOI8-R
Стандартный набор правил, свободно распространяемых разработчиками
обнаружителя сетевых вторжений Snort. Правила включают в себя т.н. сигнатуры,
т.е. наборы условий, которым должны соответствовать заголовок и содержимое
сетевых пакетов, просматриваемых Snort'ом, а также реакцию на возможное
соответствие - удаление пакета, уведомление администратора и т.д.

%package -n snort-base
Summary: Create base directory structure for Snort NIDS configuration
Summary(ru_RU.KOI8-R): Набор каталогов, используемых разными пакетами IDS Snort
Group: Security/Networking
Conflicts: snort < 2.4
%description -n snort-base
Create base directory structure for Snort NIDS configuration files.
%description -n snort-base -l ru_RU.KOI8-R
Пустой пакет, создающий каталоги, совместно используемые остальными пакетами,
на которые разбит обнаружитель сетевых атак (IDS) Snort.

%package doc
Summary: Detailed descriptions for standard rules used by Snort NIDS.
Summary(ru_RU.KOI8-R): Описания стандартных сигнатур для анализатору сетевого трафика Snort
Group: Security/Networking
%description doc
Tons of detailed textual listings describing all network intrusions known by Snort.
%description doc -l ru_RU.KOI8-R
Детальная документация по сигнатурам сетевых атак, входящим в базовый комплект
поставки свободной версии Snort - системы обнаружения сетевых вторжений.

%prep
%setup -q -c
cd rules
mv sid sid.1st
cd ..
%setup -q -D -T -a 1
cd rules
#__mv sid sid.2nd
cd ..

%build  #..nothing to do

%install
mkdir -p %buildroot{%myrulesdir,%_bindir}
install -pm 644 rules/*.rules rules/cgi-bin.list %buildroot%myrulesdir
install -p %SOURCE2 %buildroot%_bindir

echo "Generate maps..."
d=$PWD
cd %buildroot%myrulesdir
%SOURCE2 $d/rules/*sid-msg.map
cd -
echo "...done!"

%files -n snort-base
%dir %myconfdir

%files
%_bindir/snort-*
%config(noreplace) %myrulesdir
%doc rules/VRT-License.txt

%files doc
%doc doc/signatures/* docs/*

%changelog
* Mon Oct 26 2009 Mikhail Efremov <sem@altlinux.org> 2.8.5-alt2
- use config(noreplace) for rules.

* Fri Oct 23 2009 Mikhail Efremov <sem@altlinux.org> 2.8.5-alt1
- spec cleanup.
- rules from Debian package.

* Fri Jun 16 2006 Ilya Evseev <evseev@altlinux.ru> 2.4.5-alt1
- updated to latest state (community rules are grown from 11k to 55k)

* Thu Nov 10 2005 Ilya Evseev <evseev@altlinux.ru> 2.4.3-alt1
- update standard rules, added community rules
- added snort-mergesidmaps helper

* Fri Aug 12 2005 Ilya Evseev <evseev@altlinux.ru> 2.4-alt1
- initial tarball from upstream (previously rules were distributed
  in single tarball with Snort binaries) and initial package for ALTLinux
- snort-base package owns /etc/snort directory used by multiple packages

## EOF ##
