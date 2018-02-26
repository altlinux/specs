# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-is
Summary: Icelandic hunspell dictionaries
%define upstreamid 20090823
Version: 0.%{upstreamid}
Release: alt2_3
Source: http://extensions.services.openoffice.org/files/2829/1/Icelandic-dict-2009-08-23.oxt
Group: Text tools
URL: http://extensions.services.openoffice.org/project/dict-is
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Icelandic hunspell dictionaries.

%prep
%setup -q -c -n hunspell-is

%build
for i in LICENSE_en_US.txt; do
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
cp -p dictionaries/is_IS.* $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc LICENSE_en_US.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20090823-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20090823-alt2_2
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20090823-alt1_2
- import from Fedora by fcimport

