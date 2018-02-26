Name: ndisgtk
Version: 0.8.4
Release: alt2.1.1

Summary: This is ndisgtk, a graphical frontend for ndiswrapper
Group: System/Configuration/Networking
License: GPL
Url: http://jak-linux.org/projects/ndisgtk/

Source: http://jak-linux.org/projects/ndisgtk/%name-%version.tar.gz
Source1: %name.pam
Source2: %name.consolehelper
Source3: %name.desktop
Patch: alt-ndisgtk-alterator.patch

Packager: Andrey Alexandrov <demion@altlinux.ru>

BuildRequires: intltool

Requires: ndiswrapper acc alterator-net-wifi alterator-standalone >= 4.0 python-module-pygtk-libglade
BuildArch: noarch

%description
ndisgtk is a GTK based frontend for ndiswrapper, allowing an easy way to install Windows wireless drivers.

%prep
%setup
%patch -p1

%build
%make_build

%install
%makeinstall_std

# pam auth
install -d %buildroot%_bindir
install -d %buildroot%_sysconfdir/pam.d/
install -d %buildroot%_sysconfdir/security/console.apps
install -m 644 %SOURCE1 %buildroot%_sysconfdir/pam.d/%name
install -m 644 %SOURCE2 %buildroot%_sysconfdir/security/console.apps/%name
ln -s consolehelper %buildroot%_bindir/%name
%find_lang %name
install -m 644 %SOURCE3 %buildroot%_desktopdir
#exit 1

%files
#%files -f %name.lang
%doc NEWS
%_desktopdir/*.desktop
%_sbindir/ndisgtk
%_iconsdir/hicolor/48x48/apps/ndisgtk-error.png
%_iconsdir/hicolor/48x48/apps/ndisgtk.png
%_datadir/ndisgtk/ndisgtk.glade
%_pixmapsdir/ndisgtk.xpm
%config %_sysconfdir/pam.d/*
%config(noreplace) %_sysconfdir/security/console.apps/*
%_bindir/ndisgtk

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.4-alt2.1.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt2.1
- Rebuilt with python 2.6

* Thu Jan 08 2009 Andrey Alexandrov <demion@altlinux.ru> 0.8.4-alt2
-  New version

* Sat Mar 08 2008 Andrey Aleksandrov <demion@altlinux.ru> 0.8.1-alt1.1
- Fix bug whith desktop file. Add require python-module-pygtk-libglade

* Fri Mar 07 2008 Andrey Aleksandrov <demion@altlinux.ru> 0.8.1-alt1
- Initial build

