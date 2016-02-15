# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/docbook-to-man /usr/bin/docbook2html /usr/bin/doxygen /usr/bin/valgrind libexpat-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libcmml
Version:        0.9.1
Release:        alt3_17
Summary:        Library for handling Continuous Media Markup Language

Group:          System/Libraries
License:        BSD
URL:		http://www.annodex.net/
Source:		http://www.annodex.net/software/libcmml/download/%{name}-%{version}.tar.gz

BuildRequires:	doxygen
BuildRequires:	expat-devel

# libtool
BuildRequires:	gcc-c++
Source44: import.info
Patch33: libcmml-0.9.1-alt-link-libm.patch

%description
Libcmml is a library which enables the handling of documents
written in CMML (Continuous Media Markup Language) for the
Continuous Media Web (CMWeb).

It provides a very simple API for reading files marked up with the
Continuous Media Markup Language (CMML), and returns C structures
containing this information in a format which can be used by an
Annodexer for creating ANNODEX(tm) format documents (ANX).

%package devel
Summary:	Files needed for development using libcmml
Group:          Development/C
Requires:       libcmml = %{version}
Requires:       pkgconfig

%description devel
Libcmml is a library which enables the handling of documents
written in CMML (Continuous Media Markup Language) for the
Continuous Media Web (CMWeb).

It provides a very simple API for reading files marked up with the
Continuous Media Markup Language (CMML), and returns C structures
containing this information in a format which can be used by an
Annodexer for creating ANNODEX(tm) format documents (ANX).

This package contains the header files and documentation needed for
development using libcmml.

%prep
%setup -q -n %{name}-%{version}
%patch33 -p1

%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
make docdir=/doxygen DESTDIR=$RPM_BUILD_ROOT install
mv $RPM_BUILD_ROOT/doxygen .

# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# remove doxygen build stamp; fixed in upstream CVS
rm -f $RPM_BUILD_ROOT%{_datadir}/doc/libcmml/doxygen-build.stamp

%files
%doc AUTHORS ChangeLog COPYING NEWS README
# zero length NEWS file
# %doc NEWS
%{_libdir}/libcmml.so.*
%{_bindir}/cmml*

%files devel
%doc doxygen/html
%{_libdir}/libcmml.so
%{_libdir}/pkgconfig/cmml.pc
%{_includedir}/cmml.h

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt3_17
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt3_16
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt3_15
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt3_14
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt3_13
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt3_12
- update to new release by fcimport

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt3_11
- applied repocop patches

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_11
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_10
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_9
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_9
- initial import by fcimport

