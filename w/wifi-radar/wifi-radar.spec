Name: wifi-radar
Version: 1.9.8
Release: alt2.1.1

Summary: Tool for connecting to wireless networks
Group: System/Configuration/Networking
License: GPL2
Url: http://wifi-radar.systemimager.org/

Source: http://wifi-radar.systemimager.org/pub/%name-%version.tar.bz2
Source1: %name.init
Source2: %name.pam
Source3: %name.consolehelper
Source4: %name.desktop


Patch: alt-%name-makefile.patch

Packager: Andrey Alexandrov <demion@altlinux.ru>

Requires: python-module-pygtk
BuildArch: noarch

%description
WiFi Radar is a Python/PyGTK2  utility for managing WiFi profiles.
It enables you to scan for available networks and create profiles for your preferred networks. At boot time, running WiFi Radar will automatically scan for an available preferred network and connect to it. You can drag and drop your preferred networks to arrange the profile priority.

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
install -m 644 %SOURCE2 %buildroot%_sysconfdir/pam.d/%name
install -m 644 %SOURCE3 %buildroot%_sysconfdir/security/console.apps/%name
ln -s consolehelper %buildroot%_bindir/%name


mkdir -p %buildroot%_initdir
install -m 755 %SOURCE1 %buildroot%_initdir/%name
rm -rf %buildroot%_sysconfdir/init.d

install -m 644 %SOURCE4 %buildroot%_desktopdir

%files
%doc DEVELOPER_GUIDELINES README README.WPA-Mini-HOWTO.txt TODO
%_initdir/%name
%_sysconfdir/%name/%name.conf
%_sbindir/%name
%_desktopdir/%name.desktop
%_man1dir/%name.1.gz
%_man5dir/%name.conf.5.gz
%_pixmapsdir/%name.png
%_pixmapsdir/%name.svg

%config %_sysconfdir/pam.d/*
%config(noreplace) %_sysconfdir/security/console.apps/*
%_bindir/%name


%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9.8-alt2.1.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.8-alt2.1
- Rebuilt with python 2.6

* Wed Mar 12 2008 Automated package hasher <demion@altlinux.ru> 1.9.8-alt2
- Fix bug with consolehelper

* Sat Mar 08 2008 Andrey Aleksandrov <demion@altlinux.ru> 1.9.8-alt1
- Initial build

