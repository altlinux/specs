# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-smj
Summary: Lule Saami hunspell dictionaries
Version: 1.0
Release: alt2_0.4.beta7
Source: http://divvun.no/static_files/hunspell-smj.tar.gz
Group: Text tools
URL: http://www.divvun.no/index.html
License: GPLv3
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Lule Saami hunspell dictionaries.

%prep
%setup -q -n %{name}-1.0beta7.20090316

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p smj.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/smj_NO.aff
cp -p smj.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/smj_NO.dic

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
smj_NO_aliases="smj_SE"
for lang in $smj_NO_aliases; do
        ln -s smj_NO.aff $lang.aff
        ln -s smj_NO.dic $lang.dic
done

%files
%doc Copyright README GPL-3
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.4.beta7
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.3.beta7
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.3.beta7
- import from Fedora by fcimport

