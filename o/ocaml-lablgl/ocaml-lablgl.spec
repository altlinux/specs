%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
Name: ocaml-lablgl
Version: 1.06
Release: alt3
Summary: OpenGL library for OCaml
License: BSD-3-Clause
Group: Development/ML
Url: https://forge.ocamlcore.org/projects/lablgl/
# git https://forge.ocamlcore.org/anonscm/git/lablgl/lablgl.git
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

Provides: %name-runtime = %version-%release
Obsoletes: %name-runtime < %version-%release
Provides: lablGL = %version-%release
Obsoletes: lablGL

BuildRequires: ocaml-labltk-devel libXext-devel libXmu-devel libGLUT-devel tcl-togl-devel ocaml-camlp5
BuildRequires: libXxf86vm-devel
BuildRequires(pre): rpm-build-tcl

%description
LablGL is an OpenGL interface for Objective Caml.  It includes two
interfaces: the Togl widget, for comfortable use with LablTk, and
LablGlut for standalone applications not using Tcl/Tk.


%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Requires: ocaml-labltk
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1
cat > Makefile.config <<EOF
CAMLC = ocamlc.opt
CAMLOPT = ocamlopt.opt
BINDIR = %_bindir
XINCLUDES =
XLIBS = -lXext -lXmu -lX11
TKINCLUDES = -I%_includedir
GLINCLUDES =
GLLIBS = -lGL -lGLU
GLUTLIBS = -lglut -lXxf86vm
RANLIB = :
LIBDIR = %_libdir/ocaml
DLLDIR = %_libdir/ocaml/stublibs
INSTALLDIR = %_libdir/ocaml/lablGL
TOGLDIR=Togl
COPTS = $RPM_OPT_FLAGS
EOF

%build
make all opt INSTALLDIR=%_libdir/ocaml/lablGL \
	TCLLIBDIR=%_tcllibdir TOGLVERSION=%{get_version tcl-togl}

%install
mkdir -p %buildroot%_libdir/ocaml/stublibs
mkdir -p %buildroot%_bindir
%make_install install \
	INSTALLDIR=%buildroot%_libdir/ocaml/lablGL \
	DLLDIR=%buildroot%_libdir/ocaml/stublibs \
	BINDIR=%buildroot%_bindir

# Make and install a META file.
cat <<EOM >META
version="%version"
directory="+lablgl"
archive(byte) = "lablgl.cma"
archive(native) = "lablgl.cmxa"

package "togl" (
  requires = "labltk lablgl"
  archive(byte) = "togl.cma"
  archive(native) = "togl.cmxa"
)

package "glut" (
  requires = "lablgl"
  archive(byte) = "lablglut.cma"
  archive(native) = "lablglut.cmxa"
)
EOM
install -p -m644 META %buildroot%_libdir/ocaml/lablGL/META

