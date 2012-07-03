Name: sgml-common
Version: 0.6.3
Release: alt14

%define xmlcharent_version 0.3

Summary: Common SGML catalog and DTD files
Group: Publishing
License: GPL+
Url: http://sources.redhat.com/docbook-tools/
Packager: Igor Vlasenko <viy@altlinux.ru>

BuildArch: noarch

BuildRequires: xml-utils

Source0: ftp://sources.redhat.com/pub/docbook-tools/new-trials/SOURCES/%name-%version.tar.bz2
Source1: http://www.oasis-open.org/committees/docbook/xmlcharent/%xmlcharent_version/xmlcharent-%xmlcharent_version.tar.bz2
# From openjade:
Source3: xml.dcl
Source4: xml.soc
Source5: html.dcl
Source6: html.soc
Source7: sgml.buildreq
Patch0: %name-umask.patch
Patch1: %name-xmldir.patch
Patch2: %name-quotes.patch
Patch3: %name-automake.patch
Patch4: %name-0.6.3-docdir.patch

# a feature; can't yet be implemented due to #20463
%def_disable store_configs_in_etc

%define sgmlbase	%_datadir/sgml
%define sgmlconfdir	%_sysconfdir/sgml
%define sgmlentitiesdir	%sgmlbase/sgml-iso-entities-8879.1986
%define xmlbase		%_datadir/xml
%define xmlconfdir	%_sysconfdir/xml
%define xmlentitiesdir	%xmlbase/xml-iso-entities-8879.1986
%if_enabled store_configs_in_etc
%define docbookxmlcatalog	%sgmlconfdir/docbook/xmlcatalog
# old ALTLinux compatible symlink
%define xmlcataloglink	%xmlbase/docbook/catalog
%else
%define docbookxmlcatalog	%xmlbase/docbook/catalog
# new fedora compatible symlink
%define xmlcataloglink	%sgmlconfdir/docbook/xmlcatalog
%endif

%description
This package contains a collection of entities and DTDs that are useful for
processing SGML, but that do not need to be included in multiple packages.
%name also includes an up-to-date Open Catalog file.

%package -n xml-common
Summary: Common XML catalog and DTD files
License: GPL
Group: Publishing

%description -n xml-common
This package contains a collection of entities and DTDs that are useful for
processing XML, but that do not need to be included in multiple packages.

%prep
%setup -q -a 1
%patch0 -p1 -b .umask
%patch1 -p1 -b .xmldir
%patch2 -p1 -b .quotes
%patch3 -p1 -b .automake
%patch4 -p1 -b .docdir

%build
autoreconf -isfv
%configure --with-docdir=%_docdir

%install
#DESTDIR=$RPM_BUILD_ROOT
%makeinstall docdir=$RPM_BUILD_ROOT%_docdir

