Name: sleuthkit
Version: 4.5.0
Release: alt1

Summary: The Sleuth Kit

License: GPL
Group: File tools
Url: http://www.sleuthkit.org/sleuthkit/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/sleuthkit/sleuthkit/releases/download/sleuthkit-%version/sleuthkit-%version.tar.gz
Source: %name-%version.tar
Source1: mac-robber-1.02.tar.bz2
Patch: sleuthkit-unbundle.diff

# Automatically added by buildreq on Sun Aug 04 2013
# optimized out: bouncycastle bouncycastle-mail cppunit ecj gcc-java gnu-config libgcj4.7-jar libstdc++-devel python3-base zlib-devel
BuildRequires: cppunit-devel gcc-c++ glibc-devel libaff-devel libewf-devel zlib-devel sharutils

%description
The Sleuth Kit (previously known as TASK) is a collection of UNIX-based command
line file system forensic tools that allow an investigator to examine NTFS,
FAT, FFS, EXT2FS, and EXT3FS file systems of a suspect computer in a
non-intrusive fashion. The  tools have a layer-based design and can extract
data from internal file system structures. Because the tools do not rely on the
operating system to process the file systems, deleted and hidden content is
shown.

When performing a complete analysis of a system, command line tools can become
tedious. The Autopsy Forensic Browser is a graphical interface to the tools in
The Sleuth Kit, which allows one to more easily conduct an investigation.
Autopsy provides case management, image integrity, keyword searching, and other
automated operations.

%package -n libtsk
Summary: libraries for developing applications which will use libtsk
Group: Development/C

%description -n libtsk
Libraries for developing applications which will use libtsk.

%package -n libtsk-devel
Summary: Header files and libraries for developing applications which will use libtsk
Group: Development/C
Requires: libtsk = %version-%release

%description -n libtsk-devel
Header files and libraries for developing applications which will use libewf.

%prep
%setup -q -n %name-%version -a1
find -name Makefile.am | xargs subst "s| -static||g"

%build
%autoreconf
%configure --disable-static
%make_build

gcc %optflags -o mac-robber mac-robber-1.02/mac-robber.c

mv mac-robber-1.02/README README.mac-robber
mv mac-robber-1.02/CHANGES CHANGES.mac-robber
chmod 644 README.mac-robber

%install
%makeinstall_std

install -d %buildroot%_datadir/sorter
install -d %buildroot%_man1dir

install -m755 mac-robber %buildroot%_bindir/
#install -m644 man/man1/* %buildroot%_man1dir/
#install -m644 share/sorter/* %buildroot%_datadir/sorter/

