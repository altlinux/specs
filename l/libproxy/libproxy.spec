%define _unpackaged_files_terminate_build 1

%def_with curl
%def_with gnome
%def_with kde
%def_with env
%def_with sysconfig
%def_with duktape

Name: libproxy
Version: 0.5.8
Release: alt1
Summary: A library that provides automatic proxy configuration management

Group: System/Libraries
License:  GPL-2.0-or-later AND LGPL-2.1-or-later
Url: http://libproxy.github.io/libproxy
Vcs: https://github.com/libproxy/libproxy.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson rpm-build-vala rpm-build-gir
BuildRequires: meson >= 0.59.0 vala-tools
BuildRequires: pkgconfig(glib-2.0) >= 2.71.3 pkgconfig(gio-2.0) >= 2.71.3 pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0) /usr/bin/g-ir-scanner gir(Gio) = 2.0
BuildRequires: gi-docgen
%{?_with_curl:BuildRequires: pkgconfig(libcurl)}
%{?_with_gnome:BuildRequires: pkgconfig(gsettings-desktop-schemas)}
%{?_with_duktape:BuildRequires: pkgconfig(duktape)}

Provides: %name-gnome = %EVR
Obsoletes: %name-gnome < 0.5.0
Provides: %name-gnome3 = %EVR
Obsoletes: %name-gnome3 < 0.5.0
Provides: %name-kde = %EVR
Obsoletes: %name-kde < 0.5.0
Provides: %name-kde4 = %EVR
Obsoletes: %name-kde4 < 0.5.0
Provides: %name-mozjs = %EVR
Obsoletes: %name-mozjs < 0.5.0
Provides: %name-webkit = %EVR
Obsoletes: %name-webkit < 0.5.0
Provides: %name-networkmanager = %EVR
Obsoletes: %name-networkmanager < 0.5.0

%description
libproxy is a library that provides automatic proxy configuration management.

libproxy offers the following features:
- support for all major platforms: Windows, Mac and Linux/UNIX
- extremely small core footprint
- minimal dependencies within libproxy core
- only 4 functions in the stable-ish external API
- dynamic adjustment to changing network topology
- a standard way of dealing with proxy settings across all scenarios
- a sublime sense of joy and accomplishment

%package tools
Summary: A sample & test application to test what libproxy will reply
Group: Networking/Other
Requires: %name = %version-%release

%description tools
A simple application that will use libproxy to give the results you can expect from.
other applications. Great to debug what would happen.

%package gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %name library.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package devel-doc
Summary: Development docs package for %name libraries
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
Development docs package for %name libraries.

%prep
%setup -q
%patch -p1

%build
%meson \
    -Drelease=true \
    %{?_without_curl:-Dcurl=false} \
    %{?_without_gnome:-Dconfig-gnome=false} \
    %{?_without_kde:-Dconfig-kde=false} \
    %{?_without_env:-Dconfig-env=false} \
    %{?_without_sysconfig:-Dconfig-sysconfig=false} \
    %{?_without_duktape:-Dpacrunner-duktape=false} \
    -Dconfig-xdp=true \
    -Dconfig-windows=false \
    -Dconfig-osx=false

