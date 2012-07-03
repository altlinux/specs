%define include_holidayparser	0
%{?_with_holidayparser: %{expand: %%global include_holidayparser 1}}

Name: dayplanner
Packager: Repocop Q. A. Robot <repocop@altlinux.org>
Summary: An easy and clean Day Planner
Version: 0.9.2
Release: alt1.1.1
Source: http://download.gna.org/dayplanner/%name-%version.tar.bz2
Url: http://www.day-planner.org/
Group: Office
License: GPLv3+
BuildArch: noarch

#Workarround for fucking buildreq for perl
BuildRequires: perl-Gtk2 perl-Locale-gettext

%define _perl_lib_path %_datadir/%name/modules
BuildRequires: perl-autodie

%description
Day Planner is a simple time management program.

Day Planner is designed to help you easily manage your time.
It can manage appointments, birthdays and more. It makes sure you
remember your appointments by popping up a dialog box reminding you about it.

%prep
%setup -q

%install
%if include_holidayparser
%makeinstall_std DHPinstall prefix=/usr
%else
%makeinstall_std prefix=/sur
%endif

# Install the icons
install -m644 ./art/dayplanner-24x24.png -D %buildroot%_niconsdir/dayplanner.png
install -m644 ./art/dayplanner-16x16.png -D %buildroot%_miconsdir/dayplanner.png
install -m644 ./art/dayplanner-48x48.png -D %buildroot%_liconsdir/dayplanner.png
# (High contrast icons)
install -m644 ./art/dayplanner_HC24.png -D %buildroot%_niconsdir/dayplanner_HC.png
install -m644 ./art/dayplanner_HC16.png -D %buildroot%_miconsdir/dayplanner_HC.png
install -m644 ./art/dayplanner_HC48.png -D %buildroot%_liconsdir/dayplanner_HC.png

# Find the localization
%find_lang %name

%files -f dayplanner.lang
%doc AUTHORS COPYING NEWS THANKS TODO ./doc/*
%_bindir/dayplanner
%_bindir/dayplanner-daemon
%_bindir/dayplanner-notifier
%_datadir/%name/
%_niconsdir/dayplanner*.png
%_miconsdir/dayplanner*.png
%_liconsdir/dayplanner*.png
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%changelog
* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt1.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt1.1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for dayplanner

* Tue Dec 30 2008 Eugene Ostapets <eostapets@altlinux.org> 0.9.2-alt1
- First build for ALTLinux

