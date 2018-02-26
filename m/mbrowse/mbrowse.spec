Name: mbrowse
Version: 0.3.1
Release: alt6.qa3

Summary: SNMP MIB browser
License: GPL
Group: Networking/Other

URL: http://goldplated.atlcartel.com/mbrowse.html
Source0: http://goldplated.atlcartel.com/%name-%version.tar.bz2
Source1: %name.xpm

Patch0: %name-0.3.1-alt-snmpdetect.patch
Patch1: %name-0.3.1-alt-snmpconf.patch
Patch2: %name-0.3.1-alt-gcc34.patch
Patch3: %name-0.3.1-alt-x86-64-build.patch

# Automatically added by buildreq on Sun Apr 22 2007
BuildRequires: gtk+-devel libnet-snmp-devel

%description
Mbrowse is an SNMP MIB browser based on GTK and net-snmp.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure
%make_build

%install
%make_build install DESTDIR=%buildroot

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=%name
Comment=SNMP MIB browser
Icon=%{name}
Exec=%name
Terminal=false
Categories=Network;FileTransfer;
EOF

mkdir -p %buildroot/%_niconsdir/
install -m644 %SOURCE1 %buildroot/%_niconsdir/


%files
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%_bindir/%name
%_desktopdir/%name.desktop
%_niconsdir/%name.xpm

%changelog
* Sat Apr 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt6.qa3
- NMU: converted menu to desktop file

* Sat Oct 16 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.3.1-alt6.qa1.1
- Rebuild with new libnet-snmp

* Thu Nov 12 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.3.1-alt6.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for mbrowse
  * pixmap-in-deprecated-location for mbrowse
  * postclean-05-filetriggers for spec file

* Sun Apr 22 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 0.3.1-alt6
- fix x86-64 build
- update BuildReq's

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.3.1-alt5.1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Fri Dec 02 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.3.1-alt5.1
- rebuild with libnetsnmp.so.9 .

* Fri Jan 28 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 0.3.1-alt5
- fix compilation with gcc3.4

* Fri Dec 24 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 0.3.1-alt4
- workaround for broken net-snmp-config

* Fri Nov 12 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.3.1-alt3.1.1
- Removed libelf-devel from build dependencies.

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.3.1-alt3.1
- Rebuilt with openssl-0.9.7d.

* Fri Apr 30 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 0.3.1-alt3
- fix detection Net-SNMP version during configure stage

* Fri Oct 31 2003 Konstantin Timoshenko <kt@altlinux.ru> 0.3.1-alt2
- rebuild with net-snmp

* Wed Mar 26 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 0.3.1-alt1
- new version -- 0.3.1 

* Sat Jan 25 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 0.2.3-alt2
- rebuild with gcc3.2
- compile warnings cleanup
- menu icon added

* Mon Jul 15 2002 Konstantin Timoshenko <kt@altlinux.ru> 0.2.3-alt1
- Initial spec file
