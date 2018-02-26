%def_disable static

Name: opensc
Version: 0.12.2
Release: alt2.1

Group: System/Configuration/Hardware
Summary: OpenSC library - for accessing SmartCard devices using PC/SC Lite
Url: http://www.opensc-project.org/
License: LGPL

Requires: lib%name = %version-%release

Source: %name-%version.tar
Patch1: opensc-0.12.2-alt-automake-1.11.4.patch
Patch2: opensc-0.12.2-alt-DSO.patch

BuildRequires: browser-plugins-npapi-devel

# Automatically added by buildreq on Sun Feb 07 2010
BuildRequires: db2latex-xsl docbook-dtds docbook-style-xsl libXt-devel libassuan0-devel libltdl7-devel libpcsclite-devel libreadline-devel libssl-devel xsltproc zlib-devel

%package -n lib%name
Group: System/Libraries
Summary: OpenSC library - for accessing SmartCard devices using PC/SC Lite
Requires: browser-plugins-npapi

%package -n lib%name-devel
Group: Development/Other
Summary: OpenSC development files
Requires: lib%name = %version-%release

%package -n lib%name-devel-static
Group: Development/Other
Summary: Static OpenSC libraries
Requires: lib%name-devel = %version-%release

%package -n pam_opensc
Group: System/Base
Summary: OpenSC module for PAM
License: GPL
Requires: lib%name = %version-%release

%description
libopensc is a library for accessing SmartCard devices using PC/SC
Lite middleware package. It is also the core library of the OpenSC
project. Basic functionality (e.g. SELECT FILE, READ BINARY) should
work on any ISO 7816-4 compatible SmartCard. Encryption and decryption
using private keys on the SmartCard is at the moment possible only
with PKCS#15 compatible cards, such as the FINEID (Finnish Electronic
IDentity) card manufactured by Setec.

%description -n lib%name
libopensc is a library for accessing SmartCard devices using PC/SC
Lite middleware package. It is also the core library of the OpenSC
project. Basic functionality (e.g. SELECT FILE, READ BINARY) should
work on any ISO 7816-4 compatible SmartCard. Encryption and decryption
using private keys on the SmartCard is at the moment possible only
with PKCS#15 compatible cards, such as the FINEID (Finnish Electronic
IDentity) card manufactured by Setec.

%description -n lib%name-devel
OpenSC development files.

%description -n lib%name-devel-static
Static OpenSC libraries.

%description -n pam_opensc
OpenSC module for PAM.

%prep
%setup
%patch1 -p2
%patch2 -p2

%build
%autoreconf
%add_optflags %optflags_shared
PCSC_SONAME="$(objdump -p "%_libdir/libpcsclite.so"| awk '/SONAME/ {print $2}')"
%configure \
     %{subst_enable static} \
    --enable-shared \
    --enable-pcsc \
    --with-pcsc-provider="%_libdir/$PCSC_SONAME" \
    --enable-nsplugin \
    --with-plugindir=%browser_plugins_path \
    --with-xsl-stylesheetsdir=/usr/share/xml/docbook/xsl-stylesheets \
    --with-pcsc-provider=libpcsclite.so.1 \
    --disable-assert

%make_build

%install
%makeinstall_std

mkdir -p %buildroot/%_sysconfdir/
install -p -m644 etc/opensc.conf %buildroot/%_sysconfdir/opensc.conf

pushd %buildroot/%_libdir
ln -s pkcs11/opensc-pkcs11.so .
ln -s pkcs11/pkcs11-spy.so .
ln -s pkcs11/onepin-opensc-pkcs11.so .
popd

%files
# %doc doc/nonpersistent/ChangeLog 
#%doc doc/nonpersistent/wiki.out
#%doc doc/html.out/tools.html
%doc NEWS README

