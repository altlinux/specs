Name: connector
Version: 1.3.24
Release: alt2

Summary: Remote desktop chooser
License: GPL
Group: Networking/Remote access

Url: http://www.myconnector.ru
Source0: %name-%version.tar.gz
Packager: Korneechev Evgeniy <ekorneechev@altlinux.org>

BuildArch: noarch
Requires: python3 python3-module-pygobject3 xfreerdp
Requires: libgtk+3 libgtk+3-gir remmina remmina-plugins tigervnc

%define basedir %_datadir/%name

%description
This is an aggregator program to connnect to various servers
using all of the popular remote desktop protocols
(RDP, VNC, Citrix, VMware, etc).

%prep
%setup

%install
install -pDm755 %name %buildroot%_bindir/%name
install -pDm644 %name.desktop %buildroot%_desktopdir/%name.desktop
mkdir -p %buildroot%basedir/data/
install -p *.png *.glade %buildroot%basedir/data/
install -p *.py %buildroot%basedir/

%files
%_bindir/%name
%_desktopdir/%name.desktop
%basedir/data
%basedir/*.py

%changelog
* Tue Sep 13 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.24-alt2
- Fixed command open webbrowser

* Tue Sep 13 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.24-alt1
- Added function - copy ctor-file's name to clipboard

* Wed Aug 24 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.23-alt3
- Update requires - added remmina-plugins

* Fri Aug 22 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.23-alt2
- Update requires - added xfreerdp

* Fri Aug 12 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.23-alt1
- Fixed a bug - sometimes doesn't work quick connection

* Thu Jan 14 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.22-alt2
- Fixed vncviewer parameters for TigerVNC

* Tue Jan 12 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.22-alt1
- Fixed redirect smartcards, added redirect usb-storage and key /workarea. NLA is now optional

* Tue Sep 15 2015 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.21-alt1
- Added performance parameters and choise default tab

* Mon Aug 17 2015 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.19-alt1
- Added quick connect -login@server for SSH & SFTP

* Mon Aug 17 2015 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.18-alt1
- Added sound, microphone and printer for FreeRDP

* Tue Aug 11 2015 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.17-alt1
- Added WEB, smartcards

* Thu Jul 02 2015 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.15-alt1
- Added function Copy, update GTK >=3.10

* Thu Jun 25 2015 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.14-alt1
- Update GUI and FreeRDP features

* Tue Jun 23 2015 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.3.12-alt4
- Update SPEC

* Mon Jun 22 2015 Korneechev Evgeniy <ekorneechev@altlinux.org> 1.3.12-alt3
- Initial build by GEAR

* Tue Jun 16 2015 Michael Shigorin <mike@altlinux.org> 1.3.12-alt2
- spec cleanup

* Tue Jun 16 2015 Evgeniy Korneechev <ekorneechev@gmail.com> 1.3.12-alt1
- Initial build
