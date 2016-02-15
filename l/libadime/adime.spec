%define oldname adime
Name:           libadime
Version:        2.2.1
Release:        alt2_20
Summary:        Allegro Dialogs Made Easy
Group:          System/Libraries
License:        zlib
URL:            http://adime.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{oldname}/%{oldname}-%{version}.tar.gz
Patch0:         adime-2.2.1-so-fixes.patch
BuildRequires:  liballegro-devel texinfo
Source44: import.info

%description
Adime is a portable add-on library for Allegro with functions for generating
Allegro dialogs in a very simple way. Its main purpose is to give as easy an
API as possible to people who want dialogs for editing many kinds of input
data.


%package devel
Summary: Development libraries and headers for adime
Group: Development/C
Requires: libadime = %{version}

%description devel
The developmental files that must be installed in order to compile
applications which use adime.


%prep
%setup -n %{oldname}-%{version} -q
%patch0 -p1 -z .so-fixes
./fix.sh unix
rm docs/txt/tmpfile.txt
mkdir docs/html docs/rtf


%build
make %{?_smp_mflags} lib docs \
  CFLAGS="-fPIC -DPIC $RPM_OPT_FLAGS" \
  CFLAGS_NO_OPTIMIZE="-fPIC -DPIC $RPM_OPT_FLAGS" \
  LFLAGS=-g


%install
make install install-man install-info \
  SYSTEM_DIR=$RPM_BUILD_ROOT/usr \
  SYSTEM_LIB_DIR=$RPM_BUILD_ROOT%{_libdir} \
  SYSTEM_MAN_DIR=$RPM_BUILD_ROOT%{_mandir} \
  SYSTEM_INFO_DIR=$RPM_BUILD_ROOT%{_infodir}
rm $RPM_BUILD_ROOT%{_infodir}/dir
ln -s libadime.so.0 $RPM_BUILD_ROOT%{_libdir}/libadime.so


%files
%doc license.txt thanks.txt changes.txt
%{_libdir}/libadime.so.0

%files devel
%doc readme.txt docs/txt/*.txt docs/rtf docs/html
%{_includedir}/adime.h
%{_includedir}/adime
%{_libdir}/libadime.so
%{_mandir}/man3/*
%{_infodir}/adime.info.*


%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt2_20
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt2_19
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt2_18
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt2_17
- update to new release by fcimport

* Tue Oct 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt2_16
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt2_15
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt2_14
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt2_13
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt2_12
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_12
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_11
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_10
- converted from Fedora by srpmconvert script

