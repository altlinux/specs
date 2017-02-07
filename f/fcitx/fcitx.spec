# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%define _xinputconf %_sysconfdir/X11/xinit/xinput.d/fcitx.conf
%{!?gtk2_binary_version: %define gtk2_binary_version %(pkg-config  --variable=gtk_binary_version gtk+-2.0)}
%{!?gtk3_binary_version: %define gtk3_binary_version %(pkg-config  --variable=gtk_binary_version gtk+-3.0)}

Name: fcitx
Summary: Free Chinese Input Toy for X (XIM)
Version: 4.2.7
Release: alt2.1.1
License: GPLv2+
Group: Graphical desktop/Other
Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: http://code.google.com/p/%name/
Source0: http://%name.googlecode.com/files/%name-%{version}_dict.tar.xz
Source1: xinput-%name
BuildRequires: pango-devel libdbus-devel opencc-devel
BuildRequires: wget intltool chrpath sysconftool opencc
BuildRequires: ctest cmake libtool doxygen libicu-devel
BuildRequires: qt4-devel libgtk+3-devel gtk2-devel libicu
BuildRequires: xorg-bigreqsproto-devel xorg-compositeproto-devel xorg-damageproto-devel xorg-dmxproto-devel xorg-evieproto-devel xorg-fixesproto-devel xorg-fontsproto-devel xorg-glproto-devel xorg-inputproto-devel xorg-kbproto-devel xorg-pmproto-devel xorg-randrproto-devel xorg-recordproto-devel xorg-renderproto-devel xorg-resourceproto-devel xorg-scrnsaverproto-devel xorg-videoproto-devel xorg-xcbproto-devel xorg-xcmiscproto-devel xorg-xextproto-devel xorg-xf86bigfontproto-devel xorg-xf86dgaproto-devel xorg-xf86driproto-devel xorg-xf86rushproto-devel xorg-xf86vidmodeproto-devel xorg-xineramaproto-devel xorg-xproto-devel xorg-xtrans-devel
BuildRequires: gobject-introspection-devel libxkbfile-devel
BuildRequires: libenchant-devel iso-codes-devel libicu-devel
BuildRequires: libX11-devel qt-x11 libdbus-glib-devel dbus-tools-gui
BuildRequires: desktop-file-utils libxml2-devel
BuildRequires: lua-devel
Requires: %name-data = %version-%release
Requires: imsettings
Requires(post):		alternatives
Requires(postun):	alternatives
Requires: %name-libs = %version-%release
Requires: %name-gtk3 = %version-%release
Requires: %name-gtk2 = %version-%release
Source44: import.info

%description
FCITX(Free Chinese Input Toy of X) is a collection of Simplified Chinese
input methods for Linux. It supports Pinyin, QuWei and Table-based input
methods. It's small and fast.

%package data
Summary: Data files of FCITX
Group: System/Libraries
BuildArch: noarch

%description data
The %name-data package provides shared datas for FCITX.

%package libs
Summary: Shared libraries for FCITX
Group: System/Libraries
Provides: %name-keyboard = %version-%release
Obsoletes: %name-keyboard =< 4.2.3

%description libs
The %name-libs package provides shared libraries for FCITX

%package devel
Summary: Development files for FCITX
Group: Development/C
Requires: %name-libs = %version-%release

%description devel
The %name-devel package contains libraries and header files necessary for
developing programs using FCITX libraries.

%package table-chinese
Summary: Chinese table of FCITX
Group: System/Libraries
BuildArch: noarch
Requires: %name-table = %version-%release

%description table-chinese
The %name-table-chinese package provides other Chinese table for FCITX.

%package gtk2
Summary: FCITX im module for gtk2
Group: System/Libraries
Requires: %name = %version-%release
Requires: %name-libs = %version-%release

%description gtk2
This package contains fcitx im module for gtk2.

%package gtk3
Summary: FCITX im module for gtk3
Group: System/Libraries
Requires: %name = %version-%release
Requires: %name-libs = %version-%release
Requires: imsettings-gnome

