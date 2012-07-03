%define target TARGET=opt

Name: hevea
Version: 1.10
Release: alt3
Packager: Grigory Batalov <bga@altlinux.ru>

Group: Publishing
Summary: A fast and powerful LaTeX to HTML translator
License: QPL
Url: http://para.inria.fr/~maranget/hevea

Source: %url/distri/%name-%version.tar.gz

Requires: /usr/bin/latex, /usr/bin/pdflatex

BuildRequires: rpm-build-ocaml

# Automatically added by buildreq on Wed Jul 02 2008
BuildRequires: ocaml

%description
HeVeA is a LaTeX to HTML translator. Its remarkable features are
- It produces good output. By default (can be turned off) it uses the
symbol face for math symbols. Either way it usually avoids generating
zillions of picture files.
- It is highly configurable through (La)TeX macros. Though aimed at
LaTeX input it understands a fair subset of TeX' macro language.
- It runs fast.
This version of HeVeA is patched to generate by default PNG picture
files instead of GIF.

%prep
%setup -q

%build
rm -f config.sh
%make_build %target \
	PREFIX=%_prefix \
	LIBDIR=%_datadir/%name \
	LATEXLIBDIR=%_datadir/%name

%install
rm -f config.sh
%make_install %target \
	DESTDIR=%buildroot \
	PREFIX=%_prefix \
	LIBDIR=%_datadir/%name \
	LATEXLIBDIR=%_datadir/%name \
	install

%files
%_bindir/*
%_datadir/%name
%doc README CHANGES LICENSE pub.txt

%changelog
* Tue Oct 06 2009 Grigory Batalov <bga@altlinux.ru> 1.10-alt3
- Remove obsolete post-install scripts and thus tetex dependence.
- Move templates to arch-independent directory.
- Require latex and pdflatex binaries (without specifying a package).

* Wed Jul 02 2008 Alexander Myltsev <avm@altlinux.ru> 1.10-alt2
- Remove hardcoded OCaml dependency.

* Sat Dec 01 2007 ALT QA Team Robot <qa-robot@altlinux.org> 1.10-alt1.1
- Rebuilt with ocaml-3.10.

* Wed Oct 03 2007 Grigory Batalov <bga@altlinux.ru> 1.10-alt1
- New upstream release.

* Fri Feb 02 2007 Grigory Batalov <bga@altlinux.ru> 1.09-alt1
- New upstream release.
- No need for makefile patch any more.
- Texmf files have been disappeared.
- Use get_SVR macro for OCaml dependence.
- Build native binaries.
- New packager.

* Sun Jan 14 2007 Mikhail Yakshin <greycat@altlinux.org> 1.07-alt3
- Rebuilt with ocaml-3.09.3

* Tue Mar 07 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.07-alt2
- NMU.
- Rebuild with new ocaml & friends.

* Mon Jan 17 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.07-alt1
- 1.0.7

* Fri Sep 17 2004 Dmitry V. Levin <ldv@altlinux.org> 1.06-alt2.5
- Rebuilt with ocaml-3.08.0-alt0.2

* Fri May  7 2004 Alexander V. Nikolaev <avn@altlinux.org> 1.06-alt2.4
- Non-maintainer upload
- Rebuild with glibc 2.3.x and ocaml 3.07-alt6.1

* Wed Mar 17 2004 Vitaly Lugovsky <vsl@altlinux.ru> 1.06-alt2.3
- rebuild

* Wed Feb 18 2004 Vitaly Lugovsky <vsl@altlinux.ru> 1.06-alt2.2
- rebuild

* Tue Jan 27 2004 Vitaly Lugovsky <vsl@altlinux.ru> 1.06-alt2.1
- rebuild

* Thu Dec 25 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.06-alt2
- rebuild with new ocaml.

* Thu Nov 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.06-alt1
- new version

* Wed Oct 15 2003 Vitaly Lugovsky <vsl@altlinux.ru> 1.05-alt5b
- dirty workaround - build a bytecode version

* Wed Oct 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.05-alt5
- Rebuild to move to the files.

* Wed Mar 13 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.05-alt4
- Fixed %%files section.

* Mon Nov 19 2001 Stanislav Ievlev <inger@altlinux.ru> 1.05-alt3
- small cleanups

* Thu Nov 16 2001 Yuri N. Sedunov <aris@altlinux.ru> 1.05-alt2
- Added requires - tetex. 
- Added _compress_method skip (brp-compress compress .hva files
  in info directory.) 
- Cleanup spec.

* Tue Nov 13 2001 Yuri N. Sedunov <aris@altlinux.ru> 1.05-alt1
- First build for Sisyphus. PNG-patch, description, manpages
  from Debian package - hevea_1.05-6+png_i386.deb
