%define FCLIPDIR %_libdir/clip
%define VCLIPDIR %_localstatedir/clip

Name: clip-prg
Version: 1.2.0cvs
Release: alt3.qa2

Summary: XBASE/Clipper compatible program compiler
Summary(ru_RU.KOI8-R): Дополнительные программы для совместимого с XBASE/Clipper компилятора программ

License: GPL
Group: Development/Other
Url: http://www.itk.ru

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar.bz2
#Patch: %name-%version-install.patch

# manually removed: linux-libc-headers
# Automatically added by buildreq on Tue Jul 31 2007
BuildRequires: clip libclip-gtk2 libgpm-devel libpam0-devel libpth-devel

BuildPreReq: clip = %version
Provides: clip-ocmng
Obsoletes: clip-ocmng

%description
This package includes some programs for clip compiler

%description -l ru_RU.KOI8-R
Данный пакет содержит дополнительные программы для компилятора CLIP.

%prep
%setup -q
subst "s| clip | \$(CLIP) |" cobra_serv/Makefile
subst "s/^\$CLIPROOT/#\$CLIPROOT/" Install.sh
#%patch

%build
%__mkdir -p %buildroot%FCLIPDIR/locale.{pot,po,mo}
%__rm -rf ca_dbu
export CLIP_LOCALE_ROOT=`pwd`
make CLIPROOT=%FCLIPDIR

%install
%__mkdir -p %buildroot%FCLIPDIR/{bin,etc,include}
make install DESTDIR=%buildroot CLIPROOT=%FCLIPDIR

# fix broken installer in source
#mkdir -p %buildroot%_docdir
#mv %buildroot%FCLIPDIR/doc %buildroot%_docdir/%name-%version

# move locale from read only usr dir to /var/lib
mkdir -p %buildroot%VCLIPDIR
mv %buildroot%FCLIPDIR/locale* %buildroot%VCLIPDIR

%files
%FCLIPDIR/bin/*
%FCLIPDIR/cobra
%FCLIPDIR/codb_ab
#%FCLIPDIR/codb_abx
%FCLIPDIR/kamache

%FCLIPDIR/include/*
%FCLIPDIR/etc/.macro
%FCLIPDIR/etc/.templ
#%attr(0664, root, clip) %VCLIPDIR/locale.pot/*
%VCLIPDIR/locale.po/*/*
#%exclude %VCLIPDIR/locale.po/ru_RU.KOI8-R/codb.po
#%attr(0664, root, clip) %VCLIPDIR/locale.mo/*

%changelog
* Wed Sep 28 2011 Andrey Cherepanov <cas@altlinux.org> 1.2.0cvs-alt3.qa2
- Remove wrong directory permissions

* Tue May 03 2011 Andrey Cherepanov <cas@altlinux.org> 1.2.0cvs-alt3.qa1
- Rebuild for set-versioning

* Wed Jul 28 2010 Andrey Cherepanov <cas@altlinux.org> 1.2.0cvs-alt3
- fix version in repository (closes: #23138)

* Wed Jan 16 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.0cvs-alt2
- replace Conflicts clip-ocmng with Obsoletes

* Tue Aug 07 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.0cvs-alt1.1
- rebuild on x86_64

* Mon Jul 30 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.0cvs-alt1
- new version from CVS 2007-07-31

* Sat Nov 18 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt0.1
- new version

* Mon Sep 11 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.16-alt0.1
- new version

* Sun Dec 18 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1.15-alt0.1
- new version

* Thu Aug 18 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1.14-alt2
- fix build with clip missed in /usr/bin

* Mon Mar 07 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1.14-alt1
- new version

* Thu Feb 03 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1.13-alt2
- last patch (03.02.2005)

* Sat Dec 25 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.13-alt1.1
- change libpam-devel to libpam2-devel in buildreq

* Sun Dec 19 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.13-alt1
- new version

* Mon Dec 06 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.12-alt1
- new version + last patches (07.12.2004)

* Sat Sep 18 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.11-alt0.1
- new version

* Tue Jul 20 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.10-alt2
- apply last patches (19.07.04)

* Tue Jun 22 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.10-alt1
- new version

* Tue Apr 06 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.9-alt0.1
- new version

* Fri Feb 20 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.8-alt0.1
- first build for Sisyphus
