%define real_name Simplicity
%define gtk2_prefix gtk2-theme

Summary: Simplicity GTK2 Theme
Summary(ru_RU.UTF8): Тема для GTK2 Simplicity
Name: %gtk2_prefix-simplicity
Version: 1.95
Release: alt3
License: GPL
Group: Graphical desktop/GNOME
URL: http://code.google.com/p/simplicity-desktop-theme/
Packager: Denis Koryavov <dkoryavov@altlinux.org>

Source0: %real_name-%version.tar.bz2
Source1: simplicity-xfwm4.tar.bz2

Requires: gtk2-theme-clearlooks

%description
Simplicity is the fresh GTK2 theme based on Clearlooks.

%description -l ru_RU.UTF8
Simplicity - тема GTK2 основанная на Clearlooks. 

%install
%__install -m755 -d $RPM_BUILD_ROOT%_datadir/themes
%__tar xjf %SOURCE0 -C $RPM_BUILD_ROOT%_datadir/themes
%__mv $RPM_BUILD_ROOT%_datadir/themes/%real_name-%version $RPM_BUILD_ROOT%_datadir/themes/%real_name
%__tar xjf %SOURCE1 -C $RPM_BUILD_ROOT%_datadir/themes/%real_name

%files
%_datadir/themes/%real_name

%changelog
* Mon Oct 12 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.95-alt3
- Updated Xfwm4 bottom corners.

* Sun Oct 11 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.95-alt2
- Updated xfce panel background.

* Sun Oct 11 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.95-alt1
- First build for Sisyphus.


