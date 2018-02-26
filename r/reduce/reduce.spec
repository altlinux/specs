%ifarch %ix86
%define bits 32
%endif
%ifarch x86_64
%define bits 64
%endif
%define builddir %_arch-alt-linux-gnu-m%bits

Name: reduce
Version: 20120302
Release: alt1
Summary: REDUCE algebra system, Open Source release
License: BSD / GPL / LGPL
Group: Sciences/Mathematics
Url: http://reduce-algebra.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# fragment from .git/config :
#[svn-remote "svn"]
#  url = https://reduce-algebra.svn.sourceforge.net/svnroot/reduce-algebra/trunk
#  fetch = :refs/remotes/git-svn
Source: reduce-source-%version.tar.bz2
Source1: reduce.desktop

PreReq: fontconfig >= 2.4.2
Requires: gnuplot url_handler
Requires: fonts-ttf-%name = %version-%release
Requires: fonts-type1-%name = %version-%release

Requires: %name-doc = %version-%release

BuildRequires(pre): rpm-build-compat rpm-build-fonts /proc
BuildPreReq: texlive-latex-recommended
BuildPreReq: ImageMagick-tools libXrandr-devel libICE-devel
BuildPreReq: gcc-c++ gnuplot libGL-devel libGLU-devel libXcursor-devel
BuildPreReq: libXft-devel libjpeg-devel libpng-devel libtiff-devel
BuildPreReq: libXext-devel libX11-devel libncurses-devel
BuildPreReq: libtinfo-devel ghostscript-utils libwxGTK2.9-devel

%description
This is the REDUCE - symbolic mathematics system. REDUCE has two modes of
operation: the algebraic mode, which deals with polynomials and mathematical
functions in a simple procedural syntax, and the symbolic mode, which allows
Lisp-like syntax and operations.

REDUCE is a system for carrying out algebraic operations accurately, no
matter how complicated the expressions become. It can manipulate polynomials
in a variety of forms, both expanding and factoring them, and extract
various parts of them as required. REDUCE can also do differentiation and
integration. It have many options that are available for varying
computational procedures, output forms, number systems used, and so on.

REDUCE is designed to be an interactive system, so that the user can input
an algebraic expression and see its value before moving on to the next
calculation.  For those systems that do not support interactive use, or
for those calculations, especially long ones, for which a standard script
can be defined, REDUCE can also be used in batch mode. In this case,
a sequence of commands can be given to REDUCE and results obtained
without any user interaction during the computation.

%package doc
Summary: Documentation for REDUCE algebra system
Group: Documentation
BuildArch: noarch

%description doc
Documentation for REDUCE algebra system.

%package -n fonts-ttf-%name
Summary: TrueType fonts for REDUCE algebra system
Group: System/Fonts/True type
BuildArch: noarch

%description -n fonts-ttf-%name
TrueType fonts for REDUCE algebra system.

%package -n fonts-type1-%name
Summary: Type1 fonts for REDUCE algebra system
Group: System/Fonts/Type1
BuildArch: noarch

%description -n fonts-type1-%name
Type1 fonts for REDUCE algebra system.

%prep
%setup

%build
export TARGET=%_arch
export BITS=%bits
export CXXFLAGS="-g -DHAVE_LIBXFT"
export TOPDIR=$PWD
#autoreconf
alias strip=echo
./autogen.sh
%configure \
	--prefix=/ \
	--bindir=%_libexecdir/%name \
	--enable-release \
	--enable-threadsafe \
	--with-csl \
	--with-opengl \
	--with-xft \
	--with-xshm \
	--with-m%bits
sed -i "s|\(%builddir\)/lib|\1/fox/src|g" \
	cslbuild/%builddir/csl/Makefile
sed -i "s|\(%builddir\)/src|\1/fox/src|g" \
	cslbuild/%builddir/csl/Makefile
%make_build all DESTDIR=%buildroot%_libexecdir/%name

