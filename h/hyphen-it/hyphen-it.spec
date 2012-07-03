# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hyphen-it
Summary: Italian hyphenation rules
%define upstreamid 20071127
Version: 0.%{upstreamid}
Release: alt1_7
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/hyph_it_IT.zip
Group: Text tools
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: LGPLv2+
BuildArch: noarch
Requires: libhyphen
Provides: hyphen-la = 0.%{upstreamid}-3%{?dist}
Source44: import.info

%description
Italian hyphenation rules.

%prep
%setup -q -c -n hyphen-it
chmod -x *

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_it_IT.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen
pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
#http://extensions.services.openoffice.org/project/dict-la uses the it_IT for Latin
#so we'll do the same
it_IT_aliases="it_CH la_VA"
for lang in $it_IT_aliases; do
        ln -s hyph_it_IT.dic "hyph_"$lang".dic"
done

%files
%doc README_hyph_it_IT.txt
%{_datadir}/hyphen/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20071127-alt1_7
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20071127-alt1_6
- import by fcmass

