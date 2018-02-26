Name: asymptote
Version: 1.91
Release: alt1.2

Summary: Descriptive vector graphics language

Group: Sciences/Other
License: GPL
Url: http://asymptote.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%name-%version.src.tar
Patch: asymptote-1.91-alt-DSO.patch

# manually removed: libsubversion-auth-gnome-keyring libsubversion-auth-kwallet subversion tetex-core
# Automatically added by buildreq on Sat Feb 20 2010
BuildRequires: flex gcc-c++ libGL-devel libfftw3-devel libfreeglut-devel libgc-devel libgsl-devel libncurses-devel libreadline-devel zlib-devel

BuildPreReq: texlive-latex-recommended ghostscript-utils /proc rpm-build-texmf

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
%patch0 -p2
# some incompatibilities?
%__subst "s|@printindex cp||g" doc/%name.texi
gzip ChangeLog

%build
%configure --with-docdir=%_docdir/%name-doc-%version \
	--with-latex=%_texmfmain/tex/latex \
	--with-context=%_texmfmain/tex/context/third
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
