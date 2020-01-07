%def_enable snapshot

%define major 1.0
%define api_ver 2.0
%define _noarchpkgconfigdir %_datadir/pkgconfig
%define _libexecdir %_prefix/libexec

%define pkgdocdir %_docdir/lib%name-%version

%def_disable python2
%def_enable fts
%def_enable docs

Name: zeitgeist
Version: %major.2
Release: alt2

Summary: Framework providing Desktop activity awareness
Group: Office
License: LGPL-2.1 and GPL-2.0
# zeitgeist/loggers/iso_strptime.py is LGPLv3 and the rest LGPLv3+
Url: https://launchpad.net/zeitgeist

%if_disabled snapshot
Source: http://launchpad.net/%name/%major/%version/+download/%name-%version.tar.gz
%else
# VCS: git://anongit.freedesktop.org/zeitgeist/zeitgeist
Source: %name-%version.tar
%endif
Patch1: %name-0.9.12-alt-python3_syntax.patch

Requires: lib%name%api_ver = %version-%release

%define glib_ver 2.36
%define vala_ver 0.22
%define tp_glib_ver 0.18

# can't do buildreq correctly
BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: python3-devel python3-module-rdflib
BuildRequires: gcc-c++ libsqlite3-devel libdbus-devel
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel libjson-glib-devel
BuildRequires: libxapian-devel
BuildRequires: libtelepathy-glib-devel >= %tp_glib_ver
BuildRequires: gobject-introspection-devel
BuildRequires: vala-tools >= %vala_ver libtelepathy-glib-vala
BuildRequires: pkgconfig(systemd)
%{?_enable_python2:BuildRequires: python-devel python-module-rdflib}
%{?_enable_docs:BuildRequires: gtk-doc valadoc}
# for autoreconf
BuildRequires: gettext-tools

%description
Zeitgeist is a service which logs the users's activities and events (files
opened, websites visites, conversations hold with other people, etc.) and makes
relevant information available to other applications.

Note that this package only contains the daemon, which you can use
together with several different user interfaces.

%package -n lib%name%api_ver
Summary: Dynamic library to access the Zeitgeist daemon
Group: System/Libraries

%description -n lib%name%api_ver
Zeitgeist is a service which logs the users's activities and events (files
opened, websites visites, conversations hold with other people, etc.) and makes
relevant information available to other applications.

This package contains the dynamic Zeitgeist library, which provides
access to the Zeitgeist daemon.

%package -n lib%name%api_ver-devel
Summary: Development files for Zeitgeist
Group: Development/C
Requires: lib%name%api_ver = %version-%release

%description -n lib%name%api_ver-devel
Zeitgeist is a service which logs the users's activities and events (files
opened, websites visites, conversations hold with other people, etc.) and makes
relevant information available to other applications.

This package contains the development files for the Zeitgeist library.

%package -n lib%name%api_ver-gir
Summary: GObject introspection data for the Zeitgeist library
Group: System/Libraries
Requires: lib%name%api_ver = %version-%release

%description -n lib%name%api_ver-gir
Zeitgeist is a service which logs the users's activities and events (files
opened, websites visites, conversations hold with other people, etc.) and makes
relevant information available to other applications.

This package provides GObject introspection data for the Zeitgeist library.

%package -n lib%name%api_ver-gir-devel
Summary: GObject introspection devel data for the Zeitgeist library
Group: Development/Other
BuildArch: noarch
Requires: lib%name%api_ver-gir = %version-%release
Requires: lib%name%api_ver-devel = %version-%release

%description -n lib%name%api_ver-gir-devel
Zeitgeist is a service which logs the users's activities and events (files
opened, websites visites, conversations hold with other people, etc.) and makes
relevant information available to other applications.

This package provides GObject introspection devel data for the Zeitgeist library.

%package -n python-module-%name%api_ver
Summary: Python bindings for the Zeitgeist library
Group: Development/Python
BuildArch: noarch
Requires: lib%name%api_ver = %version-%release

%description -n python-module-%name%api_ver
Zeitgeist is a service which logs the users's activities and events (files
opened, websites visites, conversations hold with other people, etc.) and makes
relevant information available to other applications.

This package provides Python2 bindings for the Zeitgeist library.

%package -n python3-module-%name%api_ver
Summary: Python3 bindings for the Zeitgeist library
Group: Development/Python3
BuildArch: noarch
Requires: lib%name%api_ver = %version-%release

%description -n python3-module-%name%api_ver
Zeitgeist is a service which logs the users's activities and events (files
opened, websites visites, conversations hold with other people, etc.) and makes
relevant information available to other applications.

This package provides Python3 bindings for the Zeitgeist library.

%package -n lib%name%api_ver-devel-doc
Summary: Development documentation for lib%name%api_ver
Group: Development/Documentation
Conflicts: lib%name%api_ver < %version
BuildArch: noarch

%description -n lib%name%api_ver-devel-doc
This package contains development documentation for the Zeitgeist library.


%prep
%setup
%setup -D -c
%patch1
subst 's/_have/have/' {*/,}data/completions/%name-daemon
%{?_enable_python2:mv %name-%version py2build}

%build
%define opts --disable-static %{subst_enable fts}
%autoreconf
%configure %opts \
%{subst_enable docs} \
	PYTHON=%__python3
