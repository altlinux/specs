Name: gnome-shell-extension-weather
Summary: GNOME Shell extension for displaying weather info from several cities
Version: 1.0
Release: alt5.git.g77273a
License: GPL3
Group: Graphical desktop/GNOME
Url: https://github.com/Neroth/gnome-shell-extension-weather/
Packager: Ildar Mulyukov <ildar@altlinux.ru>
BuildArch: noarch

Source: %name.tar

Requires: gnome-shell
BuildPreReq: glib2-devel libgio-devel
# Automatically added by buildreq on Thu Jan 26 2012 (-bi)
# optimized out: perl-Encode perl-XML-Parser pkg-config termutils
BuildRequires: gnome-common intltool rpm-build-gir seed

%description
gnome-shell-extension-weather is a simple extension for displaying weather
notifications in GNOME Shell.

%prep
%setup -n %name

# Moscow
%__subst "s|<default>'Cambridge, MA'</default>|<default>'Moscow, RS'</default>|" src/org.gnome.shell.extensions.weather.gschema.xml.in

%build
./autogen.sh
%configure
make

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_desktopdir/*.desktop
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.weather.gschema.xml
%_datadir/gnome-shell/extensions/weather@gnome-shell-extensions.gnome.org
%doc README.md

%changelog
* Thu May 10 2012 Ildar Mulyukov <ildar@altlinux.ru> 1.0-alt5.git.g77273a
- new snapshot
- fix default location (Moscow)

* Sat Apr 28 2012 Ildar Mulyukov <ildar@altlinux.ru> 1.0-alt4.git.g04df3e
- new snapshot
- now works with Gnome-shell 3.4

* Fri Feb 10 2012 Ildar Mulyukov <ildar@altlinux.ru> 1.0-alt3.git.g63d314
- new snapshot

* Thu Jan 26 2012 Ildar Mulyukov <ildar@altlinux.ru> 1.0-alt2.git.g9afda8
- changed upstream from simon04 to Neroth
- new version, new configurator

* Mon Nov 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.git.g9b5572.1
- Rebuild with Python-2.7

* Tue Nov 01 2011 Ildar Mulyukov <ildar@altlinux.ru> 1.0-alt1.git.g9b5572
- initial build for ALT Linux Sisyphus

