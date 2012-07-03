Name: pbzip2
Version: 1.1.6
Release: alt1

Summary: Parallel implementation of bzip2
License: BSD-like
Group: Archiving/Compression

URL: http://compression.ca/pbzip2
Source0: %url/pbzip2-%version.tar.gz

# Automatically added by buildreq on Mon Apr 04 2011
BuildRequires: bzlib-devel gcc-c++

%description
PBZIP2 is a parallel implementation of the bzip2 block-sorting file compressor
that uses pthreads and achieves near-linear speedup on SMP machines. The output
of this version is fully compatible with bzip2 v1.0.2 (ie: anything compressed
with pbzip2 can be decompressed with bzip2).

%prep
%setup

%build
subst 's/-O./%optflags/g' Makefile
%make_build

%install
install -pD -m755 pbzip2 %buildroot%_bindir/pbzip2
install -pD -m644 pbzip2.1 %buildroot%_man1dir/pbzip2.1

%files
%doc README COPYING
%_bindir/pbzip2
%_man1dir/pbzip2.*

%changelog
* Sat Nov 12 2011 Victor Forsiuk <force@altlinux.org> 1.1.6-alt1
- 1.1.6

* Mon Jul 18 2011 Victor Forsiuk <force@altlinux.org> 1.1.5-alt1
- 1.1.5

* Wed May 04 2011 Victor Forsiuk <force@altlinux.org> 1.1.4-alt1
- 1.1.4

* Mon Apr 04 2011 Victor Forsiuk <force@altlinux.org> 1.1.3-alt1
- 1.1.3

* Wed Feb 23 2011 Victor Forsiuk <force@altlinux.org> 1.1.2-alt1
- 1.1.2

* Wed Jun 09 2010 Victor Forsiuk <force@altlinux.org> 1.1.1-alt1
- 1.1.1

* Tue Mar 16 2010 Victor Forsiuk <force@altlinux.org> 1.1.0-alt1
- 1.1.0

* Wed Jan 14 2009 Victor Forsyuk <force@altlinux.org> 1.0.5-alt1
- 1.0.5

* Wed Dec 24 2008 Victor Forsyuk <force@altlinux.org> 1.0.4-alt1
- 1.0.4

* Wed Nov 26 2008 Victor Forsyuk <force@altlinux.org> 1.0.3-alt1
- 1.0.3

* Fri Jul 27 2007 Victor Forsyuk <force@altlinux.org> 1.0.2-alt1
- 1.0.2

* Fri Jun 08 2007 Victor Forsyuk <force@altlinux.org> 1.0.1-alt1
- 1.0.1

* Thu Mar 09 2006 Igor Zubkov <icesik@altlinux.ru> 0.9.6-alt1
- 0.9.6
- add man

* Thu Sep 08 2005 Igor Zubkov <icesik@altlinux.ru> 0.9.2-alt1
- Initial build for Sisyphus
