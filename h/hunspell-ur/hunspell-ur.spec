# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-ur
Summary: Urdu hunspell dictionaries
Version: 0.64
Release: alt2_4
#http://urdudictionary.codeplex.com/Release/ProjectReleases.aspx?ReleaseId=30004#DownloadId=74761
#and click yes to agree to LGPLv2+, which stinks as a download-url :-(
Source: UrduDictionary.xpi
Group: Text tools
URL: http://urdudictionary.codeplex.com
License: LGPLv2+
BuildArch: noarch
BuildRequires: libredland

Requires: hunspell
Source44: import.info

%description
Urdu hunspell dictionaries.

%prep
%setup -q -c -n hunspell-ur

%build
rdfproc hunspell-ur parse install.rdf
rdfproc hunspell-ur print | grep install-manifest | grep -v targetApplication | sed -e 's/.*#//' | sed -e 's/], "/: /'| sed -e 's/"}//' > CREDITS

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/ur.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/ur_PK.aff
cp -p dictionaries/ur.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/ur_PK.dic
pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
ur_PK_aliases="ur_IN"
for lang in $ur_PK_aliases; do
        ln -s ur_PK.aff $lang.aff
        ln -s ur_PK.dic $lang.dic
done
popd

%files
%doc CREDITS
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.64-alt2_4
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.64-alt2_3
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.64-alt1_3
- import from Fedora by fcimport

