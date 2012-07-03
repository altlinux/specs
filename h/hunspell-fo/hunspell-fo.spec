Name: hunspell-fo
Summary: Faroese hunspell dictionaries
Version: 0.4.1
Release: alt1_1
Source: http://fo.speling.org/filer/myspell-fo-%{version}.tar.bz2
Group: Text tools
URL: http://fo.speling.org/
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Faroese hunspell dictionaries.

%prep
%setup -q -n myspell-fo-%{version}

%build
for i in Copyright contributors README; do
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
%doc README Copyright contributors COPYING
%{_datadir}/myspell/*

%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_1
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1_2
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.44-alt2_1
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.44-alt1_1
- import from Fedora by fcimport

