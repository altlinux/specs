%define _unpackaged_files_terminate_build 1

%def_with check

Name: diffuse
Version: 0.11.0
Release: alt1

Summary: graphical tool for merging and comparing text files
License: GPL-2.0-only
Group: Development/Tools
URL: https://github.com/MightyCreak/diffuse

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(gio-2.0)

Requires: libgtk+3-gir
Requires: python3-module-pygobject3
Requires: python3-module-pycairo

BuildArch: noarch

Source: %name-%version.tar

%description
Diffuse is a graphical tool for merging and comparing text files. Diffuse is
able to compare an arbitrary number of files side-by-side and gives users the
ability to manually adjust line-matching and directly edit files. Diffuse can
also retrieve revisions of files from bazaar, CVS, darcs, git, mercurial,
monotone, Subversion and GNU Revision Control System (RCS) repositories for
comparison and merging.

%prep
%setup
sed -i "s/'appdata'/'metainfo'/g" data/meson.build
sed -i "s/Categories=.*/Categories=GTK;Development;RevisionControl;/" data/io.github.mightycreak.Diffuse.desktop.in

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name --with-gnome

%check
%meson_test

%files -f %{name}.lang
%doc AUTHORS CHANGELOG.md COPYING README.md
%_bindir/diffuse
%config(noreplace) %_sysconfdir/diffuserc
%_desktopdir/io.github.mightycreak.Diffuse.desktop
%dir %_datadir/diffuse
%_datadir/diffuse/*
%_iconsdir/hicolor/scalable/apps/io.github.mightycreak.Diffuse.svg
%_iconsdir/hicolor/symbolic/apps/io.github.mightycreak.Diffuse-symbolic.svg
%_datadir/metainfo/io.github.mightycreak.Diffuse.appdata.xml
%_man1dir/diffuse.1.*
%_datadir/gnome/help/diffuse/C/diffuse.xml
%_datadir/gnome/help/diffuse/cs/diffuse.xml
%_datadir/gnome/help/diffuse/it/diffuse.xml
%_datadir/gnome/help/diffuse/ru/diffuse.xml
%_datadir/man/cs/man1/diffuse.1.*
%_datadir/man/it/man1/diffuse.1.*
%_datadir/man/ru/man1/diffuse.1.*
%_datadir/omf/diffuse/diffuse-C.omf
%_datadir/omf/diffuse/diffuse-cs.omf
%_datadir/omf/diffuse/diffuse-it.omf
%_datadir/omf/diffuse/diffuse-ru.omf

%changelog
* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 0.11.0-alt1
- New version 0.11.0.

* Sat Dec 06 2025 Nikolay Strelkov <snk@altlinux.org> 0.10.0-alt1
- Initial build for Sisyphus
