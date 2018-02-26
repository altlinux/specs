Name: make-figure
Version: 1.1
Release: alt2

Source:%name-%version.tar.gz

Packager: Paul Wolneykien <manowar@altlinux.ru>

Summary: Prepare a figure for document layout
License: GPLv3
Group: Publishing
BuildArch: noarch

# Automatically added by buildreq on Thu Apr 09 2009
BuildRequires: rpm-macros-fillup

Requires: ImageMagick
Requires: inkscape >= 0.48

%description
The make-figure is intended to help in preparing figures for
LaTeX documents. The main idea is to have one set of figure sources
accompained with the appropriate TeX template files and to produce
final TeX and graphical files from them automatically.

%package plot
Summary: A plot figure source handling for make-figure tool
License: GPLv3
Group: Publishing

Requires: octave

%description plot
The make-figure is intended to help in preparing figures for
LaTeX documents.

This is the GNU Octave plot source handling addon for make-figure tool.

%prep
%setup -q

%install
install -p -m0755 -D extract-psfrags %buildroot%_bindir/extract-psfrags
install -p -m0755 -D make-figure %buildroot%_bindir/make-figure
install -p -m0755 -D make-plot %buildroot%_bindir/make-plot
install -p -m0755 -D make-raster %buildroot%_bindir/make-raster
install -p -m0755 -D make-vector %buildroot%_bindir/make-vector

install -p -m0644 -D man/man1/make-figure.1 %buildroot%_man1dir/make-figure.1
install -p -m0644 -D man/ru/man1/make-figure.1 %buildroot%_mandir/ru/man1/make-figure.1

install -p -m0644 -D doc/README %buildroot%_docdir/%name-%version/README
install -p -m0644 -D doc/README.RUS %buildroot%_docdir/%name-%version/README.RUS
cp -Rpv doc/examples %buildroot%_docdir/%name-%version/

%files
%_bindir/extract-psfrags
%_bindir/make-figure
%_bindir/make-raster
%_bindir/make-vector
%_man1dir/make-figure.1*
%_mandir/ru/man1/make-figure.1*
%_docdir/%name-%version/README*
%_docdir/%name-%version/examples/bgvalue.svg
%_docdir/%name-%version/examples/bgvalue.tex.in
%_docdir/%name-%version/examples/gatescompare.tex.in
%_docdir/%name-%version/examples/gates.orig.ht.png
%_docdir/%name-%version/examples/gates.adapt.ht.png
%_docdir/%name-%version/examples/definitions.tex
%_docdir/%name-%version/examples/main-test.tex

%files plot
%_bindir/make-plot
%_docdir/%name-%version/examples/autotype.tex.in
%_docdir/%name-%version/examples/gradfloor.m
%_docdir/%name-%version/examples/gradient.m
%_docdir/%name-%version/examples/gradient.png
%_docdir/%name-%version/examples/grad+scr.m
%_docdir/%name-%version/examples/screenfunc.m
%_docdir/%name-%version/examples/screenfunc.png
%_docdir/%name-%version/examples/plot-test.tex

%changelog
* Fri Nov 18 2011 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt2
- Do not require octave-signal.

* Mon Apr 18 2011 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt1
- Use Inkscape LaTeX export feature for SVG figures.
- Fix Octave-Forge requires.

* Fri Feb 05 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt6
- Add missing shell functions (shell-error and shell-args).

* Fri Feb 05 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt5
- Fix missing 'overpic' package reference in the main expample.

* Thu Feb 04 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt4
- Remove ps-subset-latin utility.
- Process command line options.
- Use -c and -e to set LaTeX command or environment.
- Support for additional arguments for LaTeX command.

* Fri Jan 29 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt3
- Output files to the current working directory.
- Use make-* stuff in the figure directory.
- Ps-subset-latin utility to fix Cairo font subset.

* Thu Jul 02 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt2
- Place the package to the Publishing category.
- Add new examples.

* Wed Jul 01 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt1
- Initial release.
