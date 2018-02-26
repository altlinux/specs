# help is welcome to re-enable, fix packaging and test
%def_enable  guile
%def_disable lua
%def_disable ocaml
%def_disable php
%def_disable python
%def_disable ruby

Name: graphviz
Version: 2.28.0
Release: alt2

Summary: Graphs visualization tools
License: Common Public License 1.0
Group: Publishing

# Git: http://www.graphviz.org/pub/scm/graphviz2/.git
Url: http://www.graphviz.org
Source0: %name-%version.tar
Source1: graphviz-2.2-alt-libpath.patch
Patch0:  graphviz-2.24.0-alt-perl-5.12.patch
Packager: Michael Shigorin <mike@altlinux.org>

Requires: lib%name = %version-%release
Provides: libdotneato = %version
Obsoletes: libdotneato < %version

# Automatically added by buildreq on Wed Oct 12 2011 (-bi)
BuildRequires: flex gcc-c++ ghostscript-utils groff-base guile18-devel imake libXaw-devel libXpm-devel libexpat-devel libfreeglut-devel libgd2-devel libglade-devel libgs-devel libgtkglext-devel libgts-devel liblasi-devel libpng-devel librsvg-devel swig tk-devel xorg-cf-files

%{?_enable_lua:BuildRequires: liblua5-devel}
%{?_enable_guile:BuildRequires: guile18-devel}

%define gvlibdir %_libdir/%name
%define gvdatadir %_datadir/%name

%set_verify_elf_method unresolved=relaxed
%add_findreq_skiplist %gvdatadir/demo/*.pl
%add_findreq_skiplist %gvdatadir/demo/*.tcl

%description
Graphviz is a set of graph drawing tools originally developed
at AT&T Research.

Graph drawing addresses the problem of visualizing structural
information by constructing geometric representations of abstract
graphs and networks.  Automatic generation of graph drawings has
important applications in key technologies such as database
design, software engineering, VLSI and network design and visual
interfaces in other domains.

# {{{ subpackages
%package -n lib%name
Summary: Shared libraries for %name
Group: System/Libraries

%description -n lib%name
This package includes shared libraries for %name

%package -n lib%name-devel
Summary: Header files and C programming manual for %name
Group: Development/C
Requires: lib%name = %version-%release
Provides: %name-devel = %version
Obsoletes: %name-devel < %version

%description -n lib%name-devel
This package includes header files for %name

%package doc
Summary: Documentation for %name
Group: Publishing
Requires: %name = %version-%release
BuildArch: noarch

%description doc
This package contains most of documentation for %name

%package graphs
Summary: Demo graphs for graphviz
Group: Graphics
Requires: %name = %version-%release
BuildArch: noarch

%description graphs
This package provides some example graphs for %name.

%if_enabled guile
%package guile
Summary: Guile bindings to %name
Group: Development/Other
Requires: %name = %version-%release

%description guile
This package makes %name functionality accessible from Guile
%endif

%if_enabled lua
%package lua
Summary: Lua bindings to %name
Group: Development/Other
Requires: %name = %version-%release

%description lua
This package makes %name functionality accessible from Lua
%endif

%package perl
Summary: Perl bindings to %name
Group: Development/Perl
Requires: %name = %version-%release

%description perl
This package makes %name functionality accessible from Perl

%if_enabled python
%package python
Summary: Python bindings to %name
Group: Development/Python
Requires: %name = %version-%release

%description python
This package makes %name functionality accessible from Python
%endif

%package ruby
Summary: Ruby bindings to %name
Group: Development/Ruby
Requires: %name = %version-%release

%description ruby
This package makes %name functionality accessible from Ruby

%package tcl
Summary: Tcl bindings to %name
Group: Development/Tcl
Requires: %name = %version-%release
Requires: tcl >= 8.4.0-alt1
Provides: tcl-tkspline = %version tcl-gd = %version
Obsoletes: tcl-tkspline < %version tcl-gd < %version

%description tcl
This package makes %name functionality accessible from Tcl

# }}}

%prep
%setup
%patch0 -p1

%build
%add_optflags -DNDEBUG %optflags_fastmath
%configure \
	--disable-static \
	--with-pangocairo \
	--with-x \
	--with-gdk-pixbuf \
	--without-gnomeui \
	--with-gtk \
	--with-ipsepcola \
	--with-sfdp \
	--with-smyrna \
	%{subst_enable guile } \
	%{subst_enable lua } \
	%{subst_enable ocaml } \
	%{subst_enable php } \
	%{subst_enable python } \
	%{subst_enable ruby } \
	--enable-tcl \
	--disable-java \
	--disable-sharp

%make_build

%install
%make_install DESTDIR=%buildroot install
# avoid %%doc, install by hand
mkdir -p %buildroot%_defaultdocdir
mv %buildroot%gvdatadir/doc %buildroot%_defaultdocdir/%name-%version
cp -a AUTHORS COPYING cpl1.0.txt ChangeLog NEWS %buildroot%_defaultdocdir/%name-%version
mkdir -p %buildroot%_tcldatadir/{%name,gd,tkspline}
cat <<EOF > %buildroot%_tcldatadir/gd/pkgIndex.tcl
package ifneeded Gdtclft %version "load [file join \$dir .. .. .. lib tcl libgdtclft.so.0] Gdtclft"
EOF
cat <<EOF > %buildroot%_tcldatadir/%name/pkgIndex.tcl
package ifneeded Tcldot %version "load [file join \$dir .. .. .. lib tcl libtcldot.so.0] Tcldot"
package ifneeded Tclpathplan %version "load [file join \$dir .. .. .. lib tcl libtclplan.so.0] Tclpathplan"
EOF
cat <<EOF > %buildroot%_tcldatadir/tkspline/pkgIndex.tcl
package ifneeded Tkspline %version "
	package require Tk 8.3
        load [file join \$dir .. .. .. lib tcl libtkspline.so.0] Tkspline"
EOF
# created by %_bindir/dot -c
touch %buildroot%gvlibdir/config

rm -f %buildroot%gvlibdir/*/lib*.la
rm -f %buildroot%gvlibdir/libgvplugin_*.la

