Name:			cinnamon-applet-system-monitor
Version:		3.11
Release:		alt1
Packager:		Motsyo Gennadi <drool@altlinux.ru>
License:		GPLv2
Summary:		System monitor with graphs
Summary(ru_RU.UTF8):	Системный монитор с графиками
Summary(uk_UA.UTF8):	Системний монітор з графіками
Group:			Monitoring
Url:			https://github.com/pixunil/cinnamon-applet-system-monitor
Source0:		%name.tar.xz

BuildArch:		noarch

Requires:		libgtop-gir /usr/bin/cinnamon-settings

# Automatically added by buildreq on Sun Sep 10 2017 (-bi)
# optimized out: python-base python-modules python3 python3-base rpm-build-python3 xz
BuildRequires: python3-dev rpm-build-gir

%description
An applet for Cinnamon which shows CPU, Memory and Swap usage, Disk and Network rates with graphs

%description -l ru_RU.UTF8
Апплет с графиками для Cinnamon с отображением использования ЦПУ, ОЗУ и раздела swap, нагрузка диска и сети

%description -l uk_UA.UTF8
Аплет з графіками для Cinnamon з відображенням використання ЦПУ, ОЗП і розділу swap, навантаження диска та мережі

%prep
%setup -n %name

%install
mkdir -p %buildroot%_datadir/cinnamon/applets/system-monitor@pixunil
cp -a {*.js,*.py,*.json,modules,po} %buildroot%_datadir/cinnamon/applets/system-monitor@pixunil/

%files
%doc *.md LICENSE
%_datadir/cinnamon/applets/system-monitor@pixunil

%changelog
* Sun Sep 10 2017 Motsyo Gennadi <drool@altlinux.ru> 3.11-alt1
- initial build for ALT Linux
