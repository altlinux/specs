#https://gitlab.gnome.org/GNOME/libsoup/-/issues/225
%def_disable snapshot

%define _name libsoup
%define api_ver 3.0
%define ver_major 3.2
%def_disable static
%def_enable docs
%def_enable introspection
%def_enable vala
%def_with gssapi
%def_enable brotli
%def_disable debug
%def_disable sysprof
# moved to PyGobject since 3.0.1
%def_disable python
%def_disable check

Name: %_name%api_ver
Version: %ver_major.2
Release: alt1

Summary: HTTP client/server library for GNOME
Group: System/Libraries
License: LGPLv2+
Url: https://wiki.gnome.org/Projects/libsoup

%if_enabled snapshot
Source: %_name-%version.tar
%else
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%endif

Requires: glib-networking >= 2.70

%define glib_ver 2.69.1
%define gi_ver 1.33.3
%define psl_ver 0.20.0

BuildRequires(pre): rpm-macros-meson
%{?_enable_python:BuildRequires(pre): rpm-build-python3}
BuildRequires: meson
BuildRequires: glib2-devel >= %glib_ver
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libxml2-devel libsqlite3-devel zlib-devel
BuildRequires: docbook-dtds docbook-style-xsl
BuildRequires: xml-common xsltproc
BuildRequires: glib-networking libpsl-devel >= %psl_ver
BuildRequires: libnghttp2-devel
%{?_enable_introspection:BuildRequires(pre): rpm-build-gir
BuildRequires: gobject-introspection-devel >= %gi_ver}
%{?_enable_vala:BuildRequires(pre): rpm-build-vala
BuildRequires: vala-tools}
%{?_with_gssapi:BuildRequires: libkrb5-devel}
%{?_enable_brotli:BuildRequires: libbrotli-devel}
%{?_enable_sysprof:BuildRequires: pkgconfig(sysprof-capture-4)}
%{?_enable_docs:BuildRequires: gi-docgen}
%{?_enable_check:BuildRequires: /proc curl}

%description
libsoup is an HTTP client/server library for GNOME. It uses GObjects
and the glib main loop, to integrate well with GNOME applications.

%package devel
Summary: Headers for HTTP client/server library for GNOME
Group: Development/C
Requires: %name = %EVR

%description devel
libsoup is an HTTP client/server library for GNOME. It uses GObjects
and the glib main loop, to integrate well with GNOME applications.

This package allows to develop applications that use the Soup library.

%package devel-doc
Summary: Development documentation for HTTP client/server library for GNOME
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
libsoup is an HTTP client/server library for GNOME. It uses GObjects
and the glib main loop, to integrate well with GNOME applications.

This package contains development documentation for Soup.

%package devel-static
Summary: Headers for Simple Object Access Protocol static library
Group: Development/C
Requires: %name-devel = %EVR

%description devel-static
This package allows to develop applications that statically linked
against Soup library.

%package gir
Summary: GObject introspection data for the Soup library
Group: System/Libraries
Requires: %name = %EVR

%description gir
libsoup is an HTTP client/server library for GNOME. It uses GObjects
and the glib main loop, to integrate well with GNOME applications.

This package provides GObject introspection data for the Soup library

%package gir-devel
Summary: GObject introspection devel data for the Soup library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %EVR

%description gir-devel
libsoup is an HTTP client/server library for GNOME. It uses GObjects
and the glib main loop, to integrate well with GNOME applications.

This package provides GObject introspection devel data for the Soup library

%package -n python3-module-%name
Summary: GObject introspection devel data for the Soup library
Group: Development/Python3
BuildArch: noarch

%description -n python3-module-%name
libsoup is an HTTP client/server library for GNOME. It uses GObjects
and the glib main loop, to integrate well with GNOME applications.

This package provides PyGObject overrides for SoupMessageHeaders.

%prep
%setup -n %_name-%version

