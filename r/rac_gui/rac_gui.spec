Name: rac_gui
Version: 1.0.0
Release: alt1

Summary: 1C rac gui tool

License: GPL
Group: File tools
Url: https://bitbucket.org/svk28/rac-gui

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

# Source-git: https://bitbucket.org/svk28/rac-gui.git
Source: %name-%version.tar

Requires: tcl => 8.6.8, tk >= 8.6.8

%description
This program ia a graphics user interface for 1C rac util.

%description -l ru_RU.UTF8
Графический интерфейс к утилите управления кластером серверов 1С rac.

%prep
%setup

%build

%install
mkdir -p %buildroot{%_bindir,%_datadir/%name/lib/msg}
install -p -m755 %name.tcl %buildroot%_bindir/racgui
%__subst 's+^set\ dir(lib)+set\ dir(lib)\ %_datadir/%name/lib ;#+g' %buildroot%_bindir/racgui
%__subst 's+\[pwd\]+%_datadir/%name+g' %buildroot%_bindir/racgui
install -p -m644 lib/*.tcl %buildroot%_datadir/%name/lib
install -p -m644 %name.cfg %buildroot%_datadir/%name/
install -p -m644 lib/msg/*.* %buildroot%_datadir/%name/lib/msg/

# Menu support
#mkdir -p %buildroot%_libexecdir/menu
#cat > %buildroot%_libdir/menu/%name << EOF
#?package(%name): needs=x11 icon="projman.png" section="Applications/Development/Development environments"  title=ProjMan longtitle="Tcl/Tk Project Manager" command=projman
#EOF
#mdk icons
#install -d %buildroot{%_iconsdir,%_liconsdir,%_miconsdir}
#install -p -m644 img/icons/%name.png %buildroot%_iconsdir/
#install -p -m644 img/icons/large/%name.png %buildroot%_liconsdir/
#install -p -m644 img/icons/mini/%name.png %buildroot%_miconsdir/

%files
%doc README
%doc doc/*
%_bindir/racgui
%_datadir/%name
#%_libdir/menu/%name
#%_iconsdir/%name.png
#%_liconsdir/%name.png
#%_miconsdir/%name.png

%changelog
* Sat Sep 22 2018 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Sisyphus

* Tue Aug 06 2018 Sergey Kalinin <svk@nuk-svk.ru> 1.0.0
- Initial release
