# dropped perl(Benchmark.pm) perl(DP/CoreModules.pm) 
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Date/HolidayParser/iCalendar.pm) perl(Digest/MD5.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Fatal.pm) perl(FindBin.pm) perl(Glib.pm) perl(Gtk2.pm) perl(Gtk2/Gdk/Keysyms.pm) perl(Gtk2/SimpleList.pm) perl(Gtk2/TrayIcon.pm) perl(IO/Select.pm) perl(IO/Socket.pm) perl(IO/Socket/INET.pm) perl(IO/Socket/SSL.pm) perl(IO/Socket/UNIX.pm) perl(IPC/Open3.pm) perl(MIME/Base64.pm) perl(Mail/Sendmail.pm) perl(Socket.pm) perl(Sys/Hostname.pm) perl(Term/ReadKey.pm) perl(Term/ReadLine.pm) perl(Test/More.pm) perl(X11/GUITest.pm) perl(Moose.pm) perl-devel
# END SourceDeps(oneline)
%filter_from_provides /perl.DP.*/d
%filter_from_provides /perl.Date.HolidayParser.pm./d
%filter_from_requires /perl.DP.*/d
%filter_from_requires /perl.Date.HolidayParser.pm./d

Name: dayplanner
Summary: An easy and clean Day Planner
Version: 0.11
Release: alt1
Source:  https://github.com/downloads/zerodogg/%{name}/%{name}-%{version}.tar.bz2
Url: http://www.day-planner.org/
Group: Office
License: GPLv3+
BuildArch: noarch

BuildRequires: perl-Gtk2 perl-Locale-gettext
BuildRequires: perl-autodie
BuildRequires: gettext desktop-file-utils perl-devel

%define _perl_lib_path %_datadir/%name/modules/dayplanner
%add_perl_lib_path %_datadir/%name/modules/DP-iCalendar/lib

%description
Day Planner is a simple time management program.

Day Planner is designed to help you easily manage your time.
It can manage appointments, birthdays and more. It makes sure you
remember your appointments by popping up a dialog box reminding you about it.

%prep
%setup -q

%build
# nothing to build

%install
make install DESTDIR=%{buildroot} prefix=%{_prefix}

# Install hicolor icons
for size in 16 24 32 48; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps
  install -pm644 art/%{name}-${size}x${size}.png %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
  # (High contrast icons)
  [ -f art/%{name}_HC${size}.png ] && \
  install -pm644 art/%{name}_HC${size}.png %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}_HC.png
done

rm -f %{buildroot}%{_datadir}/pixmaps/%{name}.png

# Chmod
find %{buildroot}%{_datadir}/%{name} -name \*.pm -exec chmod 0644 {} \;

# Find the localization
%find_lang %name

%files -f dayplanner.lang
%doc AUTHORS COPYING NEWS THANKS TODO
%doc ./doc/{*_Spec,EnvironmentVariables,HACKING,README.*,TESTCASES,TODO_DPS}
%_bindir/dayplanner
%_bindir/dayplanner-daemon
%_bindir/dayplanner-notifier
%_datadir/%name/
%_datadir/icons/hicolor/*x*/apps/%{name}*.png
%_desktopdir/%name.desktop
#%_pixmapsdir/%name.png
%{_mandir}/man1/dayplanner*.1*

%changelog
* Wed Apr 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- new version

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt1.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt1.1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for dayplanner

* Tue Dec 30 2008 Eugene Ostapets <eostapets@altlinux.org> 0.9.2-alt1
- First build for ALTLinux

