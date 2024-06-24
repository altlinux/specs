Name: emacs
Version: 29.4
Release: alt1

Summary: GNU Emacs text editor
License: GPLv3+
Group: Editors
Url: http://www.gnu.org/software/emacs/

Source: %name-%version-%release.tar

%ifnarch %e2k
%def_enable natcomp
%else
%def_disable natcomp
%endif

BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gmp)
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(jansson)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(libacl)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libselinux)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(tinfo)
BuildRequires: pkgconfig(tree-sitter)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xft)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xpm)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(zlib)

BuildRequires(pre): rpm-macros-alternatives
BuildRequires: texinfo
BuildRequires: libgif-devel
BuildRequires: libXaw3d-devel libXaw-devel
%{?_enable_natcomp:BuildRequires: libgccjit13-devel}

%package athena
Summary: The GNU Emacs text editor for the X Window System (athena)
Group: Editors
Requires(pre): alternatives >= 0.2.0
Requires: emacs-common = %version-%release
Provides: /usr/bin/emacs
Provides: emacs = %version-%release
Provides: emacs-X11 = %version-%release
Provides: emacs-nox = %version-%release
Obsoletes: emacs-nox

%package gtk3
Summary: The GNU Emacs text editor for the X Window System (gtk3)
Group: Editors
Requires(pre): alternatives >= 0.2.0
Requires: emacs-common = %version-%release
Provides: /usr/bin/emacs
Provides: emacs = %version-%release
Provides: emacs-X11 = %version-%release

%package pgtk
Summary: The GNU Emacs text editor for alternative windowing systems.
Group: Editors
Requires(pre): alternatives >= 0.2.0
Requires: emacs-common = %version-%release
Provides: /usr/bin/emacs
Provides: emacs = %version-%release

%package common
Summary: Things needed to run the GNU Emacs text editor
Group: Editors
%{?_enable_natcomp:Requires: %name-el = %version-%release}
Provides: %_libexecdir/emacs
Provides: emacs-cedet = %version-%release
Provides: emacs-gnus = %version-%release
Provides: emacs-speedbar = %version-%release
Conflicts: app-defaults < 0.2.1-alt1
Conflicts: emacs-base-X11 < 0.0.2
Obsoletes: emacs-base-X11 < 0.0.2
AutoReq: yes, nopython

%package el
Summary: The sources for Lisp programs included with GNU Emacs
Group: Development/Other
BuildArch: noarch
Requires: %name-common = %version-%release

%package leim
Summary: GNU Emacs Lisp code for input methods for internationalization
Group: Editors
BuildArch: noarch
Requires: %name-common = %version-%release

%package leim-el
Summary: The Emacs Lisp source code for input methods included in %name-leim
Group: Development/Other
BuildArch: noarch
Requires: %name-leim = %version-%release

%package info
Summary: Info docs for GNU Emacs text editor
Group: Editors
BuildArch: noarch
Requires: %name-common = %version-%release

%package elisp-manual
Summary: Emacs Lisp Manual
Group: Editors
BuildArch: noarch
Requires: %name-common = %version-%release

#{{{
%define desc \
Emacs is an extensible, customizable, self-documenting real-time\
display editor.  Emacs contains special code editing features, an\
extension language (Emacs Lisp), and the capability to read mail, news\
and more without leaving the editor.

%description %desc

%description athena %desc
emacs-athena includes the GNU Emacs text editor program for use with the X
Window System using athena widget set (it provides support for the mouse and
other GUI elements).  It will also run GNU Emacs outside of X.

%description gtk3 %desc
emacs-gtk3 includes the GNU Emacs text editor program for use with the X
Window System using gtk+ toolkit v.3 (it provides support for the mouse and
other GUI elements).  It will also run GNU Emacs outside of X.

%description pgtk %desc
emacs-pgtk is the GNU Emacs text editor program for use primarily
with Wayland windowing system.
If you use exclusively X, do not use this package. There are a
number of respects in which the regular gtk3 variant works better.

%description common %desc
This package includes things you need to run the Emacs editor, so you
need to install this package if you intend to use Emacs.  You also
need to install the actual Emacs program package (emacs-athena,
emacs-gtk3 or emacs-pgtk).

%description el
Emacs-el contains the Emacs Lisp sources for many of the programs
included with the main GNU Emacs text editor package.

You need to install %name-el only if you intend to modify any of the
Emacs packages or see some Lisp examples.

If you need the sources for %name-leim, install %name-leim-el.

%description leim
The Lisp code for input methods for various international scripts for GNU Emacs.

%description leim-el
Emacs-leim-el contains the Emacs Lisp sources for the Emacs Lisp code
for input methods for various international scripts of GNU Emacs.

You need to install %name-leim-el only if you intend to modify any of theses
GNU Emacs packages, see some Lisp examples or for reference for configuring your
localized input methods.

%description info
This package contain full GNU Emacs documentation in Info format except
Emacs Lisp language documentation that contains in %name-elisp-manual
package

%description elisp-manual
This package contain full description of Emacs Lisp language
#}}}

%define _emacs_archlibdir %_libexecdir/emacs/%version/%_host_alias
%define locallisppath %_libdir/emacs/%version/site-lisp:%_datadir/emacs/%version/site-lisp
%ifarch %e2k
# on default -O3 crashes with SIGILL in lucid_event_type_list_p
%global _optlevel 2
%endif

