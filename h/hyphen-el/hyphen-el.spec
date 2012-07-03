# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hyphen-el
Summary: Greek hyphenation rules
%define upstreamid 20051018
Version: 0.%{upstreamid}
Release: alt1_6
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/hyph_el_GR.zip
Group: Text tools
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: LGPLv2+
BuildArch: noarch

Requires: libhyphen
Source44: import.info

%description
Greek hyphenation rules.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p *.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
el_GR_aliases="el_CY"
for lang in $el_GR_aliases; do
        ln -s hyph_el_GR.dic hyph_$lang.dic
done

%files
%doc README_hyph_el_GR.txt
%{_datadir}/hyphen/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20051018-alt1_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20051018-alt1_5
- import by fcmass

