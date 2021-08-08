Name: mate-terminal
Version: 1.26.0
Release: alt1
Epoch: 1
Summary: Terminal emulator for MATE
License: GPLv3+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: xvt

Source: %name-%version.tar
Source1: mate-submodules-%name.tar
Patch: %name-%version-%release.patch

BuildRequires: mate-common libSM-devel libdconf-devel libpcre2-devel libvte3-devel yelp-tools

%description
Mate-terminal is a terminal emulator for MATE. It supports translucent
backgrounds, opening multiple terminals in a single window (tabs) and
clickable URLs.

%prep
%setup -q -a1
%patch -p1

%build
%autoreconf
%configure \
	--disable-schemas-compile

%make_build

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot%_altdir
cat << __EOF__ > %buildroot%_altdir/%name
%_bindir/xvt    %_bindir/%name  48
__EOF__

%find_lang %name --with-gnome --all-name

%files -f %name.lang
%doc AUTHORS COPYING NEWS README ChangeLog
%_altdir/%name
%_bindir/%name
%_bindir/%name.wrapper
%_desktopdir/%name.desktop
%_datadir/glib-2.0/schemas/org.mate.terminal.gschema.xml
%_datadir/metainfo/mate-terminal.appdata.xml
%_man1dir/*.1*

%changelog
* Sun Aug 08 2021 Valery Inozemtsev <shrek@altlinux.ru> 1:1.26.0-alt1
- 1.26.0

* Thu Aug 05 2021 Valery Inozemtsev <shrek@altlinux.ru> 1:1.24.1-alt2
- colors from the system theme are not used (closes: #39009)

* Thu Aug 20 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:1.24.1-alt1
- 1.24.1

* Wed Feb 26 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:1.24.0-alt1
- 1.24.0

* Tue Apr 23 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt1
- 1.22.1

* Thu Mar 07 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Tue Dec 25 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.2-alt1
- 1.20.2

* Mon Jun 25 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.1-alt1
- 1.20.1

* Mon Mar 19 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Mon Oct 16 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.19.0-alt1_1
- new fc release
