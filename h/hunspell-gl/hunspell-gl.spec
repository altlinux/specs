# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-gl
Summary: Galician hunspell dictionaries
%define upstreamid 20080515
Version: 0.%{upstreamid}
Release: alt2_5
Source: http://openoffice.mancomun.org/libreeengalego/Corrector/gl_ES-pack.zip
Group: Text tools
URL: http://wiki.mancomun.org/index.php/Corrector_ortogr%%C3%%A1fico_para_OpenOffice.org#Descrici.C3.B3n
License: GPLv2
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Galician hunspell dictionaries.

%prep
%setup -q -c -n hunspell-gl

%build
unzip gl_ES.zip
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc README_gl_ES.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080515-alt2_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080515-alt2_4
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080515-alt1_4
- import from Fedora by fcimport

