%add_optflags %optflags_shared
Name:		libgcroots
Version:	0.2.3
Release:	alt2_3
License:	MIT
URL:		http://code.google.com/p/sigscheme/wiki/libgcroots

Source0:	http://sigscheme.googlecode.com/files/%{name}-%{version}.tar.bz2


Summary:	Roots acquisition library for Garbage Collector
Group:		Development/C
Source44: import.info

%description
libgcroots abstracts architecture-dependent part of garbage collector
roots acquisition such as register windows of SPARC and register stack
backing store of IA-64.
This library encourages to have own GC such as for small-footprint,
some application-specific optimizations, just learning or to test
experimental ideas.

%package devel
Summary:	Development files for libgcroots
Group:		Development/C
Requires:	libgcroots = %{version}-%{release}

%description devel
libgcroots abstracts architecture-dependent part of garbage collector
roots acquisition such as register windows of SPARC and register stack
backing store of IA-64.

This package contains a header file and development library to help you
to develop any own GC.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install

make install DESTDIR=$RPM_BUILD_ROOT

# Remove unnecessary files
rmdir $RPM_BUILD_ROOT%{_includedir}/libgcroots
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%files
%doc COPYING ChangeLog README
%{_libdir}/libgcroots.so.*

%files devel
%doc COPYING ChangeLog README
%{_includedir}/gcroots.h
%{_libdir}/libgcroots.so
%{_libdir}/pkgconfig/gcroots.pc

%changelog
* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt2_3
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt2_1
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_1
- initial import by fcimport

