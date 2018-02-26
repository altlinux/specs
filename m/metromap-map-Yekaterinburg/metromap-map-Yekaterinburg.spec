Name: metromap-map-Yekaterinburg
Version: 20070205
Release: alt1

Summary: Metro map for Yekaterinburg
License: distributable
Group: Office

Source: %name-%version.tar.bz2
Url: http://pmetro.nm.ru/Ekaterinburg.htm

BuildArch: noarch

BuildPreReq: unzip

%description
Yekaterinburg metro map (for metromap)

%prep
%setup

%build
unzip Ekaterinburg.pmz

%install
install -pD -m644 Metro.ini %buildroot%_datadir/metromap/data/Yekaterinburg/Metro.ini

%files
%_datadir/metromap/data/Yekaterinburg/

%changelog
* Sat Feb 17 2007 Andrey Rahmatullin <wrar@altlinux.ru> 20070205-alt1
- initial build