# Replace the XML character entities with the new docbook entities
%__rm -f $RPM_BUILD_ROOT%xmlentitiesdir/ISO*.ent
install -m644 xmlcharent-%xmlcharent_version/*.ent \
    $RPM_BUILD_ROOT%xmlentitiesdir/
%__perl -pi -e 's|ISO(\w+\.ent)|iso-$1|' \
    $RPM_BUILD_ROOT%xmlentitiesdir/catalog

install -d -m755 $RPM_BUILD_ROOT%sgmlbase
install -d -m755 $RPM_BUILD_ROOT%sgmlbase/docbook

install -d -m755 $RPM_BUILD_ROOT%xmlconfdir
install -d -m755 $RPM_BUILD_ROOT%xmlbase/docbook
install -d -m755 $RPM_BUILD_ROOT%sgmlconfdir/docbook


# Create an XML catalog for ISO XML character entities
CATALOG=$RPM_BUILD_ROOT%xmlentitiesdir/xmlcatalog
%_bindir/xmlcatalog --noout --create $CATALOG
%_bindir/xmlcatalog --noout --add "public" \
	"ISO 8879:1986//ENTITIES Added Latin 1//EN//XML" \
	iso-lat1.ent $CATALOG
%_bindir/xmlcatalog --noout --add "public" \
	"ISO 8879:1986//ENTITIES Added Latin 2//EN//XML" \
	iso-lat2.ent $CATALOG
%_bindir/xmlcatalog --noout --add "public" \
	"ISO 8879:1986//ENTITIES Diacritical Marks//EN//XML" \
	iso-dia.ent $CATALOG
%_bindir/xmlcatalog --noout --add "public" \
	"ISO 8879:1986//ENTITIES Box and Line Drawing//EN//XML" \
	iso-box.ent $CATALOG
%_bindir/xmlcatalog --noout --add "public" \
	"ISO 8879:1986//ENTITIES Numeric and Special Graphic//EN//XML" \
	iso-num.ent $CATALOG
%_bindir/xmlcatalog --noout --add "public" \
	"ISO 8879:1986//ENTITIES Publishing//EN//XML" \
	iso-pub.ent $CATALOG
%_bindir/xmlcatalog --noout --add "public" \
	"ISO 8879:1986//ENTITIES General Technical//EN//XML" \
	iso-tech.ent $CATALOG
%_bindir/xmlcatalog --noout --add "public" \
	"ISO 8879:1986//ENTITIES Added Math Symbols: Arrow Relations//EN//XML" \
	iso-amsa.ent $CATALOG
%_bindir/xmlcatalog --noout --add "public" \
	"ISO 8879:1986//ENTITIES Added Math Symbols: Binary Operators//EN//XML" \
	iso-amsb.ent $CATALOG
%_bindir/xmlcatalog --noout --add "public" \
	"ISO 8879:1986//ENTITIES Added Math Symbols: Delimiters//EN//XML" \
	iso-amsc.ent $CATALOG
%_bindir/xmlcatalog --noout --add "public" \
	"ISO 8879:1986//ENTITIES Added Math Symbols: Negated Relations//EN//XML" \
	iso-amsn.ent $CATALOG
%_bindir/xmlcatalog --noout --add "public" \
	"ISO 8879:1986//ENTITIES Added Math Symbols: Ordinary//EN//XML" \
	iso-amso.ent $CATALOG
%_bindir/xmlcatalog --noout --add "public" \
	"ISO 8879:1986//ENTITIES Added Math Symbols: Relations//EN//XML" \
	iso-amsr.ent $CATALOG
%_bindir/xmlcatalog --noout --add "public" \
	"ISO 8879:1986//ENTITIES Greek Letters//EN//XML" \
	iso-grk1.ent $CATALOG
%_bindir/xmlcatalog --noout --add "public" \
	"ISO 8879:1986//ENTITIES Monotoniko Greek//EN//XML" \
	iso-grk2.ent $CATALOG
%_bindir/xmlcatalog --noout --add "public" \
	"ISO 8879:1986//ENTITIES Greek Symbols//EN//XML" \
	iso-grk3.ent $CATALOG
%_bindir/xmlcatalog --noout --add "public" \
	"ISO 8879:1986//ENTITIES Alternative Greek Symbols//EN//XML" \
	iso-grk4.ent $CATALOG
%_bindir/xmlcatalog --noout --add "public" \
	"ISO 8879:1986//ENTITIES Russian Cyrillic//EN//XML" \
	iso-cyr1.ent $CATALOG
%_bindir/xmlcatalog --noout --add "public" \
	"ISO 8879:1986//ENTITIES Non-Russian Cyrillic//EN//XML" \
	iso-cyr2.ent $CATALOG

# Create an empty XML catalog.
CATALOG=$RPM_BUILD_ROOT%xmlconfdir/catalog
%_bindir/xmlcatalog --noout --create $CATALOG
# Now put the common DocBook entries in it
%_bindir/xmlcatalog --noout --add "delegatePublic" \
	"-//OASIS//ENTITIES DocBook XML" \
	"file://%docbookxmlcatalog" $CATALOG
%_bindir/xmlcatalog --noout --add "delegatePublic" \
	"-//OASIS//DTD DocBook XML" \
	"file://%docbookxmlcatalog" $CATALOG
%_bindir/xmlcatalog --noout --add "delegatePublic" \
	"ISO 8879:1986" \
	"file://%xmlentitiesdir/xmlcatalog" $CATALOG
%_bindir/xmlcatalog --noout --add "delegateSystem" \
	"http://www.oasis-open.org/docbook/" \
	"file://%docbookxmlcatalog"  $CATALOG
%_bindir/xmlcatalog --noout --add "delegateURI" \
	"http://www.oasis-open.org/docbook/" \
	"file://%docbookxmlcatalog"  $CATALOG

# Also create the common DocBook catalog
CATALOG=$RPM_BUILD_ROOT%docbookxmlcatalog
%_bindir/xmlcatalog --noout --create $CATALOG
%_bindir/xmlcatalog --noout --add "delegatePublic" \
	"ISO 8879:1986" \
	"file://%xmlentitiesdir/xmlcatalog" $CATALOG

ln -s %docbookxmlcatalog\
	$RPM_BUILD_ROOT%xmlcataloglink
# old fedora and current mandriva compatible symlink
ln -s %docbookxmlcatalog\
	$RPM_BUILD_ROOT%sgmlbase/docbook/xmlcatalog

# Install empty SGML catalog
install -m644 /dev/null $RPM_BUILD_ROOT%sgmlconfdir/catalog

# Install .dcl and .soc files from Openjade 
rm -f $RPM_BUILD_ROOT%sgmlbase/xml.dcl
install -m644 %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} \
	$RPM_BUILD_ROOT%sgmlbase

# Buildreq filter for sgml.
install -pD -m644 %SOURCE7 $RPM_BUILD_ROOT%_sysconfdir/buildreqs/files/ignore.d/sgml

%if_enabled store_configs_in_etc
## TODO mv %xmlbase/docbook/catalog %docbookxmlcatalog
%triggerpostun -- xml-common <= 0.6.3-alt12
if ! [ -L %xmlbase/docbook/catalog ];then
   mv %xmlbase/docbook/catalog %docbookxmlcatalog
   ln -s %docbookxmlcatalog %xmlbase/docbook/catalog
fi
%endif

%files
%dir %sgmlconfdir
%config(noreplace,missingok) %sgmlconfdir/catalog
%config(noreplace) %sgmlconfdir/sgml.conf
%dir %sgmlbase
%dir %sgmlbase/docbook
%sgmlbase/*.dcl
%sgmlbase/*.soc
%sgmlentitiesdir
%_bindir/sgmlwhich
%_bindir/install-catalog
%_man8dir/*
%_docdir/*
%config %_sysconfdir/buildreqs/files/ignore.d/sgml

%files -n xml-common
#%doc xmlcharent-%xmlcharent_version/*.html
%dir %xmlconfdir
%config(noreplace) %verify(not md5 size mtime) %xmlconfdir/catalog
%dir %xmlbase
%dir %xmlbase/docbook
%config(noreplace) %verify(not md5 size mtime) %docbookxmlcatalog
%xmlcataloglink
# we need it to store %docbookxmlcatalog in /etc + fedora compatible way.
%dir %sgmlconfdir/docbook
# old fedora and current mandriva compatible symlink
%sgmlbase/docbook/xmlcatalog
%xmlentitiesdir

%changelog
* Tue Jun 16 2009 Igor Vlasenko <viy@altlinux.ru> 0.6.3-alt14
- swapped back /usr/share/xml/docbook/catalog and /etc/sgml/docbook/xmlcatalog
  (fixes: #20463)
- TODO: investigate behaviour of xmllint/libxml2.

* Thu Jun 11 2009 Igor Vlasenko <viy@altlinux.ru> 0.6.3-alt13
- moved /usr/share/xml/docbook/catalog to /etc/sgml/docbook/xmlcatalog.
- added trigger to manage a symlink at the old location.
- added compat symlinks for Fedora and Mandriva compatibility.

* Thu Jun 11 2009 Igor Vlasenko <viy@altlinux.ru> 0.6.3-alt12
- I hereby claim the ownership of the package ;)
- refreshed patches from fedora srpm (cosmetics only).
- changed: License Tag

* Sun Mar 28 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.6.3-alt11
- Added buildreqs ignore filter on *.cat files in the SGML dir

* Thu Feb 26 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.6.3-alt10
- Minor cleanups

* Thu Feb 26 2004 Dmitry V. Levin <ldv@altlinux.org> 0.6.3-alt9.1
- Fixed build with fresh autotools.

* Sun May 25 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.6.3-alt9
- Synchronized with 0.6.3-14 from RedHat
- XML character entities version 0.3
- Added /etc/sgml/catalog to the file list

* Mon Nov 11 2002 Stanislav Ievlev <inger@altlinux.ru> 0.6.3-alt8
- rebuild

* Wed Mar 27 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.6.3-alt7
- New XML character entities from the DocBook project

* Sun Jan 27 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.6.3-alt6
- Removed xml filter for buildreq because XML catalog system doesn't
  involve unnecessary catalog searches
- Added centralized DocBook DTD catalogs to the buildreq ignore filter
- Added /usr/share/sgml/xml.dcl to the file list
- Create an XML catalog for XML ISO entities

* Fri Jan 25 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.6.3-alt5
- Added xml filter for buildreq.

* Thu Jan 24 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.6.3-alt4
- Added sgml filter for buildreq.

* Thu Jan 24 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.6.3-alt3
- Synchronized with RedHat 0.6.3-8
- Updated URL that was just smoking crack
- Added delegation to ISO entities to docbook catalog

* Tue Jan 08 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.6.3-alt2
- Added directories /usr/share/sgml{,docbook} to the sgml-common file list

* Mon Jan 07 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.6.3-alt1
- Synchronized with Redhat 0.6.3-6
- Removed all the wacky scripts -- sgml-common is going to be PreReq
  of anything SGML-related, no post(un)install hacks are necessary

* Sun Jul 08 2001 Mikhail Zabaluev <mhz@altlinux.ru> 0.5-alt1
- synchronized with RH's 0.5-7

* Tue Mar 20 2001 Ivan Zakharyaschev <vanyaz@mccme.ru> 0.2-ipl5mdk
- internal changes in the spec-file:
  + explicitly specify the redirection in the install time scripts;
  + a macro for the conf-dir

* Tue Mar 20 2001 Ivan Zakharyaschev <vanyaz@mccme.ru> 0.2-ipl4mdk
- internal changes in the spec-file:
  + merged RE and Cooker specs; taken from RE:
    * Sun Mar 11 2001 AEN <aen@logic.ru>
    - permissions fixed
  + %%entitiesdir macro used in the spec
- install-time scripts:
  + %%postun moved to %%preun
  + %%post splitted into %%post and %%pre
  + a macro for adding/removing the entities catalog
    to all centralized catalogs

* Wed Mar 14 2001 Camille Begnis <camille@mandrakesoft.com> 0.2-4mdk
- Redirect install-catalog output to /dev/null

* Tue Feb 13 2001 Camille Begnis <camille@mandrakesoft.com> 0.2-3mdk
- move install-catalog.8.bz2 from man/en/man8 to man/man8

* Fri Jan 05 2001 Camille Begnis <camille@mandrakesoft.com> 0.2-2mdk
- add catalog management
- fix execute permissions

* Wed Aug 23 2000 Camille Begnis <camille@mandrakesoft.com> 0.2-1mdk
- 0.2
- adapt spec from Eric Bischoff <ebisch@cybercable.tm.fr>
- Pre-LSB compliance
