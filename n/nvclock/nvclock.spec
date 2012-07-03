Name: nvclock
Version: 0.8b
Release: alt4.cvs20080308.qa2

Summary: An overclocking tool for NVIDIA cards
License: GPL
Group: System/Configuration/Hardware

Url: http://www.linuxhardware.org/nvclock/
Source0: %name%version.tar.gz
Source2: %name.png
Patch: nvclock-0.8b-alt-makefile.patch
Patch1: nvclock-0.8b-alt-DSO.patch
Packager: Vyacheslav Dikonov <slava@altlinux.ru>

Requires: NVIDIA_GLX
BuildRequires: fontconfig freetype2 gcc-c++ glib2-devel libatk-devel libgtk+2-devel libpango-devel libqt3-devel libstdc++-devel pkgconfig

Summary(ru_RU.UTF-8): Средство для разгона графических карт NVIDIA
Summary(uk_UA.UTF-8): Утиліта для "розгону" графічних карток NVIDIA

%description
This program allows you to overclock your NVIDIA based graphics card
to reach their peak performance.

%description -l ru_RU.UTF-8
NVClock позволяет вручную изменять тактовую частоту процессоров графических
карт на основе набора микросхем NVIDIA, чтобы добиться предельной
производительности.

%description -l uk_UA.UTF-8
NVClock дозволяє користувачу змінювати тактову частоту процесорів графічних
карток на базі набору мікросхем NVIDIA для досягнення найбільшої
продуктивності.

%package gtk
Summary: An overclocking tool for NVIDIA cards
Summary(ru_RU.UTF-8): GTK-интерфейс для разгона графических карт NVIDIA
Summary(uk_UA.UTF-8): GTK-Інтерфейс для "розгону" графічних карток NVIDIA
License: GPL
Group: System/Configuration/Hardware
Requires: %name

%description gtk
This is the GTK interface for nvclock - a program the allows you to overclock 
your NVIDIA based graphics card to reach their peak performance.

%description gtk -l ru_RU.UTF-8
GTK-интерфейс для nvclock - программы, которая позволяет вручную изменять 
тактовую частоту процессоров графических карт на основе набора микросхем NVIDIA, 
чтобы добиться предельной производительности.

%description gtk -l uk_UA.UTF-8
GTK-iнтерфейс для nvclock - програми, яка дозволяє користувачу змінювати тактову 
частоту процесорів графічних карток на базі набору мікросхем NVIDIA для досягнення 
найбільшої продуктивності.


%package qt
Summary: An overclocking tool for NVIDIA cards
Summary(ru_RU.UTF-8): Qt-интерфейс для разгона графических карт NVIDIA
Summary(uk_UA.UTF-8): Qt-Інтерфейс для "розгону" графічних карток NVIDIA
License: GPL
Group: System/Configuration/Hardware
Requires: %name

%description qt
This is the Qt interface for nvclock - a program the allows you to overclock 
your NVIDIA based graphics card to reach their peak performance.

%description qt -l ru_RU.UTF-8
Qt-интерфейс для nvclock - программы, которая позволяет вручную изменять 
тактовую частоту процессоров графических карт на основе набора микросхем NVIDIA, 
чтобы добиться предельной производительности.

%description qt -l uk_UA.UTF-8
Qt-iнтерфейс для nvclock - програми, яка дозволяє користувачу змінювати тактову 
частоту процесорів графічних карток на базі набору мікросхем NVIDIA для досягнення 
найбільшої продуктивності.


%prep
%setup -n %name%version
%patch -p1
%patch1 -p2

%build
unset QTDIR || : ; . /etc/profile.d/qt3dir.sh
export PATH=$QTDIR/bin:$PATH
%autoreconf
%configure --enable-qt --enable-gtk
# SMP incompatible build
%make

%install
%makeinstall
install -p -m644 -D %SOURCE2 $RPM_BUILD_ROOT%_datadir/pixmaps/%name.png
# Menu
install -m755 -d %buildroot%_desktopdir/
cat > %buildroot%_desktopdir/%{name}-qt.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=NVIDIA Overclocker (QT)
Name[ru]=Разгон видеокарт NVIDIA (QT)
Comment=An overclocking tool for NVIDIA cards
Comment[ru]=Средство для разгона графических карт NVIDIA
TryExec=nvclock_qt
Exec=xdg-su nvclock_qt
Icon=nvclock
Terminal=false
Categories=QT;Settings;HardwareSettings;X-ALTLinux-VideoSettings;
EOF
cat > %buildroot%_desktopdir/%{name}-gtk.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=NVIDIA Overclocker (GTK)
Name[ru]=Разгон видеокарт NVIDIA (GTK)
Comment=An overclocking tool for NVIDIA cards
Comment[ru]=Средство для разгона графических карт NVIDIA
TryExec=nvclock_gtk
Exec=xdg-su nvclock_gtk
Icon=nvclock
Terminal=false
Categories=GTK;Settings;HardwareSettings;X-ALTLinux-VideoSettings;
EOF

# clean up misinstalled docs
rm -rf %_docdir/%name/

%files
%_bindir/%name
%_man1dir/*
%doc AUTHORS ChangeLog COPYING FAQ README

%files gtk
%_bindir/%{name}_gtk
%_datadir/pixmaps/%name.*
%_liconsdir/%name.*
%_desktopdir/%name-gtk.desktop
%exclude %_desktopdir/%name.desktop

%files qt
%_bindir/%{name}_qt
%_datadir/pixmaps/%name.*
%_liconsdir/%name.*
%_desktopdir/%name-qt.desktop


%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8b-alt4.cvs20080308.qa2
- Fixed build

* Mon Apr 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.8b-alt4.cvs20080308.qa1
- NMU: converted menu to desktop file

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 0.8b-alt4.cvs20080308
- applied repocop patch
- minor spec cleanup

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.8b-alt3.cvs20080308.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for nvclock-gtk
 * update_menus for nvclock-qt

* Sat Mar 08 2008 L.A. Kostis <lakostis@altlinux.ru> 0.8b-alt3.cvs20080308
- 0.8b3 version.
- use 2008-03-08 CVS snapshot.
- remove obsoleted menu entries for -gtk target.
- update .spec

* Wed Dec 19 2007 L.A. Kostis <lakostis@altlinux.ru> 0.8b-alt2.cvs20071219
- 2007-12-19 CVS snapshot (due 8xxx support).
- cleanup .spec

* Mon Mar 27 2006 Michael Shigorin <mike@altlinux.org> 0.8b-alt1.1
- [NMU] updated 0.8b snapshot:
  Wednesday August 31 2005
  Various users reported bugs of which a few were critical.
  The critical ones affected affecting systems containing
  multiple Nvidia cards. Further a bug in the GTK version
  related to 3D clocks has been fixed and a temperature
  correction for the LM99 has been added. Because of
  the critical bugs I have updated the 0.8b snapshot
  to include those fixes.
- fixed build
  + removed xorg-x11-devel-static from BuildRequires
  + added Makefile patch (--Wl,--as-needed)
- tiny spec cleanup

* Sat Nov 12 2005 Vyacheslav Dikonov <slava@altlinux.ru> 0.8b-alt1
- 0.8b

* Mon Dec 01 2003 Vyacheslav Dikonov <slava@altlinux.ru> 0.6.2-alt2
- Menu bug fixed

* Mon Feb 10 2003 Vyacheslav Dikonov <slava@altlinux.ru> 0.6.2-alt1
- security fixes, update

* Tue Nov 05 2002 Vyacheslav Dikonov <slava@altlinux.ru> 0.6-alt1
- 1st ALTLinux build (GTK2 only)
