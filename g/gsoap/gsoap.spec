Summary: Generator Tools for Coding SOAP/XML Web Services in C and C++
Name: gsoap
Version: 2.7.15
Release: alt1.1
License: GPLv2+
Group: Development/Tools
URL: http://gsoap2.sourceforge.net
Packager: Evgeny Sinelnikov <sin@altlinux.ru>
Source0: http://downloads.sourceforge.net/gsoap2/gsoap_%version.tar.gz
Patch: %name-%version-%release.patch

#packagereq: optimized out: glibc-devel-static glibc-pthread libcom_err-devel libkrb5-devel libstdc++-devel perl-threads
BuildRequires: dos2unix flex gcc-c++ libssl-devel libstdc++-devel-static tzdata zlib-devel

# Dirty hack with undefined symbols by design:
#  struct namespaces;
#  soap_faultstring();
#  soap_getfault();
#  soap_serializefault();
#  soap_putfault();
#  soap_faultdetail();
#  soap_faultsubcode();
#  soap_getheader();
#  soap_serializeheader();
#  soap_faultcode();
#  soap_putheader();
# for libraries:
#  libgsoapck.so.0.0.0
#  libgsoapck++.so.0.0.0
#  libgsoap.so.0.0.0
#  libgsoap++.so.0.0.0
#  libgsoapssl.so.0.0.0
#  libgsoapssl++.so.0.0.0
%set_verify_elf_method unresolved=relaxed


%description
The gSOAP Web services development toolkit offers an XML to C/C++
language binding to ease the development of SOAP/XML Web services in C
and C/C++.


%package -n lib%name
Summary: Devel libraries and headers for linking with gSOAP generated stubs
Group: Development/C
Provides: %name = %version-%release
Requires: openssl

%description -n lib%name
The gSOAP Web services development toolkit offers an XML to C/C++
language binding to ease the development of SOAP/XML Web services in C
and C/C++.


%package -n lib%name-devel
Summary: Devel libraries and headers for linking with gSOAP generated stubs
Group: Development/C
Requires: %name = %version-%release
Requires: pkgconfig

%description -n lib%name-devel
gSOAP libraries, headers and generators for linking with and creating
gSOAP generated stubs


%package -n lib%name-devel-static
Summary: Static devel libraries and headers for linking with gSOAP generated stubs
Group: Development/C
Provides: %name-devel = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
gSOAP static libraries


%prep
%setup -q -n gsoap-2.7
%patch -p1

# a number of ~ files are distribute, but we do not want them
find . -name "*~" -exec rm {} \;

# we want all txt files to have unix end-of-line encoding
dos2unix README.txt LICENSE.txt NOTES.txt


%build
# patches change autoconf and automake files, so we must reconfigure
autoreconf --install --force

%configure --prefix=/usr

# dependencies are not declared properly
#make %{?_smp_mflags}
make

# during the build a number of files that we should not distribute are
# created in soapcpp2/samples/ (a doc directory), we must remove them
#find soapcpp2/samples/ -name ".deps" -prune -exec rm -rf {} \;

# we do not want to bother distributing samples for Windows or OS X
#rm -rf soapcpp2/samples/magic_VC
#rm -rf soapcpp2/samples/quote_VC
#rm -rf soapcpp2/samples/quote_MAC_ProjBuild

# samples do not need to be executable by default
#chmod a-x soapcpp2/samples/ssl/root.sh
#chmod a-x soapcpp2/samples/ssl/cacerts.pem


%install
make install DESTDIR=%buildroot


%check
make check


%files -n lib%name
%doc README.txt NOTES.txt LICENSE.txt
%_libdir/libgsoapck.so.0
%_libdir/libgsoapck++.so.0
%_libdir/libgsoapck.so.0.0.0
%_libdir/libgsoapck++.so.0.0.0
%_libdir/libgsoap.so.0
%_libdir/libgsoap++.so.0
%_libdir/libgsoap.so.0.0.0
%_libdir/libgsoap++.so.0.0.0
%_libdir/libgsoapssl.so.0
%_libdir/libgsoapssl++.so.0
%_libdir/libgsoapssl.so.0.0.0
%_libdir/libgsoapssl++.so.0.0.0


