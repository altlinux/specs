Name: nasm
Version: 2.10
Release: alt1

Summary: The Netwide Assembler, a portable x86 assembler with Intel-like syntax
License: BSD 2-clause
Group: Development/Other

URL: http://www.nasm.us/
# http://nasm.sourceforge.net/
Source: http://www.nasm.us/pub/nasm/releasebuilds/%version/nasm-%version.tar.bz2
#Source: http://dl.sourceforge.net/nasm/nasm-%version.tar.bz2

# Automatically added by buildreq on Sun Nov 27 2011
BuildRequires: ghostscript-utils groff-base

%package doc
Summary: Extensive documentation for NASM
Group: Development/Other
BuildArch: noarch

%package rdoff
Summary: Tools for the RDOFF binary format, sometimes used with NASM
Group: Development/Other

%description
NASM is the Netwide Assembler, a free portable assembler for the Intel
80x86 microprocessor series, using primarily the traditional Intel
instruction mnemonics and syntax.

%description doc
Extensive documentation for the Netwide Assembler, NASM, in HTML,
PostScript and text formats.

%description rdoff
Tools for the operating-system independent RDOFF binary format, which
is sometimes used with the Netwide Assembler (NASM). These tools
include linker, library manager, loader, and information dump.

%prep
%setup

%build
%configure
%make_build everything

%install
make INSTALLROOT="%buildroot" INSTALL="install -pD" install install_rdf

cd doc
install -d %buildroot%_infodir
install info/* %buildroot%_infodir/
gzip -9f *.txt *.ps || true
cd html
ln -sf nasmdoc0.html index.html

%files
%doc CHANGES TODO AUTHORS README doc/internal.doc
%_bindir/nasm
%_bindir/ndisasm
%_man1dir/nasm.1*
%_man1dir/ndisasm.1*
%_infodir/nasm.info*

%files doc
%doc doc/nasmdoc.ps.gz doc/nasmdoc.txt.gz doc/html

%files rdoff
%doc rdoff/README
%_bindir/ldrdf
%_bindir/rdf2bin
%_bindir/rdf2com
%_bindir/rdfdump
%_bindir/rdf2ihx
%_bindir/rdf2ith
%_bindir/rdflib
%_bindir/rdf2srec
%_bindir/rdx
%_man1dir/*rdf*
%_man1dir/rdx*

%changelog
* Fri Mar 16 2012 Victor Forsiuk <force@altlinux.org> 2.10-alt1
- 2.10

* Sun Nov 27 2011 Victor Forsiuk <force@altlinux.org> 2.09.10-alt1
- 2.09.10

* Wed Jul 22 2009 Victor Forsyuk <force@altlinux.org> 2.07-alt1
- 2.07
- NB: nasm is now licensed under the 2-clause (simplified) BSD license.

* Tue Jun 30 2009 Victor Forsyuk <force@altlinux.org> 2.06-alt1
- 2.06

* Thu Nov 06 2008 Victor Forsyuk <force@altlinux.org> 2.05.01-alt1
- 2.05.01

* Fri Oct 24 2008 Victor Forsyuk <force@altlinux.org> 2.05-alt1
- 2.05

* Fri Oct 03 2008 Victor Forsyuk <force@altlinux.org> 2.04-alt1
- 2.04

* Fri Aug 01 2008 Victor Forsyuk <force@altlinux.org> 2.03.01-alt1
- 2.03.01

* Tue Jun 10 2008 Victor Forsyuk <force@altlinux.org> 2.03-alt1
- 2.03

* Mon Mar 31 2008 Victor Forsyuk <force@altlinux.org> 2.02-alt1
- 2.02

* Mon Jan 21 2008 Victor Forsyuk <force@altlinux.org> 2.01-alt1
- 2.01

* Fri Nov 30 2007 Victor Forsyuk <force@altlinux.org> 2.00-alt1
- 2.00

* Mon Nov 05 2007 Victor Forsyuk <force@altlinux.org> 0.99.06-alt1
- 0.99.06

* Fri Sep 28 2007 Victor Forsyuk <force@altlinux.org> 0.99.04-alt1
- 0.99.04 (this version fixes segfault in building libglide3-20050815).

* Mon Sep 24 2007 Victor Forsyuk <force@altlinux.org> 0.99.03-alt1
- 0.99.03

* Thu May 26 2005 Victor Forsyuk <force@altlinux.ru> 0.98.39-alt1
- 0.98.39
- Fix yet another vsprintf buffer overflow (RH#152963).

* Mon Jan 24 2005 Stanislav Ievlev <inger@altlinux.org> 0.98.35-alt2
- CAN-2004-1287

* Tue Sep 30 2003 Stanislav Ievlev <inger@altlinux.ru> 0.98.35-alt1.1
- removed patch "boguself2" (this is RH's patch and RH remove it)
- fix building in hasher

* Mon Oct 28 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.98.35-alt1
- 0.98.35
- Rebuilt in new environment
- Added buildrequires

* Fri May 24 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.98.32-alt1
- 0.98.32

* Thu Jan 24 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.98.22-alt1
- 0.98.22
- Added bouself patch

* Thu Jan 03 2002 Stanislav Ievlev <inger@altlinux.ru> 0.98.08-alt2
- fixed bug  #0000305

* Wed Dec 05 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.98.08-alt1
- 0.98.08
- Some spec cleanup

* Tue Jan  2 2001 Kostya Timoshenko <kt@petr.kz>
- Build for RE
