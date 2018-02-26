# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-sv
Summary: Swedish hunspell dictionaries
Version: 1.48
Release: alt1_2
Source: http://dsso.googlecode.com/files/sv-%{version}.zip
Group: Text tools
URL: http://dsso.se/
License: LGPLv2+ or GPLv2+ or MPLv1.1
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Swedish hunspell dictionaries.

%prep
%setup -q -c -n hunspell-sv

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
sv_SE_aliases="sv_FI"
for lang in $sv_SE_aliases; do
        ln -s sv_SE.aff $lang.aff
        ln -s sv_SE.dic $lang.dic
done
popd

%files
%doc README_sv_SE.txt

%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.48-alt1_2
- update to new release by fcimport

* Sun Dec 11 2011 Igor Vlasenko <viy@altlinux.ru> 1.48-alt1_1
- update to new release by fcimport

* Fri Nov 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.47-alt1_1
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.46-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.44-alt2_2
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.44-alt1_2
- import from Fedora by fcimport

