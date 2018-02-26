# -*- mode: RPM-SPEC; tab-width: 4; fill-column: 70; -*-
# $Id: rpm-build-docs.spec,v 1.16 2005/12/07 11:39:10 maslinych Exp $

%define docsdatadir %_datadir/docs-build
%define _perl_lib_path %docsdatadir/docs_genspec:%docsdatadir/docinfo2html

Name: rpm-build-docs-experimental
Version: 0.4
Release: alt2
Packager: Artem Zolochevskiy <azol@altlinux.ru>

Summary: RPM helper macros to rebuild documentation packages
Summary(ru_RU.UTF-8): Набор утилит и макросов для автоматической сборки документации
License: GPL
Group: Development/Other
Url: http://heap.altlinux.ru/engine/Docs/Build/RpmBuildDocs

BuildArch: noarch

Requires: %_sysconfdir/rpm/macros.d 
Requires: rpm-utils xsltproc alt-docs-xsl-common alt-docs-xsl-html alt-entities
Requires: docbook-dtds sgml-tools OpenSP ALDConvert enca

Conflicts: rpm-build-docs

Source: %name-%version.tar

# Automatically added by buildreq on Sat Jun 04 2005 (-bi)
BuildRequires: perl-Archive-Tar perl-Compress-Zlib perl-HTML-Parser perl-HTML-Tagset perl-HTML-Tree perl-IO-String perl-IO-Zlib perl-Template sgml-tools xsltproc


%description
These helper macros provide possibility to rebuild documentation
modules by some Alt Docs Team Policy compatible way.

%description -l ru_RU.UTF-8
Набор утилит и макросов для автоматической сборки документации
в соответствии с Alt Docs Team Policy.

%prep
%setup

