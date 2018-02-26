# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-ar
Summary: Arabic hunspell dictionaries
%define upstreamid 20080110
Version: 0.%{upstreamid}
Release: alt2_6
Source: http://downloads.sourceforge.net/ayaspell/hunspell-ar_%{upstreamid}.tar.gz
Group: Text tools
URL: http://ayaspell.sourceforge.net/
License: GPLv2 or LGPLv2 or MPLv1.1
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Arabic (Egypt, Algeria, etc.) hunspell dictionaries

%prep
%setup -q -n %{name}_%{upstreamid}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ar.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/ar_TN.dic
cp -p ar.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/ar_TN.aff

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
ar_TN_aliases="ar_AE ar_BH ar_DJ ar_DZ ar_EG ar_ER ar_IL ar_IN ar_IQ ar_JO ar_KM ar_KW ar_LB ar_LY ar_MA ar_MR ar_OM ar_PS ar_QA ar_SA ar_SD ar_SO ar_SY ar_TD ar_YE"
for lang in $ar_TN_aliases; do
	ln -s ar_TN.aff $lang.aff
	ln -s ar_TN.dic $lang.dic
done
popd

%files
%doc AUTHORS ChangeLog-ar COPYING README-ar THANKS
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080110-alt2_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080110-alt2_5
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080110-alt1_5
- import from Fedora by fcimport

