Name: alt-entities
Version: 0.12
Release: alt1
Group: Publishing

Summary: XML Entities and DTD for ALT Linux Documentation Project

License: Distributable
Url: http://docs.altlinux.ru

PreReq: xml-common xml-utils sgml-common

Source0: http://docs.altlinux.ru/%name-%version.tar.bz2

BuildArch: noarch

%define xmlconfdir	%_sysconfdir/xml
%define altentdir       %_datadir/xml/alt-entities      
%define catalog         %xmlconfdir/catalog

%description
XML entities and DTD for ALT Linux Documentation Project, 
used for making documentation in DocBook/XML format.

%description -l ru_RU.CP1251
XML entities (сущности, переменные) и DTD, используемые в проекте 
ALT Linux Documentation для создания документации в формате
DocBook/XML.


%prep
%setup

%build

%install

%__mkdir -p %buildroot%altentdir
%__cp -a persons %buildroot%altentdir
%__mkdir -p %buildroot%altentdir/ru/entities
%__cp -a entities/*.ent %buildroot%altentdir/ru/entities
%__cp -a entities/catalog.xml %buildroot%altentdir
%__cp -a entities/catalog.sgml %buildroot%altentdir
%__cp -a dtd %buildroot%altentdir
%__mkdir -p %buildroot%_sysconfdir/buildreqs/files/ignore.d
%__cp -a alt-entities.ignore.buildreq %buildroot%_sysconfdir/buildreqs/files/ignore.d/alt-entities

# FIXME: add ChangeLog (building from cvs)
%files
%doc entities/README
%altentdir
%_sysconfdir/buildreqs/files/ignore.d/alt-entities

%post
if [ $1 = 1 ] ; then
/usr/bin/xmlcatalog --noout --add "nextCatalog" \
        "file://%altentdir/catalog.xml" \
        "" \
        %catalog ||:
/usr/bin/xmlcatalog --noout --sgml --add "%altentdir/catalog.sgml" ||:
fi

%postun
if [ $1 = "0" ] ; then
/usr/bin/xmlcatalog --noout --del \
	"file://%altentdir/catalog.xml" \
        %catalog ||:
/usr/bin/xmlcatalog --noout --sgml --del /etc/sgml/catalog "%altentdir/catalog.sgml" ||:
fi

%triggerpostun -- alt-entities = 0.1-alt1
/usr/bin/xmlcatalog --noout --add "nextCatalog" \
        "file://%altentdir/catalog.xml" \
        "" \
        %catalog ||:

%triggerpostun -- alt-entities = 0.2-alt3
/usr/bin/xmlcatalog --noout --del \
	"file://%altentdir/catalog.xml" \
        %catalog ||:
/usr/bin/xmlcatalog --noout --add "nextCatalog" \
        "file://%altentdir/catalog.xml" \
        "" \
        %catalog ||:

%changelog
* Tue Oct 09 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 0.12-alt1
- Fixed OpenOffice.org entities (#13058)

* Mon Aug 06 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 0.11-alt1
- 0.11 (added WINVISTA in common.ent)

* Fri May 04 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 0.10-alt1
- 0.10 (fixed links in common.ent)

* Mon Jun 28 2004 Vitaly A. Ostanin <vyt@altlinux.ru> 0.9-alt1
- 0.9 release (new entities, make persons.xml valid)

* Fri Mar 12 2004 Vyt <vyt@altlinux.ru> 0.8-alt1
- 0.8 release 
- updated common.ent
- updated persons.xml (added 'olpa', 'tibor', 'dmitryg', 'oes', 'oddity', 'wrar', 
  'hmepas', 'canis', 'peet', 'ilar', 'kas', 'dav', 'warframe', 'past', 'horror', 
  'mutabor', 'vk', 'brun')

- Added catalog.sgml for using with emacs-psgml-mode

* Thu Oct  9 2003 Vyt <vyt@altlinux.ru> 0.7-alt1
- 0.7 release
- Added catalog.sgml for using with emacs-psgml-mode

* Wed Sep 10 2003 Vyt <vyt@altlinux.ru> 0.6-alt2
- Fixed path to buildreq file

* Wed Sep 10 2003 Vyt <vyt@altlinux.ru> 0.6-alt1
- 0.6 release
- Added file for ignoring alt-entities from /etc/xml/catalog lockups (tnx to MhZ)

* Fri Aug  8 2003 Vyt <vyt@altlinux.ru> 0.5-alt1
- 0.5 release

* Mon May 19 2003 Vyt <vyt@altlinux.ru> 0.4-alt1
- 0.4 (added DTD DocBook customization)
- build from official tarball

* Wed Feb 12 2003 Vyt <vyt@altlinux.ru> 0.3-alt1
- 0.3 (added persons.xml and dtd)
- Moved to 'nextCatalog' catalogs resolution

* Fri Jan 24 2003 Vyt <vyt@altlinux.ru> 0.2-alt3
- Fixed numbering in changelog

* Fri Nov 29 2002 Vyt <vyt@altlinux.ru> 0.2-alt2
- added triggerpostun script (thanks to Sergey Vlasov). 
  Now update worked automatically

* Thu Nov 28 2002 Vyt <vyt@altlinux.ru> 0.2-alt1
- 0.2 (added keys.ent)
- fixed postun script (thanks to Alexander Bokovoy). 
  For update from 0.1-alt1 you should reinstall 0.2-alt1 after update :(

* Wed Sep 19 2002 Vyt <vyt@altlinux.ru> 0.1-alt1
- 0.1
- First build for Sisyphus
