%define _libexecdir %_prefix/libexec
%define rname pluma

Name: mate-text-editor
Version: 1.26.0
Release: alt2
Epoch: 1
Summary: Text editor for the MATE desktop
License: GPLv3+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: %name-data = %version-%release
Obsoletes: %name-data

Source: %rname-%version.tar
Source1: libegg.tar
Patch: %rname-%version-%release.patch

BuildPreReq: rpm-build-python3
BuildRequires: mate-common gtk-doc iso-codes-devel libSM-devel libenchant-devel libgtksourceview4-devel
BuildRequires: libgtksourceview4-gir-devel libpeas-devel libxml2-devel yelp-tools python3-devel

%description
pluma is a small, but powerful text editor designed specifically for
the MATE desktop. It has most standard text editor functions and fully
supports international text in Unicode. Advanced features include syntax
highlighting and automatic indentation of source code, printing and editing
of multiple documents in one window.

pluma is extensible through a plugin system, which currently includes
support for spell checking, comparing files, viewing CVS ChangeLogs, and
adjusting indentation levels.

%package devel
Summary: Support for developing plugins for the pluma text editor
Group: Development/Other

%description devel
Development files for pluma

%add_python3_path %_libdir/%rname/plugins

%prep
%setup -q -n %rname-%version -a1
%patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--disable-schemas-compile \
	--enable-gtk-doc \
	--enable-gtk-doc-html \
	--enable-gvfs-metadata

%make_build

%install
%make DESTDIR=%buildroot install

find %buildroot%_libdir -name \*.la -delete

%find_lang %rname --with-gnome --all-name

%files -f %rname.lang
%doc README.md COPYING AUTHORS
%_bindir/%rname
%_libdir/%rname
%_libexecdir/%rname
%_libdir/girepository-1.0/Pluma-1.0.typelib
%_datadir/%rname
%_desktopdir/*.desktop
%_datadir/metainfo/pluma.appdata.xml
%_datadir/glib-2.0/schemas/org.*.xml
%_man1dir/*.1*

%files devel
%_includedir/%rname
%_pkgconfigdir/*.pc
%_datadir/gtk-doc/html/%rname
%_datadir/gir-1.0/Pluma-1.0.gir

%changelog
* Thu Nov 24 2022 Valery Inozemtsev <shrek@altlinux.ru> 1:1.26.0-alt2
- updated translations

* Tue Aug 10 2021 Valery Inozemtsev <shrek@altlinux.ru> 1:1.26.0-alt1
- 1.26.0

* Mon Mar 01 2021 Valery Inozemtsev <shrek@altlinux.ru> 1:1.24.1-alt2
- rebuild with python 3 (closes: #39730)

* Wed Aug 26 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:1.24.1-alt1
- 1.24.1

* Wed Feb 26 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:1.24.0-alt1
- 1.24.0

* Tue Dec 03 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.2-alt2
- switch to python 3

* Thu Oct 17 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.2-alt1
- 1.22.2

* Tue Apr 23 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt1
- 1.22.1

* Thu Mar 07 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Tue Feb 12 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.4-alt1
- 1.20.4

* Wed Dec 05 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.3-alt1
- 1.20.3

* Fri Jun 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.2-alt1
- 1.20.2

* Tue Mar 27 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.1-alt1
- 1.20.1

* Mon Mar 19 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Thu Feb 22 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release
