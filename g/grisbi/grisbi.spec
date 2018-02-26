Name: grisbi
Version: 0.5.9
Release: alt2.qa2

Summary: Personal accounting application
Summary(ru_RU.KOI8-R): Программа персонального учёта финансов
License: GPL
Group: Office 
URL: http://www.grisbi.org

Source: http://prdownloads.sourceforge.net/grisbi/%name-%version.tar.bz2
Patch0: grisbi-0.5.9-alt-intl.patch
Patch1: grisbi-0.5.6-alt-docdir.patch
Patch2: grisbi-0.5.8-alt-no_toupper.patch
Patch3: grisbi-0.5.5-alt-rouble.patch
Patch4: grisbi-0.5.9-alt-link.patch

# Added on Tue Jul 05 2005
BuildRequires: glib2-devel libatk-devel libgtk+2-devel libpango-devel libxml2-devel pkgconfig zlib-devel

%description
Grisbi is a personal accounting application for Linux, written
with Gnome and Gtk, and is released under the GPL licence.

%description -l ru_RU.KOI8-R
Grisbi - это программа персонального учёта финансов для Linux,
написанная под Gnome и Gtk и распространяемая на условиях GPL.


%prep
%setup -q
%patch0 -p1
rm -fR intl
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

touch config.rpath

%build
autoreconf -ifsv
%configure --without-included-gettext
%make_build docdir='%_defaultdocdir/%name-%version'

%install
%makeinstall docdir='%buildroot%_defaultdocdir/%name-%version'
install -m 644 ABOUT-NLS AUTHORS COPYING INSTALL NEWS OLDNEWS README \
    %buildroot%_defaultdocdir/%name-%version/

# menu stuff JONS GTK
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Grisbi
GenericName=Personal accounting application
Comment=Grisbi is a personal accounting application for Linux, written with Gnome and Gtk
Icon=%{name}
Exec=%name
Terminal=false
Categories=Office;Finance;
EOF

%find_lang %name

%files -f %name.lang
%doc %_defaultdocdir/%name-%version
%_datadir/pixmaps/%name
%_man1dir/%name.1.gz
%_datadir/mime-info/%name.keys
%_datadir/mime-info/%name.mime
%_desktopdir/%name.desktop
%_bindir/%name

%changelog
* Sat Apr 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.9-alt2.qa2
- NMU: menu converted to .desktop file

* Tue Feb 09 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.5.9-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for grisbi
  * postclean-05-filetriggers for spec file

* Sat Mar 01 2008 Grigory Batalov <bga@altlinux.ru> 0.5.9-alt2
- Fix build (config.rpath is missing).

* Sun Oct 08 2006 Grigory Batalov <bga@altlinux.ru> 0.5.9-alt1
- 0.5.9.
- Description typo ("personnal") was fixed (bug #3953).
- Fix linking with --as-needed

* Fri Jan 20 2006 Grigory Batalov <bga@altlinux.ru> 0.5.8-alt1
- 0.5.8

* Tue Jul 05 2005 Grigory Batalov <bga@altlinux.ru> 0.5.7-alt1
- 0.5.7

* Tue May 24 2005 Grigory Batalov <bga@altlinux.ru> 0.5.6-alt1
- 0.5.6

* Tue Mar 01 2005 Grigory Batalov <bga@altlinux.ru> 0.5.5-alt1
- 0.5.5
- Included gettext was removed
- Russian rouble support was added
- Toupper call on multibyte symbol was removed

* Mon Jul 05 2004 Pavel S. Khmelinsky <hmepas@altlinux.ru> 0.5.0-alt3
- BuildRequires updated 

* Sat Jul 03 2004 Pavel S. Khmelinsky <hmepas@altlinux.ru> 0.5.0-alt2
- Right Summary 

* Mon Jun 21 2004 Pavel S. Khmelinsky <hmepas@altlinux.ru> 0.5.0-alt1
- 0.5.0 


* Sat Mar 27 2004 Pavel S. Khmelinsky <hmepas@altlinux.ru> 0.4.4-alt1
- First Build for Sisyphus 
