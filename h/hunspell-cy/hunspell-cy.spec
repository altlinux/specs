# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-cy
Summary: Welsh hunspell dictionaries
%define upstreamid 20040425
Version: 0.%{upstreamid}
Release: alt2_7
Source: http://www.e-gymraeg.co.uk/myspell/myspell.zip
Group: Text tools
URL: http://www.e-gymraeg.co.uk/
License: GPL+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Welsh hunspell dictionaries.

%prep
%setup -q -c -n hunspell-cy

%build
unzip PackWelsh.zip
unzip cy_GB.zip
chmod -x *
for i in README_cy_GB.txt; do
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
%doc README_cy_GB.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20040425-alt2_7
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20040425-alt2_6
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20040425-alt1_6
- import from Fedora by fcimport

