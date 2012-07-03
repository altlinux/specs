# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-csb
Summary: Kashubian hunspell dictionaries
%define upstreamid 20050311
Version: 0.%{upstreamid}
Release: alt2_6
Group: Text tools
Source: http://ftp.gnu.org/gnu/aspell/dict/csb/aspell6-csb-0.02-0.tar.bz2
URL: http://borel.slu.edu/crubadan/apps.html
License: GPL+
BuildArch: noarch
BuildRequires: aspell libhunspell-devel hunspell-utils

Requires: hunspell
Source44: import.info

%description
Kashubian hunspell dictionaries.

%prep
%setup -q -n aspell6-csb-0.02-0

%build
export LANG=csb_PL.utf8
preunzip csb.cwl
wordlist2hunspell csb.wl csb_PL
for i in Copyright doc/Crawler.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc COPYING Copyright README doc/Crawler.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050311-alt2_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050311-alt2_5
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050311-alt1_5
- import from Fedora by fcimport

