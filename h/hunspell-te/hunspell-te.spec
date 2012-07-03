%define lang te
%define langrelease 2
%define langversion 0.01

Name: hunspell-te
Summary: Telugu hunspell dictionaries
%define upstreamid 20050929
Version: 0.%{upstreamid}
Release: alt2_8
Group:          Text tools
##Upstream is unresponsive so unable to verify license version
License:        GPL+
URL:            http://aspell.net/
Source0:        ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell6-%{lang}-%{langversion}-%{langrelease}.tar.bz2
BuildArch:      noarch
BuildRequires:  aspell >= 0.60
BuildRequires:  libhunspell-devel hunspell-utils
Requires:       hunspell
Source44: import.info

%description
Telugu hunspell dictionaries.This package
contains the efforts of aspell-te that converted by
wordlist2hunspell.

%prep
%setup -q -n aspell6-%{lang}-%{langversion}-%{langrelease}
prezip-bin -d < te.cwl > te.txt

%build
export LANG=te_IN.utf8
wordlist2hunspell te.txt te_IN

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files 
%doc COPYING Copyright
%{_datadir}/myspell/*

%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050929-alt2_8
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050929-alt2_7
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050929-alt2_6
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050929-alt1_6
- import from Fedora by fcimport

