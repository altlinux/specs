%define _name gedit-code-assistance
%define ver_major 0.1
%define gedit_pluginsdir %_libdir/gedit/plugins

Name: gedit-plugins-code-assistance
Version: %ver_major.3
Release: alt1

Summary:  GEdit
License: GPL
Group: Editors
Url: http://gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%_name-%version.tar.xz

# From configure.in
%define gedit_ver 3.0.0
%define llvm_ver 2.8

Requires: gedit >= %gedit_ver

BuildPreReq: rpm-build-gnome

# From configure.in
BuildPreReq: gedit-devel >= %gedit_ver
BuildPreReq: llvm-devel >= %llvm_ver
BuildRequires: clang-devel libgio-devel libgee-devel vala-tools

%description
gEdit is a small but powerful text editor designed expressly for GNOME.

%name is a plugin for gEdit which provides code assistance for C, C++ and
Objective-C by utilizing clang.

%prep
%setup -q -n %_name-%version

%build
%configure \
    --disable-static

%make_build

%install
%make_install install DESTDIR=%buildroot

%find_lang --with-gnome %_name


%files -f %_name.lang
%gedit_pluginsdir/gcp.plugin
%gedit_pluginsdir/libgcp.so
%_datadir/gedit/plugins/gcp/

%exclude %gedit_pluginsdir/*.la

%changelog
* Fri May 11 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.3-alt1
- 0.1.3

* Sat Nov 19 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1
- 0.1.2

* Sun Nov 13 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- first build for Sisyphus

