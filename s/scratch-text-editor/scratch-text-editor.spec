%def_disable snapshot

%define _name code
%define rdn_name io.elementary.%_name
%define ver_major 7.0

Name: scratch-text-editor
Version: %ver_major.0
Release: alt1

Summary: The text editor that works
License: GPL-3.0
Group: Editors

Url: https://github.com/elementary/code

%if_disabled snapshot
Source: %url/archive/%version/%_name-%version.tar.gz
%else
Vcs: https://github.com/elementary/code.git
Source: %_name-%version.tar
%endif

Provides: %rdn_name = %version-%release

%define gtksourceview_api_ver 4
%define granite_ver 6.0.0

Requires: contractor elementary-icon-theme
Requires: editorconfig

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson gcc-c++ vala-tools libvala-devel
BuildRequires: /usr/bin/appstream-util
BuildRequires: gobject-introspection-devel
BuildRequires: libgranite-devel >= %granite_ver
BuildRequires: pkgconfig(libhandy-1)
BuildRequires: libpeas-devel libgtksourceview%gtksourceview_api_ver-devel libvte3-devel
BuildRequires: libgee0.8-devel libzeitgeist2.0-devel
BuildRequires: libdbus-devel libgranite-vala libxml2-devel
BuildRequires: libgtkspell3-devel libgit2-glib-devel
BuildRequires: libpolkit-devel
# since 3.0
BuildRequires: libeditorconfig-devel

%description
Scratch is the text editor that works for you. It auto-saves your files,
meaning they're always up-to-date. Plus it remembers your tabs so you never
lose your spot, even in between sessions.

Make it yours. Scratch is written from the ground up to be extensible. Keep
things super lightweight and simple, or install extensions to turn Scratch
into a full-blown IDE; it's your choice. And with a handful of useful
preferences, you can tweak the behavior and interface to your liking.

It's elementary. Scratch is made to be the perfect text editor for elementary,
meaning it closely follows the high standards of design, speed, and
consistency. It's sexy, but not distracting.

Works with your language. Whether you're crafting code in Vala, scripting with
PHP, or marking things up in HTML, Scratch has you covered. Experience full
syntax highlighting with nearly all programming, scripting, and markup
languages.

Other syntax-highlighted languages: Bash, C, C#, C++. Cmake, CSS, .Desktop,
Diff, Fortran, Gettext, ini, Java, JavaScript, LaTex, Lua, Makefile,
Objective C, Pascal, Perl, Python, Ruby, XML.

Additional features include:

 * syntax highlighting with gtksourceview-3
 * a find bar to search the words in the files
 * strong integration with Granite framework by elementary-team
 * tab and split documents system
 * lots of others

%package devel
Summary: Development files for scratch text editor
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files for scratch.

%package vala
Summary: Vala language bindings for the scratch text editor
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %version-%release

%description vala
This package provides Vala language bindings for the scratch text editor.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %rdn_name

%files -f %rdn_name.lang
%_bindir/%rdn_name
%_libdir/lib%{_name}core.so.*
%_libdir/%rdn_name/
%_desktopdir/%rdn_name.desktop
%_datadir/%rdn_name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/glib-2.0/schemas/%rdn_name.plugins.spell.gschema.xml
%_datadir/gtksourceview-%gtksourceview_api_ver/styles/*
%_datadir/polkit-1/actions/%rdn_name.policy
%_iconsdir/hicolor/*/*/%rdn_name.*
%_datadir/metainfo/%rdn_name.metainfo.xml

%files devel
%_libdir/*.so
%_pkgconfigdir/*.pc
%_includedir/%{_name}core.h

%files vala
%_vapidir/%{_name}core.deps
%_vapidir/%{_name}core.vapi

%changelog
* Tue Feb 07 2023 Yuri N. Sedunov <aris@altlinux.org> 7.0.0-alt1
- 7.0.0

* Mon Sep 21 2020 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt2
- updated to 3.4.1-85-gb5c646c4
- build with vala-0.50

* Tue Jun 23 2020 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Apr 06 2020 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- updated to 3.4.0-5-g34b39581

* Wed Mar 11 2020 Yuri N. Sedunov <aris@altlinux.org> 3.3.0-alt1
- updated to 3.3.0-14-g74a3e874
- built with vala-0.48

* Wed Jan 22 2020 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- updated to 3.2.0-29-gd166050c

* Wed Apr 03 2019 Yuri N. Sedunov <aris@altlinux.org> 3.1.1-alt1
- 3.1.1

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt2
- rebuilt with vala-0.44

* Thu Jan 03 2019 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt6
- rebuilt with vala-0.42

* Mon Jun 25 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt5
- rebuilt against libgranite.so.5

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt4.1
- rebuilt with vala-0.40

* Sat Jan 06 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt4
- current snapshot built against libgranite.so.4

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt3
- rebuild with vala-0.38

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt2
- rebuild with vala-0.36

* Wed Feb 22 2017 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt1
- 2.4.1

* Mon Feb 13 2017 Yuri N. Sedunov <aris@altlinux.org> 2.4-alt1
- 2.4

* Sat Sep 24 2016 Yuri N. Sedunov <aris@altlinux.org> 2.3-alt1
- 2.3

* Wed Mar 23 2016 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt3
- rebuilt with vala-0.32

* Thu Sep 24 2015 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt2
- rebuilt with vala-0.30

* Thu Sep 17 2015 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Thu Sep 10 2015 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Fri Dec 13 2013 Igor Zubkov <icesik@altlinux.org> 2.0.2-alt1
- 2.0.2

* Tue Oct 01 2013 Igor Zubkov <icesik@altlinux.org> 2.0.1-alt2
- back to Sisyphus

* Sat Sep 14 2013 Igor Zubkov <icesik@altlinux.org> 2.0.1-alt1
- 2.0 -> 2.0.1

* Thu Aug 15 2013 Igor Zubkov <icesik@altlinux.org> 2.0-alt1
- build for Sisyphus

