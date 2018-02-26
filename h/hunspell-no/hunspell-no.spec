# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/perl unzip
# END SourceDeps(oneline)
Name: hunspell-no
Summary: Norwegian hunspell dictionaries
Version: 2.0.10
Release: alt1_10
Source: http://alioth.debian.org/frs/download.php/2357/no_NO-pack2-%{version}.zip
Group: Text tools
URL: http://spell-norwegian.alioth.debian.org
License: GPL+
BuildArch: noarch
Source44: import.info

%description
Norwegian hunspell dictionaries.

%package -n hunspell-nb
Summary: Bokmaal hunspell dictionaries
Group: Text tools
Requires: hunspell

%description -n hunspell-nb
Bokmaal hunspell dictionaries.

%package -n hunspell-nn
Summary: Nynorsk hunspell dictionaries
Group: Text tools
Requires: hunspell

%description -n hunspell-nn
Nynorsk hunspell dictionaries.

%package -n hyphen-nb
Summary: Bokmaal hyphenation rules
Group: Text tools
Requires: libhyphen

%description -n hyphen-nb
Bokmaal hyphenation rules.

%package -n hyphen-nn
Summary: Nynorsk hyphenation rules
Group: Text tools
Requires: libhyphen

%description -n hyphen-nn
Nynorsk hyphenation rules

%package -n mythes-nb
Summary: Bokmaal thesaurus
Group: Text tools
Requires: libmythes

%description -n mythes-nb
Bokmaal thesaurus.

%package -n mythes-nn
Summary: Nynorsk thesaurus 
Group: Text tools
Requires: libmythes

%description -n mythes-nn
Nynorsk thesaurus.

%prep
%setup -q -c

%build
unzip -q nb_NO.zip
unzip -q nn_NO.zip
unzip -q hyph_nb_NO.zip
unzip -q hyph_nn_NO.zip
unzip -q th_nb_NO_v2.zip
unzip -q th_nn_NO_v2.zip
for i in README_nb_NO.txt README_nn_NO.txt README_hyph_nb_NO.txt \
  README_hyph_nn_NO.txt README_th_nb_NO_v2.txt README_th_nn_NO_v2.txt; do
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
cp -p nn_NO.aff nn_NO.dic nb_NO.aff nb_NO.dic $RPM_BUILD_ROOT/%{_datadir}/myspell
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_nn_NO.dic hyph_nb_NO.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_nb_NO_v2.dat th_nb_NO_v2.idx th_nn_NO_v2.dat th_nn_NO_v2.idx $RPM_BUILD_ROOT/%{_datadir}/mythes

%files -n hunspell-nb
%doc README_nb_NO.txt
%{_datadir}/myspell/nb_NO.*

%files -n hunspell-nn
%doc README_nn_NO.txt
%{_datadir}/myspell/nn_NO.*

%files -n hyphen-nb
%doc README_hyph_nb_NO.txt
%{_datadir}/hyphen/hyph_nb_NO.*

%files -n hyphen-nn
%doc README_hyph_nn_NO.txt
%{_datadir}/hyphen/hyph_nn_NO.*

%files -n mythes-nb
%doc README_th_nb_NO_v2.txt
%{_datadir}/mythes/th_nb_NO_v2.*

%files -n mythes-nn
%doc README_th_nb_NO_v2.txt
%{_datadir}/mythes/th_nn_NO_v2.*

%changelog
* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt1_10
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt1_9
- rpm Group changed to Text tools

