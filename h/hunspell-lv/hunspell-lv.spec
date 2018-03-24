# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# In case of update, update also hyphen-lv and mythes-lv, it's the same source

%define languageenglazy Latvian
%define languagecode    lv
%define lc_ctype        lv_LV

Name:           hunspell-%{languagecode}
Version:        0.9.4
Release:        alt2_13
Summary:        %{languageenglazy} hunspell dictionaries
License:        LGPLv2+
Group:          Text tools
URL:            http://dict.dv.lv/
Source0:        http://dict.dv.lv/download/lv_LV-%{version}.oxt

BuildArch:      noarch

Requires:       hunspell hunspell-utils

Requires:       locales-lv
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

AutoReqProv:    no
Source44: import.info

%description
%{languageenglazy} hunspell dictionaries.


%prep
%setup -q -c

%build
for i in README_lv_LV.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-4 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done
chmod -x *.dic

%install
install -D -m 0644 -p lv_LV.dic %{buildroot}%{_datadir}/hunspell/%{lc_ctype}.dic
install -D -m 0644 -p lv_LV.aff %{buildroot}%{_datadir}/hunspell/%{lc_ctype}.aff

#backward compatibility
mkdir -p %{buildroot}%{_datadir}/myspell
pushd %{buildroot}%{_datadir}/myspell
    ln -s ../hunspell/%{lc_ctype}.dic %{lc_ctype}.dic
    ln -s ../hunspell/%{lc_ctype}.aff %{lc_ctype}.aff
popd #%%{buildroot}%%{_datadir}/myspell

%files
%doc README_lv_LV.txt license.txt
%{_datadir}/hunspell/*
%{_datadir}/myspell/*


%changelog
* Sat Mar 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt2_13
- fixed group

* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt1_13
- new version

