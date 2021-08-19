%define rname caja-dropbox

Name: mate-file-manager-dropbox
Version: 1.26.0
Release: alt2
Epoch: 1
Summary: Dropbox extension for caja
License: GPLv3 and CC-BY-ND-3.0
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %rname-%version.tar
Patch: %rname-%version.patch

BuildRequires: mate-common mate-file-manager-devel
BuildRequires: rpm-build-python3 python3-module-pygobject3
BuildRequires: python3-module-docutils /usr/bin/rst2man.py

%description
Dropbox extension for caja file manager
Dropbox allows you to sync your files online and across
your computers automatically.

%prep
%setup -q -n %rname-%version
%patch -p1
# use rst2man.py from python3-module-docutils
rm -v rst2man.py
subst 's|python3 rst2man.py|rst2man.py|' configure.ac

%build
%autoreconf
%configure \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %rname --with-gnome --all-name

%files -f %rname.lang
%doc AUTHORS COPYING NEWS README
%_bindir/%rname
%_libdir/caja/extensions-2.0/libcaja-dropbox.so
%_desktopdir/%rname.desktop
%_datadir/%rname
%_datadir/caja/extensions/libcaja-dropbox.caja-extension
%_iconsdir/hicolor/*/apps/*.png
%_man1dir/%rname.1*

%changelog
* Thu Aug 19 2021 Vitaly Lipatov <lav@altlinux.ru> 1:1.26.0-alt2
- NMU: add BR python3-module-docutils /usr/bin/rst2man.py (used separately)
- NMU: drop internal rst2man.py, use rst2man.py from python3-module-docutils

* Tue Aug 10 2021 Valery Inozemtsev <shrek@altlinux.ru> 1:1.26.0-alt1
- 1.26.0

* Tue Jul 13 2021 Igor Vlasenko <viy@altlinux.org> 1:1.24.0-alt2
- NMU: fixed build (closes: #40104)

* Tue Mar 31 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:1.24.0-alt1
- 1.24.0

* Fri Aug 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.18.0-alt1_2.1
- NMU: updated build dependencies

* Fri Sep 15 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.18.0-alt1_2
- new fc release
