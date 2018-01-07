%def_enable snapshot

%define _name scratch
%define xdg_name org.pantheon.%_name
%define rdnn_name io.elementary.code
%define ver_major 2.4

Name: scratch-text-editor
Version: %ver_major.1
Release: alt4

Summary: The text editor that works
License: GPLv3
Group: Editors

Url: https://launchpad.net/%_name

%if_disabled snapshot
Source: %url/2.x/%version/+download/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif
Patch: %name-2.4.1-up-vala_0.36.patch

Requires: contractor

BuildRequires: intltool libappstream-glib-devel
BuildRequires: libpng-devel cmake gcc-c++ vala libwebkitgtk3-devel
BuildRequires: libvte3-devel libpixman-devel gobject-introspection-devel
BuildRequires: libGConf-devel libXdmcp-devel libxml2-devel libXdamage-devel
BuildRequires: libXxf86vm-devel libharfbuzz-devel libXinerama-devel libXi-devel
BuildRequires: libXrender-devel libXrandr-devel libXcursor-devel
BuildRequires: libXcomposite-devel libxkbcommon-devel libwayland-cursor-devel
BuildRequires: at-spi2-atk-devel libpeas-devel libgtksourceview3-devel
BuildRequires: libgee0.8-devel libzeitgeist2.0-devel libgranite-devel libgail3-devel
BuildRequires: libdbus-devel libgranite-vala libvala-devel libexpat-devel
BuildRequires: libgtkspell3-devel
# since 2.4
BuildRequires: libwebkit2gtk-devel

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
%setup -n %name-%version
#%%patch
# fix libdir
find ./ -name "CMakeLists.txt" -print0 | xargs -r0 subst 's|lib\/|${LIB_DESTINATION}/|g' --

%build
%cmake -DCMAKE_BUILD_TYPE:STRING="Release"
%cmake_build VERBOSE=1

%install
%cmakeinstall_std

%find_lang %rdnn_name

%files -f %rdnn_name.lang
%_bindir/%rdnn_name
%_libdir/lib%{_name}core.so.*
%_libdir/%rdnn_name/
%_desktopdir/%xdg_name.desktop
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/glib-2.0/schemas/%xdg_name.plugins.folder-manager.gschema.xml
#%_datadir/glib-2.0/schemas/%xdg_name.plugins.file-manager.gschema.xml
%_datadir/glib-2.0/schemas/%xdg_name.plugins.spell.gschema.xml
%_datadir/glib-2.0/schemas/%xdg_name.plugins.terminal.gschema.xml
%_iconsdir/hicolor/*/*/%rdnn_name.*
%_datadir/metainfo/%rdnn_name.appdata.xml

%files devel
%_libdir/*.so
%_pkgconfigdir/*.pc
%_includedir/%_name/

%files vala
%_vapidir/%{_name}core.deps
%_vapidir/%{_name}core.vapi

%changelog
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

