# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# in case of update, update also hyphen-cs, it's the same source

%define languageenglazy Czech
%define languagecode    cs
%define lc_ctype        cs_CZ

Name:           hunspell-%{languagecode}
Version:        20060303
Release:        alt2_21
Summary:        %{languageenglazy} hunspell dictionaries
License:        GPL+
Group:          Text tools
URL:            ftp://ftp.linux.cz/pub/localization/OpenOffice.org/devel/Czech/spell_checking/
Source0:        openoffice.org-dict-cs_CZ.tar.gz

BuildArch:      noarch

Requires:       hunspell hunspell-utils

Requires:       locales-cs
#Mageia values: 1 - aspell, 2 - hunspell, 3 - language specific
Provides:       enchant-dictionary = 2
Provides:       hunspell-dictionary
Provides:       hunspell-%{lc_ctype} = %{version}-%{release}
#Generic providing - see Mageia values
Provides:       dictionary-%{languagecode} = 2 
Provides:       dictionary-%{lc_ctype} = 2

#MySpell is deprecated
Obsoletes:      myspell-%{languagecode} < 1.0.3
Provides:       myspell-%{languagecode}
Obsoletes:      myspell-%{lc_ctype} < 1.0.3
Provides:       myspell-%{lc_ctype}

# Something old unknown thing..
Obsoletes: openoffice.org-dict-cs_CZ < %{version}-%{release}

AutoReqProv:    no
Source44: import.info

%description
%{languageenglazy} hunspell dictionaries.


%prep
%setup -q -n openoffice.org-dict-cs_CZ

%build
iconv -f ISO-8859-2 -t UTF-8 README_hyph_cs_CZ.txt > README_hyph_cs_CZ.txt.new
mv -f README_hyph_cs_CZ.txt.new README_hyph_cs_CZ.txt

%install
install -D -m 0644 -p cs*.dic %{buildroot}%{_datadir}/hunspell/%{lc_ctype}.dic
install -D -m 0644 -p cs*.aff %{buildroot}%{_datadir}/hunspell/%{lc_ctype}.aff

#backward compatibility
mkdir -p %{buildroot}%{_datadir}/myspell
pushd %{buildroot}%{_datadir}/myspell
    ln -s ../hunspell/%{lc_ctype}.dic %{lc_ctype}.dic
    ln -s ../hunspell/%{lc_ctype}.aff %{lc_ctype}.aff
popd #%%{buildroot}%%{_datadir}/myspell

%files
%doc README_cs_CZ.txt
%{_datadir}/hunspell/*
%{_datadir}/myspell/*


%changelog
* Sat Mar 24 2018 Igor Vlasenko <viy@altlinux.ru> 20060303-alt2_21
- fixed group

* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 20060303-alt1_21
- new version

