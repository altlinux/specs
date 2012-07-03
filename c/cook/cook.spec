%set_perl_req_method relaxed

Summary: a file construction tool
Name: cook
Version: 2.32
Release: alt1
License: %gpl3plus
Group: Development/Other
Source: http://miller.emu.id.au/pmiller/software/cook/%name-%version.tar.bz2
URL: http://miller.emu.id.au/pmiller/software/cook/
Icon: %name.gif

Packager:	Alexey Voinov <voins@altlinux.ru>

Patch2: %name-2.21-alt-dep.patch

BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Thu Jun 07 2007
BuildRequires: groff-dvi groff-ps librx-devel


%description
Cook is a tool for constructing files. It is given a set of files to
create, and recipes of how to create them. In any non-trivial program
there will be prerequisites to performing the actions necessary to
creating any file, such as include files.  The cook program provides a
mechanism to define these.

When a program is being developed or maintained, the programmer will
typically change one file of several which comprise the program.  Cook
examines the last-modified times of the files to see when the
prerequisites of a file have changed, implying that the file needs to be
recreated as it is logically out of date.

Cook also provides a facility for implicit recipes, allowing users to
specify how to form a file with a given suffix from a file with a
different suffix.  For example, to create filename.o from filename.c

* Cook is a replacement for the traditional make(1) tool.  However, it
  is necessary to convert makefiles into cookbooks using the make2cook
  utility included in the distribution.

* Cook has a simple but powerful string-based description language with
  many built-in functions.  This allows sophisticated filename
  specification and manipulation without loss of readability or
  performance.

* Cook is able to use fingerprints to supplement file modification
  times.  This allows build optimization without contorted rules.

* Cook is able to build your project with multiple parallel threads,
  with support for rules which must be single threaded.  It is possible
  to distribute parallel builds over your LAN, allowing you to turn your
  network into a virtual parallel build engine.

If you are putting together a source-code distribution and planning to
write a makefile, consider writing a cookbook instead.  Although Cook
takes a day or two to learn, it is much more powerful and a bit more
intuitave than the traditional make(1) tool.  And Cook doesn't interpret
tab differently to 8 space characters!

%package psdocs
Summary: Cook documentation, PostScript format
Group: Development/Other
BuildArch: noarch

%description psdocs
Cook documentation in PostScript format.

%package dvidocs
Summary: Cook documentation, DVI format
Group: Development/Other
BuildArch: noarch

%description dvidocs
Cook documentation in DVI format.

%prep
%setup -q
%patch2 -p1 -b .dep

%build
%configure --with-nlsdir=%_datadir/locale
make

%install
make RPM_BUILD_ROOT=$RPM_BUILD_ROOT install
mv $RPM_BUILD_ROOT%_libdir/%name/* $RPM_BUILD_ROOT%_datadir/locale
%find_lang %name

%files -f %name.lang
%dir %_datadir/%name
%dir %_datadir/%name/en
%_bindir/*
%_man1dir/*
%_datadir/%name/as
%_datadir/%name/bison
%_datadir/%name/c
%_datadir/%name/c++
%_datadir/%name/f77
%_datadir/%name/functions
%_datadir/%name/g77
%_datadir/%name/gcc
%_datadir/%name/home
%_datadir/%name/host_lists.pl
%_datadir/%name/java
%_datadir/%name/lex
%_datadir/%name/library
%_datadir/%name/print
%_datadir/%name/program
%_datadir/%name/rcs
%_datadir/%name/recursive
%_datadir/%name/sccs
%_datadir/%name/text
%_datadir/%name/usr
%_datadir/%name/usr.local
%_datadir/%name/yacc
%_datadir/%name/yacc_many
%_datadir/%name/en/*.txt

%files psdocs
%_datadir/%name/en/*.ps

%files dvidocs
%_datadir/%name/en/*.dvi


%changelog
* Fri Aug 15 2008 Alexey Voinov <voins@altlinux.ru> 2.32-alt1
- new version (2.32)
- noarch documentation subpackages

* Tue May 06 2008 Alexey Voinov <voins@altlinux.ru> 2.31-alt2
- directory ownership fixed

* Sun Mar 09 2008 Alexey Voinov <voins@altlinux.ru> 2.31-alt1
- new version (2.31)

* Tue Aug 21 2007 Alexey Voinov <voins@altlinux.ru> 2.30-alt1
- new version (2.30)
- license updated

* Mon Jul 30 2007 Alexey Voinov <voins@altlinux.ru> 2.29-alt1
- new version (2.29)
- url updated

* Thu Jun 07 2007 Alexey Voinov <voins@altlinux.ru> 2.28-alt1
- new version (2.28)
- buildreqs updated

* Tue Jan 17 2006 Alexey Voinov <voins@altlinux.ru> 2.26-alt1
- new version (2.26)
- removed fixincl patch [merged in upstream]
- removed option patch [merged in upstream]

* Thu Sep 29 2005 Alexey Voinov <voins@altlinux.ru> 2.25-alt3
- no more owned dirs in /usr/share/locale

* Sun Mar 13 2005 Alexey Voinov <voins@altlinux.ru> 2.25-alt2
- libintl removed from buildreqs

* Fri Sep 17 2004 Alexey Voinov <voins@altlinux.ru> 2.25-alt1
- new version (2.25)
- fixincl & option patches updated
- nlsdir patch removed

* Tue Nov 04 2003 Alexey Voinov <voins@altlinux.ru> 2.24-alt1
- new version (2.24)
- fixincl patch added
- option patch added

* Sat May 24 2003 Alexey Voinov <voins@voins.program.ru> 2.23-alt1
- new version (2.23)
- c++ cook inlude file added

* Fri Jan 24 2003 Alexey Voinov <voins@voins.program.ru> 2.21-alt4
- wrong deps on perl(host_lists.pl) removed

* Wed Jan 22 2003 Alexey Voinov <voins@voins.program.ru> 2.21-alt3
- made buildable

* Tue Oct 22 2002 Alexey Voinov <voins@altlinux.ru> 2.21-alt2
- Group fixed

* Mon Sep 02 2002 Alexey Voinov <voins@voins.program.ru> 2.21-alt1
- new version (2.21)
- spec cleanup

* Tue Jul 09 2002 Alexey Voinov <voins@voins.program.ru> 2.20-alt1
- new version (2.20)

* Mon May 20 2002 Alexey Voinov <voins@voins.program.ru> 2.19-alt1
- new version (2.19)
- spec cleanup
- nlsdir patch

* Fri Apr 26 2002 Alexey Voinov <voins@voins.program.ru> 2.18-alt2
- rebuild with shared librx
- buildreqs fixed
- fixed some compile errors related to latest bison

* Tue Nov 06 2001 Alexey Voinov <voins@voins.program.ru> 2.18-alt1
- adapted for Sisyphus from cook.spec included in tarball

