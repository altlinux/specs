Name: ladcca
Version: 0.4.0
Release: alt4.qa1

Packager: Ilya Mashkin <oddity@altlinux.ru>
Summary: Session management system for JACK and ALSA audio applications
Summary(ru_RU.KOI8-R): система управления приложениями для JACK и ALSA
License: GPL
Group: Sound
Url: http://pkl.net/~node/%name.html
Source: %name-%version.tar.bz2

BuildPreReq: libtool_1.5

BuildRequires: fontconfig libfreetype-devel gcc-c++ glib2-devel
BuildRequires: glibc-devel-static jackit-devel libalsa-devel libatk-devel
BuildRequires: libe2fs-devel libgtk+2-devel libncurses-devel libpango-devel
BuildRequires: libreadline-devel libxml2-devel zlib-devel texi2html libuuid-devel

%description
LADCCA stands for Linux Audio Developer's Configuration and Connection
API. It is a session management system for audio applications on
GNU/Linux. It understands the JACK low latency audio API and the ALSA
MIDI sequencer interface. The system is comprised of a server program -
ladccad, an application library - lib%name, and a command line control
program - laddca_control. The server and clients communicate over TCP
sockets. There are three kinds of clients: normal clients (audio
applications), user interfaces for the server, and connection patchbays.

%description -l ru_RU.KOI8-R
LADCCA означает API настройки и соединения для разработчиков
Linux-программ для работы со звуком (Linux Audio Developer's Configuration
and Connection API). Это система управления сессиями для звуковых
приложений, работающих в GNU/Linux.

%package -n %{name}d
Summary: LADCCA daemon
Summary(ru_RU.KOI8-R): демон LADCCA
Group: System/Servers
Requires: lib%name = %version-%release
#Requires: setup >= 2.2.3

%description -n %{name}d
LADCCA stands for Linux Audio Developer's Configuration and Connection
API. It is a session management system for audio applications on
GNU/Linux. It understands the JACK low latency audio API and the ALSA
MIDI sequencer interface. The system is comprised of a server program -
ladccad, an application library - lib%name, and a command line control
program - laddca_control. The server and clients communicate over TCP
sockets. There are three kinds of clients: normal clients (audio
applications), user interfaces for the server, and connection patchbays.

This package contains LADCCA daemon - %{name}d

%description -n %{name}d -l ru_RU.KOI8-R
LADCCA означает API настройки и соединения для разработчиков
Linux-программ для работы со звуком (Linux Audio Developer's Configuration
and Connection API). Это система управления сессиями для звуковых
приложений, работающих в GNU/Linux.

Этот пакет содержит демон LADCCA - %{name}d.

%package control
Summary: LADCCA daemon control program
Summary(ru_RU.KOI8-R): программа управления демоном LADCCA
Group: Sound
Requires: lib%name = %version-%release

%description control
LADCCA stands for Linux Audio Developer's Configuration and Connection
API. It is a session management system for audio applications on
GNU/Linux. It understands the JACK low latency audio API and the ALSA
MIDI sequencer interface. The system is comprised of a server program -
ladccad, an application library - lib%name, and a command line control
program - laddca_control. The server and clients communicate over TCP
sockets. There are three kinds of clients: normal clients (audio
applications), user interfaces for the server, and connection patchbays.

This package contains command line program to control LADCCA daemon.

%description control -l ru_RU.KOI8-R
LADCCA означает API настройки и соединения для разработчиков
Linux-программ для работы со звуком (Linux Audio Developer's Configuration
and Connection API). Это система управления сессиями для звуковых
приложений, работающих в GNU/Linux.

Этот пакет содержит программу управления демоном LADCCA.

%package clients
Summary: LADCCA clients
Summary(ru_RU.KOI8-R): клиенты LADCCA
Group: Sound
Requires: lib%name = %version-%release

%description clients
LADCCA stands for Linux Audio Developer's Configuration and Connection
API. It is a session management system for audio applications on
GNU/Linux. It understands the JACK low latency audio API and the ALSA
MIDI sequencer interface. The system is comprised of a server program -
ladccad, an application library - lib%name, and a command line control
program - laddca_control. The server and clients communicate over TCP
sockets. There are three kinds of clients: normal clients (audio
applications), user interfaces for the server, and connection patchbays.

This package contains client programs from %name distribution that can
interact with LADCCA daemon - %{name}d

%description clients -l ru_RU.KOI8-R
LADCCA означает API настройки и соединения для разработчиков
Linux-программ для работы со звуком (Linux Audio Developer's Configuration
and Connection API). Это система управления сессиями для звуковых
приложений, работающих в GNU/Linux.

Этот пакет содержит клиентские программы из поставки %name, которые
могут функционировать как клинты демона LADCCA - %{name}d.

%package -n lib%name
Summary: Shared library for %name
Summary(ru_RU.KOI8-R): Разделяемые библиотеки для %name
Group: System/Libraries

%description -n lib%name
LADCCA stands for Linux Audio Developer's Configuration and Connection
API. It is a session management system for audio applications on
GNU/Linux. It understands the JACK low latency audio API and the ALSA
MIDI sequencer interface. The system is comprised of a server program -
ladccad, an application library - lib%name, and a command line control
program - laddca_control. The server and clients communicate over TCP
sockets. There are three kinds of clients: normal clients (audio
applications), user interfaces for the server, and connection patchbays.

