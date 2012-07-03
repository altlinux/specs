Name: docbook-dtds
Version: 4.5
Release: alt1

Summary: SGML and XML document type definitions for DocBook
Group: Publishing
License: Distributable
URL: http://www.oasis-open.org/docbook/

Packager: XML Development Team <xml@packages.altlinux.org>

Obsoletes: docbook-dtd30-sgml docbook-dtd31-sgml
Obsoletes: docbook-dtd40-sgml docbook-dtd41-sgml
Obsoletes: docbook-dtd412-xml

Provides: docbook-dtd-xml docbook-dtd-sgml
Provides: docbook-dtd30-sgml docbook-dtd31-sgml
Provides: docbook-dtd40-sgml docbook-dtd41-sgml
Provides: docbook-dtd42-sgml
Provides: docbook-dtd43-sgml
Provides: docbook-dtd412-xml
Provides: docbook-dtd42-xml
Provides: docbook-dtd43-xml

PreReq: sgml-common >= 0.6.3
PreReq: xml-common >= 0.6.3-alt7
PreReq: xml-utils
Requires(post,preun,postun): xml-utils

AutoReqProv: no

BuildArch: noarch

Source0: docbook-3.0.tar.bz2
Source1: docbook-3.1.tar.bz2
Source2: docbook-4.0.tar.bz2
Source3: docbook-4.1.tar.bz2
Source4: docbook-xml-4.1.2.tar.bz2
Source5: docbook-4.2.tar.bz2
Source6: docbook-xml-4.2.tar.bz2
Source7: docbook-4.3.tar.bz2
Source8: docbook-xml-4.3.tar.bz2
Source9: docbook-4.4.tar.bz2
Source10: docbook-xml-4.4.tar.bz2
Source11: docbook-4.5.tar.bz2
Source12: docbook-xml-4.5.tar.bz2

Patch0: docbook-3.0-catalog.patch
Patch1: docbook-3.1-catalog.patch
Patch2: docbook-4.0-catalog.patch
Patch3: docbook-4.1-catalog.patch
Patch4: docbook-xml-4.1.2-catalog.patch
Patch5: docbook-4.2-catalog.patch
Patch6: docbook-xml-4.2-catalog.patch
Patch7: docbook-xml-4.2-xmlcatalog.patch
Patch8: docbook-4.3-catalog.patch
Patch9: docbook-xml-4.3-catalog.patch
Patch10: docbook-xml-4.3-xmlcatalog.patch
Patch11: docbook-4.4-catalog.patch
Patch12: docbook-xml-4.4-catalog.patch
Patch13: docbook-xml-4.4-xmlcatalog.patch
Patch14: docbook-4.5-catalog.patch
Patch15: docbook-xml-4.5-catalog.patch
Patch16: docbook-xml-4.5-xmlcatalog.patch

%define xmlbase		%_datadir/xml
%define sgmlbase	%_datadir/sgml
%define xmlconfdir	%_sysconfdir/xml
%define sgmlconfdir	%_sysconfdir/sgml
%define xmlentitiesdir	%xmlbase/xml-iso-entities-8879.1986
%define sgmlentitiesdir	%sgmlbase/sgml-iso-entities-8879.1986

%description
The DocBook Document Type Definition (DTD) describes the syntax of
technical documentation texts (articles, books and manual pages).
This package contains SGML and XML versions of the DocBook DTD up to
and including version 4.3.

%prep
%setup -q -T -c -a 0 -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 9 -a 10 -a 11 -a 12
# DocBook V3.0
cd docbook-3.0
%__patch -b docbook.cat %PATCH0
cd ..

# DocBook V3.1
cd docbook-3.1
%__patch -b docbook.cat %PATCH1
cd ..

# DocBook V4.0
cd docbook-4.0
%__patch -b docbook.cat %PATCH2
cd ..

# DocBook V4.1
cd docbook-4.1
%__patch -b docbook.cat %PATCH3
cd ..

# DocBook XML V4.1.2
cd docbook-xml-4.1.2
%__patch -b docbook.cat %PATCH4
cd ..

# DocBook V4.2
cd docbook-4.2
%__patch -b docbook.cat %PATCH5
cd ..

