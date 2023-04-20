Group: Text tools
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: mythes-bg
Summary: Bulgarian thesaurus
Version: 4.3
Release: alt1_24
Source: http://downloads.sourceforge.net/sourceforge/bgoffice/OOo-thes-bg-%{version}.zip
Requires: libmythes
URL: http://bgoffice.sourceforge.net/
BuildRequires: unzip
License: GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1
BuildArch: noarch
Source44: import.info

%description
Bulgarian thesaurus.

%prep
%setup -q -n OOo-thes-bg-%{version}

%build
for i in ChangeLog Copyright GPL-2.0.txt LGPL-2.1.txt MPL-1.1.txt README.bulgarian; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-2 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done
echo "UTF-8" > th_bg_BG.dat.new
tail -n +2 th_bg_BG.dat | iconv -f WINDOWS-1251 -t UTF-8 | tr -d '\r' >> th_bg_BG.dat.new
mv th_bg_BG.dat.new th_bg_BG.dat
echo "UTF-8" > th_bg_BG.idx.new
tail -n +2 th_bg_BG.idx | iconv -f WINDOWS-1251 -t UTF-8 | tr -d '\r' >> th_bg_BG.idx.new
mv th_bg_BG.idx.new th_bg_BG.idx

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_bg_BG.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_bg_BG_v2.dat
cp -p th_bg_BG.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_bg_BG_v2.idx


%files
%doc ChangeLog Copyright GPL-2.0.txt LGPL-2.1.txt MPL-1.1.txt README.bulgarian
%{_datadir}/mythes/*

%changelog
* Thu Apr 20 2023 Igor Vlasenko <viy@altlinux.org> 4.3-alt1_24
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_12
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_11
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_10
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_4
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_2
- import by fcmass