This package contains the library needed to run programs dynamically
linked with %name.

%description -n lib%name -l ru_RU.KOI8-R
LADCCA означает API настройки и соединения для разработчиков
Linux-программ для работы со звуком (Linux Audio Developer's Configuration
and Connection API). Это система управления сессиями для звуковых
приложений, работающих в GNU/Linux.

Этот пакет содержит библиотеки, необходимые для приложений динамически
слинкованных с %name.

%package -n lib%name-devel
Summary: Files for developing programs that will use %name
Summary(ru_RU.KOI8-R): файлы для разработки использующих %name приложений
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
LADCCA stands for Linux Audio Developer's Configuration and Connection
API. It is a session management system for audio applications on
GNU/Linux. It understands the JACK low latency audio API and the ALSA
MIDI sequencer interface. The system is comprised of a server program -
ladccad, an application library - lib%name, and a command line control
program - laddca_control. The server and clients communicate over TCP
sockets. There are three kinds of clients: normal clients (audio
applications), user interfaces for the server, and connection patchbays.

This package contains the headers that programmers will need to develop
applications which will use %name libraries.

%description -n lib%name-devel -l ru_RU.KOI8-R
LADCCA означает API настройки и соединения для разработчиков
Linux-программ для работы со звуком (Linux Audio Developer's Configuration
and Connection API). Это система управления сессиями для звуковых
приложений, работающих в GNU/Linux.

Этот пакет содержит файлы, необходимые для разработки приложений,
использующих %name.

%package doc
Summary: Documentation for LADCCA
Summary(ru_RU.KOI8-R): документация к LADCCA
Group: Sound
Conflicts: lib%name < %version-%release

%description doc
LADCCA stands for Linux Audio Developer's Configuration and Connection
API. It is a session management system for audio applications on
GNU/Linux. It understands the JACK low latency audio API and the ALSA
MIDI sequencer interface. The system is comprised of a server program -
ladccad, an application library - lib%name, and a command line control
program - laddca_control. The server and clients communicate over TCP
sockets. There are three kinds of clients: normal clients (audio
applications), user interfaces for the server, and connection patchbays.

This package contains documentations for LADCCA

%description doc -l ru_RU.KOI8-R
LADCCA означает API настройки и соединения для разработчиков
Linux-программ для работы со звуком (Linux Audio Developer's Configuration
and Connection API). Это система управления сессиями для звуковых
приложений, работающих в GNU/Linux.

Этот пакет содержит документацию к LADCCA.

%define __docdir %_docdir/%name-%version

%prep
%setup -q

%build
%set_libtool_version 1.5
%set_automake_version 1.10
#set_autoconf_version 2.5
%set_verify_info_method relaxed

%configure \
	--disable-static \
	--disable-gtk \
	--disable-serv-inst

%make_build

%install
%makeinstall

# install docs
find docs -name "Makefile*" -print0 |xargs -r0 rm -f --
mkdir -p %buildroot%__docdir
cp AUTHORS ChangeLog README NEWS TODO %buildroot%__docdir/
pushd docs
cp -R ladcca-manual-html-one-page ladcca-manual-html-split %buildroot%__docdir/
cp *.html %buildroot%__docdir/
popd

pushd %buildroot/%_infodir
mv %name-manual.info %name.info
popd

#menu
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=ladcca
Comment=Jack/ALSA Session Manager
Icon=sound_section
Exec=ladcca_gtk_client
Terminal=false
Categories=AudioVideo;Audio;Mixer;
EOF

# remove non-packaged files
rm -f %buildroot%_libdir/*.la

%files -n %{name}d
%_bindir/%{name}d
%_datadir/%name/dtds/*

%files control
%_bindir/%{name}_control

%files clients
%_bindir/*_client
%_bindir/ladcca_save_button_2
%_bindir/*_synth
%_desktopdir/%{name}.desktop

%files -n lib%name
%_libdir/*.so.*
%dir %_datadir/%name
%dir %_datadir/%name/dtds

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%files doc
%_infodir/*.info*
%dir %__docdir
%__docdir/*

%changelog
* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt4.qa1
- NMU: converted menu to desktop file

* Thu Jan 07 2010 Ilya Mashkin <oddity@altlinux.ru> 0.4.0-alt4
- update requires

* Sat Sep 19 2009 Ilya Mashkin <oddity@altlinux.ru> 0.4.0-alt3
- remove deprecated macros

* Sun Aug 30 2009 Ilya Mashkin <oddity@altlinux.ru> 0.4.0-alt2
- Rebuild from orphaned

* Sat Dec 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.4.0-alt1
- Fixed #6957 (actually, it was done in Nov 2006, but oh well...).

* Tue Nov 07 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.4.0-alt0.7
- Ressurrected from orphaned.
- Removed unsupported jack call.
- Changed libtool version to 1.5.
- Some spec cleanup.
- Patches merged into git source tree.

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.4.0-alt0.6.1
- Rebuilt with libreadline.so.5.

* Fri Nov 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.4.0-alt0.6
- do not package .la files.

* Thu Oct 23 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.4.0-alt0.5
- 0.4.0

* Mon Oct 06 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.3.1-alt0.6
- fixed %%build.
- fixed descriptions (close #2856)

* Tue Jul 15 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.3.1-alt0.5
- 0.3.1
- summary, descriptions by avp.

* Tue Feb 25 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.3.0-alt0.5
- First build for Sisyphus.
