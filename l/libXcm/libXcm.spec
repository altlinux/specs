# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(x11) pkgconfig(xfixes) pkgconfig(xmu)
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
Name:           libXcm
Version:        0.5.3
Release:        alt1_6
Summary:        X Color Management Library
License:        MIT
URL:            http://www.oyranos.org
Source0:        http://downloads.sourceforge.net/oyranos/libXcm-%{version}.tar.bz2
BuildRequires: ctest cmake
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  libXfixes-devel
BuildRequires:  libXmu-devel
BuildRequires: xorg-bigreqsproto-devel xorg-compositeproto-devel xorg-damageproto-devel xorg-dmxproto-devel xorg-evieproto-devel xorg-fixesproto-devel xorg-fontsproto-devel xorg-glproto-devel xorg-inputproto-devel xorg-kbproto-devel xorg-pmproto-devel xorg-randrproto-devel xorg-recordproto-devel xorg-renderproto-devel xorg-resourceproto-devel xorg-scrnsaverproto-devel xorg-videoproto-devel xorg-xcbproto-devel xorg-xcmiscproto-devel xorg-xextproto-devel xorg-xf86bigfontproto-devel xorg-xf86dgaproto-devel xorg-xf86driproto-devel xorg-xf86rushproto-devel xorg-xf86vidmodeproto-devel xorg-xineramaproto-devel xorg-xproto-devel
BuildRequires:  xorg-util-macros
BuildRequires:  xorg-xtrans-devel
Source44: import.info
Patch33: libXcm-0.5.3-alt-linkage.patch

%description
The libXcm library is a reference implementation of the net-color spec.
It allows to attach color regions to X windows to communicate with color
servers.

%package        devel
Group: Development/C
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}
Requires:       libX11-devel%{?_isa}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch33 -p1

%build
autoreconf -fisv
%configure --disable-static --enable-shared
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
find %{buildroot} -name '*.la' -delete -print

%files
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/*.so.*

%files devel
%doc docs/*.txt
%{_libdir}/cmake/Xcm/
%{_includedir}/X11/Xcm/
%{_libdir}/*.so
%{_libdir}/pkgconfig/xcm*.pc
%{_mandir}/man3/*.3*

%changelog
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

