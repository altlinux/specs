Name: uim
Version: 1.8.6
Release: alt4.git89542ac

Summary: useful input method metapackage

License: BSD
Group: Text tools
Url: https://code.google.com/p/uim/

Packager: Vladimir D. Seleznev <vseleznv@altlinux.org>
Source: %name.tar
Source1: sigscheme.tar
Source2: UimSystemConfiguration
Source3: UIMFep
Source4: UIMEl

# Automatically added by buildreq on Sat Dec 10 2016
# optimized out: at-spi2-atk fontconfig fontconfig-devel gcc-c++ glib-networking glib2-devel gnu-config libGL-devel libICE-devel libX11-devel libXext-devel libXft-devel libXrender-devel libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libncurses-devel libpango-devel libqt3-settings libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-qt3support libqt4-sql libqt4-xml libqt5-core libqt5-gui libqt5-widgets libqt5-x11extras libstdc++-devel libtinfo-devel libwayland-client libwayland-cursor libwayland-egl libwayland-server perl perl-Encode pkg-config python-base python-modules qt5-base-devel qt5-declarative-devel shared-mime-info xorg-kbproto-devel xorg-renderproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: asciidoc intltool libanthy-devel libedit-devel libgcroots-devel libgtk+2-devel libgtk+3-devel libm17n-devel libnotify-devel libqt3-devel libqt4-webkit-devel librsvg-utils phonon-devel qt5-tools-devel qt5-wayland-devel qt5-x11extras-devel ruby ruby-stdlibs

# BuildRequires: asciidoc-a2x
# BuildRequires: ruby-tools ruby-stdlibs ruby-rip
# BuildRequires: librsvg-utils

Requires: uim-fep   = %version-%release
Requires: uim-gtk   = %version-%release
Requires: uim-gtk3  = %version-%release
Requires: uim-qt4   = %version-%release
Requires: uim-qt5   = %version-%release
Requires: uim-utils = %version-%release
Requires: uim-xim   = %version-%release
Requires: uim-m17nlib   = %version-%release

%define common_descr uim is a multilingual input method library and environment. \
\
Its goal is to provide simple, easily extensible and high code-quality \
input method development platform, and useful input method environment \
for users of desktop and embedded platforms.

%description
%common_descr

This is metapackage.

%package common
Summary: useful input method common files
Group: Text tools
BuildArch: noarch

%description common
%common_descr

This package contains common files for the uim packages.

%package -n libuim-devel
Summary: Development and header files for universal input method library
Group: Text tools
Requires: libuim8 = %version-%release

%description -n libuim-devel
%common_descr

Development and header files for universal input method.

%package -n libuim8
Summary: universal input method library
Group: Text tools
Requires: libuim-custom2 = %version-%release
Requires: libuim-data    = %version-%release
Requires: libuim-scm0    = %version-%release
Requires: uim-common     = %version-%release

%description -n libuim8
%common_descr

This package contains the shared libraries for universal input method.

%package -n libuim-custom2
Summary: universal input method uim-custom API library
Group: Text tools

%description -n libuim-custom2
%common_descr

This package contains universal input method uim-custom API library.

%package -n libuim-data
Summary: universal input method data files
Group: Text tools
Requires: libuim-plugin
BuildArch: noarch

%description -n libuim-data
%common_descr

This package contains the data files for uim.

%package -n libuim-plugin
Summary: universal input method data files
Group: Text tools

%description -n libuim-plugin
%common_descr

This package contains the plugin files for uim.

%package -n libuim-scm0
Summary: universal input method API uim-scm library
Group: Text tools

%description -n libuim-scm0
%common_descr

This package contains universal input method API uim-scm library.

%package emacs
Summary: EMACS module for universal input method
Group: Text tools
Requires: libuim8 = %version-%release
Requires: uim-utils = %version-%release

%description emacs
%common_descr

EMACS module for universal input method.

%package fep
Summary: fep module for universal input method
Group: Text tools
Requires: libuim8 = %version-%release
Requires: uim-utils = %version-%release

%description fep
%common_descr

fep module for universal input method.

%package gtk
Summary: GTK+ 2.0 universal input method universal input method
Group: Text tools
Requires: libuim8 = %version-%release
Requires: uim-utils = %version-%release

%description gtk
%common_descr

This package contains an IM-module to support the use of uim on GTK+2.0
applications.

%package gtk3
Summary: GTK+3 module for universal input method
Group: Text tools
Requires: libuim8 = %version-%release
Requires: uim-utils = %version-%release

%description gtk3
%common_descr

This package contains an IM-module to support the use of uim on GTK+3.0
applications.

%package m17nlib
Summary: m17nlib plugin for universal input method
Group: Text tools
Requires: libuim8 = %version-%release
Requires: uim-utils = %version-%release

%description m17nlib
%common_descr

m17nlib plugin for universal input method.

%package qt
Summary: Qt3 module for universal input method
Group: Text tools
Requires: libuim8 = %version-%release
Requires: uim-utils = %version-%release

%description qt
%common_descr

Qt3 module for universal input method.

%package qt4
Summary: Qt4 module for universal input method
Group: Text tools
Requires: libuim8 = %version-%release
Requires: uim-utils = %version-%release

%description qt4
%common_descr

Qt4 module for universal input method.

%package qt5
Summary: Qt5 module for universal input method
Group: Text tools
Requires: libuim8 = %version-%release
Requires: uim-utils = %version-%release

%description qt5
%common_descr

Qt5 module for universal input method.

%package utils
Summary: universal input method utilities
Group: Text tools
Requires: uim-common = %version-%release

