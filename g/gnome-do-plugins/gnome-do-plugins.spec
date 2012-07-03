%def_enable banshee

Name: gnome-do-plugins
Version: 0.8.4
Release: alt1
Summary: Plugins for GNOME Do

License: %gpl3plus
Group: Graphical desktop/GNOME
Url: http://do.davebsd.com/
Packager: Alexey Shabalin <shaba@altlinux.ru>
Source: http://edge.launchpad.net/do-plugins/trunk/%version/+download/%name-%version.tar

Requires: gnome-do >= %version

BuildRequires: gnome-do-devel
BuildRequires: mono-addins-devel
BuildRequires: ndesk-dbus-devel ndesk-dbus-glib-devel
BuildRequires: dbus-sharp-devel dbus-sharp-glib-devel
BuildRequires: libgtk-sharp2-devel
BuildRequires: libnotify-sharp-devel
BuildRequires: libgnome-sharp-devel libgnome-desktop-sharp-devel
BuildRequires: libgnome-keyring-sharp-devel
BuildRequires: libgoogle-data-mono-devel
BuildPreReq: intltool glib2-devel
BuildPreReq: rpm-build-mono mono-mcs mono-devel
BuildPreReq: rpm-build-licenses
BuildRequires: /proc

%description
Plugins for GNOME Do

%package banshee
Summary: gnome-do plugin for banshee
Group: Graphical desktop/GNOME
%{?_enable_banshee:BuildRequires: banshee-devel}
Requires: banshee
Requires: %name = %version-%release

%description banshee
gnone-do plugins for banshee

%package bibtex
Summary: gnome-do plugin for bibtex
Group: Graphical desktop/GNOME
Requires: %name = %version-%release

%description bibtex
gnome-do plugins for bibtex

%package clawsmail
Summary: gnome-do-plugins for clawsmail
Group: Graphical desktop/GNOME
Requires: claws-mail
Requires: %name = %version-%release

%description clawsmail
gnome-do plugins for clawsmail

%package epiphany
Summary: gnome-do-plugins for epiphany
Group: Graphical desktop/GNOME
Requires: epiphany
Requires: %name = %version-%release

%description epiphany
gnome-do plugins for epiphany

%package eog
Summary: gnome-do-plugins for Eye of Gnome
Group: Graphical desktop/GNOME
Requires: eog
Requires: %name = %version-%release

%description eog
gnome-do plugins for Eye of Gnome

%package firefox
Summary: gnome-do-plugins for firefox
Group: Graphical desktop/GNOME
Requires: firefox
Requires: %name = %version-%release

%description firefox
gnome-do plugins for firefox.

%package flickr
Summary: gnome-do-plugins for flickr
Group: Graphical desktop/GNOME
BuildRequires: libflickr-sharp-devel
Requires: libflickr-sharp
Requires: %name = %version-%release

%description flickr
gnome-do plugins for flickr

%package pidgin
Summary: gnome-do-plugins for pidgin
Group: Graphical desktop/GNOME
Requires: pidgin
Requires: %name = %version-%release

%description pidgin
gnome-do plugins for pidgin.

%package rhythmbox
Summary: gnome-do-plugins for rhythmbox
Group: Graphical desktop/GNOME
Requires: rhythmbox
Requires: %name = %version-%release

%description rhythmbox
gnome-do plugins for rhythmbox

%package tomboy
Summary: gnome-do-plugins for tomboy
Group: Graphical desktop/GNOME
Requires: tomboy
Requires: %name = %version-%release

%description tomboy
gnome-do plugins for tomboy.

%package thunderbird
Summary: gnome-do-plugins for thunderbird
Group: Graphical desktop/GNOME
Requires: thunderbird
Requires: %name = %version-%release

%description thunderbird
gnome-do plugins for thunderbird

#%package tasque
#Summary: gnome-do-plugins for tasque
#Group: Graphical desktop/GNOME
#Requires: tasque
#Requires: %name = %version-%release

#%description tasque
#gnome-do plugins for tasque

%package vinagre
Summary: gnome-do-plugins for vinagre
Group: Graphical desktop/GNOME
Requires: vinagre
Requires: %name = %version-%release

