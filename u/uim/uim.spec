# engines
%def_with anthy
%def_with m17nlib
# lack of libraries
%def_without canna
%def_without mana
%def_without prime
%def_without sj3
%def_without skk
%def_without wnn

# toolkits and helpers
%def_enable emacs
%def_enable fep
%def_with gtk
%def_with gtk3
%def_with qt
%def_without qt4
%def_with qt5
%def_with x
%def_with xft
%def_disable gnome-applet
%def_disable gnome3-applet
%def_disable kde-applet
%def_disable kde4-applet

# misc
%def_enable dict
%def_with libedit
%def_with libnotify
# not tested
%def_disable curl
%def_disable expat
%def_disable ffi
%def_disable openssl
%def_disable sqlite3

Name: uim
Version: 1.8.9
Release: alt1

Summary: useful input method

License: BSD
Group: Text tools
Url: https://github.com/uim/uim

# git://github.com/uim/uim.git
Source0: uim.tar
# git://github.com/uim/sigscheme.git
Source1: sigscheme.tar
# git://git.altlinux.org/gears/u/uim.git
Source2: uim-alt.tar

Patch1: 0001-uim.desktop.in.in-use-generic-uim-pref.patch
Patch2: 0002-pixmaps-uim-m17nlib-relink-icons.in-fix-m17n-db-icon.patch
Patch3: 0003-uim-uim-module-manager.c-fix-installed-modules-locat.patch
Patch4: 0004-ALT-fix-build-qt5.patch
Patch5: 0001-Bump-version.patch
Patch6: 0001-Fix-version.patch
Patch7: 0001-skk-Fix-numeric-converted-string-not-null-terminated.patch
Patch8: 0001-configure-Fix-snprintf-check-for-strict-er-C99-compi.patch

BuildRequires(pre): alternatives
BuildRequires: asciidoc intltool ruby ruby-stdlibs libgcroots-devel librsvg-utils
%{?_with_libnotify:BuildRequires: libnotify-devel cmake extra-cmake-modules rpm-macros-cmake}
%{?_with_anthy:BuildRequires: libanthy-devel}
%{?_with_libedit:BuildRequires: libedit-devel}
%{?_enable_fep:BuildRequires: libncursesw-devel}
%{?_with_gtk:BuildRequires: libgtk+2-devel}
%{?_with_gtk3:BuildRequires: libgtk+3-devel}
%{?_with_m17nlib:BuildRequires: libm17n-devel libm17n-db}
%{?_with_qt:BuildRequires: libqt3-devel gcc-c++}
%{?_with_qt4:BuildRequires: libqt4-devel gcc-c++ cmake extra-cmake-modules rpm-macros-cmake}
%{?_with_qt5:BuildRequires: qt5-base-devel qt5-x11extras-devel gcc-c++ cmake extra-cmake-modules rpm-macros-cmake qt5-declarative-devel}
%{?_with_x:BuildRequires: gcc-c++ libXext-devel libXft-devel}
%{?_with_xft:BuildRequires: libXft-devel}
%{?_enable_emacs:BuildRequires: /usr/bin/emacs emacs-devel}

%{?_with_gtk:Requires: uim-gtk}
%{?_with_gtk3:Requires: uim-gtk3}
%{?_with_qt4:Requires: uim-qt4}
%{?_with_qt5:Requires: uim-qt5}
%{?_with_x:Requires: uim-xim}
Requires: uim-plugins
%{?_with_gtk:Requires: uim-pref}

%define common_descr uim is a multilingual input method library and environment.\
\
Its goal is to provide simple, easily extensible and high code-quality\
input method development platform, and useful input method environment\
for users of desktop and embedded platforms.

%description
%common_descr

This is metapackage for install uim for basic graphical toolkit and
plugins. You may want to install additional package with other tookits
and modules support. For documentaion refer to library package
libuim8.

%package data
Summary: useful input method common files
Group: Text tools
Provides: uim-common
Obsoletes: uim-common
Provides: libuim-data
Obsoletes: libuim-data
BuildArch: noarch
%{?_with_m17nlib:Requires: libm17n-db}

%description data
%common_descr

This package contains the data files for uim.

