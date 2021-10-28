%set_verify_elf_method unresolved=relaxed
%define hdf5_version 1.8.9
# TODO problem with package freehep-util
%def_without freehep
%def_without docs

Name:     scilab
Version:  6.1.1
Release:  alt2
Summary:  A high-level language and system for numerical computations

License:  GPL-2.0 and BSD-3-Clause
Group:    Sciences/Mathematics

Packager: Andrey Cherepanov <cas@altlinux.org>

Obsoletes: %name-doc
Obsoletes: scirenderer

Source0: %name-%version.tar
# VCS:   git://git.scilab.org/scilab
Source1: scilab-desktop-ru.tar
Source2: help.tar

Patch1:  scilab-alt-modules-crosslinking.patch
Patch2:  scilab-use-java-1.8.0-openjdk.patch
Patch3:  scilab-alt-fix-conflict-with-system-pause.patch
Patch4:	 scilab-fix-make-doc-ja_JP.patch
Patch5:  scilab-6.1.0-jogl-2.3.patch
Patch6:  scilab-alt-fix-missing-DSO.patch
Patch8:  scilab-5.5.2-disable-doclint.patch
Patch9:  scilab-alt-cxx-flags.patch
Patch10: scilab-alt-gcc8-fix.patch

# Debian patches
Patch11: scilab-jh.patch
Patch12: scilab-depend-scicos.patch
Patch13: scilab-missing-lib.patch
Patch14: scilab-reproducible-build.patch
Patch15: scilab-java-9.patch
Patch16: scilab-force-java-home.patch
Patch17: scilab-set-class-path.patch
Patch18: scilab-use-outside-font.patch
Patch19: scilab-java11-compatibility.patch
Patch20: scilab-force-fop-jar-into-classpath.patch
Patch21: scilab-ocaml-406.patch
Patch22: scilab-find-libs.patch
Patch23: scilab-strange-us-ascii-unmappable-character.patch
Patch24: scilab-openjdk11.patch
Patch25: scilab-fix-desktop-file-in-appdata.patch

URL: http://www.scilab.org
AutoReq: yes, noshell

# See https://bugzilla.redhat.com/show_bug.cgi?id=993239
ExcludeArch:   %{arm} aarch64 ppc64le

BuildRequires(pre): rpm-build-java
BuildRequires(pre): rpm-build-xdg
# Need for javah
BuildRequires: java-1.8.0-devel
BuildRequires: gcc-fortran
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel-static
BuildRequires: libxml2-devel

# Numerical libraries
# see "http://wiki.scilab.org/Linalg performances"
BuildRequires: liblapack-devel
BuildRequires: libarpack-ng-devel

# GUI/Console
BuildRequires: jpackage-utils
BuildRequires: /proc
BuildRequires: ant

BuildRequires: flexdock >= 1.0
BuildRequires: gluegen2
BuildRequires: jogl2 >= 2.3
BuildRequires: libGL-devel
BuildRequires: jrosetta >= 1.0.4

BuildRequires: apache-commons-logging
BuildRequires: javahelp2
BuildRequires: jlatexmath >= 1.0.2
BuildRequires: jlatexmath-fop >= 1.0.2
BuildRequires: jgraphx
BuildRequires: lucene
BuildRequires: lucene-analysis
BuildRequires: lucene-queryparser
BuildRequires: fop
BuildRequires: jeuclid
BuildRequires: batik
BuildRequires: xmlgraphics-commons
BuildRequires: ecj
%if_with freehep
BuildRequires: freehep-graphics2d
BuildRequires: freehep-util
%endif
BuildRequires: hamcrest
BuildRequires: objectweb-asm3
BuildRequires: checkstyle
BuildRequires: junit
BuildRequires: avalon-framework

Requires:      java-1.8.0-openjdk
Requires:      lucene lucene-analysis lucene-queryparser

# TCL/TK features
BuildRequires: tcl-devel
BuildRequires: tk-devel

Requires:      tcl
Requires:      tk

# Modelica
BuildRequires: ocaml

# Documentation
BuildRequires: saxon
BuildRequires: docbook-style-xsl

