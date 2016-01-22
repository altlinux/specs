%def_enable printing
%def_enable backup

Name: osmo
Version: 0.2.14
Release: alt1

Summary: Personal organizer
License: GPLv2+
Group: Office
Url: http://clayo.org/osmo/
Source: http://downloads.sourceforge.net/%name-pim/%name-%version.tar.gz

BuildRequires: libgtk+2-devel libgtkspell-devel libxml2-devel
BuildRequires: libnotify-devel libical-devel libicu-devel libwebkitgtk2-devel
%{?_enable_backup:BuildRequires: libgringotts-devel libarchive-devel}

%description
Osmo is a handy personal organizer which includes calendar, tasks manager and
address book modules. It was designed to be a small, easy to use and good
looking PIM tool to help to manage personal information. In current state the
organizer is quite convenient in use - for example, user can perform nearly
all operations using keyboard. Also, a lot of parameters are configurable to
meet user preferences.

%prep
%setup

%build
%autoreconf
%configure \
	%{?_enable_backup:--enable-backup=yes} \
	%{?_enable_printing:--enable-printing}
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/applications/*.desktop
%_datadir/icons/hicolor/*/*/%name.*
%_man1dir/*
%dir %_datadir/sounds/%name
%_datadir/sounds/%name/alarm.wav
%doc AUTHORS ChangeLog README TRANSLATORS

%changelog
* Fri Jan 22 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.14-alt1
- 0.2.14

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.12-alt1
- 0.2.12

* Mon Feb 10 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.10-alt6
- explicitly link against libm

* Wed Nov 20 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.10-alt5
- rebuilt against libical.so.1
- use automake-1.11

* Tue Jun 07 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.10-alt4
- fixed for libnotify-0.7

* Tue Jun 22 2010 Yuri N. Sedunov <aris@altlinux.org> 0.2.10-alt3
- built with backup support using libtar and libgringotts (closes #23649)

* Sat May 22 2010 Yuri N. Sedunov <aris@altlinux.org> 0.2.10-alt2
- fixed build against new broken libical

* Thu Apr 01 2010 Yuri N. Sedunov <aris@altlinux.org> 0.2.10-alt1
- 0.2.10
- updated buildreqs

* Sat Feb 13 2010 Yuri N. Sedunov <aris@altlinux.org> 0.2.8-alt1
- first build for Sisyphus

