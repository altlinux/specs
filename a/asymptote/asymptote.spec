Name: asymptote
Version: 2.39
Release: alt1

Summary: Descriptive vector graphics language

Group: Sciences/Other
License: GPL
Url: http://asymptote.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%name-%version.src.tar
Patch: asymptote-1.91-alt-DSO.patch
Patch1: asymptote-1.91-alt-glibc-2.16.patch
Patch2: asymptote-2.28-alt-gsl1.16.patch

# manually removed: libsubversion-auth-gnome-keyring libsubversion-auth-kwallet subversion tetex-core
# Automatically added by buildreq on Sat Feb 20 2010
BuildRequires: flex gcc-c++ libGL-devel libfftw3-devel libfreeglut-devel libgsl-devel libncurses-devel libreadline-devel zlib-devel

BuildRequires: libgc-devel >= 7.4.2

BuildPreReq: texlive-latex-recommended ghostscript-utils /proc rpm-build-texmf
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
Asymptote is a powerful descriptive vector graphics language for technical
drawings, inspired by MetaPost but with an improved C++-like syntax.
Asymptote provides for figures the same high-quality level of typesetting
that LaTeX does for scientific text.

%package doc
Summary: Documentation and examples for %name
Group: Documentation

%description doc
Documentation and examples for %name.

%prep
%setup
#patch0 -p2
#patch1 -p2
#patch2 -p2
# some incompatibilities?
%__subst "s|@printindex cp||g" doc/%name.texi
gzip ChangeLog

# sure we do not using internal libgc
rm -fv *.tar.gz

%build
%configure --with-docdir=%_docdir/%name-doc-%version \
	--with-latex=%_texmfmain/tex/latex \
	--with-context=%_texmfmain/tex/context/third \
	--enable-gc=system \
	--disable-gsl
%make_build

%install
%makeinstall_std

%files
%doc BUGS ChangeLog.gz LICENSE README ReleaseNotes TODO
%_bindir/asy
%_bindir/xasy
%_datadir/%name/
%_texmfmain/tex/latex/%name/
%_texmfmain/tex/context/third/%name/
%_man1dir/*.1*

%files doc
%_docdir/%name-doc-%version/
%_infodir/*.info*
%_infodir/%name/*.info*

%changelog
* Sat Jan 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2.39-alt1
- new version 2.39 (with rpmrb script)

* Tue Jul 26 2016 Vitaly Lipatov <lav@altlinux.ru> 2.38-alt1
- new version 2.38 (with rpmrb script)

* Thu Feb 25 2016 Vitaly Lipatov <lav@altlinux.ru> 2.36-alt2
- build with system libgc

* Wed Feb 24 2016 Vitaly Lipatov <lav@altlinux.ru> 2.36-alt1
- new version 2.36 (with rpmrb script)
- build without libgsl support

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 2.35-alt1.1
- NMU: added BR: texinfo

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 2.35-alt1
- new version 2.35 (with rpmrb script)

* Tue Sep 02 2014 Vitaly Lipatov <lav@altlinux.ru> 2.32-alt1
- new version 2.32 (with rpmrb script)

* Sat Jul 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.28-alt1.1
- Rebuilt with new gsl

* Tue Jun 03 2014 Vitaly Lipatov <lav@altlinux.ru> 2.28-alt1
- new version 2.28 (with rpmrb script)

* Tue Aug 27 2013 Vitaly Lipatov <lav@altlinux.ru> 2.24-alt1
- new version 2.24 (with rpmrb script)

* Sat Aug 03 2013 Vitaly Lipatov <lav@altlinux.ru> 2.23-alt1
- new version 2.23 (with rpmrb script)

* Wed Nov 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.91-alt1.3
- Fixed build with glibc 2.16

* Thu Jun 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.91-alt1.2
- Fixed build

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.91-alt1.1
- Rebuild with Python-2.7

* Fri Feb 19 2010 Vitaly Lipatov <lav@altlinux.ru> 1.91-alt1
- new version 1.91 (with rpmrb script)

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.43-alt1.1
- Rebuilt with python 2.6

* Mon Jul 21 2008 Vitaly Lipatov <lav@altlinux.ru> 1.43-alt1
- new version 1.43 (with rpmrb script)

* Thu Jan 17 2008 Vitaly Lipatov <lav@altlinux.ru> 1.40-alt1
- initial build for ALT Linux Sisyphus
