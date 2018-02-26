Name: libxmlsec1
Version: 1.2.18
Release: alt1
License: MIT
Summary: Library providing support for "XML Signature" and "XML Encryption" standards
Group: System/Libraries
Source0: http://www.aleksey.com/xmlsec/download/xmlsec1-%version.tar.gz
Url: http://www.aleksey.com/xmlsec/

# Automatically added by buildreq on Fri Jun 08 2012
# optimized out: libgpg-error libgpg-error-devel libnspr-devel libxml2-devel pkg-config
BuildRequires: help2man libgcrypt-devel libgnutls-devel libltdl7-devel libnss-devel libssl-devel libxslt-devel man

%description
XML Security Library is a C library based on LibXML2  and OpenSSL.
The library was created with a goal to support major XML security
standards "XML Digital Signature" and "XML Encryption".

%package devel
Summary: Libraries, includes, etc. to develop applications with XML Digital Signatures and XML Encryption support
Group: System/Libraries
Requires: libxmlsec1

%description devel
Libraries, includes, etc. you can use to develop applications with XML Digital
Signatures and XML Encryption support.

%package openssl
Summary: OpenSSL crypto plugin for XML Security Library
Group: System/Libraries
Requires: libxmlsec1

%description openssl
OpenSSL plugin for XML Security Library provides OpenSSL based crypto services
for the xmlsec library.

%package openssl-devel
Summary: OpenSSL crypto plugin for XML Security Library
Group: System/Libraries
Requires: libxmlsec1-devel libxmlsec1-openssl

%description openssl-devel
Libraries, includes, etc. for developing XML Security applications with OpenSSL

%package gcrypt
Summary: GCrypt crypto plugin for XML Security Library
Group: System/Libraries
Requires: libxmlsec1

%description gcrypt
GCrypt plugin for XML Security Library provides GCrypt based crypto services
for the xmlsec library.

%package gcrypt-devel
Summary: GCrypt crypto plugin for XML Security Library
Group: System/Libraries
Requires: libxmlsec1-devel libxmlsec1-gcrypt

%description gcrypt-devel
Libraries, includes, etc. for developing XML Security applications with GCrypt.

%package gnutls
Summary: GNUTls crypto plugin for XML Security Library
Group: System/Libraries
Requires: libxmlsec1 libxmlsec1-gcrypt

%description gnutls
GNUTls plugin for XML Security Library provides GNUTls based crypto services
for the xmlsec library.

%package gnutls-devel
Summary: GNUTls crypto plugin for XML Security Library
Group: System/Libraries
Requires: libxmlsec1-devel libxmlsec1-gcrypt-devel libxmlsec1-gnutls

%description gnutls-devel
Libraries, includes, etc. for developing XML Security applications with GNUTls.

%package nss
Summary: NSS crypto plugin for XML Security Library
Group: System/Libraries
Requires: libxmlsec1

%description nss
NSS plugin for XML Security Library provides NSS based crypto services
for the xmlsec library

%package nss-devel
Summary: NSS crypto plugin for XML Security Library
Group: System/Libraries
Requires: libxmlsec1-devel libxmlsec1-nss

%description nss-devel
Libraries, includes, etc. for developing XML Security applications with NSS.

%prep
%setup -n xmlsec1-%version

%build
%configure --disable-static --enable-gost
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

## positively ugly but only sane way to get around #192756
## sed 's+/lib64+/$archlib+g' < xmlsec1-config | sed 's+/lib+/$archlib+g' | sed 's+ -DXMLSEC_NO_SIZE_T++' > xmlsec1-config.$$ && mv xmlsec1-config.$$ xmlsec1-config
sed -i 's/ -DXMLSEC_NO_SIZE_T//' xmlsec1-config

%install
mkdir -p %buildroot/usr/bin
mkdir -p %buildroot/usr/include/xmlsec1
mkdir -p %buildroot%_libdir
mkdir -p %buildroot/usr/man/man1

