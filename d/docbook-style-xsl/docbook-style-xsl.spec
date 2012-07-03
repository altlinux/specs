## %%define snapshot 20080311

Name: docbook-style-xsl
Version: 1.75.2
Release: alt1
Group: Publishing

Summary: Norman Walsh's XSL stylesheets for DocBook XML

License: Distributable
Url: http://docbook.sourceforge.net/projects/xsl/

%ifdef snapshot
%define actual_version snapshot
%define actual_archive zip
%else
%define actual_version %version
%define actual_archive tar.bz2
%endif

%define xmlbase		%_datadir/xml
%define xmlconfdir	%_sysconfdir/xml
%define hack_output_encodings koi8-r koi8-u windows-1251

Provides: docbook-xsl
#PreReq: docbook-dtd-xml
PreReq: xml-common xml-utils

AutoReq: yes

Source0: http://prdownloads.sourceforge.net/docbook/docbook-xsl-%{actual_version}.%{actual_archive}
Source1: http://prdownloads.sourceforge.net/docbook/docbook-xsl-doc-%{actual_version}.%{actual_archive}
Source2: docbook-output-stub.xsl
Source3: docbook-add-output-encoding.xsl

# Fedora Core patches
#Avoid proportional-column-width for passivetex (bug #176766).
Patch1: docbook-xsl-pagesetup.patch
#Hard-code the margin-left work around to expect passivetex (bug #113456).
Patch2: docbook-xsl-marginleft.patch
#fix of #161619 - adjustColumnWidths now available
Patch3: docbook-xsl-newmethods.patch
#change a few non-constant expressions to constant - needed for passivetex(#366441)
Patch4: docbook-xsl-non-constant-expressions.patch
#added fixes for passivetex extension and list-item-body(#161371)
Patch5: docbook-xsl-list-item-body.patch


BuildArch: noarch
BuildRequires: xsltproc perl-base xml-utils unzip

%package doc
Summary: Documentation for DocBook XSL stylesheets
Group: Publishing
AutoReqProv: none

%description
These XSL stylesheets allow to convert any DocBook document to other
formats, including those suited for print formatting (FO), online use
(HTML, XHTML), and manual files (man, htmlhelp, javahelp).
The stylesheets are highly customizable.

%description doc
This package contains extensive documentation to DocBook XSL stylesheets
in the HTML format.

%prep
%setup -q -n docbook-xsl-%{actual_version} -b 1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

find . -type f -name '*.xsl.orig' -delete
find . -type f -name '.gitignore' -delete
find . -type f -perm +a+x -print0 | xargs -r0 chmod a-x

%build
for enc in %hack_output_encodings; do
    xsltproc -o html/docbook-$enc.xsl --stringparam output.encoding $enc \
	%SOURCE3 %SOURCE2
done

%install
install -d -m755 %buildroot%xmlbase/docbook/xsl-stylesheets-%version
install -p -m644 VERSION \
    %buildroot%xmlbase/docbook/xsl-stylesheets-%version/
cp -a common eclipse fo highlighting html htmlhelp images javahelp lib \
      manpages profiling slides template website xhtml xhtml-1_1 roundtrip \
    %buildroot%xmlbase/docbook/xsl-stylesheets-%version/

# Do not copy scripts in tools/bin as they are purely for docbook developers
install -d -m755 %buildroot%xmlbase/docbook/xsl-stylesheets-%version/tools
cp -a tools/make %buildroot%xmlbase/docbook/xsl-stylesheets-%version/tools/

install -p -m644 catalog.xml \
    %buildroot%xmlbase/docbook/xsl-stylesheets-%version/

# ? RH#177256
#install -d -m755 %buildroot%xmlbase/docbook/xsl-stylesheets-%version/extensions
#install -p -m644 extensions/*.jar \
#    %buildroot%xmlbase/docbook/xsl-stylesheets-%version/extensions/

ln -sf xsl-stylesheets-%version %buildroot%xmlbase/docbook/xsl-stylesheets

%files
%doc AUTHORS BUGS COPYING NEWS* README RELEASE-NOTES.* TODO
%xmlbase/docbook/xsl-stylesheets-%version
%xmlbase/docbook/xsl-stylesheets

