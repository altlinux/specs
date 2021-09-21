# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(x11)
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libXcm
Version:        0.5.3
Release:        alt1_20
Summary:        X Color Management Library
License:        MIT
URL:            http://www.oyranos.org
Source0:        http://downloads.sourceforge.net/oyranos/libXcm-%{version}.tar.bz2
BuildRequires:  ctest cmake
BuildRequires:  doxygen
BuildRequires:  graphviz libgraphviz
BuildRequires:  libtool
BuildRequires:  libXfixes-devel
BuildRequires:  libXmu-devel
BuildRequires:  xorg-proto-devel
BuildRequires:  xorg-util-macros
Source44: import.info
Patch33: libXcm-0.5.3-alt-linkage.patch

%description
The libXcm library is a reference implementation of the net-color spec.
It allows to attach color regions to X windows to communicate with color
servers.

%package        devel
Group: Development/C
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch33 -p1

%build
autoreconf -fisv
autoreconf -vif
%configure --disable-static --enable-shared
%make_build

%install
%makeinstall_std
find %{buildroot} -name '*.la' -delete -print



%files
%doc AUTHORS ChangeLog README
%doc --no-dereference COPYING
%{_libdir}/*.so.*

%files devel
%doc docs/*.txt
%{_libdir}/cmake/Xcm/
%{_includedir}/X11/Xcm/
%{_libdir}/*.so
%{_libdir}/pkgconfig/xcm*.pc
%{_mandir}/man3/*.3*

%changelog
* Tue Sep 21 2021 Igor Vlasenko <viy@altlinux.org> 0.5.3-alt1_20
- update to new release by fcimport

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt1_17
- update to new release by fcimport

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt1_13
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt1_9
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt1_7
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt1_6
- update to new release by fcimport

* Sat Oct 17 2015 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt1_5
- new version

* Tue Feb 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_4
- update to new release by fcimport

* Mon Mar 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_2
- update to new release by fcimport

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_3
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_2
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt2_1
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_1
- initial import by fcimport

