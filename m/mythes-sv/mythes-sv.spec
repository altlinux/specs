Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: mythes-sv
Summary: Swedish thesaurus
Version: 1.3
Release: alt1_25
Source: https://downloads.sourceforge.net/project/aoo-extensions/934/4/swedishthesaurus.oxt
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
* Thu Apr 20 2023 Igor Vlasenko <viy@altlinux.org> 1.3-alt1_25
- update to new release by fcimport

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 1.3-alt1_20
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_12
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_11
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_10
- update to new release by fcimport

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

