%def_disable snapshot

%define ver_major 2.56
%define _libexecdir %_prefix/libexec
%define _userinitdir %(pkg-config systemd --variable systemduserunitdir)

%def_enable libproxy
%def_enable gnome_proxy
%def_enable tls
%def_enable pkcs11
%def_enable installed_tests

Name: glib-networking
Version: %ver_major.0
Release: alt1

Summary: Networking support for GIO
Group: System/Libraries
License: LGPLv2+
Url: http://www.gnome.org

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%{?_enable_gnome_proxy:Requires: gsettings-desktop-schemas >= 3.2.0}
%{?_enable_pkcs11:Requires: ca-certificates}

%define glib_ver 2.55.1
%define gnutls_ver 2.12.8
%define p11kit_ver 0.8
%define libproxy_ver 0.3.1

BuildRequires: meson libgio-devel >= %glib_ver
%{?_enable_gnome_proxy:BuildRequires: gsettings-desktop-schemas-devel}
%{?_enable_tls:BuildRequires: libgnutls-devel >= %gnutls_ver libgcrypt-devel}
%{?_enable_pkcs11:BuildRequires: libp11-kit-devel >= %p11kit_ver ca-certificates}
%{?_enable_libproxy:BuildRequires: libproxy-devel >= %libproxy_ver}
BuildRequires: libsystemd-devel

%description
This package contains modules that extend the networking support in GIO.
In particular, it contains a libproxy-based GProxyResolver implementation
and a gnutls-based GTlsConnection implementation.

%package tests
Summary: Tests for the %name package
Group: Development/Other
Requires: %name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed %name package.


%prep
%setup
%ifarch e2k
sed -i 's,-Werror=missing-include-dirs,,' configure*
%endif

%build
%meson \
	%{?_enable_libproxy:-Dlibproxy_support=true} \
	%{?_enable_gnome_proxy:-Dgnome_proxy_support=true} \
	%{?_enable_tls:-Dtls_support=true} \
	%{?_enable_pkcs11:-Dpkcs11_support=true} \
	%{?_enable_installed_tests:-Dinstalled-tests=true} \
	-Dca-certificates_path=%_datadir/ca-certificates/ca-bundle.crt \
	-Dsystemd-user-unit-dir=%_userinitdir
%meson_build

%install
%meson_install

%find_lang %name

%check
#%%meson_test

%files -f %name.lang
%{?_enable_tls:%_libdir/gio/modules/libgiognutls.so}
%{?_enable_gnome_proxy:%_libdir/gio/modules/libgiognomeproxy.so}
%if_enabled libproxy
%_libdir/gio/modules/libgiolibproxy.so
%_libexecdir/glib-pacrunner
%_datadir/dbus-1/services/org.gtk.GLib.PACRunner.service
%_userinitdir/glib-pacrunner.service
%endif
%doc NEWS README

%if_enabled installed_tests
%files tests
#%_libexecdir/installed-tests/%name/
%_datadir/installed-tests/%name/
%endif

%changelog
* Sat Mar 10 2018 Yuri N. Sedunov <aris@altlinux.org> 2.56.0-alt1
- 2.56.0

* Fri Oct 27 2017 Yuri N. Sedunov <aris@altlinux.org> 2.54.1-alt1
- 2.54.1

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 2.54.0-alt1
- 2.54.0

* Fri Jul 28 2017 Yuri N. Sedunov <aris@altlinux.org> 2.50.0-alt2
- updated to 2.50.0-15-gb10e225 (fixed BGO #782218)

* Sat Feb 25 2017 Michael Shigorin <mike@altlinux.org> 2.50.0-alt1.1
- BOOTSTRAP: introduce libproxy knob (on by default)
- E2K: drop -Werror=missing-include-dirs (lcc)

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 2.50.0-alt1
- 2.50.0

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 2.48.2-alt1
- 2.48.2

* Tue Apr 26 2016 Yuri N. Sedunov <aris@altlinux.org> 2.48.1-alt1
- 2.48.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 2.48.0-alt1
- 2.48.0

* Wed Dec 09 2015 Yuri N. Sedunov <aris@altlinux.org> 2.46.1-alt2
- rebuilt against libgnutls.so.30

* Tue Oct 13 2015 Yuri N. Sedunov <aris@altlinux.org> 2.46.1-alt1
- 2.46.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 2.46.0-alt1
- 2.46.0

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 2.44.0-alt1
- 2.44.0

* Sun Dec 07 2014 Yuri N. Sedunov <aris@altlinux.org> 2.42.1-alt1
- 2.42.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 2.42.0-alt1
- 2.42.0

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 2.40.1-alt1
- 2.40.1

* Wed Apr 02 2014 Yuri N. Sedunov <aris@altlinux.org> 2.40.0-alt1.1
- updated to fbfd53fcce

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 2.40.0-alt1
- 2.40.0

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 2.38.2-alt1
- 2.38.2

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 2.38.1-alt1
- 2.38.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 2.38.0-alt1
- 2.38.0

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 2.36.2-alt1
- 2.36.2

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 2.36.1-alt1
- 2.36.1

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 2.36.0-alt1
- 2.36.0

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 2.34.2-alt1
- 2.34.2

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 2.34.0-alt1
- 2.34.0

* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 2.32.3-alt1
- 2.32.3

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Wed Jan 04 2012 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Tue Oct 18 2011 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Tue Sep 27 2011 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 3.2.0

* Tue May 24 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.7-alt1
- 2.28.7

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.6.1-alt1
- 2.28.6.1

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.6-alt1
- 2.28.6

* Tue Mar 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.4-alt1
- 2.28.4

* Tue Mar 08 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt2
- updated buildrqs

* Tue Feb 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Tue Feb 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- first build for Sisyphus

