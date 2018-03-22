# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           hyphen-be
Summary:        Belorussian hyphenation rules
Version:        1.1
Release:        alt1_11
Source0:        http://extensions.services.openoffice.org/files/2412/1/dict-be-official.oxt
Group:          Text tools
URL:            http://extensions.services.openoffice.org/project/dict-be-official
License:        GPL+ and LGPLv2+

BuildArch:      noarch

Requires:       libhyphen
Requires: locales-be
Source44: import.info

%description
Belorussian hyphenation rules.

%prep
%setup -q -c

%build
sed -i -e "s/microsoft-cp1251/CP1251/g" be-official.aff hyph_be_BY.dic
tail -n +3 hyph_be_BY.dic| head -n 3 > README_hyph_be_BY

%install
mkdir -p %{buildroot}%{_datadir}/hyphen
cp -p hyph_be_BY.dic %{buildroot}%{_datadir}/hyphen/hyph_be_BY.dic

%files
%doc README_hyph_be_BY
%{_datadir}/hyphen/*


%changelog
* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_11
- new version

