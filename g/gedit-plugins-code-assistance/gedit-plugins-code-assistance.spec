%define _name gedit-code-assistance
%define ver_major 0.2
%define gedit_pluginsdir %_libdir/gedit/plugins
%set_typelibdir %gedit_pluginsdir/gcp/girepository-1.0

Name: gedit-plugins-code-assistance
Version: %ver_major.0
Release: alt1

Summary:  GEdit
License: GPL
Group: Editors
Url: http://gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%_name-%version.tar.xz

# From configure.in
%define gedit_ver 3.8.0
%define llvm_ver 2.8

Requires: gedit >= %gedit_ver

# use python3
AutoReqProv: nopython
%define __python %nil

BuildPreReq: rpm-build-gnome

# From configure.in
BuildPreReq: gedit-devel >= %gedit_ver
BuildPreReq: llvm-devel >= %llvm_ver
BuildRequires: clang-devel libgio-devel libgee-devel vala-tools
BuildRequires: rpm-build-python3 python3-module-pygobject3-devel

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
%_includedir/gedit-3.0/gcp/
%gedit_pluginsdir/gcp.plugin
%gedit_pluginsdir/libgcp.so
%gedit_pluginsdir/gcp/
%_datadir/gedit/plugins/gcp/
%exclude %_vapidir/gcp.deps
%exclude %_vapidir/gcp.vapi

%exclude %gedit_pluginsdir/*.la
%exclude %gedit_pluginsdir/gcp/*/*.la

%changelog
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

