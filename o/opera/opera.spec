%define		softver 12.00
%define		buildver 1467

Name:		opera
Version:	%softver.%buildver
Release:	alt2
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Summary:	A fast and secure web browser and Internet suite
Group:		Networking/WWW
License:	Proprietary
Vendor:		Opera Software ASA
Url:		http://www.opera.com/
Source0:	%name-%softver-%buildver.i386.linux.tar.bz2
Source10:	%name-%softver-%buildver.x86_64.linux.tar.bz2
Source1:	%name
Source2:	%name-widget-manager
Source3:	%name-browser.desktop
Source4:	%name-widget-installer.desktop
Source5:	%name-widget-manager.desktop

%define		opera64 %name-%softver-%buildver.x86_64.linux

ExclusiveArch:	%ix86 x86_64

%ifarch %ix86
BuildArch:	i586
%else
BuildArch:	x86_64
%endif

BuildRequires: kde4libs libXt libgst-plugins libgtk+2 libgtk+3

%description
Opera is a small, fast, customizable, powerful and user-friendly web
browser, as well as an Internet suite, including an email client, an IRC
client, web developer tools (Opera Dragonfly), and a personal web server
(Opera Unite).

%package -n %name-engines-gtk2
Summary: Support GTK+2 for Opera browser
Group: System/Libraries
Requires: %name = %version-%release
Provides: %name-engines-gtk
Obsoletes: %name-engines-gtk < %version

%description -n %name-engines-gtk2
Support GTK+2 for Opera browser

%package -n %name-engines-gtk3
Summary: Support GTK+3 for Opera browser
Group: System/Libraries
Requires: %name = %version-%release
Provides: %name-engines-gtk
Obsoletes: %name-engines-gtk < %version

%description -n %name-engines-gtk3
Support GTK+3 for Opera browser

%package -n %name-engines-kde4
Summary: Support KDE4 for Opera browser
Group: System/Libraries
Requires: %name = %version-%release

%description -n %name-engines-kde4
Support KDE4 for Opera browser

%prep
%setup -q -n %name-%softver-%buildver.i386.linux
%ifarch x86_64
tar -xf %SOURCE10
%endif

%install
install -Dp -m 0755 %SOURCE1 %buildroot%_bindir/%name
install -Dp -m 0755 %SOURCE2 %buildroot%_bindir/%name-widget-manager
mkdir -p %buildroot{%_desktopdir,%_docdir}
cp -a %SOURCE3 %SOURCE4 %SOURCE5 %buildroot%_desktopdir/
cp -a share/doc/opera %buildroot%_docdir
%ifarch %ix86
cp -a -f lib %buildroot%_libdir
cp -a -f share/icons %buildroot%_datadir
cp -a -f share/man %buildroot%_datadir
cp -a -f share/mime %buildroot%_datadir
cp -a -f share/opera %buildroot%_datadir
%else
cp -a -f %opera64/lib %buildroot%_libdir
cp -a -f %opera64/share/icons %buildroot%_datadir
cp -a -f %opera64/share/man %buildroot%_datadir
cp -a -f %opera64/share/mime %buildroot%_datadir
cp -a -f %opera64/share/opera %buildroot%_datadir
subst 's|/usr/lib/|/usr/%_lib/|g' %buildroot%_bindir/%name
rm -rf %buildroot%_libdir/%name/pluginwrapper/operapluginwrapper-ia32-linux 
%endif

%files
%_docdir/opera
%_bindir/*
%_libdir/%name
%exclude %_libdir/opera/lib%{name}*.so
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*
%_man1dir/*
%_datadir/mime/packages/*.xml
%_datadir/opera

%files -n %name-engines-gtk2
%_libdir/opera/lib%{name}gtk2.so

%files -n %name-engines-gtk3
%_libdir/opera/lib%{name}gtk3.so

%files -n %name-engines-kde4
%_libdir/opera/lib%{name}kde4.so

%changelog
* Tue Jul 03 2012 Motsyo Gennadi <drool@altlinux.ru> 12.00.1467-alt2
- build with gtk+3 plugin

* Fri Jun 15 2012 Motsyo Gennadi <drool@altlinux.ru> 12.00.1467-alt1
- 12.00 released

* Sat May 19 2012 Motsyo Gennadi <drool@altlinux.ru> 11.64.1403-alt1
- 11.64 released

* Mon Apr 02 2012 Motsyo Gennadi <drool@altlinux.ru> 11.62.1347-alt1
- 11.62 released

* Sun Jan 29 2012 Motsyo Gennadi <drool@altlinux.ru> 11.61.1250-alt1
- 11.61 released

* Tue Dec 06 2011 Motsyo Gennadi <drool@altlinux.ru> 11.60.1185-alt1
- 11.60 released

* Sun Oct 23 2011 Motsyo Gennadi <drool@altlinux.ru> 11.52.1100-alt1
- 11.52 released

* Sat Sep 03 2011 Motsyo Gennadi <drool@altlinux.ru> 11.51.1087-alt1
- 11.51 released

* Wed Jun 29 2011 Motsyo Gennadi <drool@altlinux.ru> 11.50.1074-alt1
- 11.50 released

* Mon May 23 2011 Motsyo Gennadi <drool@altlinux.ru> 11.11.2109-alt1
- 11.11 released

* Tue Apr 12 2011 Motsyo Gennadi <drool@altlinux.ru> 11.10.2092-alt1
- 11.10 released

* Mon Jan 31 2011 Motsyo Gennadi <drool@altlinux.ru> 11.01.1190-alt1
- 11.01 released

* Thu Dec 16 2010 Motsyo Gennadi <drool@altlinux.ru> 11.00.1156-alt1
- 11.00 released

* Fri Oct 15 2010 Motsyo Gennadi <drool@altlinux.ru> 10.63.6450-alt2
- set ExclusiveArch to x86 and x86_64 only

* Thu Oct 14 2010 Motsyo Gennadi <drool@altlinux.ru> 10.63.6450-alt1
- 10.63 released

* Tue Sep 14 2010 Motsyo Gennadi <drool@altlinux.ru> 10.62.6438-alt1
- 10.62 released

* Thu Aug 12 2010 Motsyo Gennadi <drool@altlinux.ru> 10.61.6430-alt2
- add x86_64

* Thu Aug 12 2010 Motsyo Gennadi <drool@altlinux.ru> 10.61.6430-alt1
- 10.61 released
- added "export LC_MESSAGES=C" for /usr/bin/opera (flash antifreezing)
- change buildarch from i386 to i586

* Sun Jul 11 2010 Motsyo Gennadi <drool@altlinux.ru> 10.60.6386-alt1
- 10.60
  + see here: http://my.opera.com/russian/forums/topic.dml?id=593032&t=1278854249&page=2#comment6182862

* Wed Nov 25 2009 Motsyo Gennadi <drool@altlinux.ru> 10.10.4742.gcc4-alt1.shared.qt3
- 10.10 released

* Tue Nov 17 2009 Motsyo Gennadi <drool@altlinux.ru> 10.10.4672.gcc4-alt0.b1.shared.qt3
- 10.10 beta1

* Thu Mar 05 2009 Motsyo Gennadi <drool@altlinux.ru> 9.64.2480.gcc4-alt1.shared.qt3
- new version

* Tue Dec 23 2008 Motsyo Gennadi <drool@altlinux.ru> 9.63.2474.gcc4-alt1.shared.qt3
- new version

* Tue Dec 09 2008 Motsyo Gennadi <drool@altlinux.ru> 9.62.2466.gcc4-alt1.shared.qt3
- packed for ALT Linux