%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc README.md
%_libdir/*.so.*
%_libdir/%name

%files tools
%_bindir/proxy
%_man8dir/proxy.*

%files gir
%_typelibdir/*.typelib

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_girdir/*.gir
%_vapidir/libproxy-1.0.*

%files devel-doc
%_defaultdocdir/libproxy-1.0

%changelog
* Wed Jul 24 2024 Alexey Shabalin <shaba@altlinux.org> 0.5.8-alt1
- New version 0.5.8.

* Thu Jul 04 2024 Alexey Shabalin <shaba@altlinux.org> 0.5.7-alt1
- New version 0.5.7.

* Sun May 19 2024 Alexey Shabalin <shaba@altlinux.org> 0.5.6-alt1
- New version 0.5.6.

* Thu Dec 07 2023 Michael Shigorin <mike@altlinux.org> 0.5.3-alt1.2
- un-bootstrap (build with duktape again)

* Thu Dec 07 2023 Michael Shigorin <mike@altlinux.org> 0.5.3-alt1.1
- bootstrap build without duktape (to upgrade it)

* Mon Aug 21 2023 Alexey Shabalin <shaba@altlinux.org> 0.5.3-alt1
- New version 0.5.3.

* Mon Jul 03 2023 Alexey Shabalin <shaba@altlinux.org> 0.5.2-alt1
- 0.5.2

* Thu Sep 29 2022 Alexey Shabalin <shaba@altlinux.org> 0.4.18-alt1
- 0.4.18

* Wed Mar 23 2022 Alexey Shabalin <shaba@altlinux.org> 0.4.17-alt2
- Support Python 3.10 and above
- Use kf5-config instead of qtpaths

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 0.4.17-alt1.1
- NMU: spec: adapted to new cmake macros.

* Tue Jan 19 2021 Alexey Shabalin <shaba@altlinux.org> 0.4.17-alt1
- 0.4.17
- Build withot pacrunner mozjs.

* Wed Nov 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.15-alt5
- Fixed python2 and python3 switches.

* Wed Nov 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.15-alt4
- Applied security fixes from upstream (Fixes: CVE-2020-25219, CVE-2020-26154)

* Fri Apr 03 2020 Igor Vlasenko <viy@altlinux.ru> 0.4.15-alt3.1
- NMU: applied logoved fixes

* Sat Apr 20 2019 Alexey Shabalin <shaba@altlinux.org> 0.4.15-alt3
- fixed build with python-3.7
- build with mozjs-60

* Wed Oct 03 2018 Alexey Shabalin <shaba@altlinux.org> 0.4.15-alt2
- backport patches for build with mozjs-52

* Fri Jun 16 2017 Alexey Shabalin <shaba@altlinux.ru> 0.4.15-alt1
- 0.4.15

* Fri Jan 20 2017 Alexey Shabalin <shaba@altlinux.ru> 0.4.14-alt1
- 0.4.14
- add python3 package

* Tue Jun 14 2016 Alexey Shabalin <shaba@altlinux.ru> 0.4.13-alt1
- 0.4.13

* Wed Mar 16 2016 Alexey Shabalin <shaba@altlinux.ru> 0.4.12-alt1
- 0.4.12

* Tue Jan 29 2013 Alexey Shabalin <shaba@altlinux.ru> 0.4.11-alt1
- 0.4.11

* Fri Oct 26 2012 Alexey Shabalin <shaba@altlinux.ru> 0.4.10-alt1
- 0.4.10

* Tue Jan 17 2012 Alexey Shabalin <shaba@altlinux.ru> 0.4.7-alt3
- disable build with RPATH

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.7-alt2.1
- Rebuild with Python-2.7

* Mon Oct 24 2011 Alexey Shabalin <shaba@altlinux.ru> 0.4.7-alt2
- build svn snapshot (20110903)
- rebuild with new libwebkitgtk-1.6.1
- build with libmozjs

* Mon Aug 22 2011 Alexey Shabalin <shaba@altlinux.ru> 0.4.7-alt1
- 0.4.7
- build without mozjs support
- build without gnome and webkitgtk support (but with gnome3 and webkitgtk3)

* Thu May 05 2011 Alexey Shabalin <shaba@altlinux.ru> 0.4.6-alt3
- pre 0.4.7
- add gnome3 subpackage
- build gnome2 and gnome3 support
- build python binding as noarch
- build with xulrunner-2.0

* Fri Oct 08 2010 Alexey Shabalin <shaba@altlinux.ru> 0.4.6-alt2
- rebuild with new libwebkitgtk

* Tue Oct 05 2010 Alexey Shabalin <shaba@altlinux.ru> 0.4.6-alt1
- 0.4.6
- run tests

* Wed May 19 2010 Alexey Shabalin <shaba@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Fri May 07 2010 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt3
- fix upstream bug #108 (http://code.google.com/p/libproxy/issues/detail?id=108)

* Thu Apr 08 2010 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt2
- svn snapshot r659
- enable build with RPATH

* Thu Mar 11 2010 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt1
- 0.4.0 + svn snapshot r622
- disable mono binding

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.1
- Rebuilt with python 2.6

* Thu Oct 29 2009 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Wed Sep 23 2009 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt1
- 0.3.0
- networkmanager package
- .Net bindings package
- update descriptions
- add versioning

* Tue May 05 2009 Alexey Shabalin <shaba@altlinux.ru> 0.2.3-alt2.r334
- svn r334
- update spec for build from git.alt

* Fri Apr 10 2009 Alexey Shabalin <shaba@altlinux.ru> 0.2.3-alt1.1
- rebuild with webkit-1.1.4

* Tue Feb 03 2009 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- adapted for Sisyphus

* Thu Jan 22 2009 kwizart < kwizart at gmail.com > - 0.2.3-8
- Merge NetworkManager module into the main libproxy package
- Main Requires the -python and -bin subpackage
 (splitted for multilibs compliance).

* Fri Oct 24 2008 kwizart < kwizart at gmail.com > - 0.2.3-7
- Disable Gnome/KDE default support via builtin modules.
 (it needs to be integrated via Gconf2/neon instead).

* Tue Oct 21 2008 kwizart < kwizart at gmail.com > - 0.2.3-6
- Disable Obsoletes.
- Requires ev instead of evr for optionnals sub-packages.

* Tue Oct 21 2008 kwizart < kwizart at gmail.com > - 0.2.3-5
- Use conditionals build.

* Mon Sep 15 2008 kwizart < kwizart at gmail.com > - 0.2.3-4
- Remove plugin- in the name of the packages

* Mon Aug  4 2008 kwizart < kwizart at gmail.com > - 0.2.3-3
- Move proxy.h to libproxy/proxy.h
  This will prevent it to be included in the default include path
- Split main to libs and util and use libproxy to install all

* Mon Aug  4 2008 kwizart < kwizart at gmail.com > - 0.2.3-2
- Rename binding-python to python
- Add Requires: gecko-libs >= %%{gecko_version}
- Fix some descriptions
- Add plugin-webkit package

* Fri Jul 11 2008 kwizart < kwizart at gmail.com > - 0.2.3-1
- Convert to Fedora spec

* Fri Jun 6 2008 - dominique-rpm@leuenberger.net
- Updated to version 0.2.3
* Wed Jun 4 2008 - dominique-rpm@leuenberger.net
- Extended spec file to build all available plugins
* Tue Jun 3 2008 - dominique-rpm@leuenberger.net
- Initial spec file for Version 0.2.2

