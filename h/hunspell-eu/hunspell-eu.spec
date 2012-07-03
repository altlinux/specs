# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-eu
Summary: Basque hunspell dictionaries
%define upstreamid 20080507
Version: 0.%{upstreamid}
Release: alt2_5
Source0: http://www.euskara.euskadi.net/r59-20660/eu/contenidos/informacion/euskarazko_softwarea/eu_9567/adjuntos/eu-ES-hunspell.tar.gz
Source1: http://www.euskara.euskadi.net/r59-20660/eu/contenidos/informacion/euskarazko_softwarea/eu_9567/adjuntos/XUXEN_kode_irekia_eskuliburua-LINUX-OO.pdf
Group: Text tools
URL: http://www.euskara.euskadi.net/r59-20660/eu/contenidos/informacion/euskarazko_softwarea/eu_9567/xuxen.html
License: GPLv2
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Basque hunspell dictionaries.

%prep
%setup -q -c -n hunspell-eu
cp -p %{SOURCE1} .

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p eu-ES/eu-ES.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/eu_ES.dic
cp -p eu-ES/eu-ES.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/eu_ES.aff

%files
%doc XUXEN_kode_irekia_eskuliburua-LINUX-OO.pdf
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080507-alt2_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080507-alt2_4
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080507-alt1_4
- import from Fedora by fcimport

