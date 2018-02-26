# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-uz
Summary: Uzbek hunspell dictionaries
Version: 0.6
Release: alt2_5
Source0: http://www-user.uni-bremen.de/~kmashrab/uzbek-word-list/uzbek-wordlist-%{version}.tar.bz2
Group: Text tools
URL: http://www-user.uni-bremen.de/~kmashrab/uzbek-word-list
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Uzbek hunspell dictionaries.

%prep
%setup -q -n uzbek-wordlist-%{version}

%build
cd hunspell
make
cp -p README ../README.hunspell

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p hunspell/uz_UZ* $RPM_BUILD_ROOT/%{_datadir}/myspell/

%files
%doc ChangeLog Copyright README README.hunspell COPYING TODO
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_4
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_4
- import from Fedora by fcimport

