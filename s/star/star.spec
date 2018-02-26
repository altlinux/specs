Name: star
Version: 1.5.1
Release: alt2

Summary: A very fast, POSIX compliant tape archiver
License: CDDL
Group: Archiving/Backup

URL: http://cdrecord.berlios.de/old/private/star.html
Source: ftp://ftp.berlios.de/pub/star/star-%version.tar.bz2
Patch0: star-1.5-stdioconflict.patch

# Fedora patches:
# Prevent buffer overflow for filenames with length of 100 characters (RH#556664)
Patch1: star-1.5.1-bufferoverflow.patch
# Fix signedness segfault with multivol option (RH#666015)
Patch2: star-1.5.1-multivolsigsegv.patch

# Automatically added by buildreq on Wed Jun 16 2010 (-bi)
BuildRequires: chrpath libacl-devel libattr-devel libe2fs-devel

%package rmt
Summary: Schily SING version of the rmt
Group: Archiving/Backup
Conflicts: rmt

%description
Star saves many files together into a single tape or disk archive,
and can restore individual files from the archive. It includes a FIFO
for speed, a pattern matcher, multivolume support, the ability to archive
sparse files, automatic archive format detection, automatic byte order
recognition, automatic archive compression/decompression, remote archives
and special features that allow star to be used for full backups.
It also includes rmt, a truly portable version of the remote tape server
that supports remote operation between different OS and machine architectures
(hides even Linux oddities) and a portable mt tape drive control program
that is able to use the remote tape interface.

%description rmt
This is enhanced Schily SING version of the rmt remote tape server program.
rmt is a program used by programs like star and ufsdump hat like to access 
remote magnetic tape drives and files through an interprocess communication 
connection.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

# kill annoying beep'n'sleep
subst 's/^__gmake_warn.*//' RULES/mk-gmake.id

%build
subst 's/\/etc\/default/\/etc\/rmt/' rmt/rmt.c rmt/rmt.dfl

#./Gmake.linux PARCH=%_arch
%make_build CC=gcc LDCC=gcc DYNLD=gcc COPTOPT="%optflags" PARCH=%_arch

%install
make install INS_BASE=%buildroot%_prefix MANDIR=/share/man

install -m600 -pD rmt/rmt.dfl %buildroot%_sysconfdir/rmt/rmt
echo '.so star.1' > %buildroot%_man1dir/ustar.1

rm -rf %buildroot{%_man3dir,%_man5dir/m*,%_man1dir/match*}

# avoid conflicts with tar and mt-st packages:
rm -f %buildroot%_bindir/{mt,tar}

