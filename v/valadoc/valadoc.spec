%def_enable snapshot
%define ver_major 0.35
%define api_ver 1.0
# current vala major version
%define vala_ver 0.34

Name: valadoc
Version: %ver_major.0
Release: alt1

Summary: Vala documentation generator
Group: Development/Other
License: GPLv2+
Url: https://wiki.gnome.org/Projects/Valadoc

%if_disabled snapshot
Source: https://git.gnome.org/browse/valadoc/snapshot/valadoc-valac-%version.tar.xz
%else
# e95f5493defcea96349df51de4f58cc3fdf88c14
Source: %name-%version.tar
%endif

Requires: graphviz

BuildRequires: glib2-devel gtk-doc graphviz-devel libgee0.8-devel libvala-devel

%description
Valadoc is a documentation generator for Vala projects. It extracts
source code from Vala source files and can output various formats of
documentation like GTK-Doc or GIR documentation.

Documentation of many common libraries can be found at
http://valadoc.org/

%package devel
Summary: Vala documentation generator
Group: Development/Other
Requires: %name = %version-%release

%description devel
Development files for Valadoc.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_libdir/lib%name.so.*
%dir %_libdir/%name
%dir %_libdir/%name/doclets
%_libdir/%name/doclets/devhelp/
%_libdir/%name/doclets/gtkdoc/
%_libdir/%name/doclets/html/
%dir %_libdir/%name/drivers
%_libdir/%name/drivers/%vala_ver.x/
%_man1dir/%name.1.*
%_datadir/%name/

%exclude %_libdir/%name/*/*/*.la

%files devel
%_includedir/%name-%api_ver.h
%_libdir/lib%name.so
%_pkgconfigdir/%name-%api_ver.pc
%_vapidir/%name-%api_ver.deps
%_vapidir/%name-%api_ver.vapi

%changelog
* Fri Oct 28 2016 Yuri N. Sedunov <aris@altlinux.org> 0.35.0-alt1
- first build for Sisyphus

