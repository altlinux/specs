%def_without static

Name: ddrescue
Version: 1.15
Release: alt1

Summary: Data copying in presence of I/O errors
License: GPLv3+
Group: Archiving/Backup

URL: http://www.gnu.org/software/ddrescue/ddrescue.html
Source: http://ftp.gnu.org/gnu/ddrescue/ddrescue-%version.tar.gz
Patch1: http://cvs.pld-linux.org/cgi-bin/cvsweb/SOURCES/ddrescue-patch.txt
# This patch was originally from:
# http://guru.multimedia.cx/wp-content/uploads/2006/08/ddrescue-patch.txt
# Patch not maintained and about to drop next time.

# Automatically added by buildreq on Wed Dec 31 2008
BuildRequires: gcc-c++
%{?_with_static: BuildRequires: libstdc++-devel-static}

%description
ddrescue copies data from one file or block device (hard disk, cdrom, etc)
to another, trying hard to rescue data in case of read errors.

ddrescue does not truncate the output file if not asked to. So, everytime
you run it on the same output file, it tries to fill in the gaps.

If you have two or more copies of a damaged file, cdrom, etc, and run
ddrescue on all of them, one at a time, with the same output file, you
will probably obtain a complete and error-free file.

%package static
Summary: Statically built ddrescue (data recovery tool)
Group: Archiving/Backup

%description static
ddrescue copies data from one file or block device (hard disk, cdrom, etc)
to another, trying hard to rescue data in case of read errors.

This package contains statically built ddrescue utility.

%prep
%setup
#%patch1 -p1

%build
./configure --prefix=%_prefix --infodir=%_infodir --mandir=%_mandir
%make_build CXXFLAGS="%optflags %optflags_nocpp" all %{?_with_static:sddrescue}
make check

%install
%make_install install install-man DESTDIR=%buildroot
%{?_with_static: install -pD -m755 sddrescue %buildroot/bin/sddrescue}

%files
%_bindir/ddrescue
%_bindir/ddrescuelog
%_man1dir/*
%_infodir/*.info*
%doc README

%if_with static
%files static
/bin/sddrescue
%endif

%changelog
* Tue Jan 03 2012 Victor Forsiuk <force@altlinux.org> 1.15-alt1
- 1.15

* Wed Jan 12 2011 Victor Forsiuk <force@altlinux.org> 1.14-alt1
- 1.14

* Mon Aug 30 2010 Victor Forsiuk <force@altlinux.org> 1.13-alt1
- 1.13

* Thu Apr 08 2010 Victor Forsiuk <force@altlinux.org> 1.12-alt1
- 1.12

* Sun Jul 12 2009 Victor Forsyuk <force@altlinux.org> 1.11-alt1
- 1.11

* Wed Dec 31 2008 Victor Forsyuk <force@altlinux.org> 1.9-alt1
- 1.9

* Tue Jun 10 2008 Victor Forsyuk <force@altlinux.org> 1.8-alt2
- Fix info files installation.

* Tue Feb 26 2008 Victor Forsyuk <force@altlinux.org> 1.8-alt1
- 1.8 (visualization patch disabled for now).

* Mon Jul 23 2007 Victor Forsyuk <force@altlinux.org> 1.5-alt1
- 1.5
- Fetch from PLD CVS modified for 1.5 "visualization" patch.
- Install static ddrescue to /bin.

* Mon Jan 15 2007 Victor Forsyuk <force@altlinux.org> 1.3-alt1
- 1.3
- Built and packaged statically linked ddrescue.
- Ascii art patch from http://guru.multimedia.cx/ddrescue/
  (visualization of the recovery process).

* Tue Apr 25 2006 Victor Forsyuk <force@altlinux.ru> 1.2-alt1
- 1.2

* Fri Oct 14 2005 Victor Forsyuk <force@altlinux.ru> 1.1-alt1
- 1.1

* Fri Jun 10 2005 Victor Forsyuk <force@altlinux.ru> 1.0-alt1
- Initial build.
