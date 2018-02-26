# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-el
Summary: Greek hunspell dictionaries
#Epoch: 1
Version: 0.8
Release: alt2_3
Source: http://ispell.math.upatras.gr/files/ooffice/el_GR-%{version}.zip
Group: Text tools
URL: http://ispell.math.upatras.gr/?section=oofficespell&subsection=howto
License: GPLv2+ or LGPLv2+ or MPL
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Greek hunspell dictionaries.

%prep
%setup -q -c -n hunspell-el

%build
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
el_GR_aliases="el_CY"
for lang in $el_GR_aliases; do
        ln -s el_GR.aff $lang.aff
        ln -s el_GR.dic $lang.dic
done

%files
%doc README_el_GR.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.8-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.8-alt2_2
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_2
- import from Fedora by fcimport

