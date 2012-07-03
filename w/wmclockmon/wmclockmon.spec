# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: wmclockmon
Version: 0.8.1
Release: alt5

Summary: displays a clock in 12/24h mode with alarm mode and 7 different LCD styles
License: GPLv2
Group: Graphical desktop/Other
Url: http://tnemeth.free.fr/projets/dockapps.html
Packager: Slava Semushin <php-coder@altlinux.ru>

Source0: http://tnemeth.free.fr/projets/programmes/%name-%version.tar.gz
Source1: %name.menu

Patch0: wmclockmon-alt-autotools-gtk_linking.patch
Patch1: wmclockmon-alt-src-memory_leak_fix.patch
Patch2: wmclockmon-alt-src-file_leak_fix.patch
Patch3: wmclockmon-deb-src-gtk2_port.patch

BuildRequires: libXext-devel libICE-devel libXpm-devel libgtk+2-devel

%description
A stylish windowmaker dockapp which displays date and time in your
locale in varying formats, including Internet time. Contains alarm,
calendar and configuration utilities.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p2
%patch3 -p1
%autoreconf

%build
%configure
%make_build --silent --no-print-directory

%install
%makeinstall_std --silent --no-print-directory
install -pD -m 644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc AUTHORS ChangeLog THANKS TODO
%_bindir/%name
%_bindir/%name-cal
%_bindir/%name-config
%_man1dir/%name.1.*
%_man1dir/%name-cal.1.*
%_man1dir/%name-config.1.*
%_datadir/%name/
%_menudir/%name

%changelog
* Sun Jun 13 2010 Slava Semushin <php-coder@altlinux.ru> 0.8.1-alt5
- Porting to GTK+2 (patch from Debian, see deb #437442)

* Sat May 30 2009 Slava Semushin <php-coder@altlinux.ru> 0.8.1-alt4
- Fixed file descriptors leaks (found by cppcheck)

* Tue Nov 18 2008 Slava Semushin <php-coder@altlinux.ru> 0.8.1-alt3
- Imported into git and built with gear
- Replaced %%__autoreconf macros to %%autoreconf (noted by repocop)
- Removed obsolete %%update_menus/%%clean_menus calls (noted by repocop)
- More proper Licence tag
- Returned accidentally removed %%changelog entry for 0.8.1-alt1.1

* Sat Apr 07 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.8.1-alt2.1
- NMU based on spec from Slava Semushin <php-coder@>

* Thu Apr 05 2007 Slava Semushin <php-coder@altlinux.ru> 0.8.1-alt2
- Plug memory leak after usage XStringListToTextProperty() function

* Sat Mar 10 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.8.1-alt1.1
- NMU based on Slava Semushin <php-coder@> spec

* Tue Mar 06 2007 Slava Semushin <php-coder@altlinux.ru> 0.8.1-alt1
- Initial build for ALT Linux Sisyphus
- Added patch gtk_linking, which
  + Fixes warnings from autoreconf
  + Sets correct include directories and linking flags for GTK+
  + Adds auto installation for styles

