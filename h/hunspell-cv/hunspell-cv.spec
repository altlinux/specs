# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-cv
Summary: Chuvash hunspell dictionaries
Version: 1.02
Release: alt2_3
Group: Text tools
Source: http://hunspell.chv.su/files/dict-cv.oxt
URL: http://hunspell.chv.su/download.shtml
License: LGPLv2+
BuildArch: noarch
Requires: hunspell
Source44: import.info

%description
Chuvash hunspell dictionaries.

%prep
%setup -q -c

%build
for i in README_cv_RU.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p cv_RU.* $RPM_BUILD_ROOT/%{_datadir}/myspell/

%files
%doc README_cv_RU.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.02-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.02-alt2_2
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1_2
- import from Fedora by fcimport