%files
%doc CHANGES COPYRIGHT README Togl/examples/ LablGlut/examples/
%dir %_libdir/ocaml/lablGL
%_libdir/ocaml/lablGL/*.cma
%_libdir/ocaml/lablGL/*.cmi
%_libdir/ocaml/stublibs/*.so
%_bindir/lablgl
%_bindir/lablglut

%files devel
%doc CHANGES COPYRIGHT README LablGlut/examples Togl/examples
%_libdir/ocaml/lablGL/META
%_libdir/ocaml/lablGL/*.mli
%_libdir/ocaml/lablGL/*.cmxa
%_libdir/ocaml/lablGL/*.cmx
%_libdir/ocaml/lablGL/*.a
%_libdir/ocaml/lablGL/build.ml
%exclude %_libdir/ocaml/lablGL/gl*.ml
%exclude %_libdir/ocaml/lablGL/raw.ml
%exclude %_libdir/ocaml/lablGL/togl.ml

%changelog
* Sat Sep 18 2021 Anton Farygin <rider@altlinux.ru> 1.06-alt3
- fixed build with enabled LTO

* Tue Sep 08 2020 Anton Farygin <rider@altlinux.ru> 1.06-alt2
- ocaml-labltk have been renamed to ocaml-labltk-devel

* Fri Aug 16 2019 Anton Farygin <rider@altlinux.ru> 1.06-alt1
- 1.06

* Tue Jul 30 2019 Anton Farygin <rider@altlinux.ru> 1.05-alt8
- rebuilt with ocaml-4.08
- preprocessor changed from camlp4 to camlp5

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.05-alt7
- rebuilt with ocaml-4.07.1
- force libfreeglut

* Tue Sep 04 2018 Anton Farygin <rider@altlinux.ru> 1.05-alt6
- rebuilt with ocaml-4.07

* Tue Jun 05 2018 Nikolai Kostrigin <nickel@altlinux.org> 1.05-alt5
- rebuild with bundled tcl-togl 1.7 (cancel ALT Linux patch temporarily)

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 1.05-alt4
- rebuilt for ocaml 4.06.1

* Mon Jul 10 2017 Anton Farygin <rider@altlinux.ru> 1.05-alt3
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.05-alt2
- rebuild with ocaml 4.04.1

* Fri Apr 21 2017 Anton Farygin <rider@altlinux.ru> 1.05-alt1
- new version
- split to devel and main packages

* Thu Apr 06 2017 Anton Farygin <rider@altlinux.ru> 1.04-alt2
- renamed to ocaml-lablgl
- build from upstream git
- rebuild with ocaml-4.04

* Mon Dec 26 2011 Alexey Shabalin <shaba@altlinux.ru> 1.04-alt1
- 1.04

* Thu Jul 07 2011 Dmitry V. Levin <ldv@altlinux.org> 1.03-alt4
- Fixed build.

* Tue Dec 07 2008 Veaceslav Grecea <slavutich@altlinux.org> 1.03-alt3
- Resurrected from orfaned
- Rebuild

* Tue Apr 08 2008 Alexey Tourbin <at@altlinux.ru> 1.03-alt2
- rebuilt for new ocaml dependencies

* Wed Mar 12 2008 Grigory Batalov <bga@altlinux.ru> 1.03-alt1
- New upstream release.

* Sat Dec 23 2006 Grigory Batalov <bga@altlinux.ru> 1.02-alt1
- New upstream release.
- Moving to get_SVR macro.
- Requirements updated.
- Toplevel scripts moved from runtime to main package.
- Strict packaging.
- Use system tcl-togl.
- Moved to site-lib folder.
- New group, url, packager.

* Tue Mar 21 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.01-alt3
- Moving to get_dep macro.

* Tue Mar 07 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.01-alt2
- Rebuild with ocaml-3.0.9-alt1.

* Wed Dec 28 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.01-alt1.1
- Rebuild with ocaml-3.08.1-alt1.1 .

* Mon Nov 01 2004 Vitaly Lugovsky <vsl@altlinux.ru> 1.01-alt1
- new version

* Sun Jul 18 2004 Vitaly Lugovsky <vsl@altlinux.ru> 1.00-alt6
- rebuild

* Fri May  7 2004 Alexander V. Nikolaev <avn@altlinux.org> 1.00-alt5.1
- Non-maintainer upload
- Add "packager" to spec
- Rebuild with glibc 2.3.x and ocaml 3.07-alt6.1

* Wed Mar 17 2004 Vitaly Lugovsky <vsl@altlinux.ru> 1.00-alt5
- rebuild

* Wed Feb 18 2004 Vitaly Lugovsky <vsl@altlinux.ru> 1.00-alt4
- rebuild

* Tue Jan 27 2004 Vitaly Lugovsky <vsl@altlinux.ru> 1.00-alt3
rebuild

* Wed Nov 12 2003 Vitaly Lugovsky <vsl@altlinux.ru> 1.00-alt2
relaxed elf verifying

* Fri Oct 10 2003 Vitaly Lugovsky <vsl@altlinux.ru> 1.00-alt1
- a new version.

* Thu Oct 09 2003 Vitaly Lugovsky <vsl@altlinux.ru> 0.99-alt1
- A new version, rebuild with 3.07

* Wed Aug 27 2003 Vitaly Lugovsky <vsl@altlinux.ru> 0.98-alt4s
- rebuild (new ocaml version)

* Fri Jan 31 2003 Vitaly Lugovsky <vsl@altlinux.ru> 0.98-alt3s
- rebuild with a shared libraries support

* Tue Jan 21 2003 Vitaly Lugovsky <vsl@altlinux.ru> 0.98-alt3
- exact libGLU-devel dependency

*Tue Aug 20 2002 Vitaly Lugovsky <vsl@altlinux.ru> 0.98-alt2
- Rebuild with 3.06
- Runtime part now separated

*Fri Aug 2 2002 Vitaly Lugovsky <vsl@altlinux.ru> 0.98-alt1
- New version released

*Mon Jul 29 2002 Vitaly Lugovsky <vsl@altlinux.ru> 0.97-alt10
- Rebuilt with 3.05 release

*Mon Jun 24 2002 Vitaly Lugovsky <vsl@altlinux.ru> 0.97-alt9
- Rebuild with 3.04_15

*Tue May 14 2002 Vitaly Lugovsky <vsl@altlinux.ru> 4.97-alt8
- Rebuild with 3.04_10, no more post and preun scripts

*Tue Apr 16 2002 Vitaly Lugovsky <vsl@altlinux.ru> 0.97-alt7
- Rebuild with ocaml-3.04+9
- Patch from vsu <vsu@mivlgu.murom.ru> (bugfix for path in lablgltop
  script).

*Sat Mar  2 2002 Vitaly Lugovsky <vsl@altlinux.ru> 0.97-alt6
- Rebuild with ocaml-3.04+7-alt1

*Fri Feb 22 2002 Vitaly Lugovsky <vsl@altlinux.ru>
- camlp4 dependency added.

*Sun Feb 17 2002 Vitaly Lugovsky <vsl@altlinux.ru>
- Rebuild with ocaml-3.04-alt4 (shared patch disabled)

*Fri Jan 25 2002 Vitaly Lugovsky <vsl@altlinux.ru>
- native compilation added

*Mon Jan 23 2002 Vitaly Lugovsky <vsl@altlinux.ru>
- First RPM release.
