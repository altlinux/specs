Name: latex2html
Version: 2008
Release: alt1

%define compactversion 2002-2-1
%define srcname %name-%compactversion

Summary: LaTeX to HTML converter
License: GPLv2
Group: Publishing
Url: http://saftsack.fs.uni-bayreuth.de/~latex2ht
BuildArch: noarch

Source: %url/current/%srcname.tar.bz2
Patch0: latex2html-2002-gsfonts.patch
Patch1: latex2html-utf8.patch
Patch2: latex2html-koi8r.patch
Patch3: latex2html-2002-path.patch
Patch4: latex2html-2002-alt-perl-path.patch
Patch5: latex2html-2002-alt-perl-syntax.patch
Patch6: latex2html-2002-alt-manual-tex.patch
Patch7: latex2html-2002-alt-perlpath.patch
Patch8: latex2html-2002-rh-grayimg.patch
Patch9: latex2html-2002-rh-tabularx.patch

Requires: /usr/bin/latex /usr/bin/dvips
Requires: netpbm

# note that gs is required by tetex-dvips
Requires: %_bindir/gs
BuildPreReq: %_bindir/gs

BuildRequires(pre): rpm-build-texmf
# Automatically added by buildreq on Thu Mar 27 2008
BuildRequires: netpbm perl-DBM tetex-dvips tetex-latex

%description
Elaborate perl program to convert latex documents to html,
using LaTeX to process images and equations.

%prep
%setup -q -n %srcname
%patch0 -p1
#%patch1 -p1
#%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
%define _perl_lib_path %_datadir/%name
%add_findprov_skiplist %_datadir/%name/versions/*.pl

TMP=/tmp ./configure --with-gs=%_bindir/gs \
	--with-texpath=%_datadir/texmf/tex/ \
	--without-mktexlsr \
	--with-perl=%_bindir/perl \
	--prefix=%prefix \
	--libdir=%_datadir/%name \
	--shlibdir=%_datadir/%name \
	#

%make_build

cd ./docs
TEXINPUTS=.:../texinputs: latex manual
TEXINPUTS=.:../texinputs: latex manual
make
bzip2 -9f manual.ps

%install
# custom "make install" so paths are proper in the perl programs

mkdir -p %buildroot%_bindir
install -p -m755 %name pstoimg texexpand %buildroot%_bindir/

mkdir -p %buildroot%_datadir/%name
cp -avRf \
	IndicTeX-HTML L2hos.pm L2hos XyMTeX-HTML cweb2html docs example foilhtml icons makeseg styles texinputs versions \
	cfgcache.pm dot.latex2html-init l2hconf.pm makemap readme.hthtml \
	%buildroot%_datadir/%name/

mkdir -p %buildroot%_datadir/texmf/tex/latex/html
cp -avRf texinputs/* %buildroot%_datadir/texmf/tex/latex/html

# url.sty is part of latex (#10698)
rm %buildroot%_datadir/texmf/tex/latex/html/url.sty

# this russian style is subject to bNOPNYA
rm %buildroot%_datadir/%name/styles/russian.perl

# fix perl path in a few places:
sed -i '1s|/usr/local/bin/|/usr/bin/|' \
	%buildroot%_datadir/%name/cweb2html/cweb2html \
	%buildroot%_datadir/%name/cweb2html/makemake.pl \
	%buildroot%_datadir/%name/makeseg/makeseg

%files
%_bindir/*
%_datadir/%name/
%_datadir/texmf/tex/latex/html
%doc Changes FAQ LICENSE LICENSE.orig README readme.hthtml TODO BUGS INSTALL dot.latex2html-init example docs/manual.ps.bz2

%changelog
* Tue May 19 2009 Kirill Maslinsky <kirill@altlinux.ru> 2008-alt1
- NMU
- 2002-2-1 -> 2008
- new license (GPLv2)
- built with rpm-build-texmf
- replace dependencies on tetex-{latex,dvips} with /usr/bin/{latex,dvips}
- removed unnecessary calls to mktexlsr in post(un)

* Thu Mar 27 2008 Alexey Tourbin <at@altlinux.ru> 2002-alt6
- updated to 20041025 upstream tarball
- changed License tag to "non-free", packaged LICENSE
- removed /usr/share/texmf/*/url.sty which is part of latex (#10698)
- rh-grayimg.patch: fixes pstoimg ugly grey-backgrounded images
- rh-tabularx.patch: better support for tabularx environments
- relocated /usr/lib/latex2html to /usr/share/latex2html
- updated dependencies

* Sat Oct 04 2003 Dmitry V. Levin <ldv@altlinux.org> 2002-alt5
- Updated to release 2002-2-1.
- koi8r patch merged upstream.
- Fixed perl errors (at).

* Tue Jul 01 2003 Dmitry V. Levin <ldv@altlinux.org> 2002-alt4
- Fixed package dependencies.
- Fixed buildrequires.

* Wed Nov 27 2002 AEN <aen@altlinux.ru> 2002-alt3
- rebuilt with tetex-2.0

* Mon Nov 25 2002 AEN <aen@altlinux.ru> 2002-alt2
- --shlibdir added to %%configure (bug #1527)

* Mon Oct 28 2002 AEN <aen@altlinux.ru> 2002-alt1
- new version

* Mon Oct 08 2001 Dmitry V. Levin <ldv@altlinux.ru> 2000.1beta-alt2
- Updated beta tarball from ftp site.
- Added russian style patch (from Georgy Salnikov <sge@nmr.nioch.nsc.ru>).

* Thu Jun 21 2001 AEN <aen@logic.ru> 2000.1beta-alt1
- build for Sisyphus

* Tue Jun  5 2001 Matthias Badaire <mbadaire@mandrakesoft.com> 2000.1beta-2mdk
- fix pstoimg tmp variable issue

* Tue May 15 2001 Matthias Badaire <mbadaire@mandrakesoft.com> 2000.1beta-1mdk
- update to 2K.1beta

* Mon Jan 22 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 99.2beta8-4mdk
- include manual.ps following suggestion by David Aspinall <da@dcs.ed.ac.uk>

* Tue Nov  7 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 99.2beta8-3mdk
- fix specfile

* Fri Aug 25 2000 Geoffrey Lee <snailtalk@mandrakesof.com> 99.2beta8-2mdk
- readd /usr/bin/pstoimg ...oops ... (Erik Devriendt)
- fix license. There is no such thing as a GNU license.!

* Wed Aug 02 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 99.2beta8-1mdk
- new version to fix some nasty bugz (Meinhard E. Mayer)

* Sun Jul 30 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 99.2beta6-4mdk
- rebuild with cleanup

* Mon Mar 20 2000 Camille Begnis <camille@mandrakesoft.com> 99.2beta6-3mdk
- Fixed group

* Sat Mar 18 2000 Camille Begnis <camille@mandrakesoft.com> 99.2beta6-2mdk
- minor spec update

* Thu Feb 10 2000 Lenny Cartier <lenny@mandrakesoft.com>
- new in contribs
- used - once again - a great srpm provided by Vincent Danen <vdanen@linux-mandrake.com>

* Tue Feb 8 2000 Vincent Danen <vdanen@linux-mandrake.com>
- added fixes for some perl scripts that point to /usr/local/bin/perl

* Sun Feb 6 2000 Vincent Danen <vdanen@linux-mandrake.com>
- initial specfile
- bzip sources
- removed make install and replaced with custom installer to ensure correct
  paths in the latex2html perl programs