%prep
%setup
sed -ri 's,(\.\./info/[[:alpha:]-]+),\1.info,g' doc/{emacs,misc}/*.texi

%build
autoreconf -i -I m4

%define _configure_script ../configure
%define _configure_mostly --disable-build-details --sharedstatedir=/var \\\
	--without-pop --without-gpm --with-wide-int --with-modules \\\
	--enable-locallisppath=%locallisppath \\\
	%{?_enable_natcomp:--with-native-compilation=aot}

mkdir build-athena && pushd build-athena
%configure %_configure_mostly --without-cairo --without-rsvg \
	--without-dbus --without-gconf --without-gsettings \
	--with-x-toolkit=athena
popd

mkdir build-gtk3 && pushd build-gtk3
%configure %_configure_mostly --with-x-toolkit=gtk3
popd

mkdir build-pgtk && pushd build-pgtk
%configure %_configure_mostly --with-pgtk
popd

%make_build -C build-athena
%make_build -C build-gtk3
%make_build -C build-pgtk

%install
%makeinstall -C build-athena
install -pm0755 build-athena/src/emacs %buildroot%_bindir/%name-athena
install -pm0644 build-athena/src/emacs.pdmp %buildroot%_emacs_archlibdir/%name-athena.pdmp
%if_enabled natcomp
echo build-athena/native-lisp/* |sed 's,build-athena/,%_libdir/%name/%version/,' > athena.ls
%else
touch athena.ls
%endif

install -pm0755 build-gtk3/src/emacs %buildroot%_bindir/%name-gtk3
install -pm0644 build-gtk3/src/emacs.pdmp %buildroot%_emacs_archlibdir/%name-gtk3.pdmp
%if_enabled natcomp
%make_install libdir=%buildroot%_libdir install-eln -C build-gtk3
echo build-gtk3/native-lisp/* |sed 's,build-gtk3/,%_libdir/%name/%version/,' > gtk3.ls
%else
touch gtk3.ls
%endif

install -pm0755 build-pgtk/src/emacs %buildroot%_bindir/%name-pgtk
install -pm0644 build-pgtk/src/emacs.pdmp %buildroot%_emacs_archlibdir/%name-pgtk.pdmp
%if_enabled natcomp
%make_install libdir=%buildroot%_libdir install-eln -C build-pgtk
echo build-pgtk/native-lisp/* |sed 's,build-pgtk/,%_libdir/%name/%version/,' > pgtk.ls
%else
touch pgtk.ls
%endif

# better suited to handle all build variants
install -pm0755 build-pgtk/lib-src/emacsclient %buildroot%_bindir/emacsclient

# remove the installed duplicate emacs binaries
# -- it'll be a link managed by `alternatives':
rm -vf %buildroot%_bindir/emacs
rm -vf %buildroot%_bindir/emacs-%version
rm -vf %buildroot%_emacs_archlibdir/emacs.pdmp

# populate non-default part of locallisppath
cp -av %buildroot%_datadir/emacs/%version/site-lisp \
   %buildroot%_libdir/emacs/%version/site-lisp

# cleanups
sed -i 's,%buildroot,,' %buildroot%_desktopdir/*desktop \
    %buildroot%_libexecdir/systemd/user/emacs.service
mv %buildroot%_bindir/{,g}ctags
mv %buildroot%_man1dir/{,g}ctags.1.gz
rm -vf %buildroot%_infodir/dir

# alternatives
install -pm644 -D .gear/athena.alternatives %buildroot%_altdir/%name-athena
install -pm644 -D .gear/gtk3.alternatives %buildroot%_altdir/%name-gtk3
install -pm644 -D .gear/pgtk.alternatives %buildroot%_altdir/%name-pgtk

# X resources
install -pm0644 -D .gear/xresources %buildroot%_sysconfdir/X11/app-defaults/Emacs

# file lists
find %buildroot%_libexecdir/emacs/%version \
     %buildroot%_datadir/emacs/%version/etc -type d \
    | sed -e 's,^%buildroot,,' -e 's,^,%%dir ,' > common.ls

find %buildroot%_libexecdir/emacs/%version -type f \
    | sed -e 's,^%buildroot,,' -e '/movemail$/ s,^,%%attr(-\,root\,mail) ,' >> common.ls

find %buildroot%_datadir/emacs/%version/etc -type f \
    | sed -e 's,^%buildroot,,' >> common.ls

find %buildroot%_datadir/emacs/%version/lisp -type d \
    | sed -e 's,^%buildroot,%%dir ,' > lispdirs.ls

find %buildroot%_datadir/emacs/%version/lisp -type f -name \*.el -o -name \*.elc \
    | sed -e 's,^%buildroot,,' > elc.ls

find %buildroot%_datadir/emacs/%version/lisp -type f -name \*.el.gz \
    | sed -e 's,^%buildroot,,' > elgz.ls

sed -e '/\/leim/d' < lispdirs.ls >> common.ls
sed -e '/\/leim\//d' < elc.ls >> common.ls

sed -e '/\/leim\//d' < elgz.ls > el.ls

sed -ne '/\/leim/p' < lispdirs.ls > leim.ls
sed -ne '/\/leim\//p' < elc.ls >> leim.ls
sed -ne '/\/leim\//p' < elgz.ls > leim.el.ls

%set_compress_method skip

#---------------------------------------------------------------
%files athena -f athena.ls
%_altdir/%name-athena
%_bindir/%name-athena
%_emacs_archlibdir/%name-athena.pdmp

%files gtk3 -f gtk3.ls
%_altdir/%name-gtk3
%_bindir/%name-gtk3
%_emacs_archlibdir/%name-gtk3.pdmp

%files pgtk -f pgtk.ls
%_altdir/%name-pgtk
%_bindir/%name-pgtk
%_emacs_archlibdir/%name-pgtk.pdmp

%files common -f common.ls
%doc BUGS README
%config(noreplace) %_sysconfdir/X11/app-defaults/*

%_bindir/*
%exclude %_bindir/%name-athena
%exclude %_bindir/%name-gtk3
%exclude %_bindir/%name-pgtk

%dir %_libexecdir/emacs
%exclude %_emacs_archlibdir/*.pdmp

%_libexecdir/systemd/user/emacs.service

%dir %_libdir/emacs/%version
%dir %_libdir/emacs/%version/native-lisp
%_libdir/emacs/%version/site-lisp

%_emacslispdir
%dir %_datadir/emacs/%version
%_datadir/emacs/%version/site-lisp

%_datadir/metainfo/emacs.*.xml
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*
%_man1dir/*.1*

%_includedir/emacs-module.h

%files el -f el.ls

%files leim -f leim.ls

%files leim-el -f leim.el.ls

%files info
%_infodir/*
%exclude %_infodir/eintr*
%exclude %_infodir/elisp*

%files elisp-manual
%_infodir/eintr*
%_infodir/elisp*

%changelog
* Mon Jun 24 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 29.4-alt1
- 29.4 released

* Mon Mar 25 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 29.3-alt1
- 29.3 released

* Wed Jan 24 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 29.2-alt1
- 29.2 released

* Mon Dec 11 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 29.1-alt3
- utilize emacsclient from pgtk build (closes: 48754)

* Mon Sep 25 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 29.1-alt2
- add arch-dependant site-lisp directory

* Tue Sep 19 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 29.1-alt1
- 29.1 released

* Mon Aug 14 2023 Ivan A. Melnikov <iv@altlinux.org> 28.2-alt2.2
- add missing BR on rpm-macros-alternatives
  (fixes FTBFS on loongarch64)

* Tue Oct 11 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 28.2-alt2.1
- added patch for Elbrus

* Tue Sep 27 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 28.2-alt2
- site-start.el relocated to now optional emacs-base

* Mon Sep 12 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 28.2-alt1
- 28.2 released

* Wed Apr 06 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 28.1-alt1
- 28.1 released

* Thu Mar 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 28.0.92-alt1
- 28.0.92 released

* Mon Dec 06 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 27.2-alt1
- 27.2 released

* Mon Dec 06 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 26.3-alt14
- backported fix for FTBFS with glibc >= 2.34

* Thu Nov 12 2020 Igor Vlasenko <viy@altlinux.ru> 26.3-alt13
- NMU: added Requires: on emacs-base-X11 (closes: #39029)

* Sun Nov 24 2019 Terechkov Evgenii <evg@altlinux.org> 26.3-alt12
- Build without python(2)
- Update License: tag

* Tue Sep  3 2019 Terechkov Evgenii <evg@altlinux.org> 26.3-alt11
- 26.3
- Fix for ALT#37107 (recode emacs21-rus-win-keyboard-alt2.el to utf8 and fix quoting)

* Wed Jul  3 2019 Terechkov Evgenii <evg@altlinux.org> 26.2.90-alt10
- 26.2.90

* Mon Jun  3 2019 Terechkov Evgenii <evg@altlinux.org> 26.2-alt9
- Add --with-modules configure option (ALT#36839)

* Mon Jun  3 2019 Terechkov Evgenii <evg@altlinux.org> 26.2-alt8
- Add devel subpackage with emacs-module.h (ALT#36839)

* Sun Apr 14 2019 Terechkov Evgenii <evg@altlinux.org> 26.2-alt7
- 26.2

* Fri Apr 12 2019 Terechkov Evgenii <evg@altlinux.org> 26.1.92-alt6
- Rebuild with new libgif (task 216696)

* Sat Feb 23 2019 Terechkov Evgenii <evg@altlinux.org> 26.1.92-alt5
- 26.1.92

* Fri Feb 15 2019 Terechkov Evgenii <evg@altlinux.org> 26.1.91-alt4
- Fix FTBFS (#36101)

* Wed Jan 16 2019 Terechkov Evgenii <evg@altlinux.org> 26.1.91-alt3
- Build emacs26-X11-athena and emacs26-X11-motif with librsvg (ALT#35910)

* Mon Jan 14 2019 Terechkov Evgenii <evg@altlinux.org> 26.1.91-alt2
- Bump up alt1->alt2 to bypass installation check (for gnus)

* Sun Jan 13 2019 Terechkov Evgenii <evg@altlinux.org> 26.1.91-alt1
- 26.1.91

* Thu Nov 22 2018 Terechkov Evgenii <evg@altlinux.org> 26.1.90-alt1
- Drop Source9 and use native appdata file

* Wed Nov 21 2018 Terechkov Evgenii <evg@altlinux.org> 26.1.90-alt1
- 26.1.90

* Mon Jun 11 2018 Terechkov Evgenii <evg@altlinux.org> 26.1-alt1
- 26.1

* Tue May 29 2018 Anton Farygin <rider@altlinux.ru> 25.3-alt10
- Rebuilt for libImageMagick

* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 25.3-alt8
- NMU: added emacs.pc and emacs.appdata.xml

* Wed Sep 13 2017 Terechkov Evgenii <evg@altlinux.org> 25.3-alt7
- 25.3 (emergency release to fix a security vulnerability)

* Fri Aug 18 2017 Anton Farygin <rider@altlinux.ru> 25.2-alt6
- Rebuilt for new libImageMagick.

* Sun Apr 23 2017 Terechkov Evgenii <evg@altlinux.org> 25.2-alt5
- 25.2

* Sat Mar 11 2017 Terechkov Evgenii <evg@altlinux.org> 25.1.91-alt4
- 25.1.91

* Thu Sep 22 2016 Terechkov Evgenii <evg@altlinux.org> 25.1-alt3
- Fix updating alternatives

* Wed Sep 21 2016 Terechkov Evgenii <evg@altlinux.org> 25.1-alt2
- Disable LTO to avoid build-time segfault (see https://debbugs.gnu.org/cgi/bugreport.cgi?bug=22522)

* Mon Sep 19 2016 Terechkov Evgenii <evg@altlinux.org> 25.1-alt1
- 25.1

* Thu Jul 14 2016 Terechkov Evgenii <evg@altlinux.org> 25.0.95-alt1
- 25.0.95

* Thu May 26 2016 Terechkov Evgenii <evg@altlinux.org> 25.0.94-alt1
- 25.0.94

* Sun Apr 24 2016 Terechkov Evgenii <evg@altlinux.org> 25.0.93-alt1
- 25.0.93

* Thu Apr  7 2016 Terechkov Evgenii <evg@altlinux.org> 24.5-alt16
- Rebuild with libgnutls30

* Thu Apr 16 2015 Terechkov Evgenii <evg@altlinux.org> 24.5-alt15
- Use new build scheme (from upstream git) in emacs24 source package

* Wed Apr 15 2015 Terechkov Evgenii <evg@altlinux.org> 24.5-alt14
- 24.5

* Tue Mar 10 2015 Terechkov Evgenii <evg@altlinux.org> 24.4.91-alt13
- 24.4.91 (24.5 pretest)

* Sun Mar  1 2015 Evgenii Terechkov <evg@altlinux.org> 24.4.90-alt12
- Pretest version of new build scheme
- 24.4.90 (24.5 pretest)

* Thu Oct 23 2014 Evgenii Terechkov <evg@altlinux.org> 24.4-alt11
- 24.4

* Mon Apr  7 2014 Terechkov Evgenii <evg@altlinux.org> 24.3-alt10.1
- Cedet release updated

* Thu Apr  3 2014 Terechkov Evgenii <evg@altlinux.org> 24.3-alt10
- Rebuild with new libImageMagick

* Sat Mar  1 2014 Terechkov Evgenii <evg@altlinux.org> 24.3-alt9
- Fix FTBFS with gcc4.8 (disable LTO for gtk build)

* Fri Apr 19 2013 Terechkov Evgenii <evg@altlinux.org> 24.3-alt8
- Cedet release updated

* Thu Apr 18 2013 Terechkov Evgenii <evg@altlinux.org> 24.3-alt7
- Rebuild with new libImageMagick

* Fri Mar 15 2013 Terechkov Evgenii <evg@altlinux.org> 24.3-alt6
- 24.3

* Thu Sep 27 2012 Terechkov Evgenii <evg@altlinux.org> 24.2-alt5
- Rebuild with new libpng15.so.15/libtiff.so.5

* Sat Sep  1 2012 Terechkov Evgenii <evg@altlinux.org> 24.2-alt4
- Post 24.1 regression fixes

* Tue Aug 28 2012 Terechkov Evgenii <evg@altlinux.org> 24.2-alt3
- 24.2

* Thu Jun 21 2012 Terechkov Evgenii <evg@altlinux.org> 24.1-alt2
- Rebuild with new libImageMagick

* Mon Jun 11 2012 Terechkov Evgenii <evg@altlinux.org> 24.1-alt1
- 24.1

* Wed May 23 2012 Terechkov Evgenii <evg@altlinux.org> 23.3-alt4
- Fix build with new binutils
- Cedet release updated

* Tue Apr 05 2011 Eugene Vlasov <eugvv@altlinux.ru> 23.3-alt3
- New version

* Tue May 18 2010 Eugene Vlasov <eugvv@altlinux.ru> 23.2-alt2
- New version
- New subpackages - cedet and cedet-el
- Removed font set from app-defaults resources
- eshel and org el-files moved to el subpackage

* Tue Oct 13 2009 Eugene Vlasov <eugvv@altlinux.ru> 23.1-alt1
- New version
- Requires cleanup
- Obsoletes emacs22
- Build athena and motif binary with sound support
- Applied CVS fix for build with gcc-4.4.2

* Mon Jun 22 2009 Eugene Vlasov <eugvv@altlinux.ru> 23.0.95-alt0.13.pretest
- New pretest version
- Removed deprecated post/postun install_info/uninstall_info calls

* Thu Apr 02 2009 Eugene Vlasov <eugvv@altlinux.ru> 23.0.92-alt0.12.pretest
- Fixed lisp files recompilation, touch changed files

* Thu Apr 02 2009 Eugene Vlasov <eugvv@altlinux.ru> 23.0.92-alt0.11.pretest
- New pretest version
- Updated build requires

* Sat Jan 10 2009 Eugene Vlasov <eugvv@altlinux.ru> 23.0.60-alt0.10.20090110
- New snapshot
- Removed deprecated post/postun register_alternatives and
  unregister_alternatives calls

* Sun Nov 16 2008 Eugene Vlasov <eugvv@altlinux.ru> 23.0.60-alt0.9.20081116
- New snapshot
- Updated build requires
- Modified desktop entry: removed deprecated Encoding key, removed empty
  Path key
- Removed deprecated post/postun update_menus and update_desktop_database
  calls

* Sun Sep 28 2008 Eugene Vlasov <eugvv@altlinux.ru> 23.0.60-alt0.8.20080928
- New snapshot
- Updated infos list

* Fri Jun 06 2008 Eugene Vlasov <eugvv@altlinux.ru> 23.0.60-alt0.7.20080606
- New snapshot

* Thu May 01 2008 Eugene Vlasov <eugvv@altlinux.ru> 23.0.60-alt0.6.20080501
- New snapshot
- Updated README.ALT-ru_RU.KOI8-R, replaced all 22 version occurences to 23
- Added update_desktopdb and clean_desktopdb post/postun macro for X11
  package
- Removed from build requires linux-libc-headers
- Exclude GNUS-NEWS and etc/gnus/ from emacs23-common
- Pack scalable/mimetypes/emacs-document.svg icon

* Wed Mar 19 2008 Eugene Vlasov <eugvv@altlinux.ru> 23.0.60-alt0.5.20080320
- New snapshot, tramp recursive load fixes
- Fixed "Invalid face slant: roman" when using XFT fonts

* Tue Mar 18 2008 Eugene Vlasov <eugvv@altlinux.ru> 23.0.60-alt0.4.20080318
- New snapshot
- Build X variants with dbus
- Build GTK variant with rsvg support

* Sat Mar 08 2008 Eugene Vlasov <eugvv@altlinux.ru> 23.0.60-alt0.3.20080308
- New snapshot (CVS head), updated tramp version
- Changed icon set, install all icon sizes
- Removed README.unicode doc file
- Modified mime types list in desktop file

* Mon Jan 07 2008 Eugene Vlasov <eugvv@altlinux.ru> 23.0.60-alt0.2.20080106
- New snapshot
- Updated gnus version
- Disabled dvi docs build
- Info documentation packaged in emacs23-info
- Corrected infos list (added dbus, nxml-mode and remember info)
- Build nxml-mode as separate package
- Used supplied procedure for pack *.el files, looks like el-pkgutils
  broken now
- Fixed doc list
- Fixed elisp files lists
- Fixed gnus files list

* Mon Nov 05 2007 Eugene Vlasov <eugvv@altlinux.ru> 23.0.60-alt0.1.20071102
- New snapshot
- Updated tramp and erc versions
- Reapplied patches that affect files in man/, lispref/ and lispintro/ (all
  docs source located now in doc/)
- Changed dvi build code for new docs source location
- Gnus: don't pack ChangeLog files

* Tue Aug 14 2007 Eugene Vlasov <eugvv@altlinux.ru> 23.0.0-alt0.2.20070814
- New snapshot, possibly fixed bootstrap segfault
- Updated license tag to GPLv3 or later
- Updated tramp version

* Thu Jul 26 2007 Eugene Vlasov <eugvv@altlinux.ru> 23.0.0-alt0.1.20070721
- Initial GNU Emacs 23 build (from emacs-unicode-2 cvs snapshot)
- Build from GIT, all patches applied to git tree
- Updated packages versions
- Used make bootstrap and no lisp recompilation for cvs build
- Modified configure parameters:
  * Used --enable-font-backend --with-freetype --with-xft for for all
    variants except nox
  * Used --with-gpm for nox and gtk variants
- Renamed and modified for emacs23 alternatives and desktop files
- Updated build requires
- Added conflicts to emacs22

* Tue Jun 05 2007 Eugene Vlasov <eugvv@altlinux.ru> 22.1-alt1
- 22.1 release
- Regenerated and reorganized build requires
- Used "make" instead "make bootstrap", restored old build procedure (with
  lisp files recompilation on third stage)

* Thu May 24 2007 Eugene Vlasov <eugvv@altlinux.ru> 22.0.990-alt0.28.pretest
- New pretest version
- Simplified build - removed lisp files recompilation on third stage, rebuild
  only nox binary on final stage

* Sat Apr 21 2007 Eugene Vlasov <eugvv@altlinux.ru> 22.0.98-alt0.27.pretest
- New pretest version
- Rediffed more-cyrillic patch

* Fri Apr 06 2007 Eugene Vlasov <eugvv@altlinux.ru> 22.0.97-alt0.26.pretest
- New pretest version
- Added Provides: /usr/bin/emacs to packages with emacs binaries

* Fri Mar 23 2007 Eugene Vlasov <eugvv@altlinux.ru> 22.0.96-alt0.25.pretest
- New pretest version

* Wed Mar 07 2007 Eugene Vlasov <eugvv@altlinux.ru> 22.0.95-alt0.24.pretest
- New pretest version
- Rediffed more-cyrillic patch
- Autoconf used again, all patches to configure.in returned

* Wed Feb 07 2007 Eugene Vlasov <eugvv@altlinux.ru> 22.0.93-alt0.23.pretest
- alt-system patch applied to configure script (#10781)
- README.ALT - added warning about emacs22-nox restrictions, added some
  words about sound support in emacs22-X11-gtk
- Build gtk binary with sound support

* Sat Jan 27 2007 Eugene Vlasov <eugvv@altlinux.ru> 22.0.93-alt0.22.pretest
- New pretest version
- Tramp filename completion fixed in upstream - patch removed
- Update tramp version
- Used supplied configure script (now autoconf 2.61 needed)
- Patch for X resource default search path applied to configure script

* Sun Jan 07 2007 Eugene Vlasov <eugvv@altlinux.ru> 22.0.92-alt0.21.pretest
- Fixed tramp filename completion, updated tramp.el to CVS version (#10603)

* Fri Dec 22 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.92-alt0.20.pretest
- New pretest version
- Selection coding use fixed in upstream - patch removed
- Update ERC version

* Tue Nov 28 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.91-alt0.19.pretest
- Fixed use selection coding. Fix from CVS, solves problems with copy/yank
  non iso-latin-1 letters
- Removed pointer color modification from app-defaults file

* Sat Nov 25 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.91-alt0.18.pretest
- New pretest version
- Rediffed info_install patch
- Removed mode-line attributes modifications from app-defaults file
- Fixed default path for search application X resource

* Tue Oct 31 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.90-alt0.17.pretest
- First emacs22 pretest version
- Fixed build dvi manuals
- Removed %%__ macro

* Sun Oct 08 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.16.20061008
- New snapshot
- Rediffed alt-system patch

* Tue Sep 12 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.15.20060912
- New snapshot
- Update erc version
- Update tramp version
- Build .dvi manuals fixed in upstream, patch for elisp.texi removed

* Sat Jul 15 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.14.20060715
- New snapshot
- Enabled build motif binary for all arch
- Build tramp as separate package
- Increased obsoletes version for emacs-tramp
- Update erc version
- Excluded erc files from emacs22-el
- Moved ERC-NEWS to emacs22-erc
- Reverted @fonttextsize addition in elisp.texi

* Wed Jun 14 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.13.20060614
- New snapshot (closes #9635)
- Corrected infos list (removed emacs-extra)

* Sat Apr 29 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.12.20060429
- New snapshot
- Removed motif headers hack
- Disabled build motif binary for x86_64
- Increased PURESIZE

* Thu Apr 20 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.11.20060420
- New snapshot
- Disabled modification of face-font-selection-order default value
- Droped useless dependency on python (Igor Vlasenko)
- Added optional build with menu, not desktop-file, fixed menu-file (Igor
  Vlasenko)
- For backward compatibility with old distribution define %%_niconsdir if not
  defined (Igor Vlasenko)

* Sun Mar 19 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.10.20060319
- New snapshot
- Rediffed jka-compr_bz2_load patch
- Turned back fix for build with motif (for x86_64 build)
- Used %%_niconsdir macro instead of %%_iconsdir for 32x32 icon, renamed icons
- Menu-file replaced by desktop-file
- Fixed info installation

* Thu Feb 23 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.9.20060223
- New snapshot
- Rediffed uk patch (ispell-local-dictionary-alist accept now any coding 
  system, supported by Emacs)

* Sun Feb 12 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.8.20060211
- New snapshot
- Obsoletes emacs-ses <= 1.0-alt2.031130
- Added (consp) check for save-place-alist elements, loaded from
  ~/.emacs-places (#9053)
- Removed fix for build with motif and Xaw3d

* Fri Feb 03 2006 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.7.20060203
- New snapshot
- Added conflict with emacs-gnuserv <= 3.12.7-alt1
- Support for optional build of athena, motif, gtk, nox (Igor Vlasenko)
- Added .dvi files to elisp-manual (Igor Vlasenko)
- Fix for flyspell-buffer merged into upstream
- Rediffed clipboard patch
- Fixed build with motif and Xaw3d
- Added rcirc manual to infos list
- Fixed unpackaged files warning
- Fixed x86_64 build (Igor Vlasenko)
- ERC package included in upstream, build as separate package, obsolete
  old emacs-erc
- el-pkgutils 'fraction' calls replaced with awk code (Igor Vlasenko)

* Sun Dec 11 2005 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.6.20051211
- New snapshot
- Now emacs22 obsoletes emacs21, emacs-tramp, emacs-ses, emacs-elisp-manual
- Build speedbar as separate package
- Fix flyspell-buffer for large tex files (thanks to Igor Vlasenko for
  notifying)
- Fix spell checking with aspell in locale coding other than dictionary 
  coding (thanks to Igor Vlasenko for notifying)

* Tue Nov 22 2005 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.5.20051122
- New snapshot
- Rediffed more-cyrillic-support patch, require cyrillic-codepages-setup 
  only if purify-flag is nil (not while preparing to dump)
- Disabled builtin compress function for installed .el files (used compress
  function from el-pkgutils)
- Cleanup requires
- Added conflict with old emacs-w3 (with url package inside)
- Used new emacs icons (from Andrew Zhilin)
- Site-start script emacs21-rus-win-keyboard.el renamed to rus-win-keyboard.el

* Mon Oct 24 2005 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.4.20051024
- New snapshot
- Added ".bz2" to default value jka-compr-load-suffixes (to enable load
  bzipped libraries and for .el.bz2 source navigation from *Help* window)
- More substitutes for buildreq
- Don't exclude antlr-mode
- Modified build requires for M24 compatibilty (Igor Vlasenko)
- Added README.ALT
- Added check-shadows script for check list of Emacs Lisp files that
  shadow other files (#2622)
- Removed fix for mh-e autoloads
- Fixed macros warnings
- Build with emacs-devel
- Removed dir %%_libdir/emacs/site-lisp
- Added dir %%_libdir/emacs (emacs-base no more provides this dir)
- Enabled search of aspell dictionaries. Now it preserve elements of
  ispell-dictionary-alist for dictionaries that are not found
- Rediffed patch for decoding headers in gnus
- PGG now part of %name-common (info pages moved too)
- Fixed Summary
- Removed SGID bit of update-game-score binary

* Sat Oct 08 2005 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.3.20051008
- New snapshot
- Temporary disable finding aspell dictionaries
- Build gnus
- Build with new speedbar
- Now required emacs-base >= 0.0.4-alt5
- Fixed missing menu icons (thanks to viy@)
- Fixed command in menu file
- Fixed build-time generating autoloads for mh-e
- Added fix for decoding in gnus invalid encoded headers

* Fri Sep 23 2005 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.2.20050923
- New snapshot
- Corrected infos list
- Added conflict with emacs-tramp
- Used relative symlink in documentation dir
- Changed X resources default font
- Added substitute emacs22-common with emacs-common for buildreq (#5500)
- Rediffed clipboard patch

* Mon Sep 05 2005 Eugene Vlasov <eugvv@altlinux.ru> 22.0.50-alt0.1.20050902
- CVS snapshot fork
- Rediffed and reworked patches:
  * emacs-21.2-alt-system.patch
  * emacs-21.3-alt3-clipboard.patch
  * emacs-21.2-hide-rcs-deps.patch
  * emacs-21.2-Meta-Alt-Ctrl-Hyper-super-discard-state.patch
  * emacs-21.2-pc-select-private-mark.patch
  * emacs-21.2-face-font-selection-slant-important.patch
  * emacs-21.3-rh-no_rpath.patch
  * emacs-21.3-alt4-uk.patch
  * leim-21.1-uk.patch
  * leim-20.6-belarusian.patch
  * emacs-21.3-ispell-belarusian.patch
  * emacs-21.3-ispell-russianw.patch
  * emacs-21.3-alt1-more-cyrillic-support.patch
  * emacs-21.2-alt12-tutorial-ru.patch
- Removed patches (merged into upstream)
  * emacs-21.2-HEAD-pc-select.diff
  * emacs-21.2-ediff-diff-options-check-c.patch
  * emacs-21.3-use-handler-for-load-of-absolute.patch
  * emacs-21.3-use-handler-for-load-of-suffixed.patch
  * emacs-21.2-x86_64.patch
  * emacs-21.1-lang-env-prereqs.patch
- Build separate packages for athena, motif and gtk binaries
- New alternatives format
- Build ELisp manual
- Updated BuildRequires

* Thu Jul 07 2005 Igor Vlasenko <viy@altlinux.org> 21.3-alt11.vla2
- added conflict with ispell-uk<0.6

* Thu Jun 30 2005 Igor Vlasenko <viy@altlinux.org> 21.3-alt11.vla1
- fixed bug #6853 shift+7 in cyrillic-ukrainian-ms
- fixed bug #835 (added belarussian ispell dict)
- fixed bug #6855 (re-added ukrainian ispell dict)
- fixed bug #6842 (patched emacs21-rus-win-keyboard.el)

* Fri Feb 11 2005 Kachalov Anton <mouse@altlinux.ru> 21.3-alt11
- support for x86_64 (#6089)

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 21.3-alt10.1.1
- Rebuilt with libtiff.so.4.

* Thu Jun 10 2004 Stanislav Ievlev <inger@altlinux.org> 21.3-alt10.1
- NMU: fix alternatives usage (rename candidates in remove_alternative macros)

* Mon May 03 2004 Ott Alex <ott@altlinux.ru> 21.3-alt10
- Fix bug #2676
- Fix bug #883
- Fix bug #1159
- Fix bug #1502
- Fix bug #2217
- Fix bug #3885
- Fix bug #2566

* Sat Mar 27 2004 Ott Alex <ott@altlinux.ru> 21.3-alt9
- Fixing entry in menu

* Sat Jan 31 2004 Ott Alex <ott@altlinux.ru> 21.3-alt8
- Fixing entry in menu
- Install new smtpmail with support of SMTP Auth

* Mon Jan 12 2004 Ott Alex <ott@altlinux.ru> 21.3-alt7
- Fixing spec to properly rebuild

* Sat Jan 10 2004 Ott Alex <ott@altlinux.ru> 21.3-alt6
- Name changed to emacs21 
- Remove compression of .elc files
- Remove dependence on speedbar
- Remove gnus and dependence on it
- Added missed buildreq on sendmail
- Move emacs-pkgtools to emacs-base

* Sun Nov 30 2003 Ott Alex <ott@altlinux.ru> 21.3-alt5
- Reorganize package 
- move php-mode.el to emacs-prog-modes package

* Wed Apr 09 2003 Stanislav Ievlev <inger@altlinux.ru> 21.3-alt4.1
- new alternatives format

* Fri Apr  4 2003 Ivan Zakharyaschev <imz@altlinux.ru> 21.3-alt4
- lisp: autoload `cyrillic-encode-koi8-r-char' (was lost in patch20 "uk")

* Tue Apr  3 2003 Ivan Zakharyaschev <imz@altlinux.ru> 21.3-alt3
- mouse & PRIMARY X selection: restore the behaviour introduced
  by 21.2-alt11-clipboard.patch (lost in 21.3-alt1; patch3)

* Tue Apr  1 2003 Ivan Zakharyaschev <imz@altlinux.ru> 21.3-alt2
- built-in `load': always use the load-handler if it is present 
  (e.g. for compressed .elc's; fixes No. 0002355; patches 11 and 12);
- lisp: 
  + `vc-cvs-registered' function: split into parts for autoloading
    without any loops (No. 0002334 at bugs.altlinux.ru; patch13);
  + php-mode updated to 1.04;
- docs: include AUTHORS, symlink etc/;
- spec:
  + make updates (regenerate autoloads, cus-deps etc.) at the %%build stage;
  + supply install-info path to %%makeinstall (to get less error msgs);

* Tue Mar 25 2003 Ivan Zakharyaschev <imz@altlinux.ru> 21.3-alt1
- new upstream version;
- files: include /usr/bin/{ebrowse,grep-changelog} in emacs-common pkg
  (No. 0002354 at bugs.altlinux.ru)
- Cyrillic support improvements (patch33):
  + language-env detection improved for be*, ru*, uk* & *iso8859-5 locales;
  + info manual reflects the support for various Cyrillic-based language-envs
    (based on the "uk" patch);
  + Ukrainian word for "Ukrainian" fixed in HELLO (No. 0002213);
- spec & patches (not visible to a user): 
  + simplify the menu file (s:%%version:X11:);
  + include /usr/bin/* in emacs-common pkg (and exclude emacs-{nox,X11});
  + patch3 (clipboard): default xselection coding-system value is already correct upstream;
  + patch9 (regex-encoded): upstream (not ours);
  + patch20 (uk): redone, some parts extended and moved to patch33 (more-cyrillic);
  + patch31 (dumbterm-for-compile): finally upstream;
  + patch32 (cp866fix): upstream;

* Fri Mar 14 2003 Stanislav Ievlev <inger@altlinux.ru> 21.2-alt16
- PreReq fixes

* Wed Mar 12 2003 Stanislav Ievlev <inger@altlinux.ru> 21.2-alt15
- moved to new alternatives scheme
- warning to maintainer: added missing PreReq on update-alternatives


* Mon Feb 10 2003 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt14
- changes to better support various Cyrillic X fonts 
  (news in patch33):
  + faces.el: face-font-registry-alternatives: list the wide-spread 
    alternatives for Cyrillic iso8859-5 (microsoft-cp1251, koi8-u, koi8);
  + fontset.el: leave "ISO8859-5" as the REGISTRY-ENCODING for Cyrillic;
  + fontset.el: change the FAMILY for Cyrillic from "*" (any) to nil 
    (the same a sthe default), because Cyrillic is like Latin: the family
    plays just hte same role;
  + describe koi8-c X font encoding (for now, just as an alias for koi8-u);
  (patch10):
  + make :slant the most important property when selecting a font for a face
    (imho, the absence of slanted fonts makes the visual appearance dull);
  (source31):
  + remove all font-related settings from /etc/X11/app-defaults/Emacs (which
    used to be brute), add only "Emacs.default.attributeFamily: fixed";
  + now, there is no need to specify rather brute values in localized
    /etc/X11/Xresources.* in order to get the right encoded Cyrillic font --
    we get it without any special X resources, if the Cyrillic font is 
    available (modify app-defaults accordingly!);
    (a part of the fix for No. 0000825, 0001478, 0001681; complete 0000997);
- open bzipped2 .el files (as well as gzipped which was supported before)
  when following links from the Help buffer (e.g., C-h v) (patch1;
  fixes No. 0001927 at http://bugs.altlinux.ru).

* Mon Feb 10 2003 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt13
- fix regex processing for some specially encoded texts (patch9, useful
  for Gnus, sent by Alex Ott <ottalex@narod.ru>);
- add BuildRequires(install): bzip2-utils (to fix No. 0001911).

* Sun Dec  8 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt12
- files: 
  + include non-el/elc files from lisp/ (mainly xpm; fixes No. 0001387);
  + exclude gnus/ from emacs-common (it was included in a previous revision);
  + compress .el-files in *-el pkgs;
- corrected TUTORIAL.ru (Alex Ott <ottalex@narod.ru>);
- spec-file: thoroughly check that all info-files are included
  (fixes No. 0001386);

* Sun Nov 17 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt11
- make possible primary X selection setting & pasting with mouse
  (in addition to clipboard manipulation with keys; fixes No. 1356);
- pc-selection-mode: turn-offable; no conflict with traditional 
  selection manipulation keys (like C-space; fixes No. 1357 at 
  bugs.altlinux.ru);
- lisp/ediff-diff.el: refine the check for valid ediff-diff-options;

* Sat Nov  9 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt10
- make finer distinction between koi8-r & koi8-u font encodings
  (fixes No. 997 at bugs.altlinux.ru).

* Fri Nov  8 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt9
- make keys like C-h, M-x work even when the (say) Russian XKB 
  group is active (patch5, discard almost the whole state if
  a certain modifier is detected; fixes No. 852 at bugs.altlinux.ru).
  (Please REPORT any related misbehaviors!)

* Thu Nov  7 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt8
- use --host=%%_target_platform for ./configure (fixes No. 1535
  at bugs.altlinux.ru).

* Tue Nov  5 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt7
- lisp: leave gnus/format-spec.el* in the main pkg (do not put in gnus):
  kind of essential library (required by tramp);
- scripts:
  + do not install {dir,info}.info; do install idlwave.info;
  + do not install speedbar.info (belongs to the speedbar package);
    WARNING: unless you reinstall emacs-speedbar, its info entry won't
    appear in the catalog;
- gnus subpkg:
  + Provides: gnus = %%name:%%version-%%release; Conflicts: gnus !=...; 
    I suppose other Gnus pkgs should do the same;
  + move {emacs-mime,message}.info to this subpkg.

* Sun Nov  3 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt6
- install more info;
- separate gnus{,-el} (alternatives would be complex in this case due to
  info and etc/, so other gnus should merely conflict with these ones).

* Fri Jul 19 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt5
- follow the convention about using POSIX locks (with fcntl(2)) for 
  mailbox access (in movemail; nnmbox users take care on your own!);
- drop privileges of movemail utility (no dot-locking in /var/mail/); 
- link with tinfo, not ncurses (everything is there in the latest release);
- remove termcap from build deps;
- lisp: drop speedbar.el{,c}, speedbar.info -- you will find it 
        in a separate pkg (Alex Ott <ottalex@narod.ru>);
- etc: add TUTORIAL.ru (Alex Ott);
- rcs-checkin: hide the dependencies on rcs (mhz).

* Sun Apr 14 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt4
- lisp: 
  + add support for X Compound Text with Extended Segments
    in koi8-u and microsoft-cp1251 (koi8-r support already present
    in the offcial GNU release; this is the complete fix for \#786
    at bugs.altlinux.ru);
  + add cp1251 item to the list of choices for ispell coding;
- package:
  + correct preun-scripts (alternative management) (Sorry, you will 
    have to uninstall 21.2-alt3 manually with --noscripts);

* Fri Apr 12 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt3
- rename: /usr/bin/emacs-21.2 to /usr/bin/emacs-X11
  (to overcome the alternatives nightmare);

* Fri Apr 12 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt2
- package: 
  + add Confilcts on older etcskel & app-defaults (the
    old ones use values considered bad for 21.2);
  + Groups of *-el subpkgs changed to Development/Other;
- lisp: add support for X fonts in koi8 and *1251;


* Mon Apr  8 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.2-alt1
- new mainstream release (21.2):
  + now supports ICCCM Extended Segments in X selctions (fixes \#786 at
    bugs.altlinux.ru) -- don't forget to sync etcskel's to use c-text 
    for selections;
- lisp: 
  + prefer clipboard over primary selection (the reasononig given in
    \#795 at bugs.altlinux.ru);
  + the default value for selection-coding-system: 
    compound-text -> compound-text-with-extensions (this is the second part of
    the fix for \#786 at bugs.altlinux.ru)
  + Encoded-kb mode indicator turned off in mainstream release, so 
    we are not applying our previous patch any more;
-config:
  + use "Emacs" class as a specifier for X resourcers (was: "emacs" name)
    (fixes \#764 at bugs.altlinux.ru) -- don't forget to sync /etc/Xresources;
- spec-file:
  + dumbterm-for-compile patch regenerated;
  + alternatives: 
    * weights for alternatives shifted by %%{alternativeMajor}00;
    * removal in %%preun to avoid collisions;

* Thu Mar  1 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.1-alt13
- fix broken deps between emacsen-startscripts and and emacs-{X11,nox}:
  the pkgs with Emacs executables now provide `emacsen'.

* Thu Feb 28 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.1-alt12
- make co-existence with other Emacsen (XEmacs) easier:
  + move the site start scripts to a separate pkg (emacsen-startscripts; 
    they should be shared between GNU and X- Emacsen); buildreq rules for
    the directory with the scripts also moved to that pkg;
  + emacs-{nox,X11} provide emacsen (should be also provided 
    by XEmacs binaries);
  + emacs-{nox,X11} require emacsen-startscripts (should be also required 
    by XEmacs binaries);

* Sat Feb 25 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.1-alt11
- get rid of the inconsistency in versions and documentation data between 
  emacs-X11 and emacs-nox variants (fixes \#601, \#612 in bugs.altlinux.ru)
  (%%build stage modified to achieve this);
- add more strict %%release dependencies;
- add support for loading bzipped2 .el/.elc; compress several large files;
- lisp:
    + encoded-kbd: make indicator string shorter;
    + cyrillic-codepages-setup: override `valid-codes' property with more 
      correct values (this fixes hanging on C-x; Note: if you do 
      codepage-setup manually, then it is not fixed for you);
- config:
    + macros: rename noXlaunch -> TTYlaunch;
    + mouse: attempt to use mouse in Linux console and Xterm;
    + initial-features: turn on column-number and eldoc (for el only) modes;
- spec-file:
  + %%install: handle menu simpler;
  + make a patch instead of the separate HELLO.re (append it to Patch20);
  + %%install: generate filelists using el-pkgutils (it should be used also
    in other pkgs with Emacs Lisp code);

* Sun Feb  9 2002 Ivan Zakharyaschev <imz@altlinux.ru> 21.1-alt10
- lisp: 
  + new version of php-mode (1.0.2); compile it;
    on site-start, initialize autoload of it (php-mode);
  + add more seamless support for Cyrillic language environments based
    on CP1251, CP866 and CP1125;
  + fix CP866 table;
- config:
  + special bindings for selection management discarded -- the defaults 
    work fine (even for X); support for analogous KeyPad bindings added 
    (suggested by vyt@vzljot.ru);
  + X resources: set our values for colour classes; use "Helv" font 
    family for the menu;
  + do not fail completely if the Flyspell feature fails;
  + mouse wheel support turned on;
  + defined GNU-/XEmacs and Xlaunch macros (to be used in personal configs, etcskels);
  + split the config into small parts;
- menu: explicitly specify the X11-variant of emacs;
- spec-file:
  + Head: thrown away unused and recompiled sources; 
    not used terminfo patch left for a while: do we need it??;
  + build: do not copy any byte-compiled .elc files into the build 
    tree -- all of them now get recompiled from the patched sources 
    (particularly quail/cyrillic.elc from leim);
  + install: move menu entry to a separate file;
  + scriplets: use %%*_menus macros;
  + install: cut down "$RPM_BUILD_ROOT" usage;
  + detect errors during Emacs Lisp compilation;

* Thu Jan 24 2002 Dmitry V. Levin <ldv@alt-linux.org> 21.1-alt9
- Added emacs filter for buildreq.

* Thu Dec 27 2001 Ivan Zakharyaschev <imz@altlinux.ru> 21.1-alt8
- configuration:
  + really turn on pc-selection-mode;
  + move frame properties from site-start.el to X resources;
- lisp: really apply our patches by recompiling the patched sources;
- .el/.elc fractions improved:
  + do not loose any not-compiled .el-files in the emacs-common pkg;
  + split emacs-el into emacs-el and emacs-leim-el subpkgs;
- "TERM in Compile" patch extended (idea by rms@gnu.org);

* Wed Dec 26 2001 Ivan Zakharyaschev <imz@altlinux.ru> 21.1-alt7
- inherit ispell-dictionary value from the DICTIONARY environment variable
- fix the "TERM in Compile" patch -- now it works

* Wed Dec 26 2001 Ivan Zakharyaschev <imz@altlinux.ru> 21.1-alt6
- configuration from MdkRE's etcskel-* merged into the global Emacs' config
- set TERM=dumb for compile (for nice output of colorgcc and other programs)
- set ownership on various directories for clean pkg removal
- FAQ excluded from the documentation

* Tue Nov 20 2001 AEN <aen@logic.ru> 21.1-alt5
- update-alternatives fixed (bug 168,169)
- new php-mode.el (bug 170)

* Thu Nov 15 2001 AEN <aen@logic.ru> 21.1-alt4
- fix typo in previous changelog record
- some MDK improvements added

* Tue Nov 13 2001 AEN <aen@logic.ru> 21.1-alt3
- ukrainiazation from Serhii Hlodin

* Thu Nov 1 2001 AEN <aen@logic.ru> 21.1-alt2
- leim cyrillic patches restored

* Mon Oct 22 2001 AEN <aen@logic.ru> 21.1-alt1
- new version

* Fri May 18 2001 Stanislav Ievlev <inger@altlinux.ru> 20.7-ipl9mdk
- Repackaged.
- Moved common %name stuff to %name-common subpackage.
- Used update-alternatives for %name-nox and %name-X11 subpackages.
- Fixed terminfo linkage.

* Sat Feb 17 2001 AEN <aen@logic.ru>
- groups names fixed

* Sat Jan 20 2001 AEN <aen@logic.ru>
- belarusian script in HELLO fixed (Alexander Bokovoy)

* Tue Dec 26 2000 AEN <aen@logic.ru>
- spec cleanup

* Thu Dec 07 2000 AEN <aen@logic.ru>
- 20.7
- rebuild for 7.2RE

* Sat Mar 11 2000 Oleg Tihonov <tihonov@ffke-campus.mipt.ru>
- load belarusian code at startup

* Thu Jan 13 2000 Oleg Tihonov <tihonov@ffke-campus.mipt.ru>
- added belarusian language support

* Tue Nov 9 1999 AEN <aen@logic.ru>
- bzipped man-pages
- custom.gz removed
- build for 6.1RE

* Fri Sep 17 1999 Oleg Tihonov <tihonov@ffke-campus.mipt.ru>
- move to 20.4
- add Ukrainian patches

* Wed May 26 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- move the %_bindir/%name script to the %name package

* Wed May 26 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- s/arch-redhat-linux/arch-mandrake-linux
- replace %name with a shell script that runs either %name-nox or
  %name-20.3
- s/%name/%name-20.3/ in %name.wmconfig (wmconfig is always X)

* Fri Apr 23 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adpatations.
- Bzip2 info/man pages.
- Path to handle bzip2 on info files.

* Wed Mar 31 1999 Preston Brown <pbrown@redhat.com>
- updated mh-utils %name lisp file to match our nmh path locations

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 9)

* Fri Feb 26 1999 Cristian Gafton <gafton@redhat.com>
- linker scripts hack to make it build on the alpha

* Fri Jan  1 1999 Jeff Johnson <jbj@redhat.com>
- add leim package (thanks to Pavel.Janik@inet.cz).

* Fri Dec 18 1998 Cristian Gafton <gafton@redhat.com>
- build against glibc 2.1

* Wed Sep 30 1998 Cristian Gafton <gafton@redhat.com>
- backed up changes to uncompress.el (it seems that the one from 20.2 works
  much better)

* Mon Sep 28 1998 Jeff Johnson <jbj@redhat.com>
- eliminate /tmp race in rcs2log

* Wed Sep 09 1998 Cristian Gafton <gafton@redhat.com>
- upgrade to 20.3

* Tue Jun  9 1998 Jeff Johnson <jbj@redhat.com>
- add --with-pop to X11 compile.
- include contents of %_datadir/.../etc with main package.

* Mon Jun 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr

* Mon Jun 01 1998 David S. Miller <davem@dm.cobaltmicro.com>
- fix signals when linked with glibc on non-Intel architectures
  NOTE: This patch is not needed with %name >20.2

* Thu May 07 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr

* Thu May 07 1998 Cristian Gafton <gafton@redhat.com>
- added %_libdir/%name/20.2/*-mandrake-linux directory in the filelist

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- alpha started to like %name-nox again :-)

* Thu Nov  6 1997 Michael Fulbright <msf@redhat.com>
- alpha just doesnt like %name-nox, taking it out for now

* Mon Nov  3 1997 Michael Fulbright <msf@redhat.com>
- added multibyte support back into %name 20.2
- added wmconfig for X11 %name
- fixed some errant buildroot references

* Thu Oct 23 1997 Michael Fulbright <msf@redhat.com>
- joy a new version of %name! Of note - no lockdir any more.
- use post/preun sections to handle numerous GNU info files

* Mon Oct 06 1997 Erik Troan <ewt@redhat.com>
- stopped stripping it as it seems to break things

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- turned off ecoff support on the Alpha (which doesn't build anymore)

* Mon Jun 16 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Fri Feb 07 1997 Michael K. Johnson <johnsonm@redhat.com>
- Moved ctags to gctags to fit in the more powerful for C (but less
  general) exuberant ctags as the binary %_bindir/ctags and the
  man page /usr/man/man1/ctags.1
