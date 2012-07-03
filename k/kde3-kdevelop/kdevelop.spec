%undefine __libtoolize
%define _keep_libtool_files 1
%define _optlevel s
%define unstable 0
%define static 0
%define with_api_docs 1
%define qtdir %_qt3dir
%define build_req_kde_ver 3.5.9

%add_findprov_lib_path %_K3libdir
%set_findreq_skiplist %_K3apps/kdevscripting/*
%add_findreq_skiplist */*template*/*
%set_findprov_skiplist %_K3apps/kdevscripting/*
%add_verify_elf_skiplist %_K3libdir/libdesignerintegration.so*
%add_verify_elf_skiplist %_K3libdir/libdocchmplugin.so*
%add_verify_elf_skiplist %_K3libdir/libdockdevtocplugin.so*
%add_verify_elf_skiplist %_K3libdir/libdocumentation_interfaces.so*
%add_verify_elf_skiplist %_K3libdir/libkdevbuildbase.so*
%add_verify_elf_skiplist %_K3libdir/libkdevbuildtoolswidgets.so*
%add_verify_elf_skiplist %_K3libdir/libkdevcppparser.so*
%add_verify_elf_skiplist %_K3libdir/libkdevextras.so*
%add_verify_elf_skiplist %_K3libdir/libkinterfacedesigner.so*
%add_verify_elf_skiplist %_K3libdir/liblang_debugger.so*
%add_verify_elf_skiplist %_K3libdir/libprofileengine.so*
%add_verify_elf_skiplist %_K3libdir/libgdbmi_parser.so*

%define rname kdevelop
Name: kde3-kdevelop
Version: 3.5.5
Release: alt4.1
Serial: 0

Summary: Integrated Development Environment for C++/C
License: GPL/BSD
Group: Development/C++
URL: http://www.kdevelop.org/

Requires: %name-base = %serial:%version-%release
#Requires: %name-libs = %serial:%version-%release
Requires: %name-kio-chm = %serial:%version-%release

Source: %rname-%version.tar
Source1: ftp://129.187.206.68/pub/unix/ide/KDevelop/c_cpp_reference-2.0.2_for_KDE_3.2.tar

# ALT
Patch100: kdevelop-3.5.4-alt-gcc44.patch
Patch101: detect_alt_autoconf.patch
Patch102: kdevelop-3.0-alt0.11-qmake_path.patch
Patch103: kdevelop-3.5.0-alt-svn-lib.patch
Patch104: kdevelop-3.5.0-alt-filegroup-plugin-loop.patch
Patch105: kdevelop-3.5.4-alt-automake.patch
Patch106: 3.1.1-flags.patch
Patch107: 3.1.1-kdevbdb-prefix.patch
Patch108: kdevelop-3.5.4-alt-autoreconf.patch
Patch109: acinclude.patch
Patch110: kdevelop-3.5.5-alt-gcc45.patch
# Sergey A. Sukiyazov; temp fixes for cstring -> qstring troubles
Patch200: kdevelop-3.2.0-set_default_codec.patch

# Automatically added by buildreq on Wed Mar 31 2004 (-bi)
#BuildRequires: XFree86-devel XFree86-libs doxygen flex fontconfig freetype2 gcc-c++ gcc-g77 kde-settings kdelibs-devel kdesdk-cervisia libdb4.2-devel libjpeg-devel libpng-devel libqt3-devel libstdc++-devel python-devel qt3-designer qt3-doc xml-utils zlib-devel
BuildRequires(pre): kdelibs-devel
BuildRequires: doxygen flex
BuildRequires: gcc-c++ gcc-g77
BuildRequires: libdb4-devel libjpeg-devel libpng-devel libexpat-devel
BuildRequires: libqt3-devel libstdc++-devel python-devel
#BuildRequires: libapr-devel libaprutil-devel libsubversion-devel
BuildRequires: libsubversion-devel
#BuildRequires: libneon-devel
BuildRequires: qt3-designer qt3-doc xml-utils zlib-devel
BuildRequires: autoconf >= 2.53, automake >= 1.5
BuildRequires: kdesdk-cervisia >= %build_req_kde_ver
#BuildRequires: libacl-devel libattr-devel
#BuildRequires: kdelibs-devel-cxx = %__gcc_version_base
BuildRequires: kdelibs >= %build_req_kde_ver kdelibs-devel >= %build_req_kde_ver kdelibs-apidocs >= %build_req_kde_ver


%description
The KDevelop Integrated Development Environment provides many features that
developers need as well as providing a unified interface to programs like gdb,
the C/C++ compiler, and make.

KDevelop manages or provides:
   * All development tools needed for C++ programming like Compiler, Linker,
     automake and autoconf

   * KAppWizard, which generates complete, ready-to-go sample applications

   * Classgenerator, for creating new classes and integrating them into the
     current project

   * File management for sources, headers, documentation etc. to be included in
     the project

   * The creation of User-Handbooks written with SGML and the automatic
     generation of HTML-output with the KDE look and feel

   * Automatic HTML-based API-documentation for your project's classes with
     cross-references to the used libraries; Internationalization support for
     your application, allowing translators to easily add their target language
     to a project

   * WYSIWYG (What you see is what you get) creation of user interfaces with a
     built-in dialog editor

   * Debugging your application by integrating KDbg

   * Editing of project-specific pixmaps with KIconEdit

   * The inclusion of any other program you need for development by adding it to
     the "Tools" menu according to your individual needs.

%package devel
Group: Development/KDE and QT
Summary: Development libraries for kdevelop
Requires: %name-base = %serial:%version-%release

%description devel
Development libraries for kdevelop.

%if %static
%package devel-static
Group: Development/KDE and QT
Summary: Static libraries for kdevelop
Requires: %name-base = %serial:%version-%release

%description devel-static
Static libraries for kdevelop.
%endif

%package common
Summary: Common empty package for %name
Group: Graphical desktop/KDE
Requires: kde-common >= 3.2
#
%description common
Common empty package for %name

%package base
Group: Development/Other
Summary: Base files for %name
Requires: kdelibs >= %{get_version kdelibs}
Requires: %name-common = %version-%release
Requires: gcc gcc-c++ perl bash libqt3-plugin-sql libSDL-devel
Requires: autoconf automake make enscript
Requires: libssl-devel libjpeg-devel libncurses-devel
Requires: sgml-tools gettext zlib-devel ctags gettext-tools
Requires: libtool patch doxygen kernel-headers
%description base
This package contains base program files for KDevelop

%package libs
Group: Development/Other
Summary: Base libraries for %name
Requires: kdelibs >= %{get_version kdelibs}
Requires: %name-common = %version-%release
%description libs
This package contains base libraries for %name

%package kio-chm
Group: Development/Other
Summary: Embeddable HTMLHelp Viewer for KDE
Requires: kdelibs >= %{get_version kdelibs}
Requires: %name-common = %version-%release
Provides: kio-chm = %version-%release
%description kio-chm
This package contains embeddable HTMLHelp files viewer via
ms-its:/ protocol in Konqueror

%package maxi
Group: Development/Other
Summary: Only requires to other %name packages
Requires: %name-for-debug = %version-%release
Requires: %name-for-misc = %version-%release
Requires: %name-for-ada = %version-%release
Requires: %name-for-fortran = %version-%release
#Requires: %name-for-haskell = %version-%release
Requires: %name-for-kde = %version-%release
Requires: %name-for-pascal = %version-%release
Requires: %name-for-php = %version-%release
Requires: %name-for-python = %version-%release
Requires: %name-for-qt = %version-%release
Requires: %name-for-ruby = %version-%release
Requires: %name-for-wxwindows = %version-%release
#
%description maxi
This package contains only requires to other packages
for full KDevelop installation

%package big
Group: Development/KDE and QT
Summary: Only requires to other %name packages
Requires: %name-for-debug = %version-%release
Requires: %name-for-kde = %version-%release
Requires: %name-for-qt = %version-%release
#
%description big
This package contains only requires to other packages
for development KDE and QT applications with KDevelop

%package for-misc
Group: Development/Other
Summary: Only requires to other packages
Requires: %name-base = %serial:%version-%release
Requires: cvs subversion
#
%description for-misc
This package contains only requires to additional
packages for development applications with KDevelop

%package for-debug
Group: Development/Other
Summary: Only requires to other packages
Requires: %name-base = %serial:%version-%release
Requires: valgrind gdb
#
%description for-debug
This package contains only requires to other packages
for debugging applications with KDevelop

%package for-ada
Group: Development/Other
Summary: Templates for developing Ada applications with KDevelop
Requires: %name-base = %serial:%version-%release
Requires: gcc-gnat
#
%description for-ada
Templates for developing Ada applications with KDevelop

%package for-qt
Group: Development/KDE and QT
Summary: Templates for developing Qt applications with KDevelop
Requires: %name-base = %serial:%version-%release
Requires: libqt3-devel qt3-designer qt3-doc
#
%description for-qt
Templates for developing Qt applications with KDevelop

%package for-kde
Group: Development/KDE and QT
Summary: Templates for developing KDE applications with KDevelop
Requires: %name-base = %serial:%version-%release
Requires: %name-for-qt = %version-%release
Requires: kdoc kdelibs-devel kdebase-devel kdemultimedia-devel
Requires: libSDL-devel kdegraphics-kiconedit kdelibs-apidocs
#
%description for-kde
Templates for developing KDE applications with KDevelop

%package for-wxwindows
Group: Development/C++
Summary: Templates for developing WxWindows applications with KDevelop
Requires: %name-base = %serial:%version-%release
Requires: wxGTK-devel
#
%description for-wxwindows
Templates for developing WxWindows applications with KDevelop

%package for-fortran
Group: Development/Other
Summary: Templates for developing Fortran applications with KDevelop
Requires: %name-base = %serial:%version-%release
Requires: gcc-fortran
#
%description for-fortran
Templates for developing Fortran applications with KDevelop

%package for-haskell
Group: Development/Haskell
Summary: Templates for developing Haskell applications with KDevelop
Requires: %name-base = %serial:%version-%release
Requires: ghc
#
%description for-haskell
Templates for developing Haskell applications with KDevelop

%package for-pascal
Group: Development/Other
Summary: Templates for developing Pascal applications with KDevelop
Requires: %name-base = %serial:%version-%release
Requires: fpc
#
%description for-pascal
Templates for developing Pascal applications with KDevelop

%package for-php
Group: Development/Other
Summary: Templates for developing PHP applications with KDevelop
Requires: %name-base = %serial:%version-%release
Requires: /usr/bin/php
%description for-php
Templates for developing PHP applications with KDevelop

%package for-python
Group: Development/Python
Summary: Templates for developing Python applications with KDevelop
Requires: %name-base = %serial:%version-%release
Requires: tk tkinter
#
%description for-python
Templates for developing Python applications with KDevelop

%package for-ruby
Group: Development/Ruby
Summary: Templates for developing Ruby applications with KDevelop
Requires: %name-base = %serial:%version-%release
Requires: ruby
#
%description for-ruby
Templates for developing applications Ruby with KDevelop

%prep
%setup -q -n %rname-%version -a1
mv c_cpp_reference-* c_cpp_reference

%patch100 -p1
#%patch101 -p1
#%patch102 -p1
###%patch103 -p1
%patch104 -p1
%patch105 -p1
###%patch106 -p1
###%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
#
%patch200 -p1

%if %_keep_libtool_files
for f in `find $PWD -type f -name Makefile.am`
do
    grep -q LDFLAGS $f || continue
    RPATH_LINK_OPTS+=" -Wl,-rpath-link,`dirname $f`/.libs"
done
sed -i "s|\(-Wl,--as-needed\)| $RPATH_LINK_OPTS \1|g" admin/acinclude.m4.in
%else
#subst "s/\(Wl,--no-undefined\)/-Wl,--warn-unresolved-symbols \1/g" admin/acinclude.m4.in
subst "s|-Wl,--no-undefined|-Wl,--allow-shlib-undefined|g" \
    admin/acinclude.m4.in \
    parts/appwizard/common/admin/acinclude.m4.in
subst "s/\.la/.so/g" \
    admin/acinclude.m4.in \
    parts/appwizard/common/admin/acinclude.m4.in
subst "s/\-lkdeui/-lkdeui -lpthread/g" \
    admin/acinclude.m4.in \
    parts/appwizard/common/admin/acinclude.m4.in
%endif
make -f admin/Makefile.common cvs ||:

%build
%add_optflags -I%_includedir/tqtinterface
%remove_optflags -fno-exceptions
%add_optflags -fexceptions
export QTDIR=%qtdir
export KDEDIR=%prefix
export PATH=$QTDIR/bin:%_K3bindir:$PATH
export LD_LIBRARY_PATH=$QTDIR/%_lib:$KDEDIR/%_lib:$LD_LIBRARY_PATH
export LDFLAGS="-L%buildroot/%_libdir -L%buildroot/%_K3libdir -L%_libdir -L%_qt3dir/lib"

pushd c_cpp_reference
%K3configure \
  --with-qt-libraries=%_qt3dir/lib \
  --with-qt-includes=%_qt3dir/include \
  --with-extra-libs=%{_libdir}
popd

%K3configure \
%if %unstable
    --enable-debug=full \
%else
    --disable-debug \
%endif
    --enable-scripting \
    --with-qt-dir=%qtdir \
    --with-qtdoc-dir=%qtdir/doc/html/ \
    --with-kdelibsdoc-dir=%_K3doc/en/kdelibs \
    --with-kdelibsdoxy-dir=%_K3doc/en/kdelibs-apidocs \
    \
    --enable-autoproject \
    --enable-scriptproject \
    --enable-trollproject \
    --enable-customproject \
    --enable-cvs \
    --enable-subversion \
    --enable-perforce \
    --enable-clearcase \
    --disable-vba \
    \
    --enable-ada \
    --enable-bash \
    --enable-cpp \
    --enable-fortran \
    --enable-haskell \
    --enable-java \
    --enable-pascal \
    --enable-perl \
    --enable-php \
    --enable-python \
    --enable-ruby \
    --enable-sql \
    --enable-java
#    --enable-final \

%make_build
%if %with_api_docs
%make_build apidox
%endif


%install
%if %unstable
%set_strip_method none
%endif

%K3install
%if %with_api_docs
%make_build DESTDIR=%buildroot install-apidox
%endif
%make_build -C c_cpp_reference DESTDIR=%buildroot install



%files
%files common
%files maxi
%files big
%files for-debug
%files for-misc

%files for-ada
%_K3apps/kdevappwizard/templates/adahello.kdevtemplate

%files for-fortran
%_K3apps/kdevappwizard/templates/fortranhello.kdevtemplate

#%files for-haskell
#%_K3apps/kdevappwizard/templates/haskellhello.kdevtemplate

%files for-kde
%_K3xdg_apps/%{rname}_kde_cpp.desktop
%_K3apps/kdevappwizard/templates/khello.kdevtemplate
%_K3apps/kdevappwizard/templates/kicker.kdevtemplate
%_K3apps/kdevappwizard/templates/kioslave.kdevtemplate
%_K3apps/kdevappwizard/templates/dcopservice.kdevtemplate
%_K3apps/kdevappwizard/templates/kapp.kdevtemplate
%_K3apps/kdevappwizard/templates/kateplugin.kdevtemplate
%_K3apps/kdevappwizard/templates/kateplugin2.kdevtemplate
%_K3apps/kdevappwizard/templates/kcmodule.kdevtemplate
%_K3apps/kdevappwizard/templates/kdedcop.kdevtemplate
%_K3apps/kdevappwizard/templates/kfileplugin.kdevtemplate
%_K3apps/kdevappwizard/templates/konqnavpanel.kdevtemplate
%_K3apps/kdevappwizard/templates/kpartapp.kdevtemplate
%_K3apps/kdevappwizard/templates/kscreensaver.kdevtemplate
%_K3apps/kdevappwizard/templates/noatunui.kdevtemplate
%_K3apps/kdevappwizard/templates/noatunvisual.kdevtemplate

%files for-pascal
#fpcgtk
%_K3apps/kdevappwizard/templates/fpchello.kdevtemplate
%_K3apps/kdevappwizard/templates/fpcsharedlib.kdevtemplate
%_K3apps/kdevappwizard/templates/pascalhello.kdevtemplate

%files for-php
%_K3apps/kdevappwizard/templates/phphello.kdevtemplate

%files for-python
%_K3apps/kdevappwizard/templates/pythonhello.kdevtemplate
%_K3apps/kdevappwizard/templates/pytk.kdevtemplate

%files for-qt
%_K3apps/kdevappwizard/templates/qmakeapp.kdevtemplate
%_K3apps/kdevappwizard/templates/qmakesimple.kdevtemplate

%files for-ruby
%_K3xdg_apps/%{rname}_ruby.desktop
%_K3apps/kdevappwizard/templates/rubyhello.kdevtemplate

%files for-wxwindows
%_K3apps/kdevappwizard/templates/wxhello.kdevtemplate


%files base
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README HACKING TODO
#%dir %_K3libdir/kdevbdb/
#%_K3libdir/kdevbdb/bin/
#%_K3libdir/kdevbdb/docs/
%_K3bindir/*
#%_iconsdir/
%_K3libdir/kconf_update_bin/*
%_K3libdir/*.so*
%exclude %_K3libdir/libkdevwidgets.so*
%_K3lib/*.so*
%exclude %_K3lib/kio_chm.so*
%exclude %_K3lib/libkchmpart.so*
%_K3xdg_dirs/kde-development-kdevelop.directory
%_K3xdg_apps/kdevassistant.desktop
%_K3xdg_apps/kdevdesigner.desktop
%_K3xdg_apps/%rname.desktop
%_K3xdg_apps/%{rname}_c_cpp.desktop
%_K3xdg_apps/%{rname}_scripting.desktop
%_K3apps/*
%exclude %_K3apps/kdevappwizard/templates/chellogba.kdevtemplate
#%exclude %_K3apps/kdevappwizard/templates/gnomeapp.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/kmod.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/qtopiaapp.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/kdevpart.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/kdevpart2.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/kdevlang.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/fpcgtk.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/pyqt.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/adahello.kdevtemplate
#%exclude %_K3apps/kdevappwizard/templates/kbear*.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/kpartplugin.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/kopart.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/superwaba.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/javahello.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/kappjava.kdevtemplate
#
%exclude %_K3apps/kdevappwizard/templates/fortranhello.kdevtemplate
#%exclude %_K3apps/kdevappwizard/templates/haskellhello.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/khello.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/kicker.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/kioslave.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/dcopservice.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/kapp.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/kateplugin.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/kateplugin2.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/kcmodule.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/kdedcop.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/kfileplugin.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/konqnavpanel.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/kpartapp.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/kscreensaver.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/noatunui.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/noatunvisual.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/fpchello.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/fpcsharedlib.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/pascalhello.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/phphello.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/pythonhello.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/pytk.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/qmakeapp.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/qmakesimple.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/rubyhello.kdevtemplate
%exclude %_K3apps/kdevappwizard/templates/wxhello.kdevtemplate
#
%_K3conf/*
%_kde3_iconsdir/*/*/*/*.*
%_K3mimelnk/application/*
%_K3srv/*
%exclude %_K3srv/chm.protocol
%exclude %_K3srv/kchmpart.desktop
%_K3srvtyp/*
%doc %_K3doc/en/%rname
%doc %_K3doc/en/kde_app_devel
%_K3mimelnk/text/*.desktop
#%_datadir/applnk/Development/*.desktop
#%_K3apps/*
#%_K3mimelnk/application/*.desktop
#%_K3srv/
#%_K3srvtyp/*.desktop
#%_K3conf/gideonrc

#%if %static
#%files devel-static
#%_K3libdir/*.la
#%_K3libdir/*.a
#%endif

%files libs
%_K3libdir/libkdevwidgets.so*

%files kio-chm
%_K3lib/kio_chm.so
%_K3lib/libkchmpart.so*
%_K3srv/chm.protocol
%_K3srv/kchmpart.desktop


%files devel
#%_K3libdir/kdevbdb/lib/
#%_K3libdir/kdevbdb/include/
%if %_keep_libtool_files
%_K3libdir/*.la
%_K3libdir/*.la
%endif
%_K3includedir/kdevelop/
%_K3includedir/kinterfacedesigner/
%doc %_K3doc/en/kdevelop-apidocs/
# temporery moved here
%_K3apps/kdevappwizard/templates/chellogba.kdevtemplate
#%_K3apps/kdevappwizard/templates/gnomeapp.kdevtemplate
%_K3apps/kdevappwizard/templates/kmod.kdevtemplate
%_K3apps/kdevappwizard/templates/qtopiaapp.kdevtemplate
%_K3apps/kdevappwizard/templates/kdevpart.kdevtemplate
%_K3apps/kdevappwizard/templates/kdevpart2.kdevtemplate
%_K3apps/kdevappwizard/templates/kdevlang.kdevtemplate
%_K3apps/kdevappwizard/templates/fpcgtk.kdevtemplate
%_K3apps/kdevappwizard/templates/pyqt.kdevtemplate
#%_K3apps/kdevappwizard/templates/kbear*.kdevtemplate
%_K3apps/kdevappwizard/templates/kpartplugin.kdevtemplate
%_K3apps/kdevappwizard/templates/kopart.kdevtemplate
%_K3apps/kdevappwizard/templates/superwaba.kdevtemplate
%_K3apps/kdevappwizard/templates/javahello.kdevtemplate
%_K3apps/kdevappwizard/templates/kappjava.kdevtemplate


%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0:3.5.5-alt4.1
- Rebuild with Python-2.7

* Tue Apr 26 2011 Sergey V Turchin <zerg@altlinux.org> 0:3.5.5-alt4
- fix build requires, requires

* Wed Mar 09 2011 Sergey V Turchin <zerg@altlinux.org> 0:3.5.5-alt3
- move to alternate place
- fix compile with gcc-4.5
- remove conflict with kdevelop

* Tue Apr 06 2010 Sergey V Turchin <zerg@altlinux.org> 0:3.5.5-alt2
- fix to build
- rename package

* Thu Oct 15 2009 Sergey V Turchin <zerg@altlinux.org> 2:3.5.5-alt1
- new version

* Mon Aug 31 2009 Sergey V Turchin <zerg@altlinux.org> 2:3.5.4-alt3
- add libncurses-devel to requires

* Mon Aug 24 2009 Sergey V Turchin <zerg@altlinux.org> 2:3.5.4-alt2
- fix requires
- fix for new libtool

* Wed Aug 19 2009 Sergey V Turchin <zerg@altlinux.org> 2:3.5.4-alt1
- new version

* Tue Aug 26 2008 Sergey V Turchin <zerg at altlinux dot org> 2:3.5.3-alt1
- new version

* Wed Feb 27 2008 Sergey V Turchin <zerg at altlinux dot org> 2:3.5.1-alt1
- new version

* Fri Oct 19 2007 Sergey V Turchin <zerg at altlinux dot org> 2:3.5.0-alt2
- fix loop in filegroup plugin

* Thu Oct 18 2007 Sergey V Turchin <zerg at altlinux dot org> 2:3.5.0-alt1
- new version

* Thu Jul 19 2007 Sergey V Turchin <zerg at altlinux dot org> 2:3.4.1-alt3
- split kio-chm to separate package
- reorganize subpackages like kde* empty *-common

* Tue May 22 2007 Sergey V Turchin <zerg at altlinux dot org> 2:3.4.1-alt2
- update tarball from ftp.kde.org

* Mon May 21 2007 Sergey V Turchin <zerg at altlinux dot org> 2:3.4.1-alt1
- new version

* Tue Jan 30 2007 Sergey V Turchin <zerg at altlinux dot org> 2:3.4.0-alt1
- new version

* Wed Oct 18 2006 Sergey V Turchin <zerg at altlinux dot org> 2:3.3.5-alt1
- new version

* Thu Sep 07 2006 Sergey V Turchin <zerg at altlinux dot org> 2:3.3.4-alt2
- fix build requires

* Tue Sep 05 2006 Sergey V Turchin <zerg at altlinux dot org> 2:3.3.4-alt1
- new version

* Wed Jun 07 2006 Sergey V Turchin <zerg at altlinux dot org> 2:3.3.3-alt1
- new version

* Wed Apr 05 2006 Sergey V Turchin <zerg at altlinux dot org> 2:3.3.2-alt1
- new version

* Thu Feb 02 2006 Sergey V Turchin <zerg at altlinux dot org> 2:3.3.1-alt1
- new version

* Wed Jan 11 2006 Sergey V Turchin <zerg at altlinux dot org> 2:3.3.0-alt2
- fix BuildRequires to support cvs

* Tue Dec 13 2005 Sergey V Turchin <zerg at altlinux dot org> 2:3.3.0-alt1
- new version

* Tue Jun 21 2005 Sergey V Turchin <zerg at altlinux dot org> 2:3.2.1-alt3
- fix linking libkdevinterfaces

* Mon Jun 20 2005 Sergey V Turchin <zerg at altlinux dot org> 2:3.2.1-alt2
- fix KChmPart linking

* Thu Jun 09 2005 Sergey V Turchin <zerg at altlinux dot org> 2:3.2.1-alt1
- new version

* Mon Apr 04 2005 Sergey V Turchin <zerg at altlinux dot org> 2:3.2.0-alt1
- new version

* Wed Jan 12 2005 Sergey V Turchin <zerg at altlinux dot org> 2:3.1.2-alt1
- new version

* Wed Nov 03 2004 Sergey V Turchin <zerg at altlinux dot org> 2:3.1.1-alt1
- new version

* Thu Jun 10 2004 Sergey V Turchin <zerg at altlinux dot org> 2:3.0.4-alt1
- new version

* Wed Apr 21 2004 Sergey V Turchin <zerg at altlinux dot org> 2:3.0.3-alt1
- new version

* Wed Mar 31 2004 Sergey V Turchin <zerg at altlinux dot org> 2:3.0.2-alt1
- split, add requires

* Thu Mar 11 2004 Sergey V Turchin <zerg at altlinux dot org> 2:3.0.2-alt0.1
- new version

* Mon Jan 12 2004 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:3.0-alt0.12
- CVS update
- link libpthread to kdevelop executable (no .la => no .so dep recursion)

* Mon Dec 29 2003 Sergey V Turchin <zerg at altlinux dot org> 2:3.0-alt0.11.1
- remove %%_libdir/*.la; fix finding kdelibs in project apps

* Sun Nov 23 2003 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:3.0-alt0.11
- update to CVS
- qmake in $PATH patch

* Sat Nov 8 2003 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:3.0-alt0.10
- gettext-tools dependency
- non-KDE menus bugfix
- update to CVS HEAD

* Fri Oct 17 2003 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:3.0-alt0.07
- exec filename changes from gideon to kdevelop
- version numbering change

* Wed Oct 15 2003 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:3.0a7-alt1
- updated to alpha7+

* Wed Sep 24 2003 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:3.0a6-alt3
- libpcre-devel python22-devel dependencies (for hasher builds)

* Mon Sep 22 2003 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:3.0a6-alt2
- add_findprov_lib_path spec fix
- removed kiconedit depencency; not to depend on Big KDE

* Fri Sep 12 2003 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:3.0a6-alt1
- new Sisyphus requirements
- updated to the current cvs version (~alpha 6)

* Thu Sep  4 2003 Sergey A. Sukiyazov <corwin@micom.net.ru> 2:3.0-ssa0.a4a
- add graphviz build requirements
- add and disable patch to set default codec via locale.
- add patch to qstring convert via locale.

* Fri Dec 20 2002 Viktor S. Grishchenko <gritzko@altlinux.ru> 3.0-a2-cvs
- total spec clean-up
- CVS update

* Fri Oct 04 2002 Gor <vg@altlinux.ru> 2:2.1.2-alt3
- spec fixes for new kde deps
- sources updated from CVS

* Fri Oct 04 2002 Gor <vg@altlinux.ru> 2:2.1.2-alt2
- rebuild with gcc-3.2 & new kdelibs

* Wed Jul 31 2002 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:2.1.2-alt1
- update from cvs (KDE_2_2_BRANCH, 2.1.2+fixes)
- removed MDK patches (obsolete)
- removed automake hack patch
- removed  kdevelop-2.1beta1-kde3.patch
- detect_alt_autoconf.patch to choose appropriate autoconf alternative

* Fri Jun 14 2002 Sergey V Turchin <zerg@altlinux.ru> 2:2.1.1-alt3
- update from cvs (KDEVELOP_2_0_BRANCH)

* Fri May 31 2002 Sergey V Turchin <zerg@altlinux.ru> 2:2.1.1-alt2
- fix missing C reference files

* Fri May 31 2002 Sergey V Turchin <zerg@altlinux.ru> 2:2.1.1-alt1
- new version

* Thu Apr 04 2002 Sergey V Turchin <zerg@altlinux.ru> 2:2.1-alt1
- new version

* Tue Mar 19 2002 Sergey V Turchin <zerg@altlinux.ru> 2:2.0.2-alt5
- add any PreReq

* Fri Feb 15 2002 Sergey V Turchin <zerg@altlinux.ru> 2:2.0.2-alt4
- sync with cooker (add patches 3-6)

* Tue Jan 22 2002 Sergey V Turchin <zerg@altlinux.ru> 2:2.0.2-alt3
- rebuild without fam
- sync with cooker (update cvs)

* Mon Dec 10 2001 Sergey V Turchin <zerg@altlinux.ru> 2:2.0.2-alt2
- fix Patch10 (QString.patch)

* Fri Dec 07 2001 Sergey V Turchin <zerg@altlinux.ru> 2:2.0.2-alt1
- new version

* Wed Nov 21 2001 Sergey V Turchin <zerg@altlinux.ru> 1:2.2-alt8
- add Patch10 from Sergey A. Sukiyazov <corwin@micom.don.ru>

* Fri Oct 12 2001 AEN <aen@logic.ru> 2.2-alt7
- rebuild with new libpng

* Fri Oct 12 2001 Sergey V Turchin <zerg@altlinux.ru> 2.2-alt6
- rebuild with new libpng

* Tue Aug 28 2001 Sergey V Turchin <zerg@altlinux.ru> 2.2-alt5
- fix broken dependences

* Fri Aug 24 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.2-alt4
- Fixed .la bug

* Fri Aug 24 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.2-alt3
- Some spec cleanup
- Added -devel package
- Fixed filelists
- Added c_cpp_reference documentation

* Mon Aug 20 2001 Sergey V Turchin <zerg@altlinux.ru> 2.2-alt2
- fixed %%serial

* Fri Aug 17 2001 Sergey V Turchin <zerg@altlinux.ru> 2.2-alt1
- build for ALT

* Tue Aug 16 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.0-2mdk
- Fix generated menu

* Wed Aug 06 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.0-1mdk
- kdevelop 2.0 for kde 2.2

* Wed Aug 01 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2-0.pre1.1mdk
- kde 2.2 pre1

* Fri Jun 29 2001 David BAUDENS <baudens@mandrakesoft.com> 2.2-0.beta1.1mdk
- KDE 2.2.beta1

* Fri Jun 08 2001 David BAUDENS <baudens@mandrakesoft.com> 2.2-0.alpha2.3mdk
- Clean ./configure
- Enable debug and don't strip when we are not in final release

* Tue May 24 2001 David BAUDENS <baudens@mandrakesoft.com> 2.2-0.alpha2.2mdk
- Re-enable debug (low level)

* Wed May 23 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2-0.alpha2.1mdk
- kdevelop 2.2 alpha2

* Tue May 02 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2-0.alpha1.1mdk
- kdevelop 2.2 alpha1

* Wed Apr 11 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4.1-3mdk
- Add requires

* Tue Apr 10 2001 David BAUDENS <baudens@mandrakesoft.com> 1.4.1-2mdk
- Move KDE menu entries in %%_datadir/applnk
- Rebuild against latest GCC

* Wed Mar 21 2001 David BAUDENS <baudens@mandrakesoft.com> 1.4.1-1mdk
- Kdevelop 1.4.1
- Disable PATH for kdelibsdoc-dir (looks in kdelibs buildroot!???)

* Sun Mar 11 2001 David BAUDENS <baudens@mandrakesoft.com> 1.4-6mdk
- Rebuild for Linux-Mandrake 8.0 Beta 2
- Rebuild against Qt 2.3.0
- Re-enable default PATH for kdelibsdoc-dir
- Clean BuildRequires

* Thu Mar  8 2001 Stefan van der Eijk <s.vandereijk@chello.nl> 1.4-5mdk
- removed BuildRequires for libreadline4

* Thu Mar 01 2001 David BAUDENS <baudens@mandrakesoft.com> 1.4-4mdk
- Requires: libjpeg-devel

* Wed Feb 28 2001 David BAUDENS <baudens@mandrakesoft.com> 1.4-3mdk
- Add BuildRequires

* Sun Feb 25 2001 David BAUDENS <baudens@mandrakesoft.com> 1.4-2mdk
- Repackage (update in KDE 2.1 sources)

* Fri Feb 23 2001 David BAUDENS <baudens@mandrakesoft.com> 1.4-1mdk
- Kdevelop 1.4

* Tue Feb 20 2001 David BAUDENS <baudens@mandrakesoft.com> 1.4-0.20010220.1mdk
- Enable --disable-debug
- Rewrite file list to fix updates
- Remove non needed %%find_lang

* Tue Feb 13 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4-0.20010213.1mdk
- Update code
- rebuild for kde > beta 2

* Thu Jan 17 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4-0.20010116.4mdk
- Fix requires

* Thu Jan 17 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4-0.20010116.3mdk
- Fix requires

* Thu Jan 16 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4-0.20010116.2mdk
- Fix requires

* Thu Jan 16 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4-0.20010116.1mdk
- initial packaging