%package -n libuim-devel
Summary: Development and header files for universal input method library
Group: Text tools

%description -n libuim-devel
%common_descr

Development and header files for universal input method.

%package -n libuim8
Summary: universal input method library
Group: Text tools
Requires: uim-data
Requires: uim-plugins
Requires: uim-utils
%{?_without_qt4:Obsoletes: uim-qt4 < %version}

%description -n libuim8
%common_descr

This package contains the shared libraries for universal input method.

%package -n libuim-custom2
Summary: universal input method uim-custom API library
Group: Text tools

%description -n libuim-custom2
%common_descr

This package contains universal input method uim-custom API library.

%package plugins
Summary: universal input method data files
Provides: libuim-plugin
Obsoletes: libuim-plugin
Provides: uim-m17nlib
Obsoletes: uim-m17nlib
Group: Text tools
Requires(post): uim-utils
Requires(preun): uim-utils
# needed for m17nlib engine
%{?_with_m17nlib:Requires: libm17n, libm17n-db}

%description plugins
%common_descr

This package contains the plugin files for uim.

%package pref
Summary: universal input method pref
Group: Text tools
Requires: uim-pref-gtk

%description pref
%common_descr

This package contains preferences tool for uim.

%package -n libuim-scm0
Summary: universal input method API uim-scm library
Group: Text tools

%description -n libuim-scm0
%common_descr

This package contains universal input method API uim-scm library.

%if_enabled emacs
%package -n emacs-uim
Summary: EMACS module for universal input method
Group: Text tools
Provides: uim-emacs
Obsoletes: uim-emacs

%description -n emacs-uim
%common_descr

EMACS module for universal input method.

%package -n emacs-uim-el
Summary: EMACS Lisp sources for universal input method module
Group: Text tools
Requires: emacs-uim

%description -n emacs-uim-el
%common_descr

EMACS module for universal input method. This package contains EMACS Lisp
sources.
%endif # emacs

%package pref-gtk
Summary: universal input method preferences (GTK+ 2.0 UI)
Group: Text tools
Provides: /usr/bin/uim-pref

%description pref-gtk
%common_descr

Preferences used GTK+ 2.0 interface.

%package pref-gtk3
Summary: universal input method preferences (GTK+ 3.0 UI)
Group: Text tools
Provides: /usr/bin/uim-pref

%description pref-gtk3
%common_descr

Preferences used GTK+ 3.0 interface.

%package pref-qt
Summary: universal input method preferences (Qt 3 UI)
Group: Text tools
Provides: /usr/bin/uim-pref

%description pref-qt
%common_descr

Preferences used Qt 3 interface.

%package pref-qt4
Summary: universal input method preferences (Qt 4 UI)
Group: Text tools
Provides: /usr/bin/uim-pref

%description pref-qt4
%common_descr

Preferences used Qt 4 interface.

%package pref-qt5
Summary: universal input method preferences (Qt 5 UI)
Group: Text tools
Provides: /usr/bin/uim-pref

%description pref-qt5
%common_descr

Preferences used Qt 5 interface.

%if_enabled fep
%package fep
Summary: fep module for universal input method
Group: Text tools

%description fep
%common_descr

fep module for universal input method.
%endif # fep

%if_with gtk
%package gtk
Summary: GTK+ 2.0 universal input method universal input method
Group: Text tools
Requires: uim-xim

%description gtk
%common_descr

This package contains an IM-module to support the use of uim on GTK+2.0
applications.
%endif # gtk

%if_with gtk3
%package gtk3
Summary: GTK+3 module for universal input method
Group: Text tools
Requires: uim-xim

%description gtk3
%common_descr

This package contains an IM-module to support the use of uim on GTK+3.0
applications.
%endif # gtk3

%if_with qt
%package qt
Summary: Qt3 module for universal input method
Group: Text tools
Requires: uim-xim

%description qt
%common_descr

Qt3 module for universal input method.
%endif # qt

%if_with qt4
%package qt4
Summary: Qt4 module for universal input method
Group: Text tools
Requires: uim-xim

%description qt4
%common_descr

Qt4 module for universal input method.
%endif # qt4

