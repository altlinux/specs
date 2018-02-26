%define base gdm-theme
%define _name simple

Name: %base-%_name
Version: 1.95
Release: alt8

Summary: A GDM2 theme - Simple
Summary(ru_RU.UTF-8): Тема менеджера входа в систему GDM - Simple
License: GPL
Group: Graphical desktop/GNOME
Url: http://code.google.com/p/simplicity-desktop-theme
Source: %base-%_name-%version.tar.bz2
Packager: Denis Koryavov <dkoryavov@altlinux.org>
BuildArch: noarch
Requires: gdm

%description
Simple theme based on Gnome Arc Colors Brave GDM theme

%description -l ru_RU.UTF-8
Тема для менеджера входа в систему GDM - Simple. Разрабатывается
в рамках проекта Simplicity и основана на теме GDM - Arc Colors Brave.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/gdm/themes/%_name
cp -r * %buildroot%_datadir/gdm/themes/%_name

%files
%_datadir/gdm/themes/*

%changelog
* Tue Aug 02 2011 Alexandra Panyukova <mex3@altlinux.ru> 1.95-alt8
- new background image

* Fri Feb 04 2011 Lenar Shakirov <snejok@altlinux.ru> 1.95-alt7
- Font name fixed in education.xml (ALT #23495)
- Small spec cleanup

* Wed Nov 18 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.95-alt6
- Repocop warnings is taken into account.

* Mon Oct 19 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.95-alt5
- Theme xml renamed to 'simple'.

* Fri Oct 16 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.95-alt4
- Changed background image.

* Fri Oct 16 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.95-alt3
- Changed parameters for 'suspend' button (for better display his label on Russian locale).

* Tue Oct 13 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.95-alt2
- Some fixes in the interface.

* Mon Oct 12 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.95-alt1
- First build for Sisyphus.