%post
[ ! -x %_bindir/dot ] || %_bindir/dot -c >&/dev/null

%files
%_bindir/*
%dir %gvdatadir/
%gvdatadir/lefty
%gvdatadir/smyrna
%ghost %gvlibdir/config
%_man1dir/*
%_man7dir/*
%dir %_defaultdocdir/%name-%version/
%_defaultdocdir/%name-%version/AUTHORS
%_defaultdocdir/%name-%version/COPYING
%_defaultdocdir/%name-%version/cpl1.0.txt
%_defaultdocdir/%name-%version/ChangeLog
%_defaultdocdir/%name-%version/NEWS

%files -n lib%name
%_libdir/lib*.so.*
%dir %gvlibdir/
%gvlibdir/lib*.so.*
%gvlibdir/libgvplugin_*.so

%files -n lib%name-devel
%_includedir/%name
%_libdir/lib*.so
%_libdir/pkgconfig/*.pc
%_man3dir/*

%files doc
%_defaultdocdir/%name-%version/
%exclude %_defaultdocdir/%name-%version/AUTHORS
%exclude %_defaultdocdir/%name-%version/COPYING
%exclude %_defaultdocdir/%name-%version/cpl1.0.txt
%exclude %_defaultdocdir/%name-%version/ChangeLog
%exclude %_defaultdocdir/%name-%version/NEWS
%gvdatadir/examples

%files graphs
%gvdatadir/graphs

%if_enabled guile
%files guile
%dir %gvlibdir/guile/
%gvlibdir/guile/*.so
%endif

%if_enabled lua
%files lua
%dir %gvlibdir/lua/
%gvlibdir/lua/gv.so
%endif

%files perl
%dir %gvlibdir/perl/
%gvlibdir/perl/gv.pm
%gvlibdir/perl/gv.so
%gvlibdir/perl/libgv_perl.so
%perl_vendor_archlib/gv.pm
%perl_vendor_archlib/gv.so
%gvdatadir/demo/modgraph.pl

%if_enabled python
%files python
%dir %gvlibdir/python*/
%gvlibdir/python*/_gv.so
%endif