%install
export TOPDIR=$PWD
pushd cslbuild/%builddir
sed -i 's|#\(INSTALL_PROGRAM_ENV.*\)|\1|' csl/Makefile
%makeinstall_std -C fox
%makeinstall_std -C csl
popd

install -d %buildroot%_bindir
install -d %buildroot%_libexecdir/%name
install -d %buildroot%_docdir/%name/buglist
install -d %buildroot%_desktopdir

pushd cslbuild/%builddir/csl
for i in bootstrapreduce fontdemo foxdemo fwindemo makeheaders \
	objtype showmathdemo termdemo dyndemo dynmodule.so
do
	install -m755 $i %buildroot%_libexecdir/%name
done

convert reduce.doc/redlogo.gif reduce.doc/redlogo.png
#rm -f csl/reduce.doc/redlogo.gif
sed -i -e 's/redlogo\.gif/redlogo.png/g' reduce.doc/*.html

cp -fR reduce.doc %buildroot%_libexecdir/%name
install -m644 bootstrapreduce.img %buildroot%_libexecdir/%name
popd
sed -e 's/VERTAG/%version/g' < %SOURCE1 > %buildroot%_desktopdir/reduce.desktop

cat <<EOF >%buildroot%_bindir/reduce
#!/bin/bash

ulimit -Ss unlimited

%_libexecdir/%name/%name "\$@"
EOF
chmod +x %buildroot%_bindir/reduce

# packages

cp -fR packages %buildroot%_libexecdir/%name/

# fonts

#pushd cslbuild/%builddir/csl/reduce.fonts
pushd csl/cslbase/fonts
%ttf_fonts_install %name
mv reduce.files ttf-reduce.files
for i in ex mi r sy; do
	ln -s pfmfiles/cm${i}10.pfm .
	pf2afm cm${i}10
done
%type1_fonts_install %name
mv *.files ../../../
popd

# docs

install -p -m644 buglist/* %buildroot%_docdir/%name/buglist
pushd doc/help
./mkhelp
install -m644 redhelp.dvi %buildroot%_docdir/%name
popd
pushd doc/util
./mkman2
./mkpdf.bat
install -m644 r38.dvi r38.pdf %buildroot%_docdir/%name
popd

sed -i -e 's/^Encoding.*$//' %buildroot%_desktopdir/reduce.desktop

pushd %buildroot%_libexecdir/%name
rm -f fox-config install reswrap
popd

%post
%_bindir/fc-cache %_ttffontsdir/%name
%_bindir/fc-cache %_type1fontsdir/%name

%postun
%postun_fonts

%files
%doc BUGS README
%_bindir/*
%_libexecdir/%name
%_desktopdir/%name.desktop

%files doc
%_docdir/%name

%files -n fonts-ttf-%name -f ttf-%name.files

%files -n fonts-type1-%name -f %name.files

%changelog
* Fri Mar 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20120302-alt1
- New snapshot

* Sat Dec 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20111215-alt1
- New snapshot

* Fri May 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20110512-alt1
- New snapshot

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20101119-alt3
- Rebuilt for debuginfo

* Tue Feb 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20101119-alt2
- Avoid including all files in %_libexecdir

* Sat Nov 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20101119-alt1
- New snapshot

* Tue Aug 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100714-alt2
- Fixed for checkbashisms

* Mon Jul 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100714-alt1
- New snapshot

* Mon Dec 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20091218-alt1
- New snapshot
- Rebuilt with texlive instead of tetex

* Mon May 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090504-alt2
- Rebuild with automake 1.11

* Tue May 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090504-alt1
- New trunk
- Set url_handler.sh as default browser
- Fixed desktop category

* Mon May 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090425-alt2.M41.1
- Port for Branch 4.1

* Sun May 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090425-alt2.M50.1
- Port for Branch 5.0

* Sun May 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090425-alt3
- Set default browser for help: xbrowser

* Wed Apr 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090425-alt2
- Fix help menu elements & font demo
- Add desktop file
- Replace GIF logo by PNG logo

* Sat Apr 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090425-alt1
- Initial build for Sisyphus