%description gtk3
This package contains fcitx im module for gtk3.

%package qt4
Summary: FCITX im module for qt4
Group: System/Libraries
Requires: %name = %version-%release
Requires: %name-libs = %version-%release

%description qt4
This package contains fcitx im module for qt4.

%package pinyin
Summary: Pinyin Engine for Fcitx
Group: System/Libraries
Requires: %name = %version-%release
Requires: %name-libs = %version-%release
Requires: %name-data = %version-%release

%description pinyin
This package contains pinyin engine for fcitx.

%package qw
Summary: Quwei Engine for Fcitx
Group: System/Libraries
Requires: %name = %version-%release
Requires: %name-libs = %version-%release
Requires: %name-data = %version-%release

%description qw
This package contains quwei engine for fcitx.

%package table
Summary: Table Engine for Fcitx
Group: System/Libraries
Requires: %name = %version-%release
Requires: %name-libs = %version-%release
Requires: %name-data = %version-%release
Requires: %name-pinyin = %version-%release

%description table
This package contains table engine for fcitx.

%prep
%setup

%build
mkdir -p build
pushd build
%fedora_cmake .. -DENABLE_GTK3_IM_MODULE=On -DENABLE_QT_IM_MODULE=On -DENABLE_OPENCC=On -DENABLE_LUA=On -DENABLE_GIR=On -DENABLE_XDGAUTOSTART=Off
make VERBOSE=1 %{?_smp_mflags}

