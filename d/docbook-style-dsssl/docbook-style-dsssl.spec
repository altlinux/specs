Name: docbook-style-dsssl
Version: 1.79
Release: alt3
Summary: Modular stylesheets for DocBook by Norman Walsh
Group: Publishing
License: Distributable
URL: http://sourceforge.net/projects/docbook/
Requires: jade >= 1.2.1
Requires: docbook-dtds
Requires: sgml-common >= 0.5
BuildArch: noarch
Source0: http://prdownloads.sourceforge.net/docbook/docbook-dsssl-%version.tar
Source1: %name-%version.Makefile

%define sgmlbase %_datadir/sgml
%define sgmlconfdir %_sysconfdir/sgml

%description
These DSSSL stylesheets allow to convert any DocBook document to another
printed (for example, RTF or PostScript) or online (for example, HTML)
format. They are highly customizable.


%package utils
Summary: utilities for DocBook modular stylesheets
Group: Publishing

%description utils
This package contains a Perl script named collateindex.pl, which is used
to create index data for DocBook XML or SGML files.


%prep
%setup -n docbook-dsssl-%version
sed -i '1 s/^\(#![^#]*\)#.*/\1/' bin/collateindex.pl


%install
%makeinstall -f %SOURCE1
cp -a contrib %buildroot%sgmlbase/docbook/dsssl-stylesheets-%version/
ln -sf dsssl-stylesheets-%version %buildroot%sgmlbase/docbook/dsssl-stylesheets


%post
find %sgmlconfdir -type f \( -name 'sgml-docbook-*.cat' -o -name 'xml-docbook-*.cat' \) -print |
while read -r catalog; do
	%_bindir/install-catalog --add "$catalog" \
		%sgmlbase/docbook/dsssl-stylesheets-%version/catalog \
		>/dev/null 2>&1
done


%postun
if [ $1 = 0 -o ! -f %sgmlbase/docbook/dsssl-stylesheets-%version/catalog ]; then
	find %sgmlconfdir -type f \
		\( -name 'sgml-docbook-*.cat' -o -name 'xml-docbook-*.cat' \) -print |
	while read -r catalog; do
		%_bindir/install-catalog --remove "$catalog" \
			%sgmlbase/docbook/dsssl-stylesheets-%version/catalog \
			>/dev/null 2>&1
	done
fi


%triggerun -- %name < 1.78-alt2
DSLCATALOGS=$(echo %sgmlbase/docbook/dsssl-stylesheets-?.??*/catalog)
[ "$DSLCATALOGS" = '%sgmlbase/docbook/dsssl-stylesheets-?.??*/catalog' ] ||
find %sgmlconfdir -type f \
	\( -name 'sgml-docbook-*.cat' -o -name 'xml-docbook-*.cat' \) -print |
while read -r catalog; do
	for dslcatalog in $DSLCATALOGS; do
		[ "$dslcatalog" = %sgmlbase/docbook/dsssl-stylesheets-%version/catalog ] ||
		%_bindir/install-catalog --remove "$catalog" $dslcatalog >/dev/null 2>&1
	done
done


