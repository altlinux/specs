%def_disable snapshot

%define ver_major 2.50
%define _libexecdir %_prefix/libexec
%def_enable installed_tests

Name: glib-openssl
Version: %ver_major.7
Release: alt1

Summary: Network-related giomodule for glib using openssl
Group: System/Libraries
License: LGPLv2+
Url: http://www.gnome.org

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.46.0

Requires: ca-certificates

BuildRequires: libgio-devel >= %glib_ver  libssl-devel

%description
This package contains the implementations of certain GLib openssl
features that cannot be implemented directly in GLib itself because of
their dependencies.

%package tests
Summary: Tests for the %name package
Group: Development/Other
Requires: %name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed %name package.


%prep
%setup

%build
%autoreconf
%configure \
	--disable-static \
	%{?_enable_installed_tests:--enable-installed-tests}

%make_build

%install
%makeinstall_std

%find_lang %name

%check
#%%make check

%files -f %name.lang
%_libdir/gio/modules/libgioopenssl.so
%doc NEWS README

%exclude %_libdir/gio/modules/*.la

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%name/
%_datadir/installed-tests/%name/
%endif

%changelog
* Mon Feb 26 2018 Yuri N. Sedunov <aris@altlinux.org> 2.50.7-alt1
- 2.50.7

* Sun Oct 29 2017 Yuri N. Sedunov <aris@altlinux.org> 2.50.6-alt1
- 2.50.6

* Thu Oct 26 2017 Yuri N. Sedunov <aris@altlinux.org> 2.50.5-alt1
- 2.50.5

* Wed Oct 18 2017 Yuri N. Sedunov <aris@altlinux.org> 2.50.4-alt1
- 2.50.4

* Sat Jun 17 2017 Yuri N. Sedunov <aris@altlinux.org> 2.50.3-alt1
- 2.50.3

* Thu Apr 06 2017 Yuri N. Sedunov <aris@altlinux.org> 2.50.2-alt1
- 2.50.2

* Wed Mar 08 2017 Yuri N. Sedunov <aris@altlinux.org> 2.50.1-alt1
- 2.50.1

* Mon Sep 26 2016 Yuri N. Sedunov <aris@altlinux.org> 2.50.0-alt1
- first build for Sisyphus




