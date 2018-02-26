# FIXME on x86_64
#warning: Installed (but unpackaged) file(s) found:
#    /usr/lib/libclip-codb.so
#    /usr/lib/libclip.so
#    /usr/lib64/clip/cliprc/.notrm
			

%define FCLIPDIR %_libdir/clip
%define VCLIPDIR %_localstatedir/clip

Name: clip
Version: 1.2.0cvs
Release: alt3.qa3

Summary: XBASE/Clipper compatible program compiler
Summary(ru_RU.KOI8-R): Совместимый с XBASE/Clipper компилятор программ

License: GPL
Group: Development/Other
Url: http://www.itk.ru

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar.bz2
#Source10: %name-%version-2005-02-03.tar.bz2
#Patch: %name-%version.patch
Patch1: clip-1.2.0-alt-io.patch

%add_findreq_skiplist %FCLIPDIR/bin/tconv
#set_verify_elf_method textrel=relaxed
%add_findprov_lib_path %FCLIPDIR/lib

# manually removed: libclip-devel libclip-gtk libclip-gtk2 wget
# Automatically added by buildreq on Wed May 24 2006
BuildRequires: cvs flex imake libgpm-devel libncurses-devel libreadline-devel libXmu-devel openssh-clients wget xorg-cf-files zlib-devel libpth-devel

Requires: lib%name-devel = %version-%release

%description
This package includes the clip compiler and supplimentary libraries

%description -l ru_RU.KOI8-R
Данный пакет содержит компилятор clip и необходимые библиотеки

###################################################################################
%package -n lib%name
Summary: XBASE/Clipper compatible program compiler - runtime library
Summary(ru_RU.KOI8-R): Совместимый с XBASE/Clipper компилятор программ -- библиотеки времени выполнения
Group: Development/Other

%description -n lib%name
This package provides runtime shared libraries for CLIP package

%description -n lib%name -l ru_RU.KOI8-R
Данный пакет предоставляет разделяемые библиотеки времени выполнения для CLIP

###################################################################################
%package -n lib%name-devel
Summary: XBASE/Clipper compatible program compiler - headers
Summary(ru_RU.KOI8-R): Совместимый с XBASE/Clipper компилятор программ -- заголовочные файлы
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package provides headers files for CLIP package

%description -n lib%name -l ru_RU.KOI8-R
Данный пакет предоставляет заголовочные файлы для CLIP

%prep
%setup -q
#%patch
%patch1 -p1

%build
export OPTFLAGS="%optflags_shared"
CLIPROOT=%_libdir/clip BINDIR=%_bindir ./configure -s -stack || exit 1
export CLIPROOT=%buildroot%_libdir/clip
export CLIP_LOCALE_ROOT=`pwd`
# TODO: fix SMP build
%make_build || %make

%install
%makeinstall_std BINDIR=%_bindir CLIPROOT=%_libdir/clip
(cd doc ; make install DOCDIR=%buildroot%_docdir/%name-%version)
#%__mkdir -p %buildroot%FCLIPDIR
#%__cp -rf locale.pot %buildroot%FCLIPDIR/

echo "-v0
-O
-r
-l" > %buildroot%FCLIPDIR/cliprc/clipflags

# fix broken installer in source
#mkdir -p %buildroot%_docdir
#mv %buildroot%FCLIPDIR/doc %buildroot%_docdir/%name-%version
rm -f %buildroot%_libdir/libclip*
#ln -s %FCLIPDIR/clip/libclip.so %buildroot%_libdir/

# move locale from read only usr dir to /var/lib
mkdir -p %buildroot%VCLIPDIR
mv %buildroot%FCLIPDIR/locale* %buildroot%VCLIPDIR
ln -s %VCLIPDIR/locale.pot %buildroot%FCLIPDIR/
ln -s %VCLIPDIR/locale.po %buildroot%FCLIPDIR/
ln -s %VCLIPDIR/locale.mo %buildroot%FCLIPDIR/
mv %buildroot%FCLIPDIR/etc %buildroot%VCLIPDIR
ln -s %VCLIPDIR/etc %buildroot%FCLIPDIR/

