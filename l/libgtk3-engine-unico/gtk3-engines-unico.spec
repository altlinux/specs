%define _name unico
%define engine_prefix libgtk3-engine
%define unico_revision bzr20121212

Name: %engine_prefix-%_name
Version: 1.0.3
Release: alt1.%{unico_revision}

Summary: Unico GTK3 engine
License: %lgpl3only
Group: Graphical desktop/GNOME
Url: https://launchpad.net/unico
Source0: %_name-%version.tar
Packager: Vladimir Didenko <cow@altlinux.org>

%define gtk_ver 3.0.1
%define gtk_binary_ver 3.0.0
%define gtk_api_ver 3.0
%define engines_dir %_libdir/gtk-%gtk_api_ver/%gtk_binary_ver/theming-engines

BuildPreReq: rpm-build-licenses 
BuildPreReq: intltool >= 0.31.0
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: gnome-common

%description
Unico is a Gtk+ engine that aims to be the more complete yet powerful
theming engine for Gtk+ 3.0 and newer. It is the first Gtk+ engine
written with Gtk+ style context APIs in mind, using CSS as first class
citizen.

%prep
%setup -q -n %_name-%version

%build
export CFLAGS="$RPM_OPT_FLAGS -Wno-error=deprecated-declarations"
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static --enable-compile-warnings=yes

%make_build

%check
%make check

%install
%makeinstall

%files
%engines_dir/libunico.so
%doc AUTHORS README NEWS

%exclude %engines_dir/libunico.la

%changelog
* Tue Feb 19 2013 Vladimir Didenko <cow@altlinux.org> 1.0.3-alt1.bzr20121212
- Updated to 1.0.3.bzr20121212

* Fri Oct 26 2012 Vladimir Didenko <vladimir.didenko@gmail.com> 1.0.2-alt1
- Updated to 1.0.2(trunk)

* Fri Oct 28 2011 Vladimir Didenko <vladimir.didenko@gmail.com> 1.0.1-alt1
- First Build
