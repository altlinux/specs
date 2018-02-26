Name: gq
Version: 1.3.6
Release: alt0.1.qa3
Serial: 1

Summary: GQ is an interactive graphical LDAP browser
Summary(ru_RU.UTF-8): GQ - графический LDAP клиент.
License: GPL
Group: Databases
Url: http://biot.com/%name
Packager: Sergey Alembekov <rt@altlinux.ru>

Source: %name-%version.tar

Patch0: %name-1.3.6-alt-build.patch
Patch1: %name-1.3.6-alt-glib2-2.32.0.patch
Patch2: %name-1.3.6-alt-DSO.patch

#Requires: gdk-pixbuf
Requires: gtk+2
Requires: libsasl2
Requires: libgnome-keyring

BuildPreReq: libsasl2-devel libxml2-devel
# Automatically added by buildreq on Tue Oct 16 2007
BuildRequires: libgcrypt-devel libglade-devel libgnome-keyring-devel libldap-devel libssl-devel perl-XML-Parser gnome-common intltool gnome-doc-utils libkrb5-devel

%description
GQ is GTK+ LDAP client and browser utility. It can be used
for searching LDAP directory as well as browsing it using a
tree view.

%description -l ru_RU.UTF-8
GQ это LDAP клиент основанный на GTK+. Его можно использовать для посика в LDAP каталоге, а также для просмотра каталога в виде "дерева".

%prep
%setup

%patch0 -p2
%patch1 -p2
%patch2 -p2

%build
./autogen.sh
%configure \
	--enable-browser-dnd \
	--enable-cache \
	--disable-update-mimedb \
	--with-keyring-api=gnome \
	--with-kerberos5=/usr

%make_build

%install
%makeinstall

install -d %buildroot%_niconsdir
install -m 644 icons/new.xpm %buildroot%_niconsdir/%name.xpm

# those categories seems to fit better; Network has no suitable Secondary Category
sed -i -e 's,Categories=Application;Network;GTK;,Categories=System;Security;GTK;,' %buildroot%_desktopdir/%name.desktop