mkdir -p %buildroot%_sysconfdir/ld.so.conf.d
echo "%FCLIPDIR/lib" >%buildroot%_sysconfdir/ld.so.conf.d/%name.conf
rm -f %buildroot%_bindir/*

# remove unneeded broken symlink
rm -f %buildroot%_libdir/libcodb-query.so
rm -f %buildroot%_libdir/libcodb-codb.so
# don't pack static
rm -f %buildroot%_libdir/*.a
rm -f %buildroot%FCLIPDIR/lib/*.a

# FIXME: _libdir using
rm -f %buildroot/usr/lib/libcodb-query.so
rm -f %buildroot/usr/lib/libcodb-codb.so
rm -f %buildroot/usr/lib/*.a

%pre -n lib%name
/usr/sbin/groupadd -r -f %name || :

%triggerpostun -- %name <= 1.1.10-alt2
subst "s,%FCLIPDIR/lib,," /etc/ld.so.conf

%files
#%_bindir/*
%FCLIPDIR/bin/

%files -n lib%name
#%_docdir/%name-%version
%dir %FCLIPDIR
%dir %FCLIPDIR/lib
%_sysconfdir/ld.so.conf.d/%name.conf
%FCLIPDIR/lib/lib*.so
#%_libdir/libcodb-query.so

%FCLIPDIR/locale.pot
%FCLIPDIR/locale.po
%FCLIPDIR/locale.mo
%dir %VCLIPDIR/locale.pot
#%%VCLIPDIR/locale.pot/*
%dir %VCLIPDIR/locale.po
%VCLIPDIR/locale.po/*
%dir %VCLIPDIR/locale.mo
%VCLIPDIR/locale.mo/*

%dir %FCLIPDIR/cliprc
%config %FCLIPDIR/cliprc/*
#%config %FCLIPDIR/cliprc/.notrm
%FCLIPDIR/charsets
%dir %FCLIPDIR/etc
#%config %FCLIPDIR/etc/*
#%attr (0664, root, clip) %config %VCLIPDIR/etc/*
#%attr (0755, root, clip) %dir %VCLIPDIR/etc/terminfo
%VCLIPDIR/etc
%FCLIPDIR/keymaps
%FCLIPDIR/lang
%FCLIPDIR/term


%files -n lib%name-devel
%FCLIPDIR/include/
#%_docdir/%name-%version/rus/

#%files -n libclip
#%FCLIPDIR/lib/*.a


%changelog
* Wed Sep 28 2011 Andrey Cherepanov <cas@altlinux.org> 1.2.0cvs-alt3.qa3
- Remove wrong directory permissions

* Tue May 03 2011 Andrey Cherepanov <cas@altlinux.org> 1.2.0cvs-alt3.qa2
- Rebuild for set-versioning

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.0cvs-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libclip
  * postun_ldconfig for libclip
  * postclean-05-filetriggers for spec file

* Sat Feb 21 2009 Vitaly Lipatov <lav@altlinux.ru> 1.2.0cvs-alt3
- fix for build on non i386/x86_64 archs (thanks, Sergey Bolshakov)

* Wed Jan 16 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.0cvs-alt2
- update from CVS 2008-01-16

* Tue Jul 31 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.0cvs-alt1
- new version (from CVS 2007-07-31)

* Sat Nov 18 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt0.1
- new version
- enable optimisation, stack checking

* Wed May 24 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.16-alt0.1
- new version, remove unpacked binary
- fix dl linking

* Sun Dec 18 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1.15-alt0.1
- new version

* Thu Aug 18 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1.14-alt3
- remove binaries from /usr/bin (bug #7697)

* Sun Mar 20 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1.14-alt2
- split doc in doc package

* Sun Mar 06 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1.14-alt1
- new version

* Thu Feb 03 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1.13-alt2
- last patch (03.02.2005)

* Sun Dec 19 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.13-alt1
- new version
- add english docs package

* Mon Dec 06 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.12-alt1
- new version + last patches (07.12.2004)

* Sat Sep 18 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.11-alt1
- new version
- remove libclip-devel dependences (bug #5229)

* Mon Jul 19 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.10-alt2
- apply last patches (19.07.04)

* Mon Jun 21 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.10-alt1
- apply last patches (21.06.04)
- use a macro for ldconfig

* Wed May 26 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.10-alt0.1
- new version

* Tue Apr 06 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.9-alt0.2
- release to Sisyphus

* Fri Feb 27 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.9-alt0.1
- new version
- split in to different packages

* Fri Feb 20 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.8-alt0.1
- first build for Sisyphus
