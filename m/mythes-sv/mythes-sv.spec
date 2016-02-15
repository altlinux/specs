# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: mythes-sv
Summary: Swedish thesaurus
Version: 1.3
Release: alt1_9
Source: http://extensions.services.openoffice.org/files/934/3/SwedishThesaurus.oxt
Group: Text tools
URL: http://extensions.services.openoffice.org/project/SweThes
License: MIT
BuildArch: noarch
Requires: libmythes
Source44: import.info

%description
Swedish thesaurus.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p dictionaries/th_sv_SE.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_sv_SE_v2.dat
cp -p dictionaries/th_sv_SE.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_sv_SE_v2.idx
pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
sv_SE_aliases="sv_FI"
for lang in $sv_SE_aliases; do
        ln -s th_sv_SE_v2.dat "th_"$lang"_v2.dat"
        ln -s th_sv_SE_v2.idx "th_"$lang"_v2.idx"
done
popd

%files
%doc Info-en.txt
%{_datadir}/mythes/*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_4
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_2
- import by fcmass