%description vinagre
gnome-do plugins for vinagre

%package google
Summary: gnome-do-plugins for Google services
Group: Graphical desktop/GNOME
BuildRequires: libgoogle-data-mono-devel
Requires: libgoogle-data-mono
Requires: %name = %version-%release

%description google
gnome-do plugins for Google services

%prep
%setup -q

%build
rm -f *.m4
ACLOCAL="aclocal -I m4/shamrock"  %autoreconf
%configure

%make_build

%install
%make_install install DESTDIR=%buildroot

%find_lang %name

%if_enabled banshee
%files banshee
%_libdir/gnome-do/plugins/*Banshee*
%endif

%files bibtex
%_libdir/gnome-do/plugins/*Bibtex*

%files clawsmail
%_libdir/gnome-do/plugins/*ClawsMail*

%files epiphany
%_libdir/gnome-do/plugins/*Epiphany*

%files eog
%_libdir/gnome-do/plugins/EOG*

%files firefox
%_libdir/gnome-do/plugins/*Firefox*

%files flickr
%_libdir/gnome-do/plugins/*Flickr*

%files pidgin
%_libdir/gnome-do/plugins/*Pidgin*

%files rhythmbox
%_libdir/gnome-do/plugins/*Rhythmbox*
%files tomboy
%_libdir/gnome-do/plugins/*Tomboy*

%files thunderbird
%_libdir/gnome-do/plugins/*Thunderbird*

#%files tasque
#%_libdir/gnome-do/plugins/*Tasque*

%files vinagre
%_libdir/gnome-do/plugins/*Vinagre*

%files google
%_libdir/gnome-do/plugins/*YouTube*
%_libdir/gnome-do/plugins/*GoogleCalendar*
%_libdir/gnome-do/plugins/*GoogleContacts*
%_libdir/gnome-do/plugins/*GoogleDocs*

%files -f %name.lang
%doc AUTHORS COPYING COPYRIGHT
%_libdir/gnome-do/plugins
%if_enabled banshee
%exclude %_libdir/gnome-do/plugins/*Banshee*
%endif
%exclude %_libdir/gnome-do/plugins/*Bibtex*
%exclude %_libdir/gnome-do/plugins/*ClawsMail*
%exclude %_libdir/gnome-do/plugins/*Epiphany*
%exclude %_libdir/gnome-do/plugins/EOG*
%exclude %_libdir/gnome-do/plugins/*Firefox*
%exclude %_libdir/gnome-do/plugins/*Flickr*
%exclude %_libdir/gnome-do/plugins/*Pidgin*
%exclude %_libdir/gnome-do/plugins/*Rhythmbox*
%exclude %_libdir/gnome-do/plugins/*Tomboy*
%exclude %_libdir/gnome-do/plugins/*Thunderbird*
%exclude %_libdir/gnome-do/plugins/*Tasque*
%exclude %_libdir/gnome-do/plugins/*Vinagre*
%exclude %_libdir/gnome-do/plugins/*YouTube*
%exclude %_libdir/gnome-do/plugins/*GoogleCalendar*
%exclude %_libdir/gnome-do/plugins/*GoogleContacts*
%exclude %_libdir/gnome-do/plugins/*GoogleDocs*

%changelog
* Mon Feb 20 2012 Alexey Shabalin <shaba@altlinux.ru> 0.8.4-alt1
- 0.8.4
- enable banshee plugin

* Fri May 27 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.3.1-alt2
- disable tasque,banshee plugin

* Fri Mar 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.3.1-alt1
- 0.8.3.1
- drop evolution subpackage

* Tue Jan 12 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.2.1-alt1
- 0.8.2.1
- split to subpackages

* Fri Jul 10 2009 Alexey Shabalin <shaba@altlinux.ru> 0.8.2-alt2
- fix buildreq

* Fri Jul 03 2009 Alexey Shabalin <shaba@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Thu Jun 18 2009 Alexey Shabalin <shaba@altlinux.ru> 0.8.1.3-alt1
- 0.8.1.3

* Sun Feb 01 2009 Alexey Shabalin <shaba@altlinux.ru> 0.8.0.1-alt1
- initial package for ALTLinux