%make_build

%if_enabled python2
pushd py2build
%autoreconf
%configure %opts \
    PYTHON=%__python
%make_build
popd
%endif

%install
%makeinstall_std

%if_enabled python2
pushd py2build
%makeinstall_std
%endif

%if_enabled docs
install -d -m755 %buildroot%pkgdocdir
cp -aR doc/lib%name/{docs_c/html,docs_vala} %buildroot%pkgdocdir
%endif

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README
%_bindir/%name-daemon
%_bindir/%name-datahub
%_datadir/%name/
%_datadir/dbus-1/services/org.gnome.%name.Engine.service
%_datadir/dbus-1/services/org.gnome.%name.SimpleIndexer.service
%_prefix/lib/systemd/user/%name.service
%_man1dir/%name-*.*
%_sysconfdir/xdg/autostart/%name-datahub.desktop
%_datadir/bash-completion/completions/%name-daemon

%if_enabled fts
%dir %_libexecdir/%name
%_libexecdir/%name/%name-fts
%_prefix/lib/systemd/user/%name-fts.service
%endif

%if_enabled python2
%files -n python-module-%name%api_ver
%python_sitelibdir_noarch/zeitgeist/
%endif

%files -n python3-module-%name%api_ver
%python3_sitelibdir_noarch/zeitgeist/

%files -n lib%name%api_ver
%_libdir/lib%name-%api_ver.so.*

%files -n lib%name%api_ver-devel
%_includedir/%name-%api_ver/
%_libdir/lib%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc
%_vapidir/%name-%api_ver.deps
%_vapidir/%name-%api_ver.vapi
%_vapidir/%name-datamodel-%api_ver.vapi

%files -n lib%name%api_ver-gir
%_typelibdir/Zeitgeist-2.0.typelib

%files -n lib%name%api_ver-gir-devel
%_girdir/Zeitgeist-2.0.gir

%if_enabled docs
%files -n lib%name%api_ver-devel-doc
%pkgdocdir
%endif

%changelog
* Tue Jan 07 2020 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt2
- updated to v1.0.2-1-gb5c00e80 (fixed build with gettext >= 0.20)
- disabled python2 support

* Sat Jun 01 2019 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1.1
- fixed build without docs

* Tue Feb 05 2019 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Sat Jun 09 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- updated to v1.0.1-3-g2b337c8
- used gtk-doc & valadoc to build documentation

* Fri Oct 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt2
- Rebuilt with new xapian.

* Sat Apr 08 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1.1
- fixed data/completions/%name-daemon

* Fri Mar 31 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- updated to v1.0-1-g1bcc858

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.16-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Aug 11 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.16-alt1
- 0.9.16

* Fri May 22 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.15-alt2
- rebuilt against libxapian-1.2.21 & gcc5

* Sun Oct 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.9.15-alt1
- 0.9.15_ce9affa8

* Fri Aug 02 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.14-alt1
- 0.9.14

* Sun Jun 02 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.13-alt1
- 0.9.13
- enabled FTS support

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.12-alt1
- 0.9.12
- fixed syntax for python3

* Wed Mar 20 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.10-alt1
- 0.9.10
- removed upstreamed -link.patch
- updated buildreqs
- new libzeitgeist2.0{,-devel}, libzeitgeist2.0-gir{,-devel} subpackages
- prepared libzeitgeist2.0-devel-doc subpackage
- python bindings moved to separate noarch subpackages

* Sun Jun 10 2012 Vitaly Lipatov <lav@altlinux.ru> 0.9.0.1-alt1
- new version 0.9.0.1 (with rpmrb script)

* Tue Jan 24 2012 Vitaly Lipatov <lav@altlinux.ru> 0.8.2-alt1
- new version 0.8.2 (with rpmrb script)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.2-alt1.1
- Rebuild with Python-2.7

* Sun Oct 24 2010 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt1
- new version 0.5.2 (with rpmrb script)

* Sun Oct 24 2010 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt1
- initial build for ALT Linux Sisyphus

* Fri Aug 06 2010 Deji Akingunola <dakingun@gmail.com> - 0.5.0-1
- Update to 0.5.0

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jun 15 2010 Deji Akingunola <dakingun@gmail.com> - 0.4.0-1
- Update to 0.4.0

* Wed Apr 21 2010 Deji Akingunola <dakingun@gmail.com> - 0.3.3.1-1
- Update to 0.3.3.1 to fix datasource_registry bug (BZ #586238)

* Wed Apr 21 2010 Deji Akingunola <dakingun@gmail.com> - 0.3.3-1
- Update to 0.3.3

* Wed Jan 20 2010 Deji Akingunola <dakingun@gmail.com> - 0.3.2-1
- Update to 0.3.2

* Thu Jan 14 2010 Deji Akingunola <dakingun@gmail.com> - 0.3.1-1
- Add missing requires (Package reviews)
- Update license tag (Package reviews)
- Update to latest release

* Tue Dec 01 2009 Deji Akingunola <dakingun@gmail.com> - 0.3.0-1
- Update to 0.3.0

* Wed Nov 04 2009 Deji Akingunola <dakingun@gmail.com> - 0.2.1-1
- Initial Fedora packaging

