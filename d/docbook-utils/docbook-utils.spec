Name: docbook-utils
Version: 0.6.14
Release: alt4

Summary: Shell scripts for managing DocBook documents
Group: Publishing
License: GPLv2+
Url: http://sources.redhat.com/docbook-tools/
BuildArch: noarch

# ftp://sources.redhat.com/pub/docbook-tools/new-trials/SOURCES/%name-%version.tar.gz
Source0: %name-%version.tar
Source1: db2html
Source2: gdp-both.dsl
# Newer version of docbook2man-spec.pl for better handling of docbook2man
# conversion from http://sourceforge.net/projects/docbook2x/
Source3: docbook2man-spec.pl

Patch0: docbook-utils-spaces.patch
Patch1: docbook-utils-2ndspaces.patch
Patch2: docbook-utils-w3mtxtconvert.patch
Patch3: docbook-utils-grepnocolors.patch
Patch4: docbook-utils-sgmlinclude.patch
Patch5: docbook-utils-rtfmanpage.patch
Patch6: docbook-utils-papersize.patch
Patch7: docbook-utils-nofinalecho.patch

Patch11: docbook-alt-jw-grep.patch.patch
Patch12: docbook-alt-docbook2man-spec.diff

Requires: docbook-style-dsssl >= 1.72
Requires: docbook-dtds
Requires: openjade >= 1.3.2
Requires: OpenSP
Requires: perl-SGMLSpm >= 1.03ii
Conflicts: sgml-tools < 0:0.6.9-ipl24mdk

BuildPreReq: perl(SGMLS.pm)
# Automatically added by buildreq on Tue Sep 16 2008
BuildRequires: OpenSP docbook-style-dsssl openjade

%define du_dir %_datadir/sgml/docbook/utils-%version
%define _compress_method gzip
%define docdir %_docdir/%name-%version

%description
These little scripts allow to convert DocBook files to other formats
(HTML, RTF, TeX...), and to compare SGML files.

%package print
Summary: Scripts for converting DocBook documents to PDF, PostScript and DVI
Group: Publishing
Provides: %name-pdf
Obsoletes: %name-pdf < %version-%release
Requires: %name = %version-%release
Requires: jadetex >= 2.5
Requires: %_bindir/dvips

%description print
The scripts from %name distribution that allow to convert DocBook files
to formats suitable for printing (PostScript, PDF, DVI).

%prep
%setup
install -pm755 %_sourcedir/docbook2man-spec.pl helpers/
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch11 -p1
%patch12 -p1

%build
%configure
%make_build

%install
%makeinstall htmldir=%buildroot%docdir

for util in dvi html pdf ps rtf; do
	ln -s docbook2$util %buildroot%_bindir/db2$util
	ln -s jw.1 %buildroot%_man1dir/db2$util.1
done
ln -s jw.1 %buildroot%_man1dir/docbook2txt.1

# db2html is not just a symlink, as it has to create the output directory
rm %buildroot%_bindir/db2html
install -pm755 %_sourcedir/db2html %buildroot%_bindir/db2html

install -pm644 %_sourcedir/gdp-both.dsl \
	%buildroot%du_dir/docbook-utils.dsl

install -pm644 AUTHORS NEWS README TODO %buildroot%docdir/

# frontend-spec and backend-spec names are too generic
for f in %buildroot%_man7dir/*-spec.*; do
	mv -f "$f" %buildroot%_man7dir/jw-"${f##*/}"
done

%files
%du_dir/
%_bindir/*
%_man1dir/*
%_man7dir/*
%docdir/
%exclude %_bindir/*dvi
%exclude %_bindir/*pdf
%exclude %_bindir/*ps
%exclude %du_dir/backends/dvi
%exclude %du_dir/backends/pdf
%exclude %du_dir/backends/ps
%exclude %_man1dir/*dvi.1*
%exclude %_man1dir/*pdf.1*
%exclude %_man1dir/*ps.1*

%files print
%_bindir/*dvi
%_bindir/*pdf
%_bindir/*ps
%du_dir/backends/dvi
%du_dir/backends/pdf
%du_dir/backends/ps
%_man1dir/*dvi.1*
%_man1dir/*pdf.1*
%_man1dir/*ps.1*

%changelog
* Wed Sep 22 2010 Dmitry V. Levin <ldv@altlinux.org> 0.6.14-alt4
- Updated to FC docbook-utils-0.6-14-24, fixed regressions
  introduced by this update.
- jw: Fixed [:space:] bugs in regexps, uncovered by grep-2.7.

* Wed Oct 07 2009 Grigory Batalov <bga@altlinux.ru> 0.6.14-alt3
- Replace tetex-dvips requirement with dvips binary.

* Tue Sep 16 2008 Yuri N. Sedunov <aris@altlinux.org> 0.6.14-alt2
- updated buildreqs
- fix subdirectories packaging violation

* Wed Feb 25 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.6.14-alt1
- New upstream release

* Fri Mar 28 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.6.13-alt1
- New version
- Print subpackage with dependencies to jadetex and tetex-dvips

* Sat Nov 16 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.6.12-alt1
- 0.6.12
- Corrected permissions for db2html
- Prefixed too broadly named manpages in man7
- Install the documentation via make install

* Fri Sep 27 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.6.11-alt1
- 0.6.11
- Patches have gone upstream

* Tue Jun 11 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.6.10-alt3
- Patch to determine DTD version correctly
- Eliminated A4 hack stylesheet
- Abolished the pdf subpackage, as it doesn't have any outstanding dependencies

* Thu May 23 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.6.10-alt2
- Sync with 0.6.10-3 from RedHat

* Tue May 07 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.6.10-alt1
- With new version, all the patches are gone.
- Generate filelist of non-pdf binaries

* Thu May 02 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.6.9-alt3
- Synchronized with RedHat 0.6.9-25, where an insecure file writing
  vulnerability has been fixed.

* Mon Feb 18 2002 AEN <aen@logic.ru> 0.6.9-alt2
- Added docbook2rtf to %files.
- Conflicts with sgml-tools < 0:0.6.9-ipl24mdk.

* Sun Jan 27 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.6.9-alt1
- New version, sync with RedHat 0.6.9-19
- Spec cleanup
- Conflicts with sgml-tools

* Thu May 31 2001 AEN <aen@logic.ru> 0.6-alt1
- build for Sisyphus

* Fri Jan 12 2001 Camille Begnis <camille@mandrakesoft.com> 0.6-1mdk
- New for Mandrake
- Mandrakized from ftp://sources.redhat.com/pub/docbook-tools/new-trials/SPECS/docbook-utils.spec
