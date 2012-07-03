Name: recoll_applet
Version: 1.10.0
Release: alt2.1

Summary: A personal full text search package
License: GPLv2
Group: File tools

Url: http://www.recoll.org
Source: %name-%version.tgz
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Tue Sep 23 2008
BuildRequires: gcc-c++ imake kdelibs-devel libXt-devel libjpeg-devel libqt3-devel xorg-cf-files

%description
This is a simple KDE tray applet to launch recoll.

%prep
%setup -n %name

%build
%add_optflags -I%_includedir/tqtinterface
%K3configure
%make_build

%install
%K3install
%K3find_lang --with-kde %name

%files -f %name.lang
%_K3libdir/%{name}*
%_K3apps/kicker/applets/*.desktop

%changelog
* Wed May 04 2011 Sergey V Turchin <zerg@altlinux.org> 1.10.0-alt2.1
- fix to build with new kde

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 1.10.0-alt2
- applied repocop patch

* Tue Sep 23 2008 Michael Shigorin <mike@altlinux.org> 1.10.0-alt1
- built for ALT Linux (thanks sbolshakov@ for a hint)