make DESTDIR=%buildroot install
rm -f %buildroot%_libdir/*.la

%check
# TODO for those who care
true || LD_LIBRARY_PATH=%buildroot%_libdir make check

%files
%doc AUTHORS ChangeLog NEWS README Copyright
%doc %_mandir/man1/xmlsec1.1*
%_libdir/libxmlsec1.so.*
%_bindir/xmlsec1

%files devel
%doc %_defaultdocdir/xmlsec1
%_bindir/xmlsec1-config
%dir %_includedir/xmlsec1
%dir %_includedir/xmlsec1/xmlsec
%dir %_includedir/xmlsec1/xmlsec/private
%_includedir/xmlsec1/xmlsec/*.h
%_includedir/xmlsec1/xmlsec/private/*.h
%_libdir/libxmlsec1.so
%_libdir/pkgconfig/xmlsec1.pc
%_libdir/xmlsec1Conf.sh
%doc AUTHORS HACKING ChangeLog NEWS README Copyright
%_datadir/aclocal/xmlsec1.m4
%_man1dir/xmlsec1-config.*

%files openssl
%_libdir/libxmlsec1-openssl.so.*

%files openssl-devel
%_includedir/xmlsec1/xmlsec/openssl/
%_libdir/pkgconfig/xmlsec1-openssl.pc
%_libdir/libxmlsec1-openssl.so

%files gcrypt
%_libdir/libxmlsec1-gcrypt.so.*

%files gcrypt-devel
%_includedir/xmlsec1/xmlsec/gcrypt/
%_libdir/pkgconfig/xmlsec1-gcrypt.pc
%_libdir/libxmlsec1-gcrypt.so

%files gnutls
%_libdir/libxmlsec1-gnutls.so.*

%files gnutls-devel
%_includedir/xmlsec1/xmlsec/gnutls/
%_libdir/pkgconfig/xmlsec1-gnutls.pc
%_libdir/libxmlsec1-gnutls.so

%files nss
%_libdir/libxmlsec1-nss.so.*

%files nss-devel
%_includedir/xmlsec1/xmlsec/nss/
%_libdir/pkgconfig/xmlsec1-nss.pc
%_libdir/libxmlsec1-nss.so

%changelog
* Fri Jun 08 2012 Fr. Br. George <george@altlinux.ru> 1.2.18-alt1
- Initial build from FC

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu May 12 2011 Daniel Veillard <veillard@redhat.com> - 1.2.18-1
- Update to upstream release 1.2.18

* Mon Apr 11 2011 Daniel Veillard <veillard@redhat.com> - 1.2.17-1
- Update to upstream release 1.2.17
- fixes CVE-2011-1425 on xslt file creation

* Tue Mar 22 2011 Daniel Veillard <veillard@redhat.com> - 1.2.16-4
- Fix missing links to unversioned shared library files 541599

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun  2 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.2.16-2
- add missing BuildRequires: libtool-ltdl-devel

* Wed Jun  2 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.2.16-1
- update to 1.2.16
- cleanup spec file
- disable static libs
- disable rpath
- enable gcrypt subpackage

* Wed Aug 26 2009 Tomas Mraz <tmraz@redhat.com> - 1.2.12-2
- rebuilt with new openssl

* Tue Aug 11 2009 Daniel Veillard <veillard@redhat.com> - 1.2.12-1
- update to new upstream release 1.2.12
- includes fix for CVE-2009-0217
- cleanup spec file

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Tomas Mraz <tmraz@redhat.com> - 1.2.11-2
- rebuild with new openssl

* Fri Jul 11 2008 Daniel Veillard <veillard@redhat.com> - 1.2.11-1
- update to new upstream release 1.2.11
- rebuild for gnutls update

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.9-10.1
- Autorebuild for GCC 4.3

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.2.9-9
 - Rebuild for deps

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.2.9-8.1
- rebuild

* Wed Jun 14 2006 Tomas Mraz <tmraz@redhat.com> - 1.2.9-8
- rebuilt with new gnutls

* Thu Jun  8 2006 Daniel Veillard <veillard@redhat.com> - 1.2.9-7
- oops libxmlsec1.la was still there, should fix #171410 and #154142

* Thu Jun  8 2006 Daniel Veillard <veillard@redhat.com> - 1.2.9-6
- Ugly patch and sed based changes to work around #192756 xmlsec1-config
  multilib problem

* Wed Jun  7 2006 Jeremy Katz <katzj@redhat.com> - 1.2.9-5
- move .so symlinks to -devel subpackage

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.2.9-4.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.2.9-4.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Thu Dec 15 2005 Christopher Aillon <caillon@redhat.com> 1.2.9-4
- NSS has been split out of the mozilla package, so require that now
  and update separate_nspr.patch to account for the new NSS as well

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 23 2005 Tomas Mraz <tmraz@redhat.com> 1.2.9-3
- rebuilt due to gnutls library revision
* Wed Nov  9 2005 <veillard@redhat.com> 1.2.9-2
- rebuilt due to openssl library revision
* Tue Sep 20 2005 <veillard@redhat.com> 1.2.9-1
- update from upstream, release done in July
- apparently nss is now available on ppc64
* Mon Aug  8 2005 <veillard@redhat.com> 1.2.8-3
- rebuilt with new gnutls
- nspr has been split to a separate package
* Fri Jul  8 2005 Daniel Veillard <veillard@redhat.com> 1.2.8-2
- Enabling the mozilla-nss crypto backend
* Fri Jul  8 2005 Daniel Veillard <veillard@redhat.com> 1.2.8-1
- update from upstream, needed for openoffice
* Tue Mar  8 2005 Daniel Veillard <veillard@redhat.com> 1.2.7-4
- rebuilt with gcc4
* Wed Feb 23 2005 Daniel Veillard <veillard@redhat.com> 1.2.7-1
- Upstream release of 1.2.7, mostly bug fixes plus new functions
  to GetKeys from simple store and X509 handling.
* Wed Feb  9 2005 Daniel Veillard <veillard@redhat.com> 1.2.6-4
- Adding support for GNUTls crypto backend
* Wed Sep  1 2004 Daniel Veillard <veillard@redhat.com> 1.2.6-3
- adding missing ldconfig calls
* Thu Aug 26 2004 Daniel Veillard <veillard@redhat.com> 1.2.6-2
- updated with upstream release from Aleksey
* Mon Jun 21 2004 Daniel Veillard <veillard@redhat.com> 1.2.5-2
- rebuilt
* Mon Apr 19 2004 Daniel Veillard <veillard@redhat.com> 1.2.5-1
- updated with upstream release from Aleksey
* Wed Feb 11 2004 Daniel Veillard <veillard@redhat.com> 1.2.4-1
- updated with upstream release from Aleksey
* Tue Jan  6 2004 Daniel Veillard <veillard@redhat.com> 1.2.3-1
- updated with upstream release from Aleksey
* Wed Nov 12 2003 Daniel Veillard <veillard@redhat.com> 1.2.2-1
- updated with upstream release from Aleksey, specific patches should
  have been integrated now.
* Thu Nov  6 2003 Daniel Veillard <veillard@redhat.com> 1.2.1-1
- initial packaging based on the upstream one and libxml2 one.
- desactivated mozilla-nss due to detection/architecture problems
