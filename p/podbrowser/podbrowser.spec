## SPEC file for PodBrowser

%define version    0.12
%define release    alt3

Name: podbrowser
Version: %version
Release: %release

Summary: a GTK+ documentation browser for Perl
Summary(ru_RU.UTF-8): графическая GTK+ утилита просмотра документации Perl

License: %perl_license
Group: Development/Perl
URL: http://jodrell.net/projects/podbrowser

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: http://jodrell.net/files/podbrowser/%name-%version.tar.gz
Source1: %name-16.png
Source2: %name-32.png

Patch0: %name-0.10-alt-desktop_file_l10n.patch
Patch1: %name-0.10-alt-Gtk2_init.patch
Patch2: %name-0.12-alt-opener.patch
Patch3: %name-0.12-alt-podviewr_list.patch

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel 
BuildRequires: perl-Gtk2
BuildRequires: perl-Gtk2-Ex-PrintDialog perl-Gtk2-Ex-PodViewer perl-Gtk2-Ex-Simple-List
BuildRequires: perl-Locale-gettext perl-Gtk2-GladeXML perl-Storable perl-URI perl-HTML-Parser

Requires: gnome-icon-theme


%description
PodBrowser is a documentation browser for Perl. You can view, 
search and print documentation  for Perl's builtin functions, 
its "perldoc" pages,  pragmatic modules  and the default  and 
user-installed modules.

%description -l ru_RU.UTF-8
PodBrowser  -  графическая утилита просмотра  документации Perl. 
Она позволяем просматривать, искать и распечатывать документацию
по встроенным функциям Perl, руководствам "perldoc", а также 
всем установленным в системе модулям.

%prep
%setup  -n %name-%version
%patch0
%patch1
%patch2
%patch3

mv -f COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
%make_build PREFIX=%_prefix

%install
%makeinstall PREFIX=%buildroot%_prefix
install -D -m0644 -- %SOURCE1 %buildroot%_miconsdir/%name.png
install -D -m0644 -- %SOURCE2 %buildroot%_niconsdir/%name.png

%files
%doc README
%doc --no-dereference COPYING
%_bindir/html2ps-%name
%_bindir/%name
%_desktopdir/%name.desktop
%_liconsdir/%{name}*
%_miconsdir/%{name}*
%_niconsdir/%{name}*
%_man1dir/%name.*
%_datadir/%name/%name.glade


%changelog
* Fri Dec 12 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.12-alt3
- Remove obsolete %%update_menus calls
- Fix .desktop file to meet standards

* Mon Apr 07 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.12-alt2
- Add 16x16 and 32x32 scaled icons
- Fix Categories in .desktop file

* Mon Feb 25 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.12-alt1
- New version 0.12
- Adding dependency on gnome-icon-theme (fix #11724)
- Fix external browser search on non-Gnome systems
- Fix hypertext links between POD documents

* Sat Sep 16 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.10-alt1
- Initial build for ALT Linux Sisyphus

* Thu Aug 10 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.10-alt0
- Initial build