%build
%ifarch %e2k
%add_optflags -Wno-error=pointer-arith
%endif
%meson \
    %{?_enable_debug:--buildtype=debug} \
    %{?_enable_static:--default-library=both} \
    %{?_enable_gnome:-Dgnome=true} \
    %{?_disable_docs:-Ddocs=disabled} \
    %{?_enable_snapshot:-Dgtk_doc=true} \
    %{?_disable_introspection:-Dintrospection=disabled} \
    %{?_disable_gssapi:-Dgssapi=disabled} \
    %{?_disable_brotli:-Dbrotli=disabled} \
    %{?_enable_sysprof:-Dsysprof=enabled}
%meson_build

%install
%meson_install
%find_lang --output=%_name.lang %_name-%api_ver

%check
%__meson_test

%files -f %_name.lang
%_libdir/%_name-%api_ver.so.*
%doc README NEWS AUTHORS

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%_name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
%{?_enable_vala:%_vapidir/%_name-%api_ver.vapi}
%{?_enable_vala:%_vapidir/%_name-%api_ver.deps}

%if_enabled docs
%files devel-doc
%_datadir/doc/%_name-%api_ver/
%endif

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%if_enabled introspection
%files gir
%_typelibdir/Soup-%api_ver.typelib

%files gir-devel
%_girdir/Soup-%api_ver.gir
%endif

%if_enabled python
%files -n python3-module-%name
%python3_sitelibdir_noarch/gi/overrides/Soup.py
%python3_sitelibdir_noarch/gi/overrides/__pycache__/Soup*.pyc
%endif

%changelog
* Thu Nov 10 2022 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Tue Oct 11 2022 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Tue Sep 20 2022 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Sat Sep 03 2022 Yuri N. Sedunov <aris@altlinux.org> 3.1.4-alt1
- 3.1.4

* Sat Sep 03 2022 Yuri N. Sedunov <aris@altlinux.org> 3.0.8-alt1
- 3.0.8

* Thu Jun 30 2022 Yuri N. Sedunov <aris@altlinux.org> 3.0.7-alt1
- 3.0.7

* Thu Mar 31 2022 Yuri N. Sedunov <aris@altlinux.org> 3.0.6-alt1
- 3.0.6

* Fri Mar 18 2022 Yuri N. Sedunov <aris@altlinux.org> 3.0.5-alt1
- 3.0.5

* Thu Jan 06 2022 Yuri N. Sedunov <aris@altlinux.org> 3.0.4-alt1
- 3.0.4

* Wed Nov 24 2021 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Sun Oct 24 2021 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Sun Sep 26 2021 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Sat Sep 18 2021 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Fri Jun 04 2021 Yuri N. Sedunov <aris@altlinux.org> 2.99.8-alt1
- 2.99.8

* Sat May 22 2021 Yuri N. Sedunov <aris@altlinux.org> 2.99.6-alt1
- 2.99.6

* Tue Apr 20 2021 Yuri N. Sedunov <aris@altlinux.org> 2.99.4-alt1
- 2.99.4

* Wed Mar 10 2021 Yuri N. Sedunov <aris@altlinux.org> 2.99.2-alt1
- 2.99.2 (libsoup-2.4 -> libsoup-3.0)

* Mon Sep 14 2020 Yuri N. Sedunov <aris@altlinux.org> 2.72.0-alt1
- 2.72.0

* Sat Mar 07 2020 Yuri N. Sedunov <aris@altlinux.org> 2.70.0-alt1
- 2.70.0

* Tue Mar 03 2020 Yuri N. Sedunov <aris@altlinux.org> 2.68.4-alt1
- 2.68.4

* Wed Dec 04 2019 Yuri N. Sedunov <aris@altlinux.org> 2.68.3-alt1
- 2.68.3

* Wed Oct 09 2019 Yuri N. Sedunov <aris@altlinux.org> 2.68.2-alt1
- 2.68.2

* Wed Sep 11 2019 Yuri N. Sedunov <aris@altlinux.org> 2.68.1-alt1
- 2.68.1

* Wed Sep 11 2019 Yuri N. Sedunov <aris@altlinux.org> 2.66.3-alt1
- 2.66.3

* Wed May 15 2019 Yuri N. Sedunov <aris@altlinux.org> 2.66.2-alt1
- 2.66.2