%if_with qt5
%package qt5
Summary: Qt5 module for universal input method
Group: Text tools
Requires: uim-xim

%description qt5
%common_descr

Qt5 module for universal input method.
%endif # qt5

%package utils
Summary: utils for universal input method
Requires: uim-data
Group: Text tools

%description utils
%common_descr

This package contains additional utils for uim.

%if_with x
%package xim
Summary: XIM module for universal input method
Group: Text tools
Requires: uim-gtk

%description xim
%common_descr

XIM module for universal input method.
%endif # x

%prep
%setup -n uim -a1 -a2
%autopatch -p1

%build
%define _optlevel 1
%autoreconf
%configure \
	--disable-rpath \
	--disable-static \
	%{subst_enable dict} \
	%{subst_enable emacs} \
	%{subst_enable fep} \
	%{subst_enable gnome3-applet} \
	%{subst_enable gnome-applet} \
	%{subst_enable kde4-applet} \
	%{subst_enable kde-applet} \
	%{subst_with anthy} \
	%{subst_with canna} \
	%{subst_with eb} \
	%{subst_with expat} \
	%{subst_with ffi} \
	%{subst_with gtk} \
	%{subst_with gtk3} \
	%{subst_with libedit} \
	%{subst_with m17nlib} \
	%{subst_with mana} \
	%{subst_with openssl} \
	%{subst_with prime} \
	%{subst_with qt} \
	%{subst_with qt4} \
	%{subst_with qt5} \
	%{subst_with sj3} \
	%{subst_with skk} \
	%{subst_with sqlite3} \
	%{subst_with wnn} \
	%{subst_with x} \
	%{subst_with xft} \
	%{?_with_qt:%%{?_with_qt4:--enable-qt4-qt3support}} \
	%{?_with_qt:--with-qt-immodule} \
	%{?_with_qt4:--with-qt4-immodule} \
	%{?_with_qt5:--with-qt5-immodule} \
%if_with gtk
	--enable-pref \
%endif # gtk
	--enable-nls \
	--with-libgcroots=installed \
	--enable-notify=stderr%{?_with_libnotify:,libnotify} \
	--enable-conf=uim \
	--enable-maintainer-mode \
	#
# need for ruby scripts
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export LC_ALL=en_US.UTF-8
%make_build

%install
%makeinstall_std
%find_lang %name

%if_enabled emacs
mkdir -p %buildroot%_emacs_sitestart_dir
install -m0644 alt/uim.el -t %buildroot%_emacs_sitestart_dir

# compile emacs lisp
pushd %buildroot%_datadir/emacs/site-lisp/uim-el
	for i in $(find . -name "*.el"); do
		emacs -no-site-file -q -batch -eval '(setq load-path (cons "." load-path))' -f batch-byte-compile $i
	done
popd
%endif # emacs

%if_with m17nlib
install -pD -m755 alt/uim-m17nlib-icons.filetrigger -t %buildroot%_rpmlibdir
%endif

mkdir -p %buildroot%_sysconfdir/X11/xinit/xinput.d/
install -pm644 alt/xinput %buildroot%_sysconfdir/X11/xinit/xinput.d/uim.conf

# alternatives
mkdir -p %buildroot%_altdir
%{?_with_gtk:install -p -m644 alt/uim-pref-gtk %buildroot%_altdir/uim-pref-gtk}
%{?_with_gtk3:install -p -m644 alt/uim-pref-gtk3 %buildroot%_altdir/uim-pref-gtk3}
%{?_with_qt:install -p -m644 alt/uim-pref-qt %buildroot%_altdir/uim-pref-qt}
%{?_with_qt4:install -p -m644 alt/uim-pref-qt4 %buildroot%_altdir/uim-pref-qt4}
%{?_with_qt5:install -p -m644 alt/uim-pref-qt5 %buildroot%_altdir/uim-pref-qt5}

# ghost files
mkdir -p %buildroot%_localstatedir/uim
touch %buildroot%_localstatedir/uim/installed-modules.scm
touch %buildroot%_localstatedir/uim/loader.scm

find %buildroot%_libdir -type f -name \*\.la -delete