%description utils
%common_descr

This package contains a shell interpreter, IPC server, etc.

%package xim
Summary: XIM module for universal input method
Group: Text tools
Requires: libuim8 = %version-%release
Requires: uim-utils = %version-%release

%description xim
%common_descr

XIM module for universal input method.

%prep
%setup -n %name -a 1
cp %SOURCE2 .
cp %SOURCE3 .
cp %SOURCE4 .

%build
./autogen.sh
pushd sigscheme
	./autogen.sh
popd

%configure \
	--enable-dict \
	--enable-notify=libnotify \
	--enable-qt4-qt3support \
	--with-m17nlib \
	--with-qt \
	--with-qt-immodule \
	--with-qt4 \
	--with-qt4-immodule \
	--with-qt5 \
	--with-qt5-immodule \
	--with-libgcroots=installed \
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

%files

%files common
%_datadir/applications/uim.desktop
%_datadir/uim/pixmaps/*
%_datadir/uim/helperdata/*
%_datadir/uim/byeoru-data/*
%_datadir/uim/tables/*
%dir %_datadir/uim/pixmaps
%dir %_datadir/uim/helperdata
%dir %_datadir/uim/byeoru-data
%dir %_datadir/uim/tables
%doc AUTHORS
%doc COPYING
%doc NEWS
%doc README
%doc RELNOTE
%doc UimSystemConfiguration

%files emacs
%_bindir/uim-el-agent
%_bindir/uim-el-helper-agent
%_datadir/emacs/*
%doc UIMEl

%files fep
%_bindir/uim-fep
%_bindir/uim-fep-tick
%doc UIMFep

%files -n libuim-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/uim.pc

%files -n libuim8
%_libdir/libuim.so.8
%_libdir/libuim.so.8.*

%files -n libuim-custom2
%_libdir/libuim-custom.so.2
%_libdir/libuim-custom.so.2.*

%files -n libuim-data -f %name.lang
%_datadir/uim/*.scm
%_datadir/uim/lib/*
%dir %_datadir/uim
%dir %_datadir/uim/lib
%exclude %_datadir/%name/m17nlib.scm
%exclude %_datadir/%name/m17nlib-custom.scm

%files -n libuim-plugin
%_libdir/uim/notify/*.so
%_libdir/uim/plugin/*.so
%dir %_libdir/uim
%dir %_libdir/uim/notify
%dir %_libdir/uim/plugin
%exclude %_libdir/%name/plugin/libuim-m17nlib.so

%files -n libuim-scm0
%_libdir/libuim-scm.so.0
%_libdir/libuim-scm.so.0.*

%files gtk
%_bindir/uim-dict-gtk
%_bindir/uim-im-switcher-gtk
%_bindir/uim-input-pad-ja
%_bindir/uim-pref-gtk
%_bindir/uim-toolbar-gtk
%_bindir/uim-toolbar-gtk-systray
%_libdir/gtk-2.0/2.10.0/immodules/im-uim.so
%_libexecdir/uim-candwin-gtk
%_libexecdir/uim-candwin-horizontal-gtk
%_libexecdir/uim-candwin-tbl-gtk

%files gtk3
%_bindir/uim-dict-gtk3
%_bindir/uim-im-switcher-gtk3
%_bindir/uim-input-pad-ja-gtk3
%_bindir/uim-pref-gtk3
%_bindir/uim-toolbar-gtk3
%_bindir/uim-toolbar-gtk3-systray
%_libdir/gtk-3.0/3.0.0/immodules/im-uim.so
%_libexecdir/uim-candwin-gtk3
%_libexecdir/uim-candwin-horizontal-gtk3
%_libexecdir/uim-candwin-tbl-gtk3

%files m17nlib
%_bindir/uim-m17nlib-relink-icons
%_libdir/%name/plugin/libuim-m17nlib.so
%_datadir/%name/m17nlib.scm
%_datadir/%name/m17nlib-custom.scm

%files qt
%_bindir/uim-chardict-qt
%_bindir/uim-im-switcher-qt
%_bindir/uim-pref-qt
%_bindir/uim-toolbar-qt
%_libexecdir/uim-candwin-qt
%_libdir/qt3/plugins/inputmethods/libquiminputcontextplugin.so

%files qt4
%_bindir/uim-chardict-qt4
%_bindir/uim-im-switcher-qt4
%_bindir/uim-pref-qt4
%_bindir/uim-toolbar-qt4
%_libdir/qt4/plugins/inputmethods/libuiminputcontextplugin.so
%_libexecdir/uim-candwin-qt4

%files qt5
%_bindir/uim-chardict-qt5
%_bindir/uim-im-switcher-qt5
%_bindir/uim-pref-qt5
%_bindir/uim-toolbar-qt5
%_libdir/qt5/plugins/platforminputcontexts/libuimplatforminputcontextplugin.so
%_libexecdir/uim-candwin-qt5

%files utils
%_bindir/uim-help
%_bindir/uim-module-manager
%_bindir/uim-sh
%_libexecdir/uim-helper-server

%files xim
%_bindir/uim-xim
%_mandir/man1/uim-xim.1.xz

%changelog
* Sat Dec 10 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.8.6-alt4.git89542ac
- import from upsteam git

* Sat Apr  9 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.8.6-alt3
- fix menu-related additional categories in uim.desktop

* Fri Mar 25 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.8.6-alt2
- mark uim-common and libuim-data packages as noarch
- split libuim-plugin from libuim-data package

* Wed Mar 9 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.8.6-alt1
- initial build
