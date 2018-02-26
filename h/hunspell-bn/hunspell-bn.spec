%define upstreamver 0.06

Name: hunspell-bn
Summary: Bengali hunspell dictionaries
Version: %{upstreamver}
Release: alt1_1
#Epoch: 1
Group:          Text tools
Source: http://sourceforge.net/projects/bengalinux/files/bengali-spellcheck/%{name}-%{version}.tar.bz2
URL: http://ankur.org.bd/wiki
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Bengali hunspell dictionaries.

%prep
%setup -q -n %{name}-%{upstreamver}
chmod -x bn.aff  bn.dic  COPYING  Copyright README
chmod -x doc/README
mv bn.aff bn_BD.aff
mv bn.dic bn_BD.dic

# Convert to utf-8
for file in Copyright doc/README; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done


%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
bn_BD_aliases="bn_IN"
for lang in $bn_BD_aliases; do
        ln -s bn_BD.aff $lang.aff
        ln -s bn_BD.dic $lang.dic
done
popd

%files
%doc doc/README COPYING Copyright
%{_datadir}/myspell/*

%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_1
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_4
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_3
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_3
- import from Fedora by fcimport