%files -n lib%name-devel-static
%_libdir/libgsoapck.a
%_libdir/libgsoapck++.a
%_libdir/libgsoap.a
%_libdir/libgsoapssl.a
%_libdir/libgsoapssl++.a
%_libdir/libgsoap++.a


%files -n lib%name-devel
%doc README.txt NOTES.txt LICENSE.txt
%_bindir/soapcpp2
%_bindir/wsdl2h
%_libdir/libgsoapck.so
%_libdir/libgsoapck++.so
%_libdir/libgsoap.so
%_libdir/libgsoapssl.so
%_libdir/libgsoapssl++.so
%_libdir/libgsoap++.so
%_includedir/stdsoap2.h
%dir %_datadir/gsoap
%dir %_datadir/gsoap/import
%_datadir/gsoap/import/c14n.h
%_datadir/gsoap/import/dom.h
%_datadir/gsoap/import/ds2.h
%_datadir/gsoap/import/ds.h
%_datadir/gsoap/import/README.txt
%_datadir/gsoap/import/soap12.h
%_datadir/gsoap/import/stldeque.h
%_datadir/gsoap/import/stl.h
%_datadir/gsoap/import/stllist.h
%_datadir/gsoap/import/stlset.h
%_datadir/gsoap/import/stlvector.h
%_datadir/gsoap/import/wsa3.h
%_datadir/gsoap/import/wsa4.h
%_datadir/gsoap/import/wsa5.h
%_datadir/gsoap/import/wsa.h
%_datadir/gsoap/import/WS-example.c
%_datadir/gsoap/import/WS-example.h
%_datadir/gsoap/import/WS-Header.h
%_datadir/gsoap/import/wsp.h
%_datadir/gsoap/import/wsrp.h
%_datadir/gsoap/import/wsse2.h
%_datadir/gsoap/import/wsse.h
%_datadir/gsoap/import/wsu.h
%_datadir/gsoap/import/xlink.h
%_datadir/gsoap/import/xmime4.h
%_datadir/gsoap/import/xmime5.h
%_datadir/gsoap/import/xmime.h
%_datadir/gsoap/import/xml.h
%_datadir/gsoap/import/xmlmime5.h
%_datadir/gsoap/import/xmlmime.h
%_datadir/gsoap/import/xop.h
%_datadir/gsoap/import/stdstring.h
%_datadir/gsoap/import/xsd.h
%dir %_datadir/gsoap/WS
%_datadir/gsoap/WS/README.txt
%_datadir/gsoap/WS/WS-Addressing.xsd
%_datadir/gsoap/WS/WS-Addressing03.xsd
%_datadir/gsoap/WS/WS-Addressing04.xsd
%_datadir/gsoap/WS/WS-Addressing05.xsd
%_datadir/gsoap/WS/WS-Discovery.wsdl
%_datadir/gsoap/WS/WS-Enumeration.wsdl
%_datadir/gsoap/WS/WS-Policy.xsd
%_datadir/gsoap/WS/WS-Routing.xsd
%_datadir/gsoap/WS/WS-typemap.dat
%_datadir/gsoap/WS/discovery.xsd
%_datadir/gsoap/WS/ds.xsd
%_datadir/gsoap/WS/enumeration.xsd
%_datadir/gsoap/WS/typemap.dat
%_datadir/gsoap/WS/wsse.xsd
%_datadir/gsoap/WS/wsu.xsd
%dir %_datadir/gsoap/custom
%_datadir/gsoap/custom/README.txt
%_datadir/gsoap/custom/long_double.c
%_datadir/gsoap/custom/long_double.h
%_datadir/gsoap/custom/struct_timeval.c
%_datadir/gsoap/custom/struct_timeval.h
%_datadir/gsoap/custom/struct_tm.c
%_datadir/gsoap/custom/struct_tm.h
%dir %_datadir/gsoap/extras
%_datadir/gsoap/extras/README.txt
%_datadir/gsoap/extras/ckdb.c
%_datadir/gsoap/extras/ckdb.h
%_datadir/gsoap/extras/ckdbtest.c
%_datadir/gsoap/extras/ckdbtest.h
%_datadir/gsoap/extras/fault.cpp
%_datadir/gsoap/extras/logging.cpp
%_datadir/gsoap/extras/soapdefs.h
%dir %_datadir/gsoap/plugin
%_datadir/gsoap/plugin/README.txt
%_datadir/gsoap/plugin/cacerts.c
%_datadir/gsoap/plugin/cacerts.h
%_datadir/gsoap/plugin/httpda.c
%_datadir/gsoap/plugin/httpda.h
%_datadir/gsoap/plugin/httpdatest.c
%_datadir/gsoap/plugin/httpdatest.h
%_datadir/gsoap/plugin/httpform.c
%_datadir/gsoap/plugin/httpform.h
%_datadir/gsoap/plugin/httpget.c
%_datadir/gsoap/plugin/httpget.h
%_datadir/gsoap/plugin/httpgettest.c
%_datadir/gsoap/plugin/httpgettest.h
%_datadir/gsoap/plugin/httpmd5.c
%_datadir/gsoap/plugin/httpmd5.h
%_datadir/gsoap/plugin/httpmd5test.c
%_datadir/gsoap/plugin/httpmd5test.h
%_datadir/gsoap/plugin/httppost.c
%_datadir/gsoap/plugin/httppost.h
%_datadir/gsoap/plugin/logging.c
%_datadir/gsoap/plugin/logging.h
%_datadir/gsoap/plugin/md5evp.c
%_datadir/gsoap/plugin/md5evp.h
%_datadir/gsoap/plugin/plugin.c
%_datadir/gsoap/plugin/plugin.h
%_datadir/gsoap/plugin/smdevp.c
%_datadir/gsoap/plugin/smdevp.h
%_datadir/gsoap/plugin/threads.c
%_datadir/gsoap/plugin/threads.h
%_datadir/gsoap/plugin/wsaapi.c
%_datadir/gsoap/plugin/wsaapi.h
%_datadir/gsoap/plugin/wsse2api.c
%_datadir/gsoap/plugin/wsse2api.h
%_datadir/gsoap/plugin/wsseapi.c
%_datadir/gsoap/plugin/wsseapi.h
%_datadir/gsoap/plugin/wsseapi.cpp
%_libdir/pkgconfig/gsoapck.pc
%_libdir/pkgconfig/gsoapck++.pc
%_libdir/pkgconfig/gsoap.pc
%_libdir/pkgconfig/gsoap++.pc
%_libdir/pkgconfig/gsoapssl.pc
%_libdir/pkgconfig/gsoapssl++.pc
# Additions in 2.7.12-1
%_datadir/gsoap/WS/WS-ReliableMessaging.wsdl
%_datadir/gsoap/WS/WS-ReliableMessaging.xsd
%_datadir/gsoap/WS/reference-1.1.xsd
%_datadir/gsoap/WS/ws-reliability-1.1.xsd
%_datadir/gsoap/import/ref.h
%_datadir/gsoap/import/wsrm.h
%_datadir/gsoap/import/wsrm4.h
%_datadir/gsoap/import/wsrx.h
# Additions in 2.7.15
%_datadir/gsoap/plugin/httpposttest.h
%_datadir/gsoap/plugin/httpposttest.c


