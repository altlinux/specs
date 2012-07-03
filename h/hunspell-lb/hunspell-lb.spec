# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-lb
Summary: Luxembourgish hunspell dictionaries
%define upstreamid 20110821
Version: 0.%{upstreamid}
Release: alt1_2
Source: http://downloads.spellchecker.lu/packages/OOo3/SpellcheckerLu.oxt
Group: Text tools
URL: http://spellchecker.lu
License: EUPL 1.1
BuildArch: noarch
Requires: hunspell
Source44: import.info

%description
Luxembourgish hunspell dictionaries.

%package -n mythes-lb
Summary: Luxembourgish thesaurus
Group: Text tools
Requires: libmythes

%description -n mythes-lb
Luxembourgish thesaurus.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_lb_LU_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

%files
%doc registration/README_lb_LU.txt
%{_datadir}/myspell/*

%files -n mythes-lb
%doc registration/README_lb_LU.txt
%{_datadir}/mythes/th_lb_LU_v2.*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20110821-alt1_2
- update to new release by fcimport

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110821-alt1_1
- update to new release by fcimport

* Tue Aug 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110709-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110412-alt1_1
- rpm Group changed to Text tools

