Summary:	Binary diff/patch utility
Name:		bsdiff
Version:	4.3
Release:	alt3
Group:		File tools
License:	BSD-2-Clause
Packager:	Fr. Br. George <george@altlinux.org>
URL:		https://www.daemonology.net/bsdiff/
Source:		%name-%version.tar
BuildRequires:	gcc bzlib-devel

# debian patches
Patch1: 20-CVE-2014-9862.patch
Patch2: 30-bug-632585-mmap-src-file-instead-of-malloc-read-it.patch
Patch3: 31-bug-632585-mmap-dst-file-instead-of-malloc-read-it.patch
Patch4: 32-bug-632585-use-int32_t-instead-off_t-for-file-size.patch
Patch5: 33-CVE-2020-14315.patch

%description
bsdiff and bspatch are tools for building and applying patches to
binary files. By using suffix sorting (specifically, Larsson and
Sadakane's qsufsort) and taking advantage of how executable files
change, bsdiff routinely produces binary patches 50-80%% smaller
than those produced by Xdelta, and 15%% smaller than those produced
by .RTPatch.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%__cc %optflags bsdiff.c -lbz2 -o bsdiff
%__cc %optflags bspatch.c -lbz2 -o bspatch

%install
install -D -s bsdiff %buildroot%_bindir/bsdiff
install -D -s bspatch %buildroot%_bindir/bspatch

install -D bsdiff.1 %buildroot%_mandir/man1/bsdiff.1
install -D bspatch.1 %buildroot%_mandir/man1/bspatch.1

%files
%_bindir/bsdiff
%_bindir/bspatch
%_mandir/man1/bsdiff.1*
%_mandir/man1/bspatch.1*

%changelog
* Thu Jul 09 2026 Alexander Danilov <admsasha@altlinux.org> 4.3-alt3
- Added patches from debian (Fixes: CVE-2014-9862, CVE-2020-14315).

* Mon Mar 02 2020 Dmitry V. Levin <ldv@altlinux.org> 4.3-alt2
- Rebuilt.

* Sun Aug 06 2006 Fr. Br. George <george@altlinux.ru> 4.3-alt1
- Initial ALT build

* Sat Mar 18 2006 Anssi Hannula <anssi@mandriva.org> 4.3-1mdk
- initial Mandriva release
