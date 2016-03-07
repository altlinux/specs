Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%global ver_date 2014-11-08

Summary: Arabic hunspell dictionaries
Name: hunspell-ar
Version: 3.5
Release: alt1_4
License: GPLv2 or LGPLv2 or MPLv1.1
URL: http://ayaspell.sourceforge.net/
Source: http://sourceforge.net/projects/ayaspell/files/hunspell-ar_%{version}.%{ver_date}.zip

BuildArch: noarch
Requires: hunspell
Source44: import.info

%description
Arabic (Egypt, Algeria, etc.) hunspell dictionaries.

%prep
%setup -q -c

%build
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ar.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/ar_TN.dic
cp -p ar.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/ar_TN.aff

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
ar_TN_aliases="ar_AE ar_BH ar_DJ ar_DZ ar_EG ar_ER ar_IL ar_IN ar_IQ ar_JO ar_KM ar_KW ar_LB ar_LY ar_MA ar_MR ar_OM ar_PS ar_QA ar_SA ar_SD ar_SO ar_SY ar_TD ar_YE"
for lang in $ar_TN_aliases; do
    ln -s ar_TN.aff $lang.aff
    ln -s ar_TN.dic $lang.dic
done
popd

%files
%doc AUTHORS ChangeLog-ar COPYING README-* THANKS
%{_datadir}/myspell/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 3.5-alt1_4
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 3.5-alt1_3
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 3.5-alt1_2
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 3.5-alt1_1
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 3.2-alt1_2
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20080110-alt2_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20080110-alt2_9
- update to new release by fcimport

* Mon Nov 19 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080110-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080110-alt2_7
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080110-alt2_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080110-alt2_5
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080110-alt1_5
- import from Fedora by fcimport