* Tue Apr 09 2019 Yuri N. Sedunov <aris@altlinux.org> 2.66.1-alt1
- 2.66.1

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 2.66.0-alt1
- 2.66.0

* Mon Oct 22 2018 Yuri N. Sedunov <aris@altlinux.org> 2.64.2-alt1
- 2.64.2

* Mon Sep 24 2018 Yuri N. Sedunov <aris@altlinux.org> 2.64.1-alt1
- 2.64.1

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 2.64.0-alt1
- 2.64.0

* Fri Aug 10 2018 Yuri N. Sedunov <aris@altlinux.org> 2.62.3-alt1
- 2.62.3

* Thu Jun 21 2018 Yuri N. Sedunov <aris@altlinux.org> 2.62.2-alt2
- used -Wno-error=pointer-arith for %%e2k

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 2.62.2-alt1
- 2.62.2

* Mon Apr 09 2018 Yuri N. Sedunov <aris@altlinux.org> 2.62.1-alt1
- 2.62.1

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 2.62.0-alt1
- 2.62.0

* Tue Jan 09 2018 Yuri N. Sedunov <aris@altlinux.org> 2.60.3-alt1
- 2.60.3

* Fri Oct 27 2017 Yuri N. Sedunov <aris@altlinux.org> 2.60.2-alt1
- 2.60.2

* Wed Oct 11 2017 Yuri N. Sedunov <aris@altlinux.org> 2.60.1-alt1
- 2.60.1

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 2.60.0-alt1
- 2.60.0

* Mon Aug 14 2017 Yuri N. Sedunov <aris@altlinux.org> 2.58.2-alt1
- 2.58.2 (fixed CVE-2017-2885)

* Mon May 08 2017 Yuri N. Sedunov <aris@altlinux.org> 2.58.1-alt1
- 2.58.1

* Thu Apr 20 2017 Yuri N. Sedunov <aris@altlinux.org> 2.58.0-alt1
- 2.58.0

* Wed Feb 15 2017 Yuri N. Sedunov <aris@altlinux.org> 2.57.1-alt1
- 2.57.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 2.56.0-alt1
- 2.56.0

* Tue Apr 26 2016 Yuri N. Sedunov <aris@altlinux.org> 2.54.1-alt1
- 2.54.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 2.54.0-alt1
- 2.54.0

* Mon Nov 09 2015 Yuri N. Sedunov <aris@altlinux.org> 2.52.2-alt1
- 2.52.2

* Fri Oct 16 2015 Yuri N. Sedunov <aris@altlinux.org> 2.52.1-alt2
- 2.52.1_c4d290d9

* Tue Oct 13 2015 Yuri N. Sedunov <aris@altlinux.org> 2.52.1-alt1
- 2.52.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 2.52.0-alt1
- 2.52.0

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 2.50.0-alt1
- 2.50.0

* Sun Dec 07 2014 Yuri N. Sedunov <aris@altlinux.org> 2.48.1-alt1
- 2.48.1