# All optional dependencies are needed to provide a full-featured Scilab
BuildRequires: gettext-devel
BuildRequires: libfftw3-devel
BuildRequires: libmatio-devel
BuildRequires: libsuitesparse-devel
BuildRequires: libhdf5-devel
#?BuildRequires: jhdf5
BuildRequires: xml-commons-jaxp-1.3-apis
BuildRequires: checkstyle

BuildRequires: libncurses-devel
BuildRequires: libgomp-devel
BuildRequires: libatlas-devel
BuildRequires: libpcre-devel
BuildRequires: libcurl-devel
BuildRequires: eigen3

# For generated documentation
BuildRequires: fonts-ttf-liberation

# Other
BuildRequires: empty

Requires: jogl2 >= 2.3
Requires: ecj
Requires: flexdock jrosetta
Requires: saxon
Requires: apache-commons-logging
Requires: javahelp2
Requires: jlatexmath >= 1.0.2
Requires: jlatexmath-fop >= 1.0.2
Requires: jgraphx
Requires: fop
Requires: jeuclid
Requires: batik
Requires: xmlgraphics-commons
Requires: xml-commons-jaxp-1.3-apis
Requires: libfftw3
%if_with freehep
Requires: freehep-graphics2d
Requires: freehep-util
%endif
Requires: empty
Requires: avalon-framework

#Requires: jgoodies-looks skinlf ant-commons-logging avalon-framework
#Requires: docbook-style-xsl saxon

%description
Scilab is the free software for numerical computation providing a
powerful computing environment for engineering and scientific
applications. It includes hundreds of mathematical functions. It has a
high level programming language allowing access to advanced data
structures, 2-D and 3-D graphical functions.

%prep
%setup
cd scilab
tar xf %SOURCE1
%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch4 -p1
%patch5 -p2
%patch6 -p2
%patch8 -p2
%patch9 -p2
%patch10 -p2
%patch11 -p2
%patch12 -p2
%patch13 -p2
%patch14 -p2
##patch15 -p2
%patch16 -p2
##patch17 -p2
%patch18 -p2
##patch19 -p2
%patch20 -p2
%patch21 -p2
%patch22 -p2
%patch23 -p2
%patch24 -p2
%patch25 -p2

# Update saxon dependency
# http://bugzilla.scilab.org/show_bug.cgi?id=8479
#sed -i "s/com.icl.saxon.Loader/net.sf.saxon.Version/g" m4/docbook.m4 configure

# Fix Class-Path in manifest
#sed -i '/name="Class-Path"/d' build.incl.xml

# Fix file-not-utf8
iconv -f ISO_8859-1 -t UTF-8 COPYING >COPYING.utf8
mv COPYING.utf8 COPYING

%build
cd scilab
#%%define _configure_target %{_arch}-pc-linux-gnu
%undefine _configure_gettext
export LDFLAGS="$LDFLAGS -Wl,--no-as-needed"
#aclocal
%autoreconf
%configure --enable-shared \
           --enable-static=no \
           --with-tk \
           --with-gfortran \
           --with-hdf5-include=%_libdir/hdf5-seq/include/ \
           --with-tcl-library=%_libdir \
           --with-tk-library=%_libdir \
           --with-pic \
%if_without freehep
	   --without-emf \
%endif
           --without-modelica \
	   --disable-static-system-lib \
           --enable-build-help

%make
%if_with docs
%make doc SCIVERBOSE=1
%endif

%install
cd scilab
%makeinstall_std
%find_lang %name