%if_enabled ruby
%files ruby
%dir %gvlibdir/ruby/
%gvlibdir/ruby/gv.so
%endif

%files tcl
%dir %gvlibdir/tcl/
%gvlibdir/tcl/libgdtclft.so*
%gvlibdir/tcl/libgv_tcl.so
%gvlibdir/tcl/libtcldot.so*
%gvlibdir/tcl/libtcldot_builtin.so*
%gvlibdir/tcl/libtclplan.so*
%gvlibdir/tcl/libtkspline.so*
%gvlibdir/tcl/pkgIndex.tcl
%_libdir/tcl*/*
%_tcldatadir/%name
%_tcldatadir/gd/pkgIndex.tcl
%_tcldatadir/tkspline/pkgIndex.tcl
%gvdatadir/demo/doted.tcl
%gvdatadir/demo/entities.tcl
%gvdatadir/demo/gcat.tcl
%gvdatadir/demo/modgraph.tcl
%gvdatadir/demo/pathplan.tcl
%gvdatadir/demo/spline.tcl
%gvdatadir/demo/pathplan_data
%gvdatadir/demo/*.README
%gvdatadir/demo/*.html

# TODO:
# - enable/fix/test language bindings

%changelog
* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 2.28.0-alt2
- rebuilt against current liblasi

* Wed Oct 12 2011 Alexey Tourbin <at@altlinux.ru> 2.28.0-alt1.1
- rebuilt for perl-5.14

* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 2.28.0-alt1
- 2.28.0

* Sun Mar 13 2011 Michael Shigorin <mike@altlinux.org> 2.26.3-alt2
- (re)added zlib, lipbng buildreqs (overoptimization+depdrift ate 'em?)

* Sun Mar 13 2011 Michael Shigorin <mike@altlinux.org> 2.26.3-alt1
- 2.26.3

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.24.0-alt1.3
- Rebuilt for debuginfo

* Wed Nov 03 2010 Vladimir Lettiev <crux@altlinux.ru> 2.24.0-alt1.2
- rebuilt with perl 5.12
- added patch to fix linking

* Tue Oct 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.24.0-alt1.1
- rebuild with libgs.so.9

* Sat Oct 31 2009 Michael Shigorin <mike@altlinux.org> 2.24.0-alt1
- 2.24.0
  + dropped patches (merged upstream)
- enabled:
  + gtkgl, gtkglext, glade, ghostscript, gts libraries
  + sfdp neato layout engine
  + smyrna OpenGL large graph viewer
  + guile bindings
- graphs subpackage made noarch
- description cleanup

* Sat Jun 06 2009 Michael Shigorin <mike@altlinux.org> 2.22.2-alt2.2
- noarch doc subpackage
- added gvpr.1 patch so file(1) would understand it's a manpage
  and brp-compress would brp-compress would kindly process it too

* Wed Jun 03 2009 Michael Shigorin <mike@altlinux.org> 2.22.2-alt2.1
- dropped obsolete patches (weren't even applied)
- added vimdot patch per led@'s advice so as to avoid
  requisite vim dependency (and enhancing it along the way)

* Fri Apr 17 2009 Michael Shigorin <mike@altlinux.org> 2.22.2-alt2
- adapted repocop patch

* Sun Apr 05 2009 Michael Shigorin <mike@altlinux.org> 2.22.2-alt1
- 2.22.2
- doc subpackage now actually contains something (#18601)
- mann pages went man3
- added liblasi support (unicode postscript output, #6489)
- extended build environment with what else was missing:
  librsvg-devel, libgtkglext-devel, libglade-devel, groff, ps2pdf
- enabled SMP build
- spec cleanup

* Wed Dec 03 2008 Michael Shigorin <mike@altlinux.org> 2.20.3-alt3
- applied repocop patch

* Sun Nov 09 2008 Michael Shigorin <mike@altlinux.org> 2.20.3-alt2
- rebuilt against current libXaw-devel

* Sat Oct 25 2008 Michael Shigorin <mike@altlinux.org> 2.20.3-alt1
- 2.20.3: fixes for CVE-2008-4555 (boundary error in .dot parser);
  thank ldv@ for heads-up, sorry for being a bit slow with update

* Tue Sep 09 2008 Michael Shigorin <mike@altlinux.org> 2.20.2-alt2
- added missing Provides:/Obsoletes: to tcl subpackage,
  thanks Alexei V. Mezin for stumbling upon and reporting

* Mon Sep 08 2008 Michael Shigorin <mike@altlinux.org> 2.20.2-alt1
- 2.20.2
- fixed License: (text was already included in the package but header was wrong)
- suppressed requires for demo scripts
- started reworking dynamic enabling of bindings subpackages
  + adapted perl, tcl support
  + merged tcl-gd, tcl-tkspline subpackages into -tcl
  + disabled lua, ocaml, php, python, ruby support by now
    (broken build, need to fix first)
  + split -demos and merged those into language-dependent subpackages
  + introduced -graphs subpackage (following PLD 2.20.2-0.1 spec)
- hopefully fixed #16015
- huge thanks goto led@ for finding the cause for %%add_findreq_skiplist
  to miss the given patterns (which were containing "//" after expanding
  a carefully crafted macro)

* Thu Feb 14 2008 Michael Shigorin <mike@altlinux.org> 2.16.1-alt1
- 2.16.1 (#9078, #9278)
  + removed patches
  + dotneato-config disappeared
  + tcl bindings well might have broke: moved to %gvlibdir/tcl/
- tossed in parts of Debian 2.16-3 and PLD 2.14.1-2 packages
  + added lua, perl, python, ruby bindings (could mispackage)
  + didn't add guile, java, ocaml, php, C# bindings yet
- moved %_defaultdocdir/%name to %_defaultdocdir/%name-%version
- despammed descriptions
- spec macro abuse cleanup

* Fri Nov 02 2007 Denis Smirnov <mithraen@altlinux.ru> 2.2.1-alt4
- fix building

* Fri Nov 02 2007 Denis Smirnov <mithraen@altlinux.ru> 2.2.1-alt3
- rebuild

* Thu Aug 02 2007 Slava Semushin <php-coder@altlinux.ru> 2.2.1-alt2.1
- NMU
- Directory /usr/share/graphviz now belongs to package (#8702)
- Spec cleanup

* Mon Jul 03 2006 Denis Smirnov <mithraen@altlinux.ru> 2.2.1-alt2
- fix build with -Wl,--as-needed

* Mon Jun 13 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Wed Feb  9 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2-alt1
- 2.2
- merged dotneato in, no external consumers remain
- rest of old patches dropped, recent libgd doesn't needs them

* Thu Aug 12 2004 Dmitry V. Levin <ldv@altlinux.org> 1.12-alt3
- Moved dotneato library to separate subpackage (#4947).
- Rebuilt with libgd2-2.0.28.

* Sat Jun  5 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12-alt2
- fixed font handling via gd, see #4269

* Tue Apr 13 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12-alt1
- 1.12
- Tkspline packaged separately

* Thu Dec 11 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10-alt2
- built with system libgd2
- .la removed from devel subpackage

* Sat Sep 20 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.10-alt1
- 1.10

* Fri May 23 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.9-alt1
- 1.9

* Mon Jan 13 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.8.10-alt3
- rebuilt in new env

* Mon Nov 18 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.8.10-alt2
- libgd2 now in separate package
- rebuilt with (new) system libgd2

* Mon Oct 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.8.10-alt1
- 1.8.10
- additional packages separated:
  - libgd2
  - libgd2-devel
  - tcl-gd

* Thu Jul 25 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.8.8-alt1
- 1.8.8

* Fri Oct 12 2001 AEN <aen@logic.ru> 1.7.4-alt2
- rebuilt with libpng.so.3

* Wed Jul 11 2001 Peter 'Nidd' Novodvorsky <nidd@altlinux.ru> 1.7.4-alt1
- ALT Linux adaptations.

* Thu Mar 15 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.7.4-3mdk
- fix word.c

* Wed Jan 10 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.7.4-2mdk
- bzip2 sources & diff

* Thu Jan  4 2001 Pixel <pixel@mandrakesoft.com> 1.7.4-1mdk
- initial spec

