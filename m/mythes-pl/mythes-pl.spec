# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ unzip
# END SourceDeps(oneline)
Name: mythes-pl
Summary: Polish thesaurus
Version: 1.5
Release: alt1_7
Source: http://downloads.sourceforge.net/synonimy/OOo2-Thesaurus-%{version}.zip
Group: Text tools
URL: http://synonimy.ux.pl/
BuildRequires: perl
License: LGPLv2+
BuildArch: noarch
Requires: libmythes
Source44: import.info

%description
Polish thesaurus.

%prep
%setup -q -c

%build
for i in README_th_pl_PL_v2.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-2 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_pl_PL_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

%files
%doc README_th_pl_PL_v2.txt
%{_datadir}/mythes/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_7
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_6
- import by fcmass