%changelog
* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 2.7.15-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Tue Mar 09 2010 Evgeny Sinelnikov <sin@altlinux.ru> 2.7.15-alt1
- Initial build for Sisyphus

* Fri Sep 18 2009 Lubomir Rintel <lkundrak@v3.sk> - 2.7.13-2
- Fix build

* Mon May 11 2009  <matt@redhat> - 2.7.13-1
- Updated to gsoap 2.7.13

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Tomas Mraz <tmraz@redhat.com> - 2.7.12-2
- rebuild with new openssl

* Wed Dec 24 2008  <matt@redhat> - 2.7.12-1
- Updated to gsoap 2.7.12:
-  Numerous bug fixes - xml:lang, maxOccurs="unbounded", SSL, xmlns="", ...
-  New features, maintaining backward compatibility - MinGW, wsseapi, multi-endpoint connect, ...
- Patches removed (incorporated upstream):
-  datadir_importpath-2.7.10.patch
-  install_soapcpp2_wsdl2h_aux-2.7.10.patch
-  no_locale.patch as default off, enable by defining WITH_C_LOCALE
- Patches added (sent upstream):
-  unused_args.patch - eliminate many unused param warnings

* Thu Feb 21 2008  <mfarrellee@redhat> - 2.7.10-4
- Applied upd patch from upstream. It fixes glibc C locale issues,
  hp-ux h_errno definition, and xsd:dateTime timezone processing for
  WS-I
