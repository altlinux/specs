# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/perl gcc-c++ unzip
# END SourceDeps(oneline)
%define oldname mythes
Name:      libmythes
Summary:   A thesaurus library
Version:   1.2.2
Release:   alt1_2
Source:    http://downloads.sourceforge.net/hunspell/%{oldname}-%{version}.tar.gz
Group:     System/Libraries
URL:       http://hunspell.sourceforge.net/
License:   BSD
BuildRequires: libhunspell-devel hunspell-utils
Source44: import.info

%description
MyThes is a simple thesaurus that uses a structured text data file and an
index file with binary search to look up words and phrases and return 
information on part of speech, meanings, and synonyms.

%package devel
Requires: libmythes = %{version}-%{release}
Summary: Files for developing with mythes
Group: Development/C

%description devel
Includes and definitions for developing with mythes

%prep
%setup -q -n %{oldname}-%{version}

%build
%configure --disable-rpath --disable-static
make %{?_smp_mflags}

%check
./example th_en_US_new.idx th_en_US_new.dat checkme.lst
./example morph.idx morph.dat morph.lst morph.aff morph.dic

%install
make DESTDIR=$RPM_BUILD_ROOT install
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
* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_2
- update to new release by fcimport

* Tue Jan 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_3
- new version