%install
pushd build
make install INSTALL="install -p" DESTDIR=$RPM_BUILD_ROOT
rm -f %buildroot%_libdir/*.la
popd

install -pm 644 -D %SOURCE1 %buildroot%_xinputconf

%find_lang %name

desktop-file-install --delete-original \
  --dir $RPM_BUILD_ROOT%_datadir/applications \
  $RPM_BUILD_ROOT%_datadir/applications/%name-skin-installer.desktop

desktop-file-install --delete-original \
  --dir $RPM_BUILD_ROOT%_datadir/applications \
  $RPM_BUILD_ROOT%_datadir/applications/%name-configtool.desktop

desktop-file-install --delete-original \
  --dir $RPM_BUILD_ROOT%_datadir/applications \
  $RPM_BUILD_ROOT%_datadir/applications/%name.desktop
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xinputrc_fcitx<<EOF
%_sysconfdir/X11/xinit/xinputrc	%_xinputconf	55
EOF

%files -f %name.lang
%_altdir/xinputrc_fcitx
%doc AUTHORS ChangeLog THANKS TODO COPYING
%config %_xinputconf
%_bindir/fcitx-*
%_bindir/fcitx
%_bindir/createPYMB
%_bindir/mb2org
%_bindir/mb2txt
%_bindir/readPYBase
%_bindir/readPYMB
%_bindir/scel2org
%_bindir/txt2mb
%_datadir/applications/%name-skin-installer.desktop
%_datadir/%name/dbus/daemon.conf
%_datadir/applications/%name-configtool.desktop
%_datadir/applications/%name.desktop
%_datadir/mime/packages/x-fskin.xml
%_docdir/%name/
%_mandir/man1/createPYMB.1*
%_mandir/man1/fcitx-remote.1*
%_mandir/man1/fcitx.1*
%_mandir/man1/mb2org.1*
%_mandir/man1/mb2txt.1*
%_mandir/man1/readPYBase.1*
%_mandir/man1/readPYMB.1*
%_mandir/man1/scel2org.1*
%_mandir/man1/txt2mb.1*

%files libs
%doc
%_libdir/libfcitx*.so.*
%dir %_libdir/%name/
%_libdir/%name/%name-[!pqt]*.so
%_libdir/%name/%name-punc.so
%_libdir/%name/%name-quickphrase.so
%_libdir/%name/qt/
%dir %_libdir/girepository-1.0/
%_libdir/girepository-1.0/Fcitx-1.0.typelib

%files data
%doc
%_datadir/icons/hicolor/16x16/apps/%name.png
%_datadir/icons/hicolor/22x22/apps/%name.png
%_datadir/icons/hicolor/24x24/apps/%name.png
%_datadir/icons/hicolor/32x32/apps/%name.png
%_datadir/icons/hicolor/48x48/apps/%name.png
%_datadir/icons/hicolor/128x128/apps/%name.png
%_datadir/icons/hicolor/16x16/status/*.png
%_datadir/icons/hicolor/22x22/status/*.png
%_datadir/icons/hicolor/24x24/status/*.png
%_datadir/icons/hicolor/48x48/status/*.png
%_datadir/icons/hicolor/scalable/status/*.svg
%_datadir/icons/gnome/scalable/status/*.svg
%_datadir/%name/skin/
%_datadir/%name/addon/%name-[!pqt]*.conf
%_datadir/%name/addon/%name-punc.conf
%_datadir/%name/addon/%name-quickphrase.conf
%_datadir/%name/data/
%_datadir/%name/spell/
%_datadir/%name/configdesc/[!ft]*.desc
%_datadir/%name/configdesc/fcitx-[!p]*.desc

%files devel
%doc
%_bindir/fcitx4-config
%_libdir/libfcitx*.so
%_libdir/pkgconfig/fcitx*.pc
%_includedir/fcitx*
%_datadir/cmake/%name/
%dir %_datadir/gir-1.0
%_datadir/gir-1.0/Fcitx-1.0.gir

%files table-chinese
%doc
%_datadir/%name/table/
%_datadir/%name/imicon/[!ps]*.png

%files pinyin
%doc
%_datadir/%name/inputmethod/pinyin.conf
%_datadir/%name/inputmethod/shuangpin.conf
%_datadir/%name/pinyin/
%_datadir/%name/configdesc/fcitx-pinyin.desc
%_datadir/%name/configdesc/fcitx-pinyin-enhance.desc
%_datadir/%name/addon/fcitx-pinyin.conf
%_datadir/%name/addon/fcitx-pinyin-enhance.conf
%_datadir/%name/imicon/pinyin.png
%_datadir/%name/imicon/shuangpin.png
%_libdir/%name/%name-pinyin.so
%_libdir/%name/%name-pinyin-enhance.so
%_datadir/%name/py-enhance/

%files qw
%doc
%_datadir/%name/inputmethod/qw.conf
%_libdir/%name/%name-qw.so
%_datadir/%name/addon/fcitx-qw.conf

%files table
%doc
%_datadir/%name/configdesc/table.desc
%_libdir/%name/%name-table.so
%_datadir/%name/addon/fcitx-table.conf

%files gtk2
%_libdir/gtk-2.0/%gtk2_binary_version/immodules/im-fcitx.so

%files gtk3
%_libdir/gtk-3.0/%gtk3_binary_version/immodules/im-fcitx.so

%files qt4
%_libdir/qt4/plugins/inputmethods/qtim-fcitx.so

%changelog
* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.7-alt2.1.1
- rebuild with new lua 5.3

* Mon Feb 29 2016 Andrey Cherepanov <cas@altlinux.org> 4.2.7-alt2.1
- rebuild with new icu

* Fri Sep 05 2014 Ilya Mashkin <oddity@altlinux.ru> 4.2.7-alt2
- build for Sisyphus

* Fri Jun 21 2013 Igor Vlasenko <viy@altlinux.ru> 4.2.7-alt1_4
- update to new release by fcimport

* Fri Mar 08 2013 Igor Vlasenko <viy@altlinux.ru> 4.2.7-alt1_1
- update to new release by fcimport

* Tue Jan 29 2013 Igor Vlasenko <viy@altlinux.ru> 4.2.6.1-alt1_3
- update to new release by fcimport

* Thu Dec 27 2012 Igor Vlasenko <viy@altlinux.ru> 4.2.6.1-alt1_2
- initial fc import

