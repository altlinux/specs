Name: eiskaltdcpp
Version: 2.2.5
Release: alt1
Summary: EiskaltDC++ - Direct Connect client
License: GPLv3
Group: Networking/File transfer
Url: http://code.google.com/p/eiskaltdc/
Packager: Aeliya Grevnyov <gray_graff@altlinux.org>

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ libqt4-devel bzlib-devel libaspell-devel liblua5-devel
BuildRequires: libgtk+2-devel libglade-devel glib2-devel libpango-devel libnotify-devel 
BuildRequires: boost-devel boost-signals-devel boost-interprocess-devel
BuildRequires: phonon-devel libssl-devel libidn-devel libxmlrpc-devel
BuildRequires: aspell perl-RPC-XML perl-Term-ShellUI

%add_findreq_skiplist *xmms2_audacious2.ru_RU.UTF-8.php
%add_findreq_skiplist *commands.ru_RU.UTF-8.php

%description
EiskaltDC++ is a cross-platform program that uses the Direct Connect and ADC protocol. 
It is compatible with other DC clients, such as the original DC from Neomodus, DC++ and derivatives. 
EiskaltDC++ also interoperates with all common DC hub software. 


%package common
Group: Networking/File transfer
Summary: Common files for %name
Requires: lib%name = %version-%release
BuildArch: noarch
%description common
Common files for %name

%package gtk
Group: Networking/File transfer
Summary: GTK-based graphical interface
Requires: %name-gtk-data = %version-%release
%description gtk
Gtk interface based on code of FreeDC++ and LinuxDC++

%package gtk-data
Group: Networking/File transfer
Summary: noarch files for GTK-based graphical interface
Requires: %name-common = %version-%release
BuildArch: noarch
%description gtk-data
noarch files for Gtk interface based on code of FreeDC++ and LinuxDC++

%package qt
Group: Networking/File transfer
Summary: Qt-based graphical interface
Provides: %name = %version-%release
Obsoletes: %name <= 2.0.3-alt1
Requires: %name-qt-data = %version-%release
%description qt
Qt-based graphical interface

%package qt-data
Group: Networking/File transfer
Summary: Qt-based graphical interface
Requires: %name-common = %version-%release
BuildArch: noarch
%description qt-data
noarch files for Qt-based graphical interface

%package -n lib%name
Group: System/Libraries
Summary: eiskaltdcpp libraries
Obsoletes: libdcpp
%description -n lib%name
eiskaltdcpp libraries

%package daemon
Group: Networking/File transfer
Summary: Daemon interface
Requires: %name-common = %version-%release
%description daemon
Daemon interface

%package cli
Group: Networking/File transfer
Summary: cli for Daemon
Requires: %name-daemon = %version-%release
%description cli
command line interface for XML-RPC Daemon

%prep
%setup

%build
mkdir -p BUILD
pushd BUILD
cmake .. \
 -DCMAKE_BUILD_TYPE=Release \
 -DCMAKE_SKIP_RPATH:BOOL=yes \
 -DCMAKE_C_FLAGS:STRING='%optflags' \
 -DCMAKE_CXX_FLAGS:STRING='%optflags' \
 -DCMAKE_INSTALL_PREFIX=%prefix \
 -DLIB_DESTINATION=%_lib \
%if %_lib == lib64
 -DLIBDIR=lib64 \
%endif
 -DUSE_ASPELL=ON \
 -DUSE_QT=ON \
 -DFREE_SPACE_BAR_C=ON \
 -DUSE_MINIUPNP=ON \
 -DLOCAL_MINIUPNP=ON \
 -DUSE_GTK=ON \
 -DDBUS_NOTIFY=ON \
 -DUSE_JS=ON \
 -DLUA_SCRIPT=ON \
 -DWITH_LUASCRIPTS=ON \
 -DWITH_SOUNDS=ON \
 -DUSE_QT_SQLITE=ON \
 -DNO_UI_DAEMON=ON \
 -DXMLRPC_DAEMON=ON \
 -DUSE_CLI_XMLRPC=ON