# Remove more advanced repl, user should use CLI options instead
rm -fr %buildroot%_desktopdir/%{name}-*.desktop
# Remove la files
rm -fr %buildroot%_libdir/%name/*.la

%if_without docs
tar xf %SOURCE2 -C %buildroot%_datadir/scilab/modules/helptools/jar/
%endif

%files -f scilab/%name.lang
%doc scilab/README.md scilab/ACKNOWLEDGEMENTS scilab/CHANGES.md scilab/COPYING scilab/COPYING-BSD
%_bindir/*
%_libdir/pkgconfig/*
%_libdir/%name
%_includedir/%name
%_datadir/%name
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*.png
%_datadir/appdata/scilab.appdata.xml
%_datadir/mime/packages/scilab.xml

%changelog
* Wed Oct 27 2021 Andrey Cherepanov <cas@altlinux.org> 6.1.1-alt2
- Explicitly use java-1.8.0-openjdk.
- Add avalon-framework to requirements (ALT #40586).

* Mon Jul 26 2021 Andrey Cherepanov <cas@altlinux.org> 6.1.1-alt1
- New version (ALT #40149).

* Sat May 02 2020 Andrey Cherepanov <cas@altlinux.org> 6.1.0-alt1
- New version.

* Fri Feb 15 2019 Andrey Cherepanov <cas@altlinux.org> 6.0.2-alt1
- New version.

* Fri Feb 15 2019 Ivan Razzhivin <underwit@altlinux.org> 6.0.1-alt4
- GCC8 fix

* Thu Nov 29 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.1-alt3
- Fix build with gfortran 8.
- Do not build on aarch64.

* Mon Mar 19 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.1-alt2
- Use generated documentation on x64_64.

* Fri Feb 16 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.1-alt1
- New version.
- Build without docs.

* Sat Dec 02 2017 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt3.2
- NMU: added batik 1.9 to supported batik versions (ALT #34263)

* Fri Dec 01 2017 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt3.1
- NMU: fixed build with new jgraphx (ALT #34263)

* Mon Nov 20 2017 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt3
- Show scinotes menu only in Development section

* Wed Nov 15 2017 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt2
- Build docs (ALT #34037)
- Fix run from menu (ALT #33976)
- Remove duplicate categories

* Wed Jun 07 2017 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt1
- New version

* Wed Mar 22 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 5.5.2-alt1.qa1
- NMU: rebuild against Tcl/Tk 8.6

* Tue Jan 24 2017 Andrey Cherepanov <cas@altlinux.org> 5.5.2-alt1
- New version (ALT #31794)
- Build from upstream git repository
- Require version-independed JDK
- Build with bundled scirenderer
- Add jogl2 and ecj to requirements

* Sun Nov 16 2014 Andrey Cherepanov <cas@altlinux.org> 5.5.1-alt1
- New version

* Mon Nov 10 2014 Andrey Cherepanov <cas@altlinux.org> 5.5.0-alt2
- Add ecj to requirements to fix build documentation

* Mon Apr 14 2014 Andrey Cherepanov <cas@altlinux.org> 5.5.0-alt1
- New version
- Do not use freehep* package for EMF support

* Fri Feb 28 2014 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt2
- Fix build (use unversioned libgomp-devel)

* Tue Jul 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.1-alt1.1
- Rebuilt with new libhdf5

* Sun May 26 2013 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt1
- New version 5.4.1
- Build docs again (fixed in upstream bug 4134)

* Fri May 24 2013 Andrey Cherepanov <cas@altlinux.org> 5.4.0-alt1
- New version 5.4.0 (ALT #25996)
- Translate desktop files into Russian
- Disable build documentation

* Tue Oct 20 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.1-alt3
- build doc (ALT #21904)

* Sat Sep 12 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.1-alt2
- remove libumfpack-devel from buildrequres

* Thu Jul 16 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.1-alt1
- 5.1.1

* Wed Dec 24 2008 Denis Medvedev <nbr@altlinux.ru> 4.1.2-alt6
- with gtk2, bugfix for #18307 ALT bugzilla

* Wed Sep 24 2008 Denis Medvedev <nbr@altlinux.ru> 4.1.2-alt5
- Fix bug with not working editor (#17318) 

* Sat Sep 20 2008 Denis Medvedev <nbr@altlinux.ru> 4.1.2-alt4
- repocop suggested change /tmp to /home/denis/tmp for safety

* Tue May 06 2008 Denis Medvedev <nbr@altlinux.ru> 4.1.2-alt3
- bug 15556 - BWidged removed and used in-system

* Tue May 06 2008 Denis Medvedev <nbr@altlinux.ru> 4.1.2-alt1.M40.1
- Updates to Branch M40

* Tue May 06 2008 Denis Medvedev <nbr@altlinux.ru> 4.1.2-alt2
- repocop icondirs

* Tue May 06 2008 Denis Medvedev <nbr@altlinux.ru> 4.1.2-alt1
 - 4.1.2 version from upstream

* Fri Sep 28 2007 Denis Medvedev <nbr@altlinux.ru> 4.1.1-alt1.3
- Debug option, pic option

* Thu Aug 30 2007 Denis Medvedev <nbr@altlinux.ru> 4.1.1-alt1.2
- changes for x86_64 compilation

* Tue Aug 28 2007 Denis Medvedev <nbr@altlinux.ru> 4.1.1-alt1.1
- Taken from orphaned, new version

* Wed Feb 08 2006 ALT QA Team Robot <qa-robot@altlinux.org> 3.1.1-alt1.1
- Rebuild with libXaw3d.so.8 .

* Tue Dec 20 2005 Dimitry V. Ketov <dketov@altlinux.ru> 3.1.1-alt1
- 3.1.1
- app-defaults location fix

* Wed Dec 08 2004 Dimitry V. Ketov <dketov@altlinux.ru> 3.0-alt1
- 3.0
- misc. spec bugfixes, sources clean before build
- menu and new scilab mascot icons

* Tue Apr 08 2003 Stanislav Ievlev <inger@altlinux.ru> 2.7-alt1
- 2.7

* Mon Oct  7 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.6-alt8
- rebuilt with tcl 8.4

* Wed Sep 18 2002 Stanislav Ievlev <inger@altlinux.ru> 2.6-alt7
- rebuild with new XFree86

* Wed Sep 04 2002 Stanislav Ievlev <inger@altlinux.ru> 2.6-alt6
- rebuild with gcc3
- termcap -> terminfo

* Sat Jun 15 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.6-alt5
- rebuilt in new env

* Mon Dec 24 2001 Stanislav Ievlev <inger@altlinux.ru> 2.6-alt4
- fix links in app-defaults

* Thu Oct 11 2001 Stanislav Ievlev <inger@altlinux.ru> 2.6-alt3
- MDK merges

* Fri May 25 2001 Stanislav Ievlev <inger@altlinux.ru> 2.6-alt2
- path bugfix. Remove doc package.

* Thu Apr 12 2001 Stanislav Ievlev <inger@altlinux.ru> 2.6-alt1
- Up to 2.6. spec clean up and bugfix

* Tue Jan 09 2001 AEN <aen@logic.ru>
- adopted for RE

* Sun Oct 22 2000 Fernando M. Roxo da Motta <roxo@conectiva.com.br>
- inserted documentation package

* Fri Oct 20 2000 Fernando M. Roxo da Motta <roxo@conectiva.com.br>
- Fixed hardwired PATH's

* Wed Oct 18 2000 Fernando M. Roxo da Motta <roxo@conectiva.com.br>
- Packaged for Conectiva Linux
- Fixed a lot of macros

* Tue Sep 26 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.4.1-3mdk
- build release
- macros
- menu

* Wed May 03 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.4.1-2mdk
- bzip2 patches
- fix group

* Thu Dec 30 1999 Lenny Cartier <lenny@mandrakesoft.com>
- new in contribs
- bz2 archive

* Wed Aug 18 1999 Tim Powers <timp@redhat.com>
- exludearch alpha

* Wed Jul 21 1999 Tim Powers <timp@redhat.com>
- rebuilt for 6.1

* Wed May 12 1999 Bill Nottingham <notting@redhat.com>
- clean up dependencies

* Wed May 05 1999 Bill Nottingham <notting@redhat.com>
- update to 2.4.1

* Fri Oct 23 1998 Jeff Johnson <jbj@redhat.com>
- Upgrade to 2.4.

* Thu Oct 22 1998 Jeff Johnson <jbj@redhat.com>
- Fixes to permit compile on alpha.
- Eliminate lurking dependencies on /bin/sh5 and SCILABGS.
- Modify default value of SCI variable to be correct for users.
- Add /usr/bin/scilab symlink.

* Sat Jul 11 1998 Jeff Johnson <jbj@redhat.com>
- Create powertools package.