%files doc
%doc doc/*

%post
CATALOG=%xmlconfdir/catalog
/usr/bin/xmlcatalog --noout --add "rewriteSystem" \
	"http://docbook.sourceforge.net/release/xsl/%version" \
	"%xmlbase/docbook/xsl-stylesheets-%version" $CATALOG ||:
/usr/bin/xmlcatalog --noout --add "rewriteURI" \
	"http://docbook.sourceforge.net/release/xsl/%version" \
	"%xmlbase/docbook/xsl-stylesheets-%version" $CATALOG ||:
/usr/bin/xmlcatalog --noout --add "rewriteSystem" \
	"http://docbook.sourceforge.net/release/xsl/current" \
	"%xmlbase/docbook/xsl-stylesheets-%version" $CATALOG ||:
/usr/bin/xmlcatalog --noout --add "rewriteURI" \
	"http://docbook.sourceforge.net/release/xsl/current" \
	"%xmlbase/docbook/xsl-stylesheets-%version" $CATALOG ||:

%postun
if [ ! -d "%xmlbase/docbook/xsl-stylesheets-%version" ]; then
    CATALOG=%xmlconfdir/catalog
    /usr/bin/xmlcatalog --noout --del \
	"%xmlbase/docbook/xsl-stylesheets-%version" $CATALOG ||:
fi

%changelog
* Fri Jul 09 2010 Alexey Shabalin <shaba@altlinux.ru> 1.75.2-alt1
- 1.75.2
- Sync patches with fedora
- Don't ship the extensions (bug RH#177256)

* Sat Mar 22 2008 Alexander Bokovoy <ab@altlinux.org> 1.73.2-alt1
- 1.73.1
- Add post-release fixes from subversion repository
- Add correct BuildReqs
- Fix installation of utility scripts and makefiles

* Sun Oct 15 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.71.0-alt1
- Release 1.71.0
- Patch4 no longer applies
- Packaged catalog.xml (bug 10126)

* Wed May 31 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.70.1-alt1
- Release 1.70.1
- Patch3 no longer applies

* Sun Feb 19 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.69.1-alt2
- Summarily applied patches from FC package 1.69.1-5 (bug 9087)

* Fri Aug 12 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.69.1-alt1
- New upstream release

* Tue Jul 19 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.69.0-alt1
- New upstream release
- Retired the makefile
- Documentation now comes in a separate archive

* Tue Feb 15 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.68.1-alt1
- New upstream release

* Fri Feb 11 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.68.0-alt1
- New upstream release
- Patch0 has gone upstream

* Tue Dec 07 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.67.2-alt2
- Patch from CVS snapshot to fix GTK+ build (SF bug #1079453)

* Fri Dec 03 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.67.2-alt1
- New upstream release

* Wed Nov 10 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.67.0-alt1
- New upstream release

* Sun Sep 19 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.66.1-alt1
- New upstream release
- Removed bogus executable file permissions

* Sat Sep 11 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.66.0-alt1
- New upstream release

* Tue Dec 16 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.64.0-alt1
- New upstream release

* Tue Sep 30 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.62.4-alt1
- New upstream release

* Mon Sep 29 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.62.3-alt1
- New upstream release

* Mon Sep 29 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.62.2-alt1
- New upstream release

* Wed Sep 03 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.62.0-alt1
- New version

* Tue Jun 24 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.61.3-alt1
- New version

* Sat May 24 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.61.2-alt1
- New version

* Mon May 19 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.61.1-alt1
- New version

* Sat May 10 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.61.0-alt1
- New version

* Sun Jan 26 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.60.1-alt1
- 1.60.1

* Mon Jan 20 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.59.2-alt1
- 1.59.2

* Mon Jan 13 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.59.1-alt1
- 1.59.1

* Wed Dec 04 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.58.1-alt2
- Corrected description (bug #1655)

* Sat Nov 30 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.58.1-alt1
- 1.58.1
- dropped image scaling patch, not necessary now
- marker patch has gone upstream

* Sat Nov 16 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.57.0-alt1
- 1.57.0
- Marker patch from RedHat

* Fri Oct 11 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.56.1-alt1
- 1.56.1

* Thu Sep 26 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.55.0-alt1
- 1.55.0

* Thu Sep 12 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.54.1-alt1
- 1.54.1

* Wed Jul 31 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.53.0-alt1
- 1.53.0
- Actually applied the image scaling patch sent by Vyt. Sorry.
- Patch for common/targetdatabase.xml by Bob Stayton, passed by Vyt.

* Fri Jul 26 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.52.2-alt1
- 1.52.2
- Two fixes by Vyt (bugs 1118, 1119)

* Wed Jun 05 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.51.1-alt1
- 1.51.1
- Hack output encoding for Cyrillic charsets
- Use symlinks instead of duplication of saxon jars
- Separated doc package, as the unpacked docs amount to pretty big

* Tue Mar 26 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.50.0-alt1
- 1.50.0

* Mon Mar 11 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.49-alt1
- 1.49
- Make install scripts always happy
- Makefile overhaul, installs only jars off extensions

* Wed Jan 16 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.48-alt1
- Updated to next, non-experimental, version
- PreReq: xml-utils

* Mon Jan 07 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.47-alt1
- Adopted to ALT Linux
- Specfile cleanup
- Synchronized with RedHat 1.47-2
- Doc list fixes

* Fri Dec 14 2001 Camille Begnis <camille@mandrakesoft.com> 1.47-1mdk
- 1.47

* Thu Oct 25 2001 Camille Begnis <camille@mandrakesoft.com> 1.45-1mdk
- 1.45

* Wed Aug 22 2001 Camille Begnis <camille@mandrakesoft.com> 1.44-1mdk
- 1.44

* Tue Jul 03 2001 Camille Begnis <camille@mandrakesoft.com> 1.40-1mdk
- 1.40
- remove jade require
- update URL and Source (now on sourceforge)
- add a linkk from {sgmlbase}/docbook/xsl-stylesheets to xsl-stylesheets-{Version}

* Mon Jun 11 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.29-4mdk
- Merge patches from Abel Cheung:
- Remove extraneous character in Summary
- s/Copyright/License/
- Source is not downloadable itself, it's just a re-compressed archive
- Rearrange BuildArch to bottom, no idea why source and patch refuses
  to be removed otherwise
- More macros
- Removed useless variable
- Simplify %%files

* Tue Feb 27 2001 Camille Begnis <camille@mandrakesoft.com> 1.29-3mdk
- The VERSION file is in fact a stylesheet...

* Thu Feb 15 2001 Camille Begnis <camille@mandrakesoft.com> 1.29-2mdk
- Remove jade prereq

* Fri Feb 09 2001 Camille Begnis <camille@mandrakesoft.com> 1.29-1mdk
- 1.29
- move doc directory to {docdir}
- remove docsrc

* Fri Jan 05 2001 Camille Begnis <camille@mandrakesoft.com> 1.24-1mdk
- 1.24
- fix bin permissions

* Thu Nov 14 2000 Camille Begnis <camille@mandrakesoft.com> 1.18-1mdk
- New
- Much work To do: file perms, catalog?
