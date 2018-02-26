# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-wa
Summary: Walloon hunspell dictionaries
Version: 0.4.15
Release: alt2_6
Source0: http://chanae.walon.org/walon/aspell-wa-%{version}.tar.bz2
Group: Text tools
URL: http://chanae.walon.org/walon/aspell.php
License: LGPLv2+
BuildArch: noarch
Patch0: hunspell-wa-0.4.15-buildfix.patch

Requires: hunspell
Source44: import.info

%description
Walloon hunspell dictionaries.

%prep
%setup -q -n aspell-wa-%{version}
%patch0 -p1 -b .buildfix

%build
make myspell
for i in TODO README; do
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
cp -p wa.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/wa_BE.dic
cp -p wa.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/wa_BE.aff

%files
%doc README LGPL ChangeLog TODO
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.15-alt2_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.15-alt2_5
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.15-alt1_5
- import from Fedora by fcimport

