%define _name gedit-code-assistance
%define ver_major 0.3
%define gedit_pluginsdir %_libdir/gedit/plugins

Name: gedit-plugins-code-assistance
Version: %ver_major.0
Release: alt1

Summary: Code assistance plugin for gEdit
License: GPL
Group: Editors
Url: http://gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%_name-%version.tar.xz

Requires: gnome-code-assistance

# From configure.in
%define gedit_ver 3.8.0
%define gee_ver 0.10

Requires: gnome-code-assistance
Requires: gedit >= %gedit_ver

BuildPreReq: rpm-build-gnome
# From configure.in
BuildPreReq: gedit-devel >= %gedit_ver
BuildRequires: libgio-devel libgee0.8-devel >= %gee_ver vala-tools

%description
gEdit is a small but powerful text editor designed expressly for GNOME.

%name is a plugin for gEdit which provides code assistance supported by
gnome-code-assistance service.

%prep
%setup -n %_name-%version

%build
%configure \
    --disable-static

%make_build

%install
%makeinstall_std

%find_lang --with-gnome %_name


%files -f %_name.lang
%gedit_pluginsdir/codeassistance.plugin
%gedit_pluginsdir/libcodeassistance.so
%_datadir/gedit/plugins/codeassistance/

%exclude %gedit_pluginsdir/*.la


%changelog
* Thu Nov 14 2013 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- 0.2.0

* Sat Oct 20 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt1
- 0.1.5

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.4-alt1
- 0.1.4

* Fri May 11 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.3-alt1
- 0.1.3

* Sat Nov 19 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1
- 0.1.2

* Sun Nov 13 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- first build for Sisyphus

