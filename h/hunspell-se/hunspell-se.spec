# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-se
Summary: Northern Saami hunspell dictionaries
Version: 1.0
Release: alt2_0.4.beta7
Source: http://divvun.no/static_files/hunspell-se.tar.gz
Group: Text tools
URL: http://www.divvun.no/index.html
License: GPLv3
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Northern Saami hunspell dictionaries.

%prep
%setup -q -n %{name}-1.0beta7.20090316

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p se.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/se_NO.aff
cp -p se.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/se_NO.dic

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
se_NO_aliases="se_SE se_FI"
for lang in $se_NO_aliases; do
        ln -s se_NO.aff $lang.aff
        ln -s se_NO.dic $lang.dic
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

