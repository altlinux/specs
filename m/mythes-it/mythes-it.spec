# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ unzip
# END SourceDeps(oneline)
Name: mythes-it
Summary: Italian thesaurus
Version: 2.0.9l
Release: alt1_7
Source: http://downloads.sourceforge.net/sourceforge/linguistico/thesaurus2_it_02_09_l_2008_11_29.zip
Group: Text tools
URL: http://linguistico.sourceforge.net/pages/thesaurus_italiano.html
License: AGPLv3
BuildArch: noarch
Requires: libmythes
Source44: import.info

%description
Italian thesaurus.

%prep
%setup -q -c

%build
for i in th_it_IT_README th_it_IT_ChangeLog th_it_IT_AUTHORS; do
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
cp -p th_it_IT.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_it_IT_v2.dat
cp -p th_it_IT.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_it_IT_v2.idx

pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
it_IT_aliases="it_CH"
for lang in $it_IT_aliases; do
        ln -s th_it_IT_v2.dat "th_"$lang"_v2.dat"
        ln -s th_it_IT_v2.idx "th_"$lang"_v2.idx"
done

%files
%doc th_it_IT_README th_it_IT_ChangeLog th_it_IT_COPYING th_it_IT_INSTALL th_it_IT_copyright_licenza.txt th_it_IT_lettera_in_inglese.txt  th_it_IT_AUTHORS
%{_datadir}/mythes/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.9l-alt1_7
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.9l-alt1_6
- import by fcmass

