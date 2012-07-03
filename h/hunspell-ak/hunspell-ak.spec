# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-ak
Summary: Akan hunspell dictionaries
Version: 0.6
Release: alt2_4
Group: Text tools
Source: http://releases.mozilla.org/pub/mozilla.org/addons/9978/akan_ns__mfuaasekyer__-%{version}-fx.xpi
URL: http://kasahorow.org/content/akan-nsɛmfuaasekyerɛ
#https://addons.mozilla.org/en-US/firefox/versions/license/73122
License: LGPLv3
BuildArch: noarch
BuildRequires: libredland

Requires: hunspell
Source44: import.info

%description
Akan hunspell dictionaries.

%prep
%setup -q -c

%build
rdfproc hunspell-oc parse install.rdf
rdfproc hunspell-oc print | grep install-manifest | grep -v targetApplication | sed -e 's/.*#//' | sed -e 's/], "/: /'| sed -e 's/"}//' > CREDITS
chmod -x dictionaries/ak-GH.*

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/ak-GH.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/ak_GH.aff
cp -p dictionaries/ak-GH.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/ak_GH.dic

%files
%doc CREDITS
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_4
- update to new release by fcimport

* Wed Sep 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_3
- new release by fedoraimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_2
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_2
- import from Fedora by fcimport

