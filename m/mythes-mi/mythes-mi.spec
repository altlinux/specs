# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ unzip
# END SourceDeps(oneline)
Name: mythes-mi
Summary: Maori thesaurus
%define upstreamid 20080630
Version: 0.%{upstreamid}
Release: alt1_6
Source: http://packages.papakupu.maori.nz/mythes/mythes-mi-0.1.%{upstreamid}-beta.tar.gz
Group: Text tools
URL: http://papakupu.maori.nz/
License: Public Domain
BuildArch: noarch
Requires: libmythes
Source44: import.info

%description
Maori thesaurus.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p mi.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_mi_NZ_v2.dat
cp -p mi.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_mi_NZ_v2.idx

%files
%doc mi.AUTHORS mi.README mi.LICENSE
%{_datadir}/mythes/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_5
- import by fcmass

