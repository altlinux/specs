Name: cvsps
Version: 2.2
Release: alt0.1

Summary: A patchset tool for CVS
License: GPL
Group: Development/Other
Url: http://www.cobite.com/cvsps/

# git://git.altlinux.org/gears/c/cvsps.git
Source: %name-%version-%release.tar

Requires: cvs
BuildRequires: zlib-devel

%description
CVSps is a program for generating 'patchset' information from a CVS
repository.  A patchset in this case is defined as a set of changes
made to a collection of files, and all committed at the same time
(using a single 'cvs commit' command).  This information is valuable
to seeing the big picture of the evolution of a cvs project.  While
cvs tracks revision information, it is often difficult to see what
changes were committed 'atomically' to the repository.

%prep
%setup -n %name-%version-%release

%build
%make_build CFLAGS='%optflags'

%install
install -pD -m755 cvsps %buildroot%_bindir/cvsps
install -pD -m644 cvsps.1 %buildroot%_man1dir/cvsps.1

%files
%_bindir/*
%_man1dir/*
%doc CHANGELOG README merge_utils.sh

%changelog
* Thu Apr 18 2013 Dmitry V. Levin <ldv@altlinux.org> 2.2-alt0.1
- Merged branch 'master' of git://repo.or.cz/cvsps-yd.
- Merged Fedora fixes.

* Sat Apr 07 2007 Dmitry V. Levin <ldv@altlinux.org> 2.1-alt2
- Merged branch 'master' of http://ydirson.free.fr/soft/git/cvsps.
- Fixed compilation warnings.

* Fri Nov 25 2005 Dmitry V. Levin <ldv@altlinux.org> 2.1-alt1
- Initial revision.
