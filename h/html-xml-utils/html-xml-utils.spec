Name: html-xml-utils
Version: 5.5
Release: alt1

Summary: A number of simple utilties for manipulating HTML and XML files
License: GPL
Group: System/Base
Url: http://www.w3.org/Tools/HTML-XML-utils
Source: %name-%version.tar

Summary(ru_RU.UTF-8): Несколько простых утилит для обработки XML- и HTML-файлов

%description
A number of simple utilties for manipulating HTML and XML files:
    cexport (1)          - create headerfile of exported declarations from a C file
    hxaddid (1)          - add ID's to selected elements
    hxcite (1)           - replace bibliographic references by hyperlinks
    hxcite-mkbib (1)     - expand references and create bibliography
    hxcopy (1)           - copy an HTML file while preserving relative links
    hxcount (1)          - count elements and attributes in HTML or XML files
    hxextract (1)        - extract selected elements
    hxclean (1)          - apply heuristics to correct an HTML file
    hxprune (1)          - remove marked elements from an HTML file
    hxincl (1)           - expand included HTML or XML files
    hxindex (1)          - create an alphabetically sorted index
    hxmkbib (1)          - create bibliography from a template
    hxmultitoc (1)       - create a table of contents for a set of HTML files
    hxname2id            - move some ID= or NAME= from A elements to their parents
    hxnormalize (1)      - pretty-print an HTML file
    hxnum (1)            - number section headings in an HTML file
    hxpipe (1)           - convert XML to a format easier to parse with Perl or AWK
    hxprintlinks (1)     - number links & add table of URLs at end of an HTML file
    hxtoc (1)            - insert a table of contents in an HTML file
    hxuncdata (1)        - replace CDATA sections by character entities
    hxunent (1)          - replace HTML predefined character entities to UTF-8
    hxunpipe (1)         - convert output of pipe back to XML format
    hxunxmlns (1)        - replace "global names" by XML Namespace prefixes
    hxwls (1)            - list links in an HTML file
    hxxmlns (1)          - replace XML Namespace prefixes by "global names"
    asc2xml, xml2asc (1) - convert between UTF8 and &#nnn; entities
    hxref (1)            - generate cross-references
    hxselect (1)         - extract elements that match a (CSS) selector

%prep
%setup

%build
%configure
%make_build

%install
DESTDIR=%buildroot %make_install install

%files
%_bindir/*
%_man1dir/*
%doc README AUTHORS ChangeLog TODO

%changelog
* Wed Sep 16 2009 Denis Klimov <zver@altlinux.org> 5.5-alt1
- updated to version 5.5
- remove needless -q param from %setup macros
- change source archive type to tar from tar.gz
- remove rename bin files. It's needless after 5.0 version
- remove BuildPreReq: sed

* Mon May 23 2005 Ilya G. Evseev <evseev@altlinux.ru> 3.7-alt1
- updated to version 3.7

* Mon Feb 28 2005 Ilya G. Evseev <evseev@altlinux.ru> 3.6-alt1
- version 3.6, containing new name2id utility
- specfile: changed URL

* Sun Nov 21 2004 Ilya G. Evseev <evseev@altlinux.ru> 3.5-alt1
- update to version 3.5
- Source0 URL changed to w3c site because project seems not dead
- manual pages are patched for providing links to renamed pages

* Sat Jul 10 2004 Ilya G. Evseev <evseev@altlinux.ru> 3.0-alt3
- replace dirnames by filepatterns in %files section for preventing
  package intersections (directories are already owned by main systems)

* Tue Jul  6 2004 Ilya G. Evseev <evseev@altlinux.ru> 3.0-alt2
- specfile fixups for compatibility with ALTLinux Specfile Convention
- added README.alt

* Tue Jun 15 2004 Ilya G. Evseev <evseev@altlinux.ru> 3.0-1
- Initial RPM build