%files
%doc README INSTALL COPYING ChangeLog NEWS TODO AUTHORS
%_bindir/%name
%_niconsdir/%{name}*
%_pixmapsdir/%name/*
%_desktopdir/%name.desktop
%_datadir/%name
%_iconsdir/hicolor/16x16/apps/*
/usr/share/gnome/help/gq-manual
/usr/share/mime/packages/gq-ldif.xml
/usr/share/omf/gq-manual

%changelog
* Thu Jun 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.6-alt0.1.qa3
- Fixed build

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.6-alt0.1.qa2
- Fixed build

* Tue Apr 12 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.3.6-alt0.1.qa1
- NMU: dropped obsolete menu entry; added desktop categories

* Wed Jan 19 2011 Timur Aitov <timonbl4@altlinux.org> 1:1.3.6-alt0.1
- git89f21913fe05035475ff056fb7f1d21d1eb6377f

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt2.2.qa1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Thu Nov 12 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1:1.0.1-alt2.2.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for gq
  * postclean-05-filetriggers for spec file

* Tue Sep 01 2009 Sergey Alembekov <rt@altlinux.ru> 1:1.0.1-alt2.2
- Rebuild with libldap2.4 

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1:1.0.1-alt2.1
- Automated rebuild due to libcrypto.so.6 -> libcrypto.so.7 soname change.

* Tue Oct 23 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 1:1.0.1-alt2
- return to 1.0.1 -- all new versions are not usable

* Tue Oct 16 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.1-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Thu Nov 23 2006 Sergey Alembekov <rt@altlinux.ru> 1.0.1-alt1
- New upstream release

* Sat Sep 23 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 0.7.0-alt12.beta2.3
- rebuild with latest Sisyphus

* Sun Nov 21 2004 Serge A. Volkov <vserge at altlinux.ru> 0.7.0-alt12.beta2
- FIX: bug - seg. fault when expand on browse tab ldap server tree (gq-openlda-2.2.x-upgrade.patch)
- Update BuildReq

* Sat Nov 13 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.7.0-alt11.beta2.1
- Rebuilt with openldap-2.2.18-alt3.

* Mon Aug 02 2004 Serge A. Volkov <vserge@altlinux.ru> 0.7.0-alt11.beta2
- Changed RPM Group from Networking/Other to Databases (like tora)
- Changed Menu locations from Networking/Other to Applications/Databases

* Tue May 11 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.7.0-alt10.beta2.1
- Rebuilt with openssl-0.9.7d.

* Sun Apr 25 2004 Serge A. Volkov <vserge@altlinux.ru> 0.7.0-alt10.beta2
- Rebuild (remove autoreconf).

* Sat Feb 28 2004 Serge A. Volkov <vserge@altlinux.ru> 0.7.0-alt9.beta2
- Rebuild with new autotools
- Add gq-0.7.0-beta2-ALT-po-Makefile.patch for correction po files install

* Fri Feb 13 2004 Serge A. Volkov <vserge@altlinux.ru> 0.7.0-alt8.beta2
- Rebuild with sasl2 and new OpenLDAP (libdb4.2)

* Mon Dec 29 2003 Serge A. Volkov <vserge@altlinux.ru> 0.7.0-alt7.beta2
- Update for build with Sisyphus

* Wed Nov 06 2002 Serge A. Volkov <vserge@altlinux.ru> 0.7.0-alt6.beta2
- Add UTF-8 Description and Summary -- now menu ganerate right.

* Thu Oct 31 2002 Serge A. Volkov <vserge@altlinux.ru> 0.7.0-alt5.beta2
- Add requires of autoconf and automake old version!!!

* Mon Oct 28 2002 Serge A. Volkov <vserge@altlinux.ru> 0.7.0-alt4.beta2
- Update Requires

* Thu Oct 24 2002 Serge A. Volkov <vserge@altlinux.ru> 0.7.0-alt3.beta2
- Add patch from Peter Stemfest
- Correct rpm Group
- Update BuildRequires
- Add translations for descritions and Summary
- Add Requires and BuildRequires for libsasl2 and libsasl2-devel (buildreq utils not find it)

* Wed Oct 16 2002 Serge A. Volkov <vserge@altlinux.ru> 0.7.0beta2-alt2
- Update to new beta2 version
- Add --with-included-gettext (langpack0)

* Mon Oct 07 2002 Serge A. Volkov <vserge@altlinux.ru> 0.7.0beta1-alt1
- Update to new beta1 version

* Tue Jul 16 2002 Serge A. Volkov <vserge@altlinux.ru> 0.6.0-alt3
- Correct BuildRequies for gdk-pixbuf-devel now realy can see jpegPhoto

* Thu Jul 11 2002 Serge A. Volkov <vserge@altlinux.ru> 0.6.0-alt2
- Add new options for configure
  - --enable-browser-dnd for drag and drop support in browse mode
  - --enable-cache for supports the OpenLDAP experimental client cache
- Update BuildRequires

* Thu Jul 11 2002 Serge A. Volkov <vserge@altlinux.ru> 0.6.0-alt1
- Update for 0.6.0
- spec correction

* Tue Mar 19 2002 Serge A. Volkov <vserge@altlinux.ru> 0.5.0-alt1
- Update version to 0.5.0
- Spec cleanup

* Sat May 05 2001 Rider <rider@altlinux.ru> 0.4.0-alt1
- first build for ALT Linux

* Thu Mar 15 2001 Christian Zoffoli <czoffoli@linux-mandrake.com> 0.4.0-2.1mdk
- changed make macro

* Thu Mar 08 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.4.0-2mdk
- fixes from Christian Zoffoli <czoffoli@linux-mandrake.com>
- changes in menu entry

* Tue Mar 06 2001 Christian Zoffoli <czoffoli@linux-mandrake.com> 0.4.0-1mdk
- new package