* Wed Dec 03 2014 Yuri N. Sedunov <aris@altlinux.org> 2.48.0-alt2
- updated to 2.48.0_c8ff05b7 (fixed BGO ##738003, 727138, 729987...)

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 2.48.0-alt1
- 2.48.0

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 2.46.0-alt1
- 2.46.0

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 2.44.2-alt1
- 2.44.2

* Sat Oct 26 2013 Yuri N. Sedunov <aris@altlinux.org> 2.44.1-alt2
- fixed BGO #695652 from upstream

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 2.44.1-alt1
- 2.44.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 2.44.0-alt1
- 2.44.0
- libsoup-compat.lds: removed symbols:
  soup_proxy_resolver_static_get_type
  soup_proxy_resolver_static_new

* Thu Apr 25 2013 Yuri N. Sedunov <aris@altlinux.org> 2.42.2-alt1
- 2.42.2

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 2.42.1-alt1
- 2.42.1

* Tue Apr 02 2013 Yuri N. Sedunov <aris@altlinux.org> 2.42.0-alt1.1
- after 2.42.0 snapshot (6666b3cd)

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 2.42.0-alt1
- 2.42.0
- libsoup-compat.lds: removed symbols:
  soup_auth_manager_emit_authenticate
  soup_auth_manager_ntlm_get_type
  soup_session_cleanup_connections
  soup_session_make_connect_message
  soup_session_send_queue_item
  soup_session_set_item_status
  soup_session_unqueue_item

* Tue Jan 15 2013 Yuri N. Sedunov <aris@altlinux.org> 2.40.3-alt1
- 2.40.3

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 2.40.2-alt1
- 2.40.2

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 2.40.1-alt1
- 2.40.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 2.40.0-alt1
- 2.40.0
- removed soup_connection_get_tunnel_addr from libsoup-compat.lds

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 2.38.1-alt1
- 2.38.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 2.38.0-alt1
- 2.38.0
- removed soup_marshal_* from libsoup-compat.lds
- %%check temporarily disabled

* Tue Oct 18 2011 Yuri N. Sedunov <aris@altlinux.org> 2.36.1-alt1
- 2.36.1

* Tue Sep 20 2011 Yuri N. Sedunov <aris@altlinux.org> 2.35.92-alt1
- 2.35.92
- removed soup_connection_start_ssl from libsoup-compat.lds

* Tue Aug 02 2011 Dmitry V. Levin <ldv@altlinux.org> 2.34.3-alt1
- Updated to 2.34.3 (fixes CVE-2011-2524).

* Tue May 24 2011 Yuri N. Sedunov <aris@altlinux.org> 2.34.2-alt1
- 2.34.2

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 2.34.1-alt1
- 2.34.1

* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 2.34.0-alt1
- 2.34.0

* Thu Mar 24 2011 Alexey Tourbin <at@altlinux.ru> 2.33.92-alt2
- disabled symbol versioning

* Tue Mar 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.33.92-alt1
- 2.33.92

* Tue Feb 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.33.90-alt1
- 2.33.90

* Sat Dec 18 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.2-alt1
- 2.32.2

* Tue Nov 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Fri Nov 05 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt2
- rebuild for update dependencies

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Tue Aug 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.6-alt1
- 2.31.6
- updated version scripts for SOUP_2.31.6
- introspection support

* Tue Jun 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt2
- fix for gnome bug #622857 from upstream

* Tue Jun 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2
- updated version script for SOUP_2.30.2

* Thu Apr 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Thu Apr 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt2
- fixed https://bugzilla.gnome.org/show_bug.cgi?id=613442

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0
- %%check section

* Mon Mar 15 2010 Alexey Shabalin <shaba@altlinux.ru> 2.29.91-alt2
- rebuild with new libproxy-0.4.0

* Tue Feb 23 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Tue Feb 09 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt1
- 2.29.90 from git
- updated version scripts for SOUP_2.29.90

* Tue Jan 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.6-alt1
- 2.29.6

* Tue Jan 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.5-alt1
- 2.29.5
- updated version scripts for SOUP_2.29.5

* Wed Dec 02 2009 Yuri N. Sedunov <aris@altlinux.org> 2.29.3-alt1
- 2.29.3
- updated version scripts for SOUP_2.29.3

* Tue Oct 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Wed Sep 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Tue Aug 25 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91
- updated version script for SOUP_2.27.91 and  SOUP_GNOME_2.27.91

* Tue Aug 11 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- 2.27.90
- updated version scripts for SOUP_2.27.90

* Mon Aug 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.5-alt1
- 2.27.5

* Mon Jul 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.4-alt1
- 2.27.4
- updated version scripts for SOUP_2.27.4

* Tue Jun 30 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3
- updated version scripts for SOUP_2.26.3

* Mon May 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Thu Apr 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0.9-alt1
- new version
- updated version script for SOUP_GNOME_2.26.0.9

* Tue Mar 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Tue Feb 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.91-alt1
- 2.25.91

* Tue Feb 03 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.5-alt1
- 2.25.5
- added libproxy-devel to buildreqs

* Wed Jan 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.4-alt1
- 2.25.4
- updated version scripts for SOUP_2.25.4
- new libsoup-gnome{,-devel} packages
- added versioning for SOUP_GNOME_2.25.4
- updated buildreqs

* Tue Jan 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Mon Jan 05 2009 Alexey Shabalin <shaba@altlinux.ru> 2.24.2.1-alt1.1
- rebuild with gnutls-2.6

* Tue Nov 25 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2.1-alt1
- new version

* Mon Nov 24 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- removed obsolete *ldconfig from %%post{,un}

* Tue Oct 21 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1
- don't rebuild documentation

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0.1-alt1
- 2.24.0.1
- add versioning
- build devel-doc as noarch

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> %api_ver.1-alt1
- 2.4.1

* Mon Mar 17 2008 Alexey Shabalin <shaba@altlinux.ru> %api_ver.0-alt1.1
- build for Sisyphus

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> %api_ver.0-alt1
- add provides/obsoletes

* Wed Mar 12 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> %api_ver.0-alt0.1
- 2.4.0

* Fri Nov 30 2007 Ilya Mashkin <oddity@altlinux.ru> 2.2.104-alt1
- updated to 2.2.104

* Thu Nov 22 2007 Ilya Mashkin <oddity@altlinux.ru> 2.2.103-alt1
- updated to 2.2.103  (fix #13486)
- add libsoup-2.2.103-client-ssl.patch (fix #13485)

* Sat Feb 24 2007 Ilya Mashkin <oddity@altlinux.ru> 2.2.100-alt1
- updated to 2.2.100
- disabled old patches

* Mon Jan 01 2007 Ilya Mashkin <oddity@altlinux.ru> 2.2.96-alt2
- fix URL

* Fri Sep 01 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.2.96-alt1
- Updated to 2.2.96

* Tue May 30 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.2.93-alt1
- Release 2.2.93
- Patch1: Remove internal dependencies from pkgconfig flags,
  using the Requires tag instead (bug 9568)

* Sat Apr 15 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.2.92-alt1
- Release 2.2.92

* Thu Mar 30 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.2.91-alt2
- Patch0: add missing libraries to linker flags

* Thu Mar 30 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.2.91-alt1
- 2.2.91
- Install the license symlink
- Compressed ChangeLog

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.2.7-alt1.1
- Rebuilt for new pkg-config dependencies.

* Tue Nov 29 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.2.7-alt1
- 2.2.7

* Wed Aug 31 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.2.6.1-alt1
- Updated to 2.2.6.1

* Wed Jun 01 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.2.3-alt1.1
- Rebuilt with libgnutls.so.12.

* Tue Mar 15 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.2.3-alt1
- 2.2.3

* Fri Feb 18 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.2.2-alt1
- 2.2.2
- documentation moved to devel-doc subpackage.

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Thu Sep 09 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Tue Jul 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.1.12-alt1
- 2.1.12

* Sat Jun 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.1.11-alt1
- 2.1.11

* Fri May 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.1.10-alt1
- 2.1.10

* Thu Apr 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.1.9-alt2
- rebuild against new gnutls (1.0.10).

* Tue Apr 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.1.9-alt1
- 2.1.9

* Sat Mar 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.1.8-alt1
- 2.1.8

* Wed Feb 11 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.1.7-alt1
- 2.1.7

* Tue Feb 10 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.1.6-alt1
- 2.1.6

* Tue Jan 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- new version

* Thu Jun 19 2003 AEN <aen@altlinux.ru> 1.99.23-alt1
- new version
- obsolete packagw soup

* Mon Nov 18 2002 AEN <aen@altlinux.ru> 0.7.9-alt1
- 0.7.9 release

* Fri Oct 25 2002 AEN <aen@altlinux.ru> 0.7.9-alt0.1
- first Sisyphus build, spec based on Ximian's

* Fri Oct 25 2002 Ximian, Inc.

- Version: 0.7.8.99-snap.ximian.200210250601
- Summary: New build.
- New automated build.

* Tue Oct 1 2002 Ximian, Inc.

- Version: 0.7.8-ximian.1
- Summary: New build.
- New automated build.

* Sun Mar 3 2002 Ximian, Inc.

- Version: 0.6.0-ximian.1
- Summary: New build.
- New automated build.