- Removed tru64_hp_ux patches, they are present in upstream's upd
  patch
- Added no_locale.patch to stop configure from checking for locale
  version of functions

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.7.10-3
- Autorebuild for GCC 4.3

* Mon Feb 18 2008  <mfarrellee@redhat> - 2.7.10-2
- Removed --disable-namespaces from configure, result is code compiled
  against gsoap does not need to call set_soap_namespaces

* Sun Jan 27 2008  <mfarrellee@redhat> - 2.7.10-1
- Upgraded to 2.7.10 release
- Stopped hosting patches on grid.et.redhat.com
- Removed import_dom_h patch, it was integrated
- Removed large autotools patch, replaced with patch
  (use_libtool-2.7.10.patch) changing configure.in, gsoap/Makefile.am
  and gsoap/wsdl/Makefile.am, which enable libtool use, and a
  call to autoreconf
- Changed soapcpp2 references to gsoap as per new layout of source
  distribution
- Updated tru64_hp_up_c/pp patches to handle new source layout
- Install of soapcpp2/import with cp removed in favor of a patch to
  gsoap/Makefile.am (install_soapcpp2_wsdl2h_aux-2.7.10.patch)
- No pre-generated Makefiles are distributed, no longer removing them
- stdsoap2_cpp.cpp not in distribution, no longer removing it
- Added datadir_importpath-2.7.10.patch to set SOAPCPP2_IMPORT_PATH
  and WSDL2H_IMPORT_PATH, useful defaults, using ${datadir} instead of
  `pwd`
- Added autoconf, automake and libtool to BuildRequires, because
  configure.in and gsoap/Makefile.am are patched
- Added ?dist to Release

* Fri Nov 30 2007  <mfarrellee@redhat> - 2.7.9-0.4.l
- Added OpenSSL requirement

* Tue Nov 27 2007  <mfarrellee@redhat> - 2.7.9-0.3.l
- Decided soapcpp2/import/ files should be in /usr/share instead of
  /usr/include because they are not really headers gcc can
  process. Also, this is likely the location new versions of gsoap
  will install the import headers. People should use -I
  /usr/share/gsoap/import

* Mon Nov 26 2007  <mfarrellee@redhat> - 2.7.9-0.2.l
- Changed license tag to GPLv2+, which is more accurate
- Resolved bz399761 by adding soapcpp2/import/*.h to the -devel
  package as /usr/include/gsoap, users will need to add -I
  /usr/include/gsoap to their soapcpp2 line

* Sun Sep 30 2007  <mfarrellee@redhat> - 2.7.9-0.1.l
- Updated to 2.7.9l (2.7.9k patches still apply)
- Added patch for import/dom.h missing xsd__anyAttribute definitions
- Removed removal of .deps directories and autom4te.cache

* Mon Sep 24 2007  <mfarrellee@redhat> - 2.7.9-0.2.k
- Moved pkgconfig requirement to -devel package

* Tue Sep 11 2007  <mfarrellee@redhat> - 2.7.9-0.1.k
- Initial release