%build
sed -i 's,%%_docsdatadir,%docsdatadir,g' \
	bin/* data/docs_genspec/Heap/Config.pm data/docsbuild/* 

%install
mkdir -p \
	%buildroot/%_bindir \
	%buildroot/%docsdatadir/{docs_genspec,docsbuild,docs_navigation,docinfo2html} \
	%buildroot%_sysconfdir/rpm/macros.d 

cp -f bin/* %buildroot/%_bindir
cp -f rpm/* %buildroot/%_sysconfdir/rpm/macros.d/rpm-build-docs
cp -rf data/* %buildroot/%docsdatadir/

%files
%_bindir/*
%docsdatadir
%_sysconfdir/rpm/macros.d/rpm-build-docs
%doc README.ru.txt examples/

%changelog
* Thu Apr 21 2011 Dmitry V. Levin <ldv@altlinux.org> 0.4-alt2
- Added docbook-dtds to requirements.

* Mon Aug 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.4-alt1
- new version
  + changed issue source file name to unified "index.html"

* Thu Jul 19 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.3-alt1
- new version
  + issue file name shold be: %%issuename.html (desktop.html)
  + License file for issue is also needed
  + added exmple module and issue specs 

* Thu Jul 19 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- new version
  + added %%setup_docs_issue for using in issue specs
- fixed previous changelog entry

* Wed Jul 18 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus based on rpm-build-docs
- changes against rpm-build-docs:
  + %%setup_docs_module requires only two arguments:
    * module name
    * language for navigation links
  + %%_bindir/docs_issue_requires can handle modules without commiter_id now

* Thu May 17 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 0.4.5-alt11
- Added dirty hack for build m-k files in utf-8 encoding

* Thu Apr 26 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 0.4.5-alt10
- Construct requires from adt links, rpmquery not used

* Wed Dec 20 2006 Kirill Maslinsky <kirill@altlinux.ru> 0.4.5-alt9
- alttune.xsl removed, use tuning.xsl from alt-docs-xsl-common instead 
  (closes #10459, thanks vyt@)
- tighten requirements (alt-docs-xsl-{common,html} instead of alt-docs-xsl)
- Url updated

* Thu May 25 2006 Kirill Maslinsky <kirill@altlinux.ru> 0.4.5-alt8
- bugfix release
- docinfo2html: fixed rpm name generation for bugzilla links
- spec cleanup:
  + removed unnecessary macros and subst
  + fixed unquoted macros in changelog

* Wed Dec 07 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.4.5-alt7
- added alttune.xsl (wrapper xsl style)
- docsbuild/db_alt: rewritten (for correct work with new alt-docs-xsl
  and alttune.xsl)

* Wed Nov 16 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.4.5-alt6
docsbuild/db_alt: collect_images workaround (needs a better solution)

* Tue Nov 15 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.4.5-alt5
docsbuild/db_alt: added collect_images.xsl processing

* Thu Nov 10 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.4.5-alt4
- fixed %%docs_build macro parameters processing
	+ docs_navigation now is called from docsbuild script, 
	corresponding %%docs_navigation macro removed 
- html file conversion to utf8 moved to docsbuild and now is performed 
	only for the file with docs_navigation bar

* Fri Oct 28 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.4.5-alt3
- docsbuild/db_alt; added possibility for separate parameters supplying for both build stages

* Thu Oct 27 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.4.5-alt2
- docsbuild/modules.sh: fixed regex for DocBook/XML (ALT)

* Tue Oct 25 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.4.5-alt1
- docsbuild rewritten by george@
	+ docsbuild/extras added (george@)
	+ docsbuild/html fixed (kirill@)
- docs_genspec updated (kirill@)
	+ new release upgrading scheme 
	+ default URL added (heap.altlinux.ru)

* Tue Oct 04 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.4.4-alt5
- bugfixes:
  + html build module #8086
  + no more absolute links creation in docinfo2html

* Mon Sep 19 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.4.4-alt4
- found lost changes

* Tue Sep 13 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.4.4-alt3
- small bugfixes

* Tue Sep 13 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.4.4-alt2
- docs_genspec: bugfix in tempdir creation

* Sat Sep 10 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.4.4-alt1
- docs_genspec: new version processing logic

* Wed Aug 03 2005 Alexey Gladkov <legion@altlinux.ru> 0.4.3-alt1
- docs_genspec bugfix.

* Sun Jul 17 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.4.2-alt3
- new bugfixes
- db_alt enhanced (tuning.xsl added)

* Sat Jul 16 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.4.2-alt2
- bugfixes in docs_genspec, docinfo2html, docsbuild, rpm macros

* Sat Jul 16 2005 Alexey Gladkov <legion@altlinux.ru> 0.4.2-alt1
- new version;
- bugfixes;

* Tue Jun 14 2005 Alexey Gladkov <legion@altlinux.ru> 0.4.1-alt1
- many scripts bugfixes;

* Wed Jun 08 2005 Alexey Gladkov <legion@altlinux.ru> 0.4-alt2
- docs_navigation bugfix;

* Thu Jun 02 2005 Alexey Gladkov <legion@altlinux.ru> 0.4-alt1
- new version;
- scripts docinfo2html, docs_issue.pl, docs_issue_requires, 
  docs_mklinks and docs_navigation added;
- rpm macros changed;

* Fri Apr 29 2005 Alexey Gladkov <legion@altlinux.ru> 0.3.2-alt5
- remove rpm-build-docs from the BuildRequires.

* Thu Apr 28 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.3.2-alt4
- added dependency on OpenSP (for docsbuild sgml module)

* Sat Apr 23 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.3.2-alt3
- fixed %%_docsdatadir substitution in data/* source
- added package descriptions in Russian

* Tue Apr 19 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.3.2-alt2
- fixed error in docs_genspec
- fixed error in docsbuild

* Mon Apr 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.3.2-alt1
- in docs_genspec:
  + changed version processing logic (thx legion@);
  + option -V added for inserting explicit version;
  + now not adding changelog if no -c option given;
  + now better modifying existing spec;
- in docsbuild:
  + sgml module added to docsbuild (LinuxDoc to HTML); 
  + html module added (very simple, just move .html files and add index.html);
- rpm macros fix;
- README.ru.txt added;

* Thu Mar 31 2005 Alexey Gladkov <legion@altlinux.ru> 0.3.1-alt1
- help bugfix;

* Mon Mar 28 2005 Alexey Gladkov <legion@altlinux.ru> 0.3-alt1
- rpm macros rewritten by kirill@.
- genspec was renamed to docs_genspec and rewritten on perl.
- docsbuild major modifications.

* Wed Feb 10 2005 Alexey Gladkov <legion@altlinux.org> 0.2-alt1
- Initial build.