popd
%make_build -C BUILD

%install
%makeinstall -C BUILD DESTDIR="%buildroot/"
%find_lang %name-gtk
%find_lang lib%name

%files qt
%_bindir/%name-qt

%files qt-data
%_desktopdir/%name-qt.desktop
%_datadir/%name/qt
%_man1dir/%name-qt*

%files gtk
%_bindir/%name-gtk

%files gtk-data -f %name-gtk.lang
%_desktopdir/%name-gtk.desktop
%_datadir/%name/gtk
%_man1dir/%name-gtk*

%files -n lib%name -f lib%name.lang
%_libdir/lib%name.so.*

%files common
%_datadir/%name/emoticons
%_datadir/%name/examples
%_datadir/%name/sounds
%_datadir/%name/update_geoip
%_datadir/%name/luascripts
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_iconsdir/hicolor/128x128/apps/%name.png
%_iconsdir/hicolor/64x64/apps/%name.png
%_iconsdir/hicolor/24x24/apps/%name.png
%_iconsdir/hicolor/22x22/apps/%name.png
%_pixmapsdir/*

%files daemon
%_bindir/%name-daemon
%_man1dir/%name-daemon*

%files cli
%_bindir/%name-cli
%_man1dir/%name-cli*
%_datadir/%name/cli

%changelog
* Tue Jan 03 2012 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.5-alt1
- 2.2.5 release

* Wed Oct 12 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.4-alt1
- 2.2.4 release
- Build with command line interface for XML-RPC Daemon

* Wed Oct 12 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.3-alt4
- Fix build

* Wed Sep 28 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.3-alt3
- Build with xmlrpc server daemon

* Wed Jul 13 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.3-alt2
- Build with Daemon (ALT#26360)

* Sat Jun 25 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.3-alt1
- 2.2.3 release

* Sat Jun 18 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.2-alt1
- 2.2.2 release

* Tue Apr 05 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.1-alt2
- Install luascripts

* Wed Mar 09 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.1-alt1
- 2.2.1 release

* Tue Feb 15 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.0-alt2
- Fix build

* Mon Jan 17 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.0-alt1
- 2.2.0 release

* Fri Jan 07 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.0-alt0.2.beta2
- Really 2.2.0 beta2 (ALT#24869)

* Tue Jan 04 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.0-alt0.1.beta2
- 2.2.0 beta2
- fix posible crashes (remove cmake macros. thanx Ivan A. Melnikov)

* Tue Nov 23 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.1.1-alt1
- 2.1.1 release

* Mon Nov 08 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.1.0-alt1
- 2.1.0 release

* Sun Oct 31 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.1.0-alt0.5.beta3
- 2.1.0-beta3

* Fri Oct 22 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.1.0-alt0.4.beta2
- 2.1.0-beta2

* Tue Oct 19 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.1.0-alt0.3.svn1989
- svn r1989 (ALT#24361)
- rename libdcpp to libeiskaltdcpp

* Thu Sep 02 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.1.0-alt0.2.svn1666
- svn r1666

* Thu Aug 12 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.1.0-alt0.1.svn1521
- svn r1521
- split to subpackages(qt,gtk,common,libdcpp)

* Wed Jun 09 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.0.3-alt1
- 2.0.3 release 

* Thu May 06 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.0.2-alt1
- 2.0.2 release

* Mon Apr 19 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.0.1-alt1
- 2.0.1 release

* Mon Mar 22 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.0-alt1
- 2.0 release

* Fri Mar 19 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 1.99-alt0.2
- Updated to revision 366
  +  Fixed crushing on Oxygen theme
  +  Fixed desktop file (repocop)
  +  Added aspell support

* Sat Mar 06 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 1.99-alt0.1
- 1.99 (beta!)
- Initial build for sisyphus
