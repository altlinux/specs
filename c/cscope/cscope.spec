# vim: set ft=spec: -*- mode: rpm-spec; -*-

Name: cscope
Version: 15.7a
Release: alt1.qa1

Summary: Cscope is a text screen based source browsing tool
Group: Development/Other
License: BSD
Url: http://cscope.sourceforge.net/

Packager: Sir Raorn <raorn@altlinux.ru>

# git://git.altlinux.org/people/raorn/packages/%name.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Sun Oct 15 2006
BuildRequires: flex libncurses-devel

%description
Cscope is a text screen based source browsing tool.  Although it is
primarily designed to search C code (including lex and yacc files), it
can also be used for C++ code.

Using cscope, you can easily search for where symbols are used and
defined.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build clean
%make_build all

%install
%make_install DESTDIR=%buildroot install

# The package contains a CVS/.svn/.git/.hg/.bzr/_MTN directory of revision control system.
# It was most likely included by accident since CVS/.svn/.hg/... etc. directories 
# usually don't belong in releases. 
# When packaging a CVS/SVN snapshot, export from CVS/SVN rather than use a checkout.
find $RPM_BUILD_ROOT -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \; ||:
# the find below is useful in case those CVS/.svn/.git/.hg/.bzr/_MTN directory is added as %%doc
find . -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \; ||:

%files
%doc TODO COPYING AUTHORS README contrib
%_bindir/*
%_man1dir/*

%changelog
* Wed May 18 2011 Repocop Q. A. Robot <repocop@altlinux.org> 15.7a-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * pkg-contains-cvs-or-svn-control-dir for cscope
  * postclean-03-private-rpm-macros for ([not specified])
  * postclean-05-filetriggers for ([not specified])

* Thu May 07 2009 Alexey I. Froloff <raorn@altlinux.org> 15.7a-alt1
- [15.7a] (closes: #19952)
 + CVE-2009-0148

* Tue Feb 17 2009 Sir Raorn <raorn@altlinux.ru> 15.7-alt1
- [15.7]

* Mon Oct 16 2006 Sir Raorn <raorn@altlinux.ru> 15.6-alt2
- Fix tempdir handling.

* Sun Oct 15 2006 Sir Raorn <raorn@altlinux.ru> 15.6-alt1
- [15.6]
- Repacked source, all patched applied in GIT repository
- Updated buildrequires
- Added packager tag
- Added URL tag (closes: #9277)

* Wed Dec 01 2004 Sir Raorn <raorn@altlinux.ru> 15.5-alt2
- CAN-2004-0996

* Sat Sep 06 2003 Sir Raorn <raorn@altlinux.ru> 15.5-alt1
- [15.5]

* Mon Jan 27 2003 Sir Raorn <raorn@altlinux.ru> 15.4-alt1
- [15.4]

* Mon Dec 03 2001 Sir Raorn <raorn@altlinux.ru> 15.3-alt1
- Built for Sisyphus

