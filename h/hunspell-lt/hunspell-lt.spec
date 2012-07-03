# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-lt
Summary: Lithuanian hunspell dictionaries
Version: 1.2.1
Release: alt2_7
Source: ftp://ftp.akl.lt/ispell-lt/lt_LT-%{version}.zip
Group: Text tools
URL: ftp://ftp.akl.lt/ispell-lt/
License: BSD
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Lithuanian hunspell dictionaries.

%prep
%setup -q -n lt_LT-%{version}

%build
chmod -x *
for i in INSTRUKCIJOS.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc README.EN INSTRUKCIJOS.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_7
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_6
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_6
- import from Fedora by fcimport

