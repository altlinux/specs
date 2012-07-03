# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-ast
Summary: Asturian hunspell dictionaries
#Epoch: 1
Version: 0.02
Release: alt1_2
Group: Text tools
Source: http://extensions.services.openoffice.org/e-files/3932/1/asturianu.oxt
URL: http://softastur.org/
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Asturian hunspell dictionaries.

%prep
%setup -q -c

%build
chmod -x dictionaries/*

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/ast.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/ast_ES.aff
cp -p dictionaries/ast.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/ast_ES.dic

%files
%doc LICENSES-en.txt LICENCES-ast.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_2
- update to new release by fcimport

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2_2
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_2
- import from Fedora by fcimport