# remove devel files (thus avoid conflict with cdrtools-devel!)
rm -rf %buildroot%_includedir
rm -f %buildroot%_libdir/*.a
rm -rf %buildroot%_libdir/profiled

# rpath is evil
chrpath -d %buildroot%_bindir/* %buildroot%_sbindir/*

%files
%_bindir/*tar*
%_bindir/smt
%_bindir/scpio
%_bindir/spax
%exclude %_bindir/gnutar
%_man1dir/*tar*
%_man1dir/scpio*
%_man1dir/smt*
%_man1dir/spax*
%exclude %_man1dir/gnutar*
%_man5dir/*
%doc README star/README.crash star/README.largefiles star/README.mtio
%doc star/README.otherbugs star/README.pattern star/README.pax
%doc star/README.posix-2001 star/STARvsGNUTAR
%exclude %_datadir/doc/star
%exclude %_datadir/doc/rmt

%files rmt
%dir %_sysconfdir/rmt/
%config(noreplace) %_sysconfdir/rmt/rmt
%_sbindir/rmt
%_man1dir/rmt.1.*

%changelog
* Wed Feb 09 2011 Victor Forsiuk <force@altlinux.org> 1.5.1-alt2
- Apply patches from Fedora (including fix for crashing buffer overflow).
  Thnx ender@ for suggestion!

* Wed Jun 16 2010 Victor Forsiuk <force@altlinux.org> 1.5.1-alt1
- 1.5.1

* Tue Jun 09 2009 Victor Forsyuk <force@altlinux.org> 1.5-alt2
- Fix build failure due to symbols conflicting with stdio.

* Fri Apr 18 2008 Victor Forsyuk <force@altlinux.org> 1.5-alt1
- 1.5 release! :)

* Thu Mar 20 2008 Victor Forsyuk <force@altlinux.org> 1.5-alt0.1a89
- 1.5.a89

* Tue Oct 30 2007 Victor Forsyuk <force@altlinux.org> 1.5-alt0.1a87
- 1.5.a87

* Wed Oct 17 2007 Victor Forsyuk <force@altlinux.org> 1.5-alt0.1a86
- 1.5.a86

* Thu Aug 23 2007 Victor Forsyuk <force@altlinux.org> 1.5-alt0.1a84
- 1.5.a84 (contains security-related fixes!)

* Mon Jul 23 2007 Victor Forsyuk <force@altlinux.org> 1.5-alt0.1a83
- 1.5a83

* Wed Jun 06 2007 Victor Forsyuk <force@altlinux.org> 1.5-alt0.1a80
- 1.5a80

* Wed May 02 2007 Victor Forsyuk <force@altlinux.org> 1.5-alt0.1a79
- 1.5a79

* Mon Apr 16 2007 Victor Forsyuk <force@altlinux.org> 1.5-alt0.1a78
- 1.5a78

* Thu Mar 22 2007 Victor Forsyuk <force@altlinux.org> 1.5-alt0.1a77
- 1.5a77

* Fri Oct 20 2006 Victor Forsyuk <force@altlinux.org> 1.5-alt0.1a75
- 1.5a75

* Wed Jun 07 2006 Victor Forsyuk <force@altlinux.ru> 1.5-alt0.1a74
- 1.5a74

* Mon Apr 10 2006 Victor Forsyuk <force@altlinux.ru> 1.5-alt0.1a73
- 1.5a73
- Refresh build requirements.

* Mon Nov 21 2005 Victor Forsyuk <force@altlinux.ru> 1.5-alt0.1a70
- 1.5a70
- Exclude gnutar from package.

* Fri Aug 26 2005 Victor Forsyuk <force@altlinux.ru> 1.5-alt0.1a65
- 1.5a65

* Wed Jun 22 2005 Victor Forsyuk <force@altlinux.ru> 1.5-alt0.1a60
- Fix URL.
- Apply %%optflags and build with parallel make.
- License changed from GPL to CDDL.
- Fix buildreqs, many other spec cleanups and fixes.

* Sat Nov 16 2002 Igor Homyakov <homyakov at altlinux dot ru> 1.5-alt0.1a09
- 1.5a09
- russian translation for star-rmt
- 'mt' command is 'smt' now (renamed by author)
- 'smt' moved to star package
- spec cleanup

* Tue Sep 17 2002 Igor Homyakov <homyakov at altlinux dot ru> 1.5-alt0.1a08
- 1.5a08
- build Shily's (r)mt utilies (star-rmt package)
 
* Wed Jul 17 2002 Igor Homyakov <homyakov at altlinux dot ru> 1.5-alt0.1a05
- 1.5a05

* Mon Jun 24 2002 Igor Homyakov <homyakov at altlinux dot ru> 1.5-alt0.1a04
- 1.5a04

* Fri May 24 2002 Igor Homyakov <homyakov@altlinux.ru> 1.4-alt1
- 1.4 (stable) 

* Wed May 15 2002 Igor Homyakov <homyakov@altlinux.ru> 1.4-alt0.1a26
- 1.4a26

* Mon Apr 15 2002 Igor Homyakov <homyakov@altlinux.ru> 1.4-alt0.1a21
- build 1.4a21  
- spec cleanup  

* Tue Mar 05 2002 Igor Homyakov <homyakov@altlinux.ru> 1.4-alt0.1a18
- Build package for ALTLinux
- russian translation for spec file