%config(noreplace) %_sysconfdir/opensc.conf
%_bindir/opensc-tool
%_bindir/pkcs15-init
#%_bindir/rutoken-tool
#%_bindir/cardos-info
%_bindir/cardos-tool
%_bindir/pkcs15-tool
%_bindir/eidenv
%_bindir/opensc-explorer
%_bindir/netkey-tool
%_bindir/cryptoflex-tool
%_bindir/pkcs11-tool
%_bindir/piv-tool
%_bindir/pkcs15-crypt
%_bindir/westcos-tool
%doc %_mandir/*/*

%files -n lib%name
%_libdir/lib*.so.*
%_libdir/opensc-pkcs11.so*
%_libdir/pkcs11-spy.so*
%_libdir/onepin-opensc-pkcs11.so*
%dir %_libdir/pkcs11
%_libdir/pkcs11/pkcs11-spy.so
%_libdir/pkcs11/opensc-pkcs11.so
%_libdir/pkcs11/onepin-opensc-pkcs11.so
%dir %_datadir/opensc
%_datadir/opensc/*.profile
#%browser_plugins_path/opensc-signer.so
#%_libdir/opensc-signer.so*

%files -n lib%name-devel
#%doc doc/html.out/api.html
#%_libdir/pkgconfig/libopensc.pc
#%_libdir/pkgconfig/libpkcs15init.pc
#%_libdir/pkgconfig/libscconf.pc
#%_bindir/opensc-config
%_libdir/libopensc.so
#%_libdir/libpkcs11.so
#%_libdir/libpkcs15init.so
#%_libdir/libscconf.so
#%_libdir/libscldap.so
#%_libdir/libscrandom.a
#%_libdir/libscam.a
#%_libdir/libopensc.la
#%_libdir/libpkcs15init.la
#%_libdir/libscconf.la
#%_libdir/libscldap.la
#%_includedir/opensc

%if_enabled static
%files -n lib%name-devel-static
%_libdir/libopensc.a
%_libdir/libpkcs15init.a
%_libdir/libscconf.a
%_libdir/libscldap.a
%endif

#%files -n pam_opensc
#/lib/security/pam_opensc.so

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.2-alt2.1
- Fixed build

* Fri Apr 20 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.2-alt2
- Repair build with automake >= 1.11.4

* Thu Oct 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.2-alt1
- 0.12.2
- build with pcsc-lite

* Tue Jan 25 2011 Timur Aitov <timonbl4@altlinux.org> 0.12.0-alt1
- New version

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 0.11.13-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sun Jun 27 2010 Alexey I. Froloff <raorn@altlinux.org> 0.11.13-alt1
- [0.11.13]

* Sun Feb 07 2010 Dmitry V. Levin <ldv@altlinux.org> 0.11.9-alt5
- Rebuilt with libassuan0.so.0.

* Thu Feb 04 2010 Sergey V Turchin <zerg@altlinux.org> 0.11.9-alt4
- Rebuilt with static libassuan0

* Tue Sep 29 2009 Alexey I. Froloff <raorn@altlinux.org> 0.11.9-alt3
- Rebuilt with new browser-plugins-npapi
- lib%name should depend on browser-plugins-npapi

* Thu Sep 24 2009 Alexey I. Froloff <raorn@altlinux.org> 0.11.9-alt2
- Don't display errors that happen during readers detection

* Thu Sep 10 2009 Alexey I. Froloff <raorn@altlinux.org> 0.11.9-alt1
- [0.11.9]
- Enabled PC/SC support

* Sun May 17 2009 Andriy Stepanov <stanv@altlinux.ru> 0.11.8-alt1
- New upstream version.

* Thu Feb 26 2009 Andriy Stepanov <stanv@altlinux.ru> 0.11.7-alt1
- New upstream version.

* Tue Sep 02 2008 Andriy Stepanov <stanv@altlinux.ru> 0.11.6-alt2
- fix rights to opensc.conf

* Tue Sep 02 2008 Andriy Stepanov <stanv@altlinux.ru> 0.11.6-alt1
- update to new upstream version

* Tue Apr 22 2008 Andriy Stepanov <stanv@altlinux.ru> 0.11.4-alt5
- Update patch for from rutoken (opensc-0.11.4-0.11.4.rutoken-0.3.2.diff)

* Tue Nov 06 2007 Andriy Stepanov <stanv@altlinux.ru> 0.11.4-alt4
- ruToken: rnd bug

* Tue Oct 30 2007 Andriy Stepanov <stanv@altlinux.ru> 0.11.4-alt3
- Patch from ruToken

* Tue Oct 30 2007 Andriy Stepanov <stanv@altlinux.ru> 0.11.4-alt2
- Patch from ruToken

* Tue Oct 30 2007 Andriy Stepanov <stanv@altlinux.ru> 0.11.4-alt1
- Fixed ruToken for work with GOST keys

* Wed Sep 26 2007 Anton Farygin <rider@altlinux.ru> 0.11.3-alt4
- Updated rutoken patch

* Mon Sep 24 2007 Andriy Stepanov <stanv@altlinux.ru> 0.11.3-alt3
- Applay new changes for RuToken

* Mon Aug 13 2007 Andriy Stepanov <stanv@altlinux.ru> 0.11.3-alt2
- debug

* Thu Aug 02 2007 Andriy Stepanov <stanv@altlinux.ru> 0.11.3-alt1
- Switch to new version. Add rutoken support.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.11.1-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Mon Jul 03 2006 Sergey V Turchin <zerg at altlinux dot org> 0.11.1-alt1
- new version

* Mon Nov 15 2004 Sergey V Turchin <zerg at altlinux dot org> 0.8.1-alt4
- fix BuildRequires

* Mon Oct 11 2004 Sergey V Turchin <zerg at altlinux dot org> 0.8.1-alt3
- rebuild

* Tue Apr 06 2004 Sergey V Turchin <zerg at altlinux dot org> 0.8.1-alt2
- add patches from PLD

* Mon Nov 24 2003 Sergey V Turchin <zerg at altlinux dot org> 0.8.1-alt1
- new version
- compile without text relocations

* Mon Sep 29 2003 Sergey V Turchin <zerg at altlinux dot org> 0.7.0-alt1
- build for ALT

* Wed Mar 12 2003 PLD Team <feedback@pld.org.pl>
All persons listed below can be reached at <cvs_login>@pld.org.pl

$Log: opensc.spec,v $
Revision 1.7  2003/03/12 11:13:58  qboosh
- nest support

Revision 1.6  2003/03/11 18:08:25  wiget
- remove libtools macros from acinclude.m4

Revision 1.5  2003/03/11 17:08:19  qboosh
- added fix for SEGV

Revision 1.4  2003/03/11 13:12:19  qboosh
- added nolibs patch - -lresolv is not necessary

Revision 1.3  2003/03/10 20:22:49  qboosh
- ac >= 2.52

Revision 1.2  2003/03/10 16:10:29  qboosh
- some work - builds now

Revision 1.1  2002/12/18 22:34:06  hunter
-NYF!
