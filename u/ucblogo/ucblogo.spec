Name: ucblogo
Version: 6.2.3
Release: alt1
Summary: An interpreter for the Logo programming language
Group: Development/Functional
License: GPLv2+
Source: %name-%version.tar.gz
Source1: logo-mode.tar.gz
Patch: FromUTF8.patch
Patch1: ucblogo-6.2.2-fix-desktop-file.patch
Url: http://www.cs.berkeley.edu/~bh

# Automatically added by buildreq on Tue Nov 23 2021
# optimized out: at-spi2-atk emacs-base emacs-common fontconfig glibc-kernheaders-generic glibc-kernheaders-x86 libat-spi2-core libcairo-gobject libgdk-pixbuf libgpg-error libp11-kit libstdc++-devel libwayland-client libwayland-cursor libwayland-egl libwxBase3.1-devel openssh-clients perl perl-Encode perl-Text-Unidecode perl-Unicode-EastAsianWidth perl-Unicode-Normalize perl-libintl perl-parent python3 python3-base sh4 tex-common texlive texlive-collection-basic texlive-dist
BuildRequires: emacs-nox gcc-c++ libX11-devel libwxGTK3.2-devel makeinfo texi2dvi libncursesw-devel

BuildRequires: autoconf-archive texi2html tex(manfnt.sty)

%description
Berkeley Logo (ucblogo) is an interpreter for the Logo programming
language. Logo is a computer programming language designed for use by
learners, including children. This dialect of Logo features
random-access arrays, variable number of inputs to user-defined
procedures, various error handling improvements, comments and
continuation lines, first-class instruction and expression templates,
and macros.

%package emacs
Summary: Emacs Logo mode
Group: Development/Functional
BuildArch: noarch
Requires: %name = %version-%release

%description emacs
Emacs mode for UCBLogo.

%prep
%setup
%setup -a 1
%patch -p1
%patch1 -p2

# no dot files in directories
sed -i  's|\.logo|dot.logo|g' emacs/dot.*
sed -i 's|/\.logo|/dot.logo|g' emacs/makefile
sed -i 's|\.LOOPS|dot.LOOPS|g' emacs/dot.*
sed -i 's|/\.LOOPS|/dot.LOOPS|g' emacs/makefile

# correct directories /usr/lib -> /usr/share and /usr/local ->  /usr
sed -i 's|/local/lib/logo|/share/logo|g' *.c README.md
sed -i 's|/lib/logo|/share/logo|g' *.c makefile*
sed -i "s|/usr/local/bin/logo|%_bindir/logo|g" docs/ucblogo.texi
sed -i "s|/usr/local/bin/logo|%_bindir/logo|g" README.md
sed -i "s|/usr/local/info|%_datadir/info|g" README.md

%build
%autoreconf
# build WX version
rm -f config.cache
%configure --x-includes=%_includedir --x-libraries=%_libdir --enable-x11 --with-wx-config=/usr/bin/wx-config
%make_build ucblogo
mv ucblogo logo-wx
# build traditional version
make clean
%configure --x-includes=%_includedir --x-libraries=%_libdir --enable-x11 --with-wx-config=no
%make_build
# compile emacs files
%make -C emacs BINDIR=%_bindir EMACSDIR=%_datadir/emacs/site-lisp/logo INFODIR=%_infodir LIBLOC=%_datadir/logo

make html

%install
%makeinstall

install -m0755 logo-wx %buildroot%_bindir
install -D %name.desktop %buildroot%_desktopdir/%name.desktop
install -D ucblogo.png %buildroot%_iconsdir/hicolor/256x256/apps/ucblogo.png

# install emacs files
%make -C emacs install BINDIR=%buildroot%_bindir EMACSDIR=%buildroot%_datadir/emacs/site-lisp/logo
mkdir -p %buildroot%_datadir/emacs/site-lisp/site-start.d
cp -f emacs/dot.emacs %buildroot%_datadir/emacs/site-lisp/site-start.d/logo-mode.el
rm %buildroot%_bindir/install-logo-mode
rm %buildroot%_datadir/emacs/site-lisp/logo/README
rm %buildroot%_datadir/emacs/site-lisp/logo/*.el

%files
%doc docs/*html docs/*.pdf README* plm changes.txt
%_bindir/*
%_datadir/ucblogo
%_infodir/*
%_man1dir/*
%_desktopdir/*
%_iconsdir/*/*/*/*
%_pixmapsdir/*
%exclude %_defaultdocdir/%name

%files emacs
%doc emacs/README
%_datadir/emacs/site-lisp/logo
%_datadir/emacs/site-lisp/site-start.d

%changelog
* Fri Mar 24 2023 Fr. Br. George <george@altlinux.org> 6.2.3-alt1
- Autobuild version bump to 6.2.3

* Wed Sep 21 2022 Anton Midyukov <antohami@altlinux.org> 6.2.2-alt2
- NMU: rebuild with wxGTK3.2
- NMU: fix desktop file (Closes: 43837)

* Wed Jun 15 2022 Fr. Br. George <george@altlinux.org> 6.2.2-alt1
- Autobuild version bump to 6.2.2

* Tue Nov 23 2021 Fr. Br. George <george@altlinux.ru> 6.2.1-alt1
- Autobuild version bump to 6.2.1

* Tue Sep 07 2021 Fr. Br. George <george@altlinux.ru> 6.2-alt1
- Version up
- Desktop file added

* Mon Mar 12 2018 Igor Vlasenko <viy@altlinux.ru> 6.0-alt3.1
- NMU: fixed BR: for texlive 2017

* Mon Jan 25 2016 Fr. Br. George <george@altlinux.ru> 6.0-alt3
- Fix build

* Thu Jan 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0-alt2.qa3
- Fixed build

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 6.0-alt2.qa1
- NMU: rebuilt for debuginfo.

* Fri Nov 05 2010 Fr. Br. George <george@altlinux.ru> 6.0-alt2
- Resurrect build:
- tetex-related patch nd pre/post section removed
- documentation fixes

* Sun Mar 01 2009 Fr. Br. George <george@altlinux.ru> 6.0-alt1
- Initial build from FC

* Sat Nov 22 2008 Gerard Milmeister <gemi@bluewin.ch> - 6.0-2
- re-add emacs logo-mode from previous release as a separate package

* Thu Nov 20 2008 Gerard Milmeister <gemi@bluewin.ch> - 6.0-1
- new release 6.0

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.5-10
- Autorebuild for GCC 4.3

* Thu Feb 22 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.5-9
- add patch for fixing ncurses problem

* Wed Feb 21 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.5-8
- add fix to use cursesw instead of curses

* Wed Feb 21 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.5-7
- replace BR libtermcap-devel by BR ncurses-devel

* Sun Feb 11 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.5-6
- rebuild to use ncurses

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.5-5
- Rebuild for FE6

* Thu Jun 29 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.5-4
- added BR texi2html
- added BR libXt-devel
- added include and libs options for X11 to configure

* Sat Jun  3 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.5-3
- added BuildReq: texinfo-tex
- make owned the directory %_datadir/emacs/site-lisp/site-start.d

* Sun Aug 14 2005 Gerard Milmeister <gemi@bluewin.ch> - 5.5-2
- New Version 5.5

* Mon Mar  7 2005 Gerard Milmeister <gemi@bluewin.ch> - 5.4-1
- New Version 5.4

* Thu Feb 26 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:5.3-0.fdr.2
- Install info files
- Install emacs site-start file

* Sun Oct 26 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:5.3-0.fdr.1
- First Fedora release
