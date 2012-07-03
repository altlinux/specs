Name: libpst
Version: 0.6.54
Release: alt1

Summary: Tools for conversion of Outlook files to mailbox and other formats
License: %gpl2plus
Group: System/Libraries

Url: http://www.five-ten-sg.com/libpst
Source: %url/packages/%name-%version.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue Aug 04 2009
BuildRequires: ImageMagick-tools boost-python-devel gcc-c++ libgd2-devel

%define pkgdocdir %_docdir/%name-%version

%description
libpst converts Outlook PST files to mailbox and others formats:
kmail, its own recursive format or separate each email into its own
file. It currently handles EMails, Folders and mostly Contacts.

This is a fork of the libpst project at SourceForge. Another fork is
located at http://alioth.debian.org/projects/libpst/

This version can now convert both 32 bit Outlook files (pre 2003), and
the 64 bit Outlook 2003 pst files. Utilities are supplied to convert
email messages to both mbox and MH mailbox formats, and to DII load file
format for use with many of the CT Summation products. Contacts can be
converted to a simple list, to vcard format, or to ldif format for
import to an LDAP server.

%package devel
Summary: Development files for libpst
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides header and libraries for build programs
against libpst

%package tools
Summary: libpst tools
Group: File tools
Requires: %name = %version-%release

%description tools
Tools to cope with PST (Outlook Personal Folders) files:
  readpst - convert to mbox and other formats
  lspst - list PST file data
  readpstlog - convert a readpst logfile to text format
  pst2ldif - extract contacts in .ldif format
  pst2dii - extract email messages into DII load format

%package docs
Summary: libpst documentation
Group: Documentation
Requires: %name = %version-%release
BuildArch: noarch

%description docs
Developer's documentation for libpst

%prep
%setup

%build
%autoreconf
%configure \
	--enable-libpst-shared \
	--disable-static
%make

%install
%makeinstall_std

%files
%_libdir/*.so.*
%dir %pkgdocdir
%pkgdocdir/[A-Z]*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*
%_man5dir/*

%files tools
%_bindir/*
%_man1dir/*

%files docs
%pkgdocdir/*/
%exclude %pkgdocdir/[A-Z]*

%changelog
* Mon Feb 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.6.54-alt1
- 0.6.54

* Mon Sep 26 2011 Michael Shigorin <mike@altlinux.org> 0.6.53-alt2
- s/patch/autoreconf/ as per upstream advice

* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 0.6.53-alt1
- 0.6.53

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.6.47-alt1.qa1
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Fri Jul 23 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.6.47-alt1
- update to 0.6.47
- use macro in License tag
- fix typo in devel package Summary

* Wed Dec 23 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.6.45-alt1
- update to 0.6.45

* Sat Nov 14 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.6.44-alt1
- update to 0.6.44

* Thu Aug 06 2009 Michael Shigorin <mike@altlinux.org> 0.6.41-alt2
- moved %%pkgdocdir from docs to main subpackage (repocop)
- noarch docs (ouch!)

* Tue Aug 04 2009 Michael Shigorin <mike@altlinux.org> 0.6.41-alt1
- 0.6.41
  + fixed FTBFS
- adopted an orphan
  + I'm happy not to have to cope with PST by now,
    proper maintainer is pretty welcome
- spec cleanup
- buildreq

* Mon Jan 26 2009 Yuri N. Sedunov <aris@altlinux.org> 0.6.25-alt1
- Build fork from http://www.five-ten-sg.com/libpst that required for evolution
- new devel and tools subpackages

* Sat Jan 27 2007 Michael Shigorin <mike@altlinux.org> 0.5.2-alt1
- 0.5.2
- added Packager:
- fixed build

* Fri Jan 06 2006 Michael Shigorin <mike@altlinux.org> 0.5.1-alt1
- built for ALT Linux (packaged this time)
- based on PLD spec v1.2 for 0.5 by <qboosh pld-linux org>
  + fix/cleanup
  + updated Url
