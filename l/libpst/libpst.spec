%define _unpackaged_files_terminate_build 1

Name: libpst
Version: 0.6.76
Release: alt4
Summary: Tools for conversion of Outlook files to mailbox and other formats
License: %gpl2plus
Group: System/Libraries

Url: http://www.five-ten-sg.com/libpst
Source0: %url/packages/%name-%version.tar
Source100: libpst.watch
Patch1: %name-%version-alt-known-fields.patch
Patch2: %name-%version-python3.12.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Tue Aug 04 2009
BuildRequires: ImageMagick-tools gcc-c++ libgd3-devel zlib-devel
BuildRequires: python3-devel boost-python3-devel
BuildRequires: libgsf-devel
BuildRequires: xmlto doxygen graphviz

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
Requires: %name = %EVR

%description devel
This package provides header and libraries for build programs
against libpst

%package tools
Summary: libpst tools
Group: File tools
Requires: %name = %EVR

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
Requires: %name = %EVR
BuildArch: noarch
# License for xml/MAPI_definitions.pdf is GFDL1.1 with no invariant sections etc.,
# therefore it must be GPL2-compatible. (In case that file is packaged.)

%description docs
Developer's documentation for libpst

%package -n python3-module-%name
Summary: Python interface to libpst (for reading Outlook files)
Group: Development/Python3

%description  -n python3-module-%name
Python interface to libpst (for reading Outlook files)

%prep
%setup
%patch1 -p1
%patch2 -p2

%build
%autoreconf
%configure \
	--enable-libpst-shared \
	--disable-static \
	--with-boost-python=boost_python%{python_version_nodots python3} \
	%nil

%make_build

%install
%makeinstall_std

# Some reverse-engineered documentation:
mkdir -p %buildroot%pkgdocdir/format-documentation
install -m0644 xml/*.pdf -t %buildroot%pkgdocdir/format-documentation/

# remove unpackaged files
rm -f %buildroot%_libdir/python*/site-packages/*.la

%files
%_libdir/*.so.*
%dir %pkgdocdir
# LICENSE etc.
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
%pkgdocdir/*
# LICENSE etc.
%exclude %pkgdocdir/[A-Z]*

%files -n python3-module-%name
%python3_sitelibdir/*.so

%changelog
* Wed Dec 20 2023 Grigory Ustinov <grenka@altlinux.org> 0.6.76-alt4
- Fix building with python3.12.

* Sat Jan 28 2023 Grigory Ustinov <grenka@altlinux.org> 0.6.76-alt3
- Fix building with python3.11.

* Thu Jan 13 2022 Grigory Ustinov <grenka@altlinux.org> 0.6.76-alt2
- Add patch for building with python3.10.

* Thu May 13 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.76-alt1
- Updated to upstream version 0.6.76.
- Rebuilt with python-3.

* Mon Dec 16 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.68-alt2.2
- Rebuilt with boost-1.71.0.

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.68-alt2.1
- NMU: rebuilt with boost-1.67.0

* Wed Sep 21 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.68-alt2
- a further fix for empty headers instead of the authentic correct ones
  for the very rare case when the first internet header is wrapped
  (thx Carl from upstream, hg commit e4c414ff8fa2)

* Tue Sep 20 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.68-alt1
- rebased onto 0.6.68 ("To: " has become a "known" header in readpst, too).

* Tue Aug 30 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.67-alt5
- more known fields (in order to have less noise in the debugging log in:
  grep -A 5 'Ignore bogus headers' *log) (thx Carl Byington)

* Fri Aug 26 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.67-alt4
- all items are saved in folders with mixed items
  (thx Carl Byington, RH#1369499) (ALT#32425).
- python-module-libpst packaged.
- libpst-docs: include the .pdf with old reverse-engeneered documentation.

* Wed Aug 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.67-alt3
- readpst -r: don't produce malformed mbox files
  for folders with mixed content (RH#1369499, ALT#32422).

* Thu Jul 21 2016 Denis Medvedev <nbr@altlinux.org> 0.6.67-alt1
- new version (0.6.67 uupdate).

* Sat Sep 12 2015 Michael Shigorin <mike@altlinux.org> 0.6.65-alt1
- new version (watch file uupdate)

* Sun Mar 22 2015 Michael Shigorin <mike@altlinux.org> 0.6.64-alt1
- new version (watch file uupdate)

* Thu Jan 02 2014 Michael Shigorin <mike@altlinux.org> 0.6.63-alt1
- new version (watch file uupdate)

* Wed Aug 07 2013 Michael Shigorin <mike@altlinux.org> 0.6.61-alt1
- new version (watch file uupdate)

* Wed Feb 20 2013 Michael Shigorin <mike@altlinux.org> 0.6.58-alt1
- new version (watch file uupdate)

* Thu Aug 23 2012 Michael Shigorin <mike@altlinux.org> 0.6.55-alt1
- new version (watch file uupdate)

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
