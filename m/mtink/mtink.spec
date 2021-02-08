Name: mtink
Version: 1.0.16
Release: alt2
License: GPLv2+
Group: System/Configuration/Printing

Url: http://xwtools.automatix.de/english/startE.html
# site is dead
# Source: http://xwtools.automatix.de/files/%name-%version.tar.gz
Source: %name-%version.tar
Source1: mtinkd.init
Source2: mtinkd.sysconfig
Source3: printutils.png
Source4: micon.gif
Source5: %name.desktop
Source6: %name.conf
Source7: mtinkd.service
Patch: mtink-1.0.14-ru_font.patch
Patch1: mtink-fhs_fixes.patch
Patch2: mtink-path_to_printer.desc.patch
Patch3: mtink-1.0.16-link.patch
Patch4: mtink-1.0.16-mga-www-browser.patch
Patch5: alt-fix-ftbfs.patch

BuildRequires: libgimp-devel ImageMagick-tools lesstif-devel libX11-devel libXt-devel
BuildRequires: xorg-printproto-devel

Summary: Status monitor and configuration tool for Epson inkjet printers
%description
Mtink is a status monitor which allow to get the remaining ink quantity,
printing of test patterns, changing and cleaning cartridges.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p0
%patch4 -p1
%patch5 -p1

cp %SOURCE1 mtinkd.init
cp %SOURCE2 mtinkd.sysconfig
cp %SOURCE3 printutils.png
cp %SOURCE7 mtinkd.service

%build
perl -p -i -e 's|(/usr/X11R6)/lib\b|\1/%_lib|g' Makefile.ORG
perl -p -i -e 's|(/usr)/lib\b|\1/%_lib|g' Makefile.ORG
perl -p -i -e 's|(/usr)/lib$|\1/%_lib|g' Configure
perl -p -i -e 's|(''/usr/)lib('')|$1%_lib$2|g' checkMotifVersion.sh
%__subst "s|^DBG = .*|DBG = $CFLAGS|g" Makefile.ORG

./Configure --no-suid --prefix /usr

%make

# Fix some small bugs
#perl -p -i -e "s/START_LEVEL=S99mtink/START_LEVEL=S59mtink/" etc/installInitScript.sh
#perl -p -i -e "s/STOP_LEVEL=K02mtink/START_LEVEL=K61mtink/" etc/installInitScript.sh
#perl -p -i -e "s/for d in 2 3 4 5/XXXXXXXXXX/" etc/installInitScript.sh
#perl -p -i -e "s/for d in 0 1 6/for d in 2 3 4 5/" etc/installInitScript.sh
#perl -p -i -e "s/XXXXXXXXXX/for d in 0 1 6/" etc/installInitScript.sh
#perl -p -i -e "s!cp mtink /etc/init.d!!" etc/installInitScript.sh
perl -p -i -e "s!chmod 744 /etc/init.d/mtink!!" etc/installInitScript.sh

%install
install -d %buildroot%_sysconfdir/sysconfig
install -d %buildroot%_initdir
install -d %buildroot%_unitdir
install -d %buildroot%_bindir
install -d %buildroot%_sbindir
install -d %buildroot%_libdir/gimp/2.0/plug-ins
install -d %buildroot%_libdir/cups/backend
install -d %buildroot%_localstatedir/mtink
install -d %buildroot%_datadir/mtink

install -m0755 mtink %buildroot%_bindir/
install -m0755 ttink %buildroot%_bindir/
install -m0755 mtinkc %buildroot%_bindir/
install -m0755 mtinkd %buildroot%_sbindir/
install -m0755 mtinkd.init %buildroot%_initdir/
install -m0644 mtinkd.service %buildroot%_unitdir/
install -m0644 mtinkd.sysconfig %buildroot%_sysconfdir/sysconfig/mtinkd

install -m0644 utils/printer.desc.bldin %buildroot%_datadir/mtink/printer.desc
install -m0644 utils/*.align %buildroot%_datadir/mtink/

install -m0755 etc/installInitScript.sh %buildroot%_sbindir/mtink-installInitScript
install -m0755 detect/askPrinter %buildroot%_sbindir/
install -m0755 etc/mtink-cups %buildroot%_libdir/cups/backend/mtink
install -m0755 gimp-mtink %buildroot%_libdir/gimp/2.0/plug-ins/

# Documentation
cp -ax etc/readme README.mtinkd.startup

# Menu icon
# Menu entries for printer-utils package
mkdir -p %buildroot%_iconsdir/hicolor/16x16/apps/
install -m 644 printutils.png %buildroot%_iconsdir/hicolor/16x16/apps/

# mtink icon
mkdir -p %buildroot/%_miconsdir
mkdir -p %buildroot/%_iconsdir
mkdir -p %buildroot/%_liconsdir
convert %SOURCE4 -resize 16x16 %buildroot/%_miconsdir/%name.png
convert %SOURCE4 -resize 32x32 %buildroot/%_iconsdir/%name.png
convert %SOURCE4 -resize 48x48 %buildroot/%_liconsdir/%name.png

# Menu entries
mkdir -p %buildroot%_desktopdir
cp %SOURCE5 %buildroot%_desktopdir/

mkdir -p %buildroot%_tmpfilesdir
cp %SOURCE6 %buildroot%_tmpfilesdir/

%post
%post_service mtinkd

%preun
%preun_service mtinkd

%files
%doc README.mtinkd.startup CHANGE.LOG doc/*
%_initdir/mtinkd.init
%_unitdir/mtinkd.service
%attr(0644,root,sys) %config(noreplace) %_sysconfdir/sysconfig/mtinkd
%_tmpfilesdir/%name.conf
%_sbindir/mtinkd
%_sbindir/askPrinter
%_sbindir/mtink-installInitScript
%attr(0755,root,sys) %_bindir/mtinkc
# These four must be SGID sys/SUID root to be able to access the printer
# devices
%attr(6711,root,sys) %_bindir/mtink
%attr(6711,root,sys) %_bindir/ttink
%attr(2711,lp,sys) %_libdir/gimp/2.0/plug-ins/gimp-mtink

%_desktopdir/%name.desktop
%_iconsdir/hicolor/16x16/apps/printutils.png
%_miconsdir/%name.png
%_iconsdir/%name.png
%_liconsdir/%name.png
%dir %_datadir/mtink
%_datadir/mtink/*
%_libdir/cups/backend/mtink
%attr(0750,lp,sys) %dir %_localstatedir/mtink

%changelog
* Mon Feb 08 2021 Oleg Solovyov <mcpain@altlinux.org> 1.0.16-alt2
- fix build

* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 1.0.16-alt1
- Initial build for ALT

