# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-so
Summary: Somali hunspell dictionaries
Version: 1.0.2
Release: alt2_2
Group: Text tools
Source: http://extensions.services.openoffice.org/e-files/2727/2/dict-so.oxt
URL: http://www.opensourcesomalia.org/index.php?page=hingaad-saxe
License: GPLv2+
BuildArch: noarch
Requires: hunspell
Source44: import.info

%description
Somali hunspell dictionaries.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p so_SO.* $RPM_BUILD_ROOT/%{_datadir}/myspell

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
so_SO_aliases="so_DJ so_ET so_KE"
for lang in $so_SO_aliases; do
        ln -s so_SO.aff $lang.aff
        ln -s so_SO.dic $lang.dic
done
popd


%files
%doc README_so_SO.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_2
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_1
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_1
- import from Fedora by fcimport

