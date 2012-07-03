# -*- rpm-spec -*-
# $Id: smalltalk,v 1.13 2002/10/05 12:54:06 lioka Exp $

%def_disable jit
%def_disable preemption
%def_disable checking
%def_disable static

Name: smalltalk
Version: 3.2.4
Release: alt1.git.263.ga839464

Summary: Smalltalk free language implementation
License: GPL
Group: Development/Other
Url: http://smalltalk.gnu.org/

Packager: Ildar Mulyukov <ildar@altlinux.ru>

#git://git.sv.gnu.org/smalltalk.git
Source: %name-%version.tar
#Source: ftp://ftp.gnu.org/gnu/smalltalk/%name-%version.tar
#Source.gz
Source1: VisualGST.desktop
Source2: http://upload.wikimedia.org/wikipedia/commons/0/08/GNU_Smalltalk_logo.svg
Provides: VisualGST
Obsoletes: VisualGST

%if_enabled jit
BuildPreReq: lightning
%endif

# Automatically added by buildreq on Wed Feb 22 2012 (-bi)
# optimized out: cpio elfutils emacs-base emacs-common fontconfig fontconfig-devel glib2-devel libGL-devel libGLU-devel libICE-devel libSDL-devel libX11-devel libX11-locales libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libncurses-devel libpango-devel libtinfo-devel pkg-config python-base tcl-devel termutils tzdata xorg-xproto-devel
BuildRequires: chrpath emacs-nox flex libSDL_image-devel libSDL_mixer-devel libSDL_sound-devel libSDL_ttf-devel libSM-devel libexpat-devel libffi-devel libfreeglut-devel libgdbm-devel libgmp-devel libgtk+2-devel libltdl7-devel libpq-devel libreadline-devel libsigsegv-devel libsqlite3-devel python-module-distribute tk-devel zip zlib-devel

Requires: %_bindir/ginstall %_bindir/zip

%description
GNU Smalltalk is a Free (or Open Source) implementation that closely
follows the Smalltalk-80 language as described in the book Smalltalk-80:
the Language and its Implementation by Adele Goldberg and David
Robson. GNUSmalltalk runs on most versions of Unix or Unix like
systems (GNU/Linux, FreeBSD, etc...).
There is even a version for commercial operating systems like MS-NT.

%if_enabled static

%package static
Summary: static libraries for %name
Group: Development/Other
Requires: %name = %version-%release

%description static
static libraries for %name

%endif

%package -n emacs-mode-%name
Summary: SmallTalk mode for GNU Emacs
Group: Editors
BuildArch: noarch
Requires: %name = %version-%release

%description -n emacs-mode-%name
SmallTalk mode for GNU Emacs

%package -n emacs-mode-%name-el
Summary: The Emacs Lisp sources for bytecode included in emacs-mode-%name
Group: Editors
BuildArch: noarch
Requires: emacs-mode-%name = %version-%release

%description -n emacs-mode-%name-el
The Emacs Lisp sources for bytecode included in emacs-mode-%name

%package doc
Summary: GNU Smalltalk html doc
Group: Development/Other
BuildArch: noarch

%description doc
GNU Smalltalk html doc

%prep
%setup

%build
%autoreconf
%configure --with-tcl=%_libdir --with-tk=%_libdir \
	--with-imagedir=/var/lib/smalltalk \
	%{subst_enable jit} \
	%{subst_enable preemption} \
	%{subst_enable checking} \
	--enable-disassembler \
	--with-system-libffi \
	--with-system-libsigsegv \

rm -rf libffi sigsegv
%make_build lispstartdir=%_sysconfdir/emacs/site-start.d
make -C doc html
bzip2 ChangeLog ||:

%check
%make_build -k check

%install
mkdir -p \
	%buildroot%_desktopdir \
	%buildroot%_iconsdir/hicolor/scalable/apps
%make install DESTDIR=%buildroot lispstartdir=%_sysconfdir/emacs/site-start.d
install -p %SOURCE1 %buildroot%_desktopdir
install -p %SOURCE2 %buildroot%_iconsdir/hicolor/scalable/apps

#FIXME: remove RPATH while building
find %buildroot%_libdir -name \*.so\* -type f -print
find %buildroot -type f \( -path %buildroot%_libdir/\*.so\* -or -path %buildroot%_bindir/\* \) -print -exec sh -c \
	"chrpath -l {} | egrep RPATH=%_libdir$ && \
		chrpath -d {}
	" \;

