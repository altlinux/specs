# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/nasm /usr/bin/yasm gcc-c++ libncurses-devel libsilc-devel libsocket libtinfo-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Summary: SILC Client Library
Name:    libsilc
Version: 1.1.10
Release: alt3_15
License: GPLv2 or BSD
Group:   System/Libraries
URL:     http://www.silcnet.org/
Source0: http://www.silcnet.org/download/toolkit/sources/silc-toolkit-%{version}.tar.bz2
Patch0:  silc-toolkit-1.1-wordsize.patch
Patch1:  silc-toolkit-1.1.5-docinst.patch
Patch2:  silc-toolkit-1.1.10-libs.patch
BuildRequires: libidn-devel
BuildRequires: libtool, autoconf, automake

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
Source44: import.info

%description
SILC Client Library libraries for clients to connect to SILC networks.

SILC (Secure Internet Live Conferencing) is a protocol which provides
secure conferencing services on the Internet over insecure channel.

%package devel
Summary: Headers and shared libraries for %{name}
Group:   Development/C
Requires: libsilc = %{version}
Requires: pkgconfig

%description devel
The SILC Toolkit development libraries and headers. Required for building
SILC clients.

%package doc
Summary: Development documentation for %{name}
Group:   Documentation

%description doc
The SILC Toolkit documentation in HTML format. Useful for writing new SILC
applications.

%prep
%setup -q -n silc-toolkit-%{version}
%patch0 -p1 -b .wordsize
%patch1 -p1 -b .docinst
%patch2 -p1 -b .libs


%build
autoreconf -f -i
%configure --libdir=%{_libdir} --enable-shared --without-libtoolfix \
           --includedir=%{_includedir}/silc --with-simdir=%{_libdir}/silc/modules \
           --docdir="%{_docdir}/%{name}" CFLAGS="$RPM_OPT_FLAGS"

# WARNING! smp flags cause bad binaries!
make

%install
# clear the buildroot

# make install
make DESTDIR=$RPM_BUILD_ROOT install
chmod 0755 ${RPM_BUILD_ROOT}%{_libdir}/lib* ${RPM_BUILD_ROOT}%{_libdir}/silc/modules/*.so

# move doc files that would be deleted by rpm
mkdir docinst
mv $RPM_BUILD_ROOT%{_docdir}/%{name}/{toolkit,tutorial} docinst/
# fix encoding of zlib.html
mv docinst/toolkit/zlib.html docinst/toolkit/zlib.html.orig
iconv -f iso-8859-15 -t utf8 -o docinst/toolkit/zlib.html docinst/toolkit/zlib.html.orig
rm -f docinst/toolkit/zlib.html.orig

# remove files we don't want into the package, but are being installed to buildroot
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/silcalgs.conf $RPM_BUILD_ROOT%{_sysconfdir}/silcd.conf

# remove .a and .la
rm -f $RPM_BUILD_ROOT%{_libdir}/libsilc.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libsilc.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libsilcclient.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libsilcclient.la

# Fix encoding of CREDITS
mv CREDITS CREDITS.orig
iconv -f iso-8859-15 -t utf8 -o CREDITS CREDITS.orig

%check
# If this fails, the filter-provides script needs an update.
[ -d $RPM_BUILD_ROOT%{_libdir}/silc/modules ]

%files
%{_docdir}/%{name}
%exclude %{_docdir}/%{name}/INSTALL
%{_libdir}/libsilc-1.1.so.*
%{_libdir}/libsilcclient-1.1.so.*
%dir %_libdir/silc
%dir %_libdir/silc/modules
%{_libdir}/silc/modules/*.so

# sub-package libsilc-devel
%files devel
%{_libdir}/libsilc.so
%{_libdir}/libsilcclient.so
%{_libdir}/pkgconfig/silc.pc
%{_libdir}/pkgconfig/silcclient.pc
%dir %_includedir/silc
%{_includedir}/silc/*.h

%files doc
%doc COPYING BSD GPL
%doc docinst/toolkit
%doc docinst/tutorial


%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.10-alt3_15
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.1.10-alt3_14
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.10-alt3_13
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.10-alt3_12
- update to new release by fcimport

* Sat Jan 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.10-alt3_11
- update to new release by fcimport

* Tue Aug 20 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.10-alt3_10
- fc update

* Mon Apr 22 2013 Repocop Q. A. Robot <repocop@altlinux.org> 1.1.10-alt3_8.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * arch-dep-package-consists-of-usr-share for libsilc-doc

* Sun Feb 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.10-alt3_8
- update to new release by fcimport

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.10-alt3_7
- applied repocop patches

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.10-alt2_7
- update to new release by fcimport

* Fri Jun 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.10-alt2_6.1
- Fixed build

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.10-alt2_6
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.10-alt2_5
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.10-alt1_5
- initial import by fcimport

