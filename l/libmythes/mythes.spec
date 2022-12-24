Group: System/Libraries
%define oldname mythes
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:      libmythes
Summary:   A thesaurus library
Version:   1.2.5
Release:   alt1_1
Source:    https://github.com/hunspell/%{oldname}/releases/download/v%{version}/%{oldname}-%{version}.tar.xz
URL:       https://github.com/hunspell/mythes
License:   BSD and MIT
BuildRequires: hunspell-utils libhunspell-devel, gcc-c++
Source44: import.info

%description
MyThes is a simple thesaurus that uses a structured text data file and an
index file with binary search to look up words and phrases and return 
information on part of speech, meanings, and synonyms.

%package devel
Group: Development/Other
Requires: libmythes = %{version}-%{release}, pkgconfig
Summary: Files for developing with mythes

%description devel
Includes and definitions for developing with mythes

%prep
%setup -n %{oldname}-%{version} -q

%build
%configure --disable-rpath --disable-static
%make_build

%check
make check
./example th_en_US_new.idx th_en_US_new.dat checkme.lst
./example morph.idx morph.dat morph.lst morph.aff morph.dic

%install
%makeinstall_std
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes



%files
%doc README COPYING AUTHORS
%{_libdir}/*.so.*
%{_datadir}/mythes

%files devel
%doc data_layout.txt
%{_includedir}/mythes.hxx
%{_libdir}/*.so
%{_libdir}/pkgconfig/mythes.pc
%{_bindir}/th_gen_idx.pl

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 1.2.5-alt1_1
- update to new release by fcimport

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt1_15
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt1_8
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt1_6
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt1_4
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt1_2
- update to new release by fcimport

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt1_1
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_4
- update to new release by fcimport

* Fri Nov 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_3
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_2
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_1
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_2
- update to new release by fcimport

* Tue Jan 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_3
- new version

