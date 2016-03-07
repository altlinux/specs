Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-sr
Summary: Serbian hunspell dictionaries
%global upstreamid 20130330
Version: 0.%{upstreamid}
Release: alt1_6
Source: http://extensions.services.openoffice.org/e-files/ext/1572/10/dict-sr.oxt
URL: http://extensions.services.openoffice.org/project/dict-sr
License: LGPLv3
BuildArch: noarch
Requires: hunspell
Provides: hunspell-bs = %{version}-%{release}
Source44: import.info

%description
Serbian hunspell dictionaries.

%package -n hyphen-sr
Group: Text tools
Requires: libhyphen
Summary: Serbian hyphenation rules
Provides: hyphen-bs = %{version}-%{release}

%description -n hyphen-sr
Serbian hyphenation rules.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p sr.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/sr_YU.dic
cp -p sr.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/sr_YU.aff
cp -p sr-Latn.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/sh_YU.dic
cp -p sr-Latn.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/sh_YU.aff

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_sr.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_sr_YU.dic
cp -p hyph_sr-Latn.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_sh_YU.dic

sr_YU_aliases="sr_ME sr_RS"
sh_YU_aliases="sh_ME sh_RS bs_BA"

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
for lang in $sr_YU_aliases; do
	ln -s sr_YU.aff $lang.aff
	ln -s sr_YU.dic $lang.dic
done
for lang in $sh_YU_aliases; do
	ln -s sh_YU.aff $lang.aff
	ln -s sh_YU.dic $lang.dic
done
popd

pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
for lang in $sr_YU_aliases; do
	ln -s hyph_sr_YU.dic "hyph_"$lang".dic"
done
for lang in $sh_YU_aliases; do
	ln -s hyph_sh_YU.dic "hyph_"$lang".dic"
done
popd


%files
%doc registration/license*.txt
%{_datadir}/myspell/*

%files -n hyphen-sr
%doc registration/license*.txt
%{_datadir}/hyphen/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20130330-alt1_6
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20130330-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20130330-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20130330-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20130330-alt1_2
- update to new release by fcimport

* Tue Apr 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.20130330-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20100920-alt2_6
- update to new release by fcimport

* Fri Nov 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.20100920-alt2_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20100920-alt2_4
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20100920-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20100920-alt2_2
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20100920-alt1_2
- import from Fedora by fcimport