# DocBook XML V4.2
cd docbook-xml-4.2
%__patch -b docbook.cat %PATCH6
%__patch -b catalog.xml %PATCH7
cd ..

# DocBook V4.3
cd docbook-4.3
%__patch -b docbook.cat %PATCH8
cd ..

# DocBook XML V4.3
cd docbook-xml-4.3
%__patch -b docbook.cat %PATCH9
%__patch -b catalog.xml %PATCH10
cd ..

# DocBook V4.4
cd docbook-4.4
%__patch -b docbook.cat %PATCH11
cd ..

# DocBook XML V4.4
cd docbook-xml-4.4
%__patch -b docbook.cat %PATCH12
%__patch -b catalog.xml %PATCH13
cd ..

# DocBook V4.5
cd docbook-4.5
%__patch -b docbook.cat %PATCH14
cd ..

# DocBook XML V4.5
cd docbook-xml-4.5
%__patch -b docbook.cat %PATCH15
%__patch -b catalog.xml %PATCH16
cd ..

# Documentation
for ver in 3.0 3.1 4.0 4.1 4.2 4.3 4.4 4.5; do
    %__install -d -m755 doc/$ver-sgml
done
for ver in 3.0 3.1 4.0 4.1; do
    %__mv docbook-$ver/*.txt		doc/$ver-sgml
done
for ver in 4.2 4.3 4.4 4.5; do
    %__mv docbook-$ver/README		doc/$ver-sgml
done
# no ChangeLog in 4.5
for ver in 3.1 4.1 4.2 4.3 4.4; do
    %__mv docbook-$ver/ChangeLog	doc/$ver-sgml
done
for ver in 4.1.2 4.2 4.3 4.4 4.5; do
    %__install -d -m755 doc/$ver-xml
done
for ver in 4.1.2; do
    %__mv docbook-xml-$ver/*.txt	doc/$ver-xml
done
for ver in 4.2 4.3 4.4 4.5; do
    %__mv docbook-xml-$ver/ChangeLog	doc/$ver-xml
done

%install
for ver in 3.0 3.1 4.0 4.1 4.2 4.3 4.4 4.5; do
    cd docbook-$ver
    DESTDIR=$RPM_BUILD_ROOT%sgmlbase/docbook/dtd/$ver
    %__install -d -m755 $DESTDIR
    %__install -p -m644 *.dcl $DESTDIR
    %__install -p -m644 docbook.cat $DESTDIR/catalog
    %__install -p -m644 *.dtd $DESTDIR
    %__install -p -m644 *.mod $DESTDIR
    cd ..
done

for ver in 4.1.2 4.2 4.3 4.4 4.5; do
    cd docbook-xml-$ver
    DESTDIR=$RPM_BUILD_ROOT%xmlbase/docbook/dtd/$ver
    %__install -d -m755 $DESTDIR
    %__install -p -m644 docbook.cat $DESTDIR/catalog
    %__install -p -m644 *.dtd $DESTDIR
    %__install -p -m644 *.mod $DESTDIR
    %__ln_s -nf $(relative %xmlentitiesdir %xmlbase/docbook/dtd/$ver/) $DESTDIR/ent
    cd ..
done
for ver in 4.2 4.3 4.4 4.5; do
    DESTDIR=$RPM_BUILD_ROOT%xmlbase/docbook/dtd/$ver
    %__install -p -m644 docbook-xml-$ver/catalog.xml $DESTDIR
done

# Hack: back-port XML catalog from 4.2 to 4.1.2
sed -e 's/4\.2/4\.1\.2/g' < docbook-xml-4.2/catalog.xml \
    > $RPM_BUILD_ROOT%xmlbase/docbook/dtd/4.1.2/catalog.xml

# Create empty centralized SGML catalogs and symlinks
mkdir -p $RPM_BUILD_ROOT%sgmlconfdir
for ver in 3.0 3.1 4.0 4.1 4.2 4.3 4.4 4.5; do
    %__install -m644 /dev/null \
	$RPM_BUILD_ROOT%sgmlconfdir/sgml-docbook-$ver.cat
done
for ver in 4.1.2 4.2 4.3 4.4 4.5; do
    %__install -m644 /dev/null \
	$RPM_BUILD_ROOT%sgmlconfdir/xml-docbook-$ver.cat
done
%__ln_s -f sgml-docbook-%version.cat \
    $RPM_BUILD_ROOT%sgmlconfdir/sgml-docbook.cat
%__ln_s -f xml-docbook-%version.cat \
    $RPM_BUILD_ROOT%sgmlconfdir/xml-docbook.cat

%files
%doc doc/*
%sgmlbase/docbook/*
%xmlbase/docbook/*
%config(noreplace) %sgmlconfdir/sgml-docbook-*.cat
%config(noreplace) %sgmlconfdir/xml-docbook-*.cat
%sgmlconfdir/sgml-docbook.cat
%sgmlconfdir/xml-docbook.cat

%pre
for ver in 4.1.2 4.2; do
    %__rm -rf %xmlbase/docbook/dtd/$ver/ent
done

%post
## NOTE: When editing this script, be sure to replicate changes in the
## triggerpostun scripts below.

##
## SGML catalog
##

# Update the centralized catalogs
UpdateCentralized() {
    %_bindir/xmlcatalog --sgml --noout --add \
	%sgmlconfdir/sgml-docbook-$1.cat \
	%sgmlbase/docbook/dtd/$1/catalog ||:
    %_bindir/xmlcatalog --sgml --noout --add \
	%sgmlconfdir/sgml-docbook-$1.cat \
	%sgmlentitiesdir/catalog ||:
}
UpdateCentralizedXML() {
    %_bindir/xmlcatalog --sgml --noout --add \
	%sgmlconfdir/xml-docbook-$1.cat \
	%xmlbase/docbook/dtd/$1/catalog ||:
    %_bindir/xmlcatalog --sgml --noout --add \
	%sgmlconfdir/xml-docbook-$1.cat \
	%sgmlentitiesdir/catalog ||:
}
UpdateCentralized 3.0
UpdateCentralized 3.1
UpdateCentralized 4.0
UpdateCentralized 4.1
UpdateCentralized 4.2
UpdateCentralized 4.3
UpdateCentralized 4.4
UpdateCentralized 4.5
UpdateCentralizedXML 4.1.2
UpdateCentralizedXML 4.2
UpdateCentralizedXML 4.3
UpdateCentralizedXML 4.4
UpdateCentralizedXML 4.5
##
## XML catalog
##

AddXMLCatalog() {
    %_bindir/xmlcatalog --noout --add "delegatePublic" \
	"-//OASIS//DTD DocBook XML V${1}" \
	"file://%xmlbase/docbook/dtd/${1}/catalog.xml" \
	%xmlbase/docbook/catalog
}
AddXMLRewrite() {
    %_bindir/xmlcatalog --noout --add "rewriteSystem" \
	"http://www.oasis-open.org/docbook/xml/${1}" \
	"dtd/${2}" %xmlbase/docbook/catalog ||:
    %_bindir/xmlcatalog --noout --add "rewriteURI" \
	"http://www.oasis-open.org/docbook/xml/${1}" \
	"dtd/${2}" %xmlbase/docbook/catalog ||:
}
AddXMLCatalog 4.1.2
AddXMLCatalog 4.2
AddXMLCatalog 4.3
AddXMLCatalog 4.4
AddXMLCatalog 4.5
#AddXMLRewrite 4.0 4.1.2
AddXMLRewrite 4.1.2 4.1.2
AddXMLRewrite 4.2 4.2
AddXMLRewrite 4.3 4.3
AddXMLRewrite 4.4 4.4
AddXMLRewrite 4.5 4.5

%preun
if [ $1 = 0 ]; then
    CATALOG=%sgmlconfdir/catalog
    %_bindir/xmlcatalog --sgml --noout --del $CATALOG \
	"%sgmlconfdir/sgml-docbook-3.0.cat" ||:
    %_bindir/xmlcatalog --sgml --noout --del $CATALOG \
	"%sgmlconfdir/sgml-docbook-3.1.cat" ||:
    %_bindir/xmlcatalog --sgml --noout --del $CATALOG \
	"%sgmlconfdir/sgml-docbook-4.0.cat" ||:
    %_bindir/xmlcatalog --sgml --noout --del $CATALOG \
	"%sgmlconfdir/sgml-docbook-4.1.cat" ||:
    %_bindir/xmlcatalog --sgml --noout --del $CATALOG \
	"%sgmlconfdir/sgml-docbook-4.2.cat" ||:
    %_bindir/xmlcatalog --sgml --noout --del $CATALOG \
	"%sgmlconfdir/sgml-docbook-4.3.cat" ||:
    %_bindir/xmlcatalog --sgml --noout --del $CATALOG \
	"%sgmlconfdir/sgml-docbook-4.4.cat" ||:
    %_bindir/xmlcatalog --sgml --noout --del $CATALOG \
	"%sgmlconfdir/xml-docbook-4.1.2.cat" ||:
    %_bindir/xmlcatalog --sgml --noout --del $CATALOG \
	"%sgmlconfdir/xml-docbook-4.2.cat" ||:
    %_bindir/xmlcatalog --sgml --noout --del $CATALOG \
	"%sgmlconfdir/xml-docbook-4.3.cat" ||:
    %_bindir/xmlcatalog --sgml --noout --del $CATALOG \
	"%sgmlconfdir/xml-docbook-4.4.cat" ||:
    %_bindir/xmlcatalog --sgml --noout --del $CATALOG \
	"%sgmlconfdir/xml-docbook-4.5.cat" ||:
fi

%postun
RemoveXMLCatalog() {
    if [ $1 = 0 -o ! -d "%xmlbase/docbook/dtd/${1}" ]; then
	%_bindir/xmlcatalog --noout --del \
	    "file://%xmlbase/docbook/dtd/${1}/catalog.xml" \
	    %xmlbase/docbook/catalog ||:
	%_bindir/xmlcatalog --noout --del \
	    "dtd/${1}" %xmlbase/docbook/catalog ||:
    fi
}
RemoveXMLCatalog 4.1.2
RemoveXMLCatalog 4.2
RemoveXMLCatalog 4.3
RemoveXMLCatalog 4.4
RemoveXMLCatalog 4.5

%triggerpostun -- docbook-dtd30-sgml docbook-dtd31-sgml docbook-dtd40-sgml docbook-dtd41-sgml
# Update the centralized catalogs that might get emptied
UpdateCentralized() {
    %_bindir/xmlcatalog --sgml --noout --add \
	%sgmlconfdir/sgml-docbook-$1.cat \
	%sgmlbase/docbook/dtd/$1/catalog ||:
    %_bindir/xmlcatalog --sgml --noout --add \
	%sgmlconfdir/sgml-docbook-$1.cat \
	%sgmlentitiesdir/catalog ||:
}
UpdateCentralized 3.0
UpdateCentralized 3.1
UpdateCentralized 4.0
UpdateCentralized 4.1
UpdateCentralized 4.2
UpdateCentralized 4.3
UpdateCentralized 4.4
UpdateCentralized 4.5

%__ln_s -f sgml-docbook-%version.cat %sgmlconfdir/sgml-docbook.cat

%triggerpostun -- docbook-dtd412-xml
##
## SGML catalog
##
UpdateCentralizedXML() {
    %_bindir/xmlcatalog --sgml --noout --add \
	%sgmlconfdir/xml-docbook-$1.cat \
	%xmlbase/docbook/dtd/$1/catalog ||:
    %_bindir/xmlcatalog --sgml --noout --add \
	%sgmlconfdir/xml-docbook-$1.cat \
	%sgmlentitiesdir/catalog ||:
}
UpdateCentralizedXML 4.1.2
UpdateCentralizedXML 4.2
UpdateCentralizedXML 4.3
UpdateCentralizedXML 4.4
UpdateCentralizedXML 4.5

%__ln_s -f xml-docbook-%version.cat %sgmlconfdir/xml-docbook.cat

##
## XML catalog
##
AddXMLCatalog() {
    %_bindir/xmlcatalog --noout --add "delegatePublic" \
	"-//OASIS//DTD DocBook XML V${1}" \
	"file://%xmlbase/docbook/dtd/${1}/catalog.xml" \
	%xmlbase/docbook/catalog
}
AddXMLRewrite() {
    %_bindir/xmlcatalog --noout --add "rewriteSystem" \
	"http://www.oasis-open.org/docbook/xml/${1}" \
	"dtd/${2}" %xmlbase/docbook/catalog ||:
    %_bindir/xmlcatalog --noout --add "rewriteURI" \
	"http://www.oasis-open.org/docbook/xml/${1}" \
	"dtd/${2}" %xmlbase/docbook/catalog ||:
}
AddXMLCatalog 4.1.2
AddXMLCatalog 4.2
#AddXMLRewrite 4.0 4.1.2
AddXMLRewrite 4.1.2 4.1.2
AddXMLRewrite 4.2 4.2
AddXMLRewrite 4.3 4.3
AddXMLRewrite 4.4 4.4
AddXMLRewrite 4.5 4.5

%triggerun -- docbook-dtds < 1.0-alt8
for ver in 3.0 3.1 4.0 4.1 4.2; do
    %_bindir/xmlcatalog --sgml --noout --del \
	%sgmlconfdir/sgml-docbook-$ver.cat \
	%sgmlbase/docbook/sgml-dtd-$ver/catalog ||:
done
for ver in 4.1.2 4.2; do
    # Hide files under symlink from being purged on uninstall of old package
    %__mv -f %xmlbase/docbook/dtd/$ver/ent{,-tmp}
done

%triggerpostun -- docbook-dtds < 1.0-alt8
for ver in 4.1.2 4.2; do
    # Restore previously mangled symlink
    %__mv -f %xmlbase/docbook/dtd/$ver/ent{-tmp,}
done

%changelog
* Wed Oct 08 2008 Yuri N. Sedunov <aris@altlinux.org> 4.5-alt1
- Packaged DTDs version 4.5

* Sun Mar 27 2005 Mikhail Zabaluev <mhz@altlinux.ru> 4.4-alt1
- Packaged DTD version 4.4 (SGML and XML)
- Restored an XML catalog missing due to a spec error (bug #6313)

* Mon Nov 22 2004 Mikhail Zabaluev <mhz@altlinux.ru> 4.3-alt1
- Changed the versioning scheme to reflect the latest DTD version
- Packaged DTD version 4.3 (SGML and XML)
- Further rationalized names for sources, patches and build directories
- Removed a rewrite for 4.0 system ID for 4.1.2.
  That was a documentation bug, not an intended feature.

* Mon Jan 19 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0-alt9
- Added OVERRIDE YES to all SGML catalogs.
  Jade won't stumble over system IDs anymore.
- More coherent patch set

* Sun Aug 31 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.0-alt8
- Don't search and add DSSSL and OpenJade catalogs on install
- Cleaned up install scripts
- Unified DTD path convention for SGML and XML DTDs
- Use directory symlinks to XML character entities dir rather than symlinks
  to individual files
- Flagged centralized catalogs as noreplace
- Split requires for xml-utils

* Wed Apr 30 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.0-alt7
- Fixed stupid path error in the Docbook XML catalog updates

* Wed Dec 04 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.0-alt6
- 4.0 system ID rewritten to the 4.1.2 path, as required by
  the DTD documentation.

* Mon Nov 11 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0-alt5
- rebuild

* Wed Jul 31 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.0-alt4
- Added DTDs for Docbook V4.2 and Docbook XML V4.2
- Create dedicated catalog.xml for 4.1.2 as it's provided in 4.2

* Wed Mar 27 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.0-alt3
- Use references to system-wide ISO XML character entities
  instead of cool URNs that OpenJade doesn't grok.

* Fri Mar 08 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.0-alt2
- Made install scripts always happy

* Mon Jan 28 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.0-alt1
- Adopted to ALT Linux
- Using both /usr/share/sgml and /usr/share/xml
- Listed centralized catalog files as config so they don't just disappear
  and don't require wacky uninstall scripts
- Explicitly remove DTD catalogs from /etc/sgml/catalog on uninstall
- Triggers to fix up after docbook-dtd* uninstallation

* Thu Jan 17 2002 Tim Waugh <twaugh@redhat.com> 1.0-1
- Merged all the DTD packages into one (bug #58448).
- Use /usr/share/sgml exclusively.
- Prevent catalog files from disappearing on upgrade (bug #58463).