%files
%doc ChangeLog.txt INSTALL.txt README.mac-robber README.md licenses/*
%doc CHANGES.mac-robber
%_bindir/blkcalc
%_bindir/blkcat
#_bindir/disk_sreset
#_bindir/disk_stat
%_bindir/fcat
%_bindir/fiwalk
%_bindir/jpeg_extract
%_bindir/blkls
%_bindir/blkstat
%_bindir/ffind
%_bindir/fls
%_bindir/fsstat
%_bindir/hfind
%_bindir/icat
%_bindir/ifind
%_bindir/ils
%_bindir/img_cat
%_bindir/img_stat
%_bindir/istat
%_bindir/jcat
%_bindir/jls
%_bindir/mac-robber
%_bindir/mactime
#%_bindir/md5
%_bindir/mmls
%_bindir/mmstat
%_bindir/mmcat
#%_bindir/sha1
%_bindir/sigfind
%_bindir/sorter
%_bindir/srch_strings
%_bindir/tsk_*
%_bindir/usnjls
%_man1dir/blkcalc.1*
%_man1dir/blkcat.1*
#_man1dir/disk_sreset.1*
#_man1dir/disk_stat.1*
%_man1dir/blkls.1*
%_man1dir/blkstat.1*
%_man1dir/ffind.1*
%_man1dir/fls.1*
%_man1dir/fcat.1*
%_man1dir/fsstat.1*
%_man1dir/hfind.1*
%_man1dir/icat.1*
%_man1dir/ifind.1*
%_man1dir/ils.1*
%_man1dir/img_cat.1*
%_man1dir/img_stat.1*
%_man1dir/istat.1*
%_man1dir/jcat.1*
%_man1dir/jls.1*
%_man1dir/mactime.1*
%_man1dir/mmls.1*
%_man1dir/mmcat.1*
%_man1dir/mmstat.1*
%_man1dir/sigfind.1*
%_man1dir/sorter.1*
%_man1dir/tsk_*
%_man1dir/usnjls.1*
%_datadir/tsk/

%files -n libtsk
%_libdir/*.so.*

%files -n libtsk-devel
%_libdir/*.so
%_includedir/tsk/

%changelog
* Sun Feb 25 2018 Vitaly Lipatov <lav@altlinux.ru> 4.5.0-alt1
- new version 4.5.0 (with rpmrb script)

* Thu Dec 07 2017 Vitaly Lipatov <lav@altlinux.ru> 4.4.2-alt2
- drop BR:bouncycastle-tsp

* Tue Nov 07 2017 Vitaly Lipatov <lav@altlinux.ru> 4.4.2-alt1
- new version 4.4.2 (with rpmrb script)

* Sun Jan 29 2017 Vitaly Lipatov <lav@altlinux.ru> 4.4.0-alt1
- new version 4.4.0 (with rpmrb script)

* Sun Dec 25 2016 Vitaly Lipatov <lav@altlinux.ru> 4.3.0-alt1
- new version (4.3.0) with rpmgs script

* Sun Jan 03 2016 Vitaly Lipatov <lav@altlinux.ru> 4.2.0-alt1
- new version 4.2.0 (with rpmrb script)

* Wed Apr 02 2014 Vitaly Lipatov <lav@altlinux.ru> 4.1.3-alt1
- new version 4.1.3 (with rpmrb script)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 4.1.0-alt1
- new version 4.1.0 (with rpmrb script)

* Wed Nov 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Version 4.0.0

* Thu Aug 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.3-alt1
- Version 3.2.3

* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 3.0.0-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libtsk
  * postun_ldconfig for libtsk
  * postclean-05-filetriggers for spec file

* Fri Nov 07 2008 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt2
- fix rpath problem on i586

* Fri Nov 07 2008 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- initial build for ALT Linux Sisyphus

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.09-4mdv2009.0
+ Revision: 260795
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.09-3mdv2009.0
+ Revision: 252599
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.09-1mdv2008.1
+ Revision: 136503
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 07 2007 Oden Eriksson <oeriksson@mandriva.com> 2.09-1mdv2008.0
+ Revision: 81984
- 2.09
- unbundle file, afflib and libewf

* Fri Aug 31 2007 Oden Eriksson <oeriksson@mandriva.com> 2.05-2mdv2008.0
+ Revision: 76894
- rebuild

* Sat Jul 29 2006 Oden Eriksson <oeriksson@mandriva.com> 2.05-1mdv2007.0
- 2.05
- fix deps

* Wed Oct 19 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.03-1mdk
- New release 2.03
- %%mkrel

* Sun Dec 26 2004 Stefan van der Eijk <stefan@mandrake.org> 1.73-1mdk
- 1.73
- rediffed p0

* Thu Nov 25 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.72-2mdk
- fix #12488

* Sun Oct 31 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.72-1mdk
- 1.72
- fix P0

* Wed Sep 01 2004 Stefan van der Eijk <stefan@mandrake.org> 1.71-1mdk
- 1.71

* Thu May 06 2004 Michael Scherer <misc@mandrake.org> 1.69-1mdk
- New release 1.69
- rpmbuildupdate aware
- update patch
- [DIRM]

