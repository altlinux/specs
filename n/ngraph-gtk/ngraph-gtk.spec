%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%def_with check

Name: ngraph-gtk
Version: 6.09.11
Release: alt1

Summary: Tool for creating scientific 2-dimensional graphs
License: GPL-2.0-or-later
Group: Sciences/Mathematics
Url: https://github.com/htrb/ngraph-gtk

Source: %name-%version.tar

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gtksourceview-5)
BuildRequires: pkgconfig(gsl)
BuildRequires: ruby
BuildRequires: gcc-c++

Requires: libngraph = %{version}-%{release}
Requires: ngraph-gtk-data = %{version}-%{release}

%description
Ngraph is the program to create scientific 2-dimensional graphs for
researchers and engineers. Graphs can be exported to PostScript, SVG,
PNG or PDF format.

%package -n libngraph
Group: System/Libraries
Summary: Ngraph shared library

%description -n libngraph
Ngraph shared library for %{name}.

%package -n libngraph-devel
Group: Development/C++
Summary: Development files for lib%{name}
Requires: libngraph = %{version}-%{release}

%description -n libngraph-devel
Development files for lib%{name}.

%package data
Group: Sciences/Mathematics
BuildArch: noarch
Summary: Architecture independent files for %name

%description data
Architecture independent files for %name.

%prep
%setup
sed -i "s|Categories=.*|Categories=GTK;GNOME;DataVisualization;Science;|" misc/com.github.htrb.ngraph-gtk.desktop

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

# remove static library
rm -vf %buildroot%_libdir/libngraph.a

# install all other useful files
install -Dm644 misc/com.github.htrb.ngraph-gtk.desktop %buildroot%_desktopdir/com.github.htrb.ngraph-gtk.desktop
install -Dm644 misc/ngraph.keys %buildroot%_datadir/mime-info/ngraph.keys
install -Dm644 misc/ngraph.mime %buildroot%_datadir/mime-info/ngraph.mime
install -Dm644 misc/ngraph.bash %buildroot%_datadir/bash-completion/completions/ngraph
install -Dm644 misc/ngraph.applications %buildroot%_datadir/application-registry/ngraph.applications

%check
%make_build check

%files
%doc AUTHORS COPYING NEWS README README.md
%_bindir/ngp2
%_bindir/ngraph

%files -n libngraph
%_libdir/libngraph.so.0
%_libdir/libngraph.so.0.0.0

%files -n libngraph-devel
%_includedir/ngraph.h
%_libdir/libngraph.so
%dir %_libexecdir/ngraph-gtk
%_libexecdir/ngraph-gtk/*

%files data
%dir %_sysconfdir/ngraph-gtk
%_sysconfdir/ngraph-gtk/Ngraph.ini
%_sysconfdir/ngraph-gtk/Ngraph.ngp
%_sysconfdir/ngraph-gtk/Ngraph.nsc
%_sysconfdir/ngraph-gtk/accel_map
%_sysconfdir/ngraph-gtk/fit.ngp
%dir %_sysconfdir/ngraph-gtk/init.d
%_sysconfdir/ngraph-gtk/init.d/10append_addins.nsc
%dir %_sysconfdir/ngraph-gtk/zsh
%_sysconfdir/ngraph-gtk/zsh/_ngp2
%_sysconfdir/ngraph-gtk/zsh/_ngraph
%_datadir/application-registry/ngraph.applications
%_desktopdir/com.github.htrb.ngraph-gtk.desktop
%_datadir/bash-completion/completions/ngraph
%dir %_datadir/doc/ngraph-gtk
%exclude %_datadir/doc/ngraph-gtk/AUTHORS
%exclude %_datadir/doc/ngraph-gtk/COPYING
%exclude %_datadir/doc/ngraph-gtk/ChangeLog
%exclude %_datadir/doc/ngraph-gtk/NEWS
%exclude %_datadir/doc/ngraph-gtk/README
%dir %_datadir/doc/ngraph-gtk/html
%_datadir/doc/ngraph-gtk/html/*.*
%dir %_datadir/doc/ngraph-gtk/html/img
%_datadir/doc/ngraph-gtk/html/img/*.*
%dir %_datadir/doc/ngraph-gtk/html/ja
%_datadir/doc/ngraph-gtk/html/ja/*.*
%dir %_datadir/doc/ngraph-gtk/html/ja/dialogs
%_datadir/doc/ngraph-gtk/html/ja/dialogs/*.*
%dir %_datadir/doc/ngraph-gtk/html/ja/tutorial
%_datadir/doc/ngraph-gtk/html/ja/tutorial/*.*
%_iconsdir/hicolor/scalable/apps/ngraph.svg
%_iconsdir/hicolor/scalable/mimetypes/application-x-ngraph-graphic.svg
%_iconsdir/hicolor/scalable/mimetypes/application-x-ngraph-script.svg
%_iconsdir/hicolor/scalable/mimetypes/application-x-ngraph.svg
%_man1dir/ngp2.1.xz
%_man1dir/ngraph.1.xz
%_datadir/metainfo/com.github.htrb.ngraph-gtk.metainfo.xml
%_datadir/mime-info/ngraph.keys
%_datadir/mime-info/ngraph.mime
%dir %_datadir/ngraph-gtk
%dir %_datadir/ngraph-gtk/addin
%_datadir/ngraph-gtk/addin/*.*
%dir %_datadir/ngraph-gtk/demo
%_datadir/ngraph-gtk/demo/*.*
%dir %_datadir/ngraph-gtk/gtksourceview
%_datadir/ngraph-gtk/gtksourceview/ngraph-math.lang

%changelog
* Thu Jan 15 2026 Nikolay Strelkov <snk@altlinux.org> 6.09.11-alt1
- Initial build for Sisyphus
