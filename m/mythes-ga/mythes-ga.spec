# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name: mythes-ga
Summary: Irish thesaurus
%define upstreamid 20071001
Version: 0.%{upstreamid}
Release: alt1_8
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/thes_ga_IE_v2.zip
Group: Text tools
URL: http://borel.slu.edu/lsg/index-en.html
BuildRequires: unzip
License: GFDL
BuildArch: noarch
Requires: libmythes
Source44: import.info

%description
Irish thesaurus.

%prep
%setup -q -c

%build
for i in README_th_ga_IE_v2.txt; do
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
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_ga_IE_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

%files
%doc README_th_ga_IE_v2.txt
%{_datadir}/mythes/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20071001-alt1_8
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20071001-alt1_7
- import by fcmass

