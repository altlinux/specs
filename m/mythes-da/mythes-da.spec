# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ unzip
# END SourceDeps(oneline)
Name: mythes-da
Summary: Danish thesaurus
%define upstreamid 20100629.15.16
Version: 0.%{upstreamid}
Release: alt1_3
Source: http://extensions.services.openoffice.org/e-files/1388/12/DanskeSynonymer.oxt
Group: Text tools
URL: http://synonym.oooforum.dk
License: GPLv2 or LGPLv2 or MPLv1.1
BuildArch: noarch
Requires: libmythes
Source44: import.info

%description
Danish thesaurus.

%prep
%setup -q -c

%build
for i in README_th_da_DK.txt README_th_da_DK.txt README_th_en-US.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_da_DK.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_da_DK_v2.dat
cp -p th_da_DK.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_da_DK_v2.idx

%files
%doc README_th_da_DK.txt README_th_en-US.txt release_note.txt
%{_datadir}/mythes/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20100629.15.16-alt1_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20100629.15.16-alt1_2
- import by fcmass