%files
%doc BUGS README ChangeLog WhatsNew RELEASE-NOTES.*
%sgmlbase/docbook/*


%files utils
%_bindir/*
%_man1dir/*


%changelog
* Fri Dec 16 2011 Michael Shigorin <mike@altlinux.org> 1.79-alt3
- built for Sisyphus

* Fri Dec 16 2011 Led <led@massivesolutions.co.uk> 1.79-cx0
- removed Conflicts
- updated Requires
- cleaned up spec
- fixed URL

* Thu Jun 19 2008 Led <led@altlinux.ru> 1.79-alt2
- fixed Conflicts

* Fri Nov 05 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.79-alt1
- New upstream release

* Sat Oct 04 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.78-alt3
- Remove comment from the collateindex.pl interpreter line that ticked off
  perl.req

* Mon Sep 01 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.78-alt2
- Streamlined the install scripts
- PreReq docbook-dtds rather than docbook-dtd-sgml
- Do not require openjade, it's only one of the processing tools
- Split requires for sgml-common

* Fri Mar 14 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.78-alt1
- 1.78
- moved collateindex.pl to utils subpackage
- moved frames to the stylesheet dir

* Thu Aug 01 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.77-alt1
- 1.77
- Moved contrib to be a legitimate part of the stylesheets

* Mon Mar 11 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.76-alt1
- 1.76
- An attempt at super robust install scripts
- Edited Makefile to fill gaps in files
- Added contrib and frames subdirectories to docs

* Fri Jan 25 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.74b-alt1
- New version, sync with RedHat 1.74b-2
- Corrected makefile
- Outsourced doc package since its source has independent versioning
- Disable shell and perl in AutoReq
- Spec cleanup

* Wed Jun 13 2001 AEN <aen@logic.ru> 1.64-alt3
- catalog name fixed (thnx to Aleksndr Blohin)

* Thu May 31 2001 AEN <aen@logic.ru> 1.64-alt2
- provides dssl-stylesheets

* Thu May 31 2001 AEN <aen@logic.ru> 1.64-alt1
- new version
- sync with MDK

* Wed Mar 21 2001 Ivan Zakharyaschev <vanyaz@mccme.ru> 1.62-ipl7mdk
- return right permissions to docs.

* Wed Mar 21 2001 Ivan Zakharyaschev <vanyaz@mccme.ru> 1.62-ipl6mdk
- don't redirect output of install-catalog to /dev/null
- indicate Conflicts with older sgml-tools

* Tue Mar 20 2001 Ivan Zakharyaschev <vanyaz@mccme.ru> 1.62-ipl5mdk
- install-time scripts: docbook-dtd31-sgml (and 41) triggered explicitly (specifying virtual
  docbook-dtd-sgml doesn't work)

* Tue Mar 20 2001 Ivan Zakharyaschev <vanyaz@mccme.ru> 1.62-ipl4mdk
- internal changes in the spec-file:
  + explicitly specify the redirection in the install time scripts;
  + a macro for the conf-dir
  + permissions fixed
  + %%dsssldir macro used in the spec
- install-time scripts:
  + %%postun moved to %%preun
  + %%post splitted into %%post and %%pre; %%post moved to %%triggerin
  + a macro for adding/removing the dsssl catalog
    to all centralized docbook catalogs

* Tue Mar 13 2001 Camille Begnis <camille@mandrakesoft.com> 1.62-4mdk
- Redirect install-catalog output to /dev/null

* Thu Feb 22 2001 Camille Begnis <camille@mandrakesoft.com> 1.62-3mdk
- The last change was to add a link from %sgmlbase/docbook/dsssl-stylesheets
  to dsssl-stylesheets-%version

* Mon Feb 05 2001 Camille Begnis <camille@mandrakesoft.com> 1.62-2mdk
- Add a

* Tue Jan 30 2001 Camille Begnis <camille@mandrakesoft.com> 1.62-1mdk
- 1.62

* Mon Jan 29 2001 Camille Begnis <camille@mandrakesoft.com> 1.61-1mdk
- 1.61

* Fri Jan 05 2001 Camille Begnis <camille@mandrakesoft.com> 1.60-2mdk
- remove management of openjade catalogs (why the hell it was here???)

* Wed Jan 03 2001 Camille Begnis <camille@mandrakesoft.com> 1.60-1mdk
- 1.60

* Mon Nov 20 2000 Camille Begnis <camille@mandrakesoft.com> 1.59-1mdk
- 1.59
- improve upgrading scripts

* Wed Aug 30 2000 Camille Begnis <camille@mandrakesoft.com> 1.57-1mdk
- 1.57

* Thu Aug 24 2000 Camille Begnis <camille@mandrakesoft.com> 1.56-3mdk
- Prereq : sgml-common >= 0.2

* Thu Aug 24 2000 Camille Begnis <camille@mandrakesoft.com> 1.56-2mdk
- install openjade's catalog, not jade's

* Wed Aug 23 2000 Camille Begnis <camille@mandrakesoft.com> 1.56-1mdk
- adapt spec from Eric Bischoff <ebisch@cybercable.tm.fr>
- Pre-LSB compliance