%find_lang %name
%add_findreq_skiplist %_datadir/smalltalk/examples/shell

%files -f %name.lang
%_bindir/*
%_includedir/gst*.h
%_libdir/libgst*.so*
%_pkgconfigdir/gnu-smalltalk.pc
%_libdir/%name
%_libexecdir/%name
%exclude %_libdir/%name/*.a
%exclude %_libdir/%name/*.la
%_datadir/aclocal/gst*
%_desktopdir/*.desktop
%_iconsdir/hicolor/scalable/apps/GNU_Smalltalk_logo.svg
%_infodir/*.info*
%_man1dir/gst*
%_datadir/%name
/var/lib/smalltalk
%doc AUTHORS NEWS README THANKS TODO ChangeLog*

%files -n emacs-mode-%name
%_emacslispdir/*.elc
%_sysconfdir/emacs/site-start.d/*.elc

%files -n emacs-mode-%name-el
%_emacslispdir/*.el
%_sysconfdir/emacs/site-start.d/*.el

%if_enabled static
%files static
%_libdir/%name/*.a
%_libdir/libgst.a
%endif

%files doc
%doc doc/html/*

%changelog
* Wed Feb 22 2012 Ildar Mulyukov <ildar@altlinux.ru> 3.2.4-alt1.git.263.ga839464
- new version
- fix RPATHs manually

* Wed Aug 18 2010 Ildar Mulyukov <ildar@altlinux.ru> 3.2.2-alt1.git.7.g39420d7
- new version
- include VisualGST now
- disable checking temporary due to upstream problems

* Wed Jul 22 2009 Ildar Mulyukov <ildar@altlinux.ru> 3.1_115_g2762e1d-alt1
- new version
- Closes: #19896
- disable static by default
- some packages made noarch

* Thu May 22 2008 Ildar Mulyukov <ildar@altlinux.ru> 3.0.3-alt2
- PreReq: install_info removed
- make check only for i586 arch

* Sun May 18 2008 Ildar Mulyukov <ildar@altlinux.ru> 3.0.3-alt1
- new version
- %name-systemffi.patch is now a part of upstream
- new sqlite3 database access library is now built

* Sat May 10 2008 Ildar Mulyukov <ildar@altlinux.ru> 3.0.2-alt1
- 3.0.2
- "systemffi" hack changed to the upstream "--with-system-libffi"

* Mon Dec 31 2007 Ildar Mulyukov <ildar@altlinux.ru> 2.95h-alt2
- some deps fixes for build

* Sat Dec 29 2007 Ildar Mulyukov <ildar@altlinux.ru> 2.95h-alt1
- new upstream version
- patch/dynamic-bins in upstream, so removed
- SMP build
- patch/systemffi updated

* Wed Nov 28 2007 Ildar Mulyukov <ildar@altlinux.ru> 2.95d-alt0.1
- new version after 4 years!
- gear/git build
- html doc package

* Tue Oct 28 2003 Stanislav Ievlev <inger@altlinux.org> 2.1.5-alt1
- 2.1.5
- added subpackages: emacs-mode,static libraries

* Wed Mar 26 2003 Stanislav Ievlev <inger@altlinux.ru> 2.0.11-alt1
- 2.0.11

* Sat Oct  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.95.12-alt3
- rebuilt with tcl 8.4

* Tue Jul 16 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.95.12-alt2
- rebuilt with new tcl layout

* Sat Jun 29 2002 Dmitry V. Levin <ldv@altlinux.org> 1.95.12-alt1
- 1.95.12
- Patched to link with libtinfo.

* Thu Mar 21 2002 Stanislav Ievlev <inger@altlinux.ru> 1.95.9-alt1
- 1.95.9
- Added more directories to packages ;)

* Mon Apr 02 2001 Stanislav Ievlev <inger@altlinux.ru> 1.95.4-alt1
- Cleanup spec. Upgrade to 1.95.4

* Wed Feb 14 2001 AEN <aen@logic.ru>
- %post removed

* Tue Jan 16 2001 AEN <aen@logic.ru>
- RE adaptations

* Sun Nov 19 2000 Daouda Lo <daouda@mandrakesoft.com> 1.8.3-1mdk
- first mandrake rpm.