%post plugins
# $1 is equal to 2 when package is upgrading
if [ $1 -eq 2 ]; then
        # We shouldn't remove all the modules but it's OK while every avalible
	# modules are shipping in uim-plugins. Otherwise, it should be fixed.
	/usr/bin/uim-module-manager --unregister-all
fi
/usr/bin/uim-module-manager --register

%preun plugins
# package is removing
if [ $1 -eq 0 ]; then
        # We shouldn't remove all the modules but it's OK while every avalible
	# modules are shipping in uim-plugins. Otherwise, it should be fixed.
	/usr/bin/uim-module-manager --unregister-all
fi

%files

%files data -f %name.lang
%dir %_datadir/uim
%_datadir/uim
%_rpmlibdir/uim-m17nlib-icons.filetrigger
%exclude %_datadir/%name/m17nlib.scm
%exclude %_datadir/%name/m17nlib-custom.scm

%if_enabled emacs
%files -n emacs-uim
%doc alt/UIMEl
%_bindir/uim-el-agent
%_bindir/uim-el-helper-agent
%_datadir/emacs/site-lisp/uim-el/*.elc
%_emacs_sitestart_dir/uim.el
%exclude %_datadir/emacs/site-lisp/uim-el/*.el

%files -n emacs-uim-el
%_datadir/emacs/site-lisp/uim-el/*.el
%endif # emacs

%if_with gtk
%files pref
%_datadir/applications/uim.desktop

%files pref-gtk
%_altdir/uim-pref-gtk
%_bindir/uim-pref-gtk
%_bindir/uim-toolbar-gtk
%_bindir/uim-toolbar-gtk-systray
%endif # gtk

%if_with gtk3
%files pref-gtk3
%_altdir/uim-pref-gtk3
%_bindir/uim-pref-gtk3
%_bindir/uim-toolbar-gtk3
%_bindir/uim-toolbar-gtk3-systray
%endif # gtk3

%if_with qt
%files pref-qt
%_altdir/uim-pref-qt
%_bindir/uim-pref-qt
%_bindir/uim-toolbar-qt
%endif # qt

%if_with qt4
%files pref-qt4
%_altdir/uim-pref-qt4
%_bindir/uim-pref-qt4
%_bindir/uim-toolbar-qt4
%endif # qt4

%if_with qt5
%files pref-qt5
%_altdir/uim-pref-qt5
%_bindir/uim-pref-qt5
%_bindir/uim-toolbar-qt5
%endif # qt5

%if_enabled fep
%files fep
%_bindir/uim-fep
%_bindir/uim-fep-tick
%doc alt/UIMFep
%endif # fep

%files -n libuim-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/uim.pc

%files -n libuim8
%doc AUTHORS COPYING NEWS README RELNOTE
%doc alt/UimSystemConfiguration
%_libdir/libuim.so.8
%_libdir/libuim.so.8.*
%_localstatedir/uim
%ghost %_localstatedir/uim/installed-modules.scm
%ghost %_localstatedir/uim/loader.scm

%files -n libuim-custom2
%_libdir/libuim-custom.so.2
%_libdir/libuim-custom.so.2.*

%files plugins
%doc AUTHORS COPYING NEWS README RELNOTE
%if_with libnotify
%_libdir/uim/notify
%endif # libnotify
%_libdir/uim/plugin/*.so
%dir %_libdir/uim
%dir %_libdir/uim/plugin
%if_with m17nlib
%_libdir/%name/plugin/libuim-m17nlib.so
%_datadir/%name/m17nlib.scm
%_datadir/%name/m17nlib-custom.scm
%endif # m17nlib

%files -n libuim-scm0
%_libdir/libuim-scm.so.0
%_libdir/libuim-scm.so.0.*

%if_with gtk
%files gtk
%if_enabled dict
%_bindir/uim-dict-gtk
%endif # dict
%_bindir/uim-im-switcher-gtk
%_bindir/uim-input-pad-ja
%_libdir/gtk-2.0/2.10.0/immodules/im-uim.so
%_libexecdir/uim-candwin-gtk
%_libexecdir/uim-candwin-horizontal-gtk
%_libexecdir/uim-candwin-tbl-gtk
%endif # gtk

%if_with gtk3
%files gtk3
%if_enabled dict
%_bindir/uim-dict-gtk3
%endif # dict
%_bindir/uim-im-switcher-gtk3
%_bindir/uim-input-pad-ja-gtk3
%_libdir/gtk-3.0/3.0.0/immodules/im-uim.so
%_libexecdir/uim-candwin-gtk3
%_libexecdir/uim-candwin-horizontal-gtk3
%_libexecdir/uim-candwin-tbl-gtk3
%endif # gtk3

%if_with qt
%files qt
%_bindir/uim-chardict-qt
%_bindir/uim-im-switcher-qt
%_libexecdir/uim-candwin-qt
%_libdir/qt3/plugins/inputmethods/libquiminputcontextplugin.so
%endif # qt

%if_with qt4
%files qt4
%_bindir/uim-chardict-qt4
%_bindir/uim-im-switcher-qt4
%_libdir/qt4/plugins/inputmethods/libuiminputcontextplugin.so
%_libexecdir/uim-candwin-qt4
%endif # qt4

%if_with qt5
%files qt5
%_bindir/uim-chardict-qt5
%_bindir/uim-im-switcher-qt5
%_libdir/qt5/plugins/platforminputcontexts/libuimplatforminputcontextplugin.so
%_libexecdir/uim-candwin-qt5
%endif # qt5

%files utils
%_bindir/uim-help
%{?_with_m17nlib:%_bindir/uim-m17nlib-relink-icons}
%_bindir/uim-module-manager
%_bindir/uim-sh
%_libexecdir/uim-helper-server

%if_with x
%files xim
%config %_sysconfdir/X11/xinit/xinput.d/uim.conf
%_bindir/uim-xim
%_mandir/man1/uim-xim.1.xz
%endif

%changelog
* Sun Aug 21 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.8.9-alt1
- Updated UIM to 1.8.9.
- Built without Qt4 support.

* Thu Dec 16 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.8.8.0.50.d1ac9d931-alt2
- Fixed FTBFS.

* Thu Jan 21 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.8.8.0.50.d1ac9d931-alt1
- Updated UIM to 1.8.8-50-gd1ac9d931.

* Wed Dec 23 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.8.8.0.49.git49d1515ce-alt2
- Fixed alternatives weight for uim-pref.

* Sat Sep 26 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.8.8.0.49.git49d1515ce-alt1
- Updated UIM to 1.8.8-49-g49d1515ce.
- Updated SigScheme to 0.9.1-2-gccf1f92d6.

* Tue Apr 14 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.8.8.0.33.git3be53b4-alt1
- Updated UIM to 1.8.8-33-g3be53b423.
- Updated SigScheme to 0.9.0-4-gfbd7fc82b.

* Sat May 04 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.8.8-alt2
- emacs-uim: packaged compiled EMACS lisp
- separated emacs-uim-el subpackage with EMACS lisp sources
- fixed build without gtk, gtk3, qt, qt4 and qt5 knobs

* Sun May 20 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.8.8-alt1
- 1.8.8
- uim-emacs -> emacs-uim (Emacs packaging policy)
- uim-plugin -> uim-plugins
- uim-common, libuim-data -> uim-data
- uim-m17nlib was included to uim-plugins
- added uim.el site-start script to emacs-uim
- added alternatives for uim-pref
- added filetrigger to relink m17n-db icons
- fixed modules location path
- added xinput.d/uim.conf to uim-xim
- revisited interpackage dependencies

* Mon Oct 23 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.8.6-alt4.git89542ac.2
- uim-qt5: rebuilt to work with new Qt5 version (5.9.2)

* Thu May 11 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.8.6-alt4.git89542ac.1
- rebuilt with libm17n-db
- moved %%_datadir/applications/uim.desktop to uim-gtk package
- fixed dependencies

* Sat Dec 10 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.8.6-alt4.git89542ac
- import from upsteam git

* Sat Apr  9 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.8.6-alt3
- fix menu-related additional categories in uim.desktop

* Fri Mar 25 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.8.6-alt2
- mark uim-common and libuim-data packages as noarch
- split libuim-plugin from libuim-data package

* Wed Mar 9 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.8.6-alt1
- initial build
