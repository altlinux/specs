Name: libgcroots
Version: 0.3.1
Release: alt1

License: MIT
Url: https://github.com/uim/libgcroots

# git://git.altlinux.org/gears/l/libgcroots.git
Source: %name-%version-%release.tar

Summary: Roots acquisition library for Garbage Collector
Group: Development/Other

%description
libgcroots abstracts architecture-dependent part of garbage collector
roots acquisition such as register windows of SPARC and register stack
backing store of IA-64.
This library encourages to have own GC such as for small-footprint,
some application-specific optimizations, just learning or to test
experimental ideas.

%package devel
Summary: Development files for libgcroots
Group: Development/Other
Requires: %name

%description devel
libgcroots abstracts architecture-dependent part of garbage collector
roots acquisition such as register windows of SPARC and register stack
backing store of IA-64.

This package contains a header file and development library to help you
to develop any own GC.

%prep
%setup -n %name-%version-%release

%build
%add_optflags %optflags_shared
%autoreconf
%configure --disable-static
%make_build

%install
make install DESTDIR=%buildroot INSTALL="install -p"

%files
%doc COPYING README
%_libdir/libgcroots.so.*

%files devel
%doc COPYING README
%_includedir/gcroots.h
%_libdir/libgcroots.so
%_libdir/pkgconfig/gcroots.pc

%changelog
* Thu Apr 25 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.3.1-alt1
- Updated to 0.3.1.
- Updated upstream Url.
- Based on Fedora import package, cleaned spec file up.

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt2_14
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt2_12
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt2_11
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt2_10
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt2_9
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt2_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt2_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt2_6
- update to new release by fcimport

* Tue Apr 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt2_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt2_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt2_3
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt2_1
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_1
- initial import by fcimport

