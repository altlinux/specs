# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define hyphendir %{_datadir}/hyphen

Name: hyphen-cs
Version: 20060303
Release: alt1_19
Summary: Czech hyphenation rules
License: GPL+
Group:   Text tools
URL: ftp://ftp.linux.cz/pub/localization/OpenOffice.org/devel/Czech/spell_checking/
Source0: openoffice.org-dict-cs_CZ.tar.gz
BuildArch: noarch
Requires: libhyphen
Requires: locales-cs
Obsoletes: openoffice.org-dict-cs_CZ < %{version}-%{release}
Source44: import.info

%description
Czech hyphenation rules.

%prep
%setup -q -n openoffice.org-dict-cs_CZ

%build
iconv -f ISO-8859-2 -t UTF-8 README_hyph_cs_CZ.txt > README_hyph_cs_CZ.txt.new
mv -f README_hyph_cs_CZ.txt.new README_hyph_cs_CZ.txt

%install
mkdir -p $RPM_BUILD_ROOT%{hyphendir}
install -m 644 hyph*.dic $RPM_BUILD_ROOT%{hyphendir}

%files
%doc README_hyph_cs_CZ.txt
%{hyphendir}/hyph_cs*


%changelog
* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 20060303-alt1_19
- new version

