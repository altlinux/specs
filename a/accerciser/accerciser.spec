%def_disable snapshot

%define ver_major 3.42
%define xdg_name org.gnome.accerciser

Name: accerciser
Version: %ver_major.0
Release: alt1

Summary: Interactive Python accessibility explorer
Group: Accessibility
License: BSD-3-Clause
Url: https://wiki.gnome.org/Apps/Accerciser

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

BuildArch: noarch

Requires: python3-module-%name = %EVR
Requires: python3-module-ipython
Requires: at-spi2-core

%add_python3_path %_datadir/%name
%add_python3_req_skip gi.repository.GLib
%add_python3_req_skip gi.repository.Gio

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: rpm-build-gnome libappstream-glib-devel
BuildRequires: yelp-tools libgtk+3-devel python3-module-pygobject3-devel
BuildRequires: desktop-file-utils libat-spi2-core-devel
BuildRequires: python3-module-ipython
%{?_enable_snapshot:BuildRequires: libappstream-glib-devel}

%description
An interactive Python accessibility explorer for the GNOME desktop.

It uses AT-SPI2 to inspect and control widgets, allowing you to check
if an application is providing correct information to assistive
technologies and automated test frameworks. Accerciser has a simple
plugin framework which you can use to create custom views of
accessibility information.

Accerciser uses libwnck designed to work in X11 only.

%package -n python3-module-%name
Summary: Python module for accerciser
Group: Development/Python3
BuildArch: noarch
Requires: typelib(Gtk) = 3.0 libgtk+3-gir >= 3.24
Requires: typelib(Wnck) = 3.0

%description -n python3-module-%name
An interactive Python accessibility explorer.

This package contains Python module for accerciser.

%prep
%setup
%{?_enable_snapshot:ln -s README.md README}

%build
#NOCONFIGURE=1 ./autogen.sh
%autoreconf
%configure PYTHON=%__python3
%make_build

%install
%makeinstall_std
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=X-Development-Accessibility \
        %buildroot%_desktopdir/%name.desktop

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_datadir/%name
%_desktopdir/%name.desktop
%_man1dir/*
%_datadir/glib-2.0/schemas/*
%_datadir/icons/hicolor/*/*/%name.png
%_datadir/icons/hicolor/scalable/apps/accerciser.svg
%_datadir/icons/hicolor/symbolic/apps/accerciser-symbolic.svg
%_datadir/metainfo/accerciser.appdata.xml
%doc AUTHORS README* COPYING NEWS

%files -n python3-module-%name
%python3_sitelibdir/%name/

%changelog
* Sun Oct 08 2023 Yuri N. Sedunov <aris@altlinux.org> 3.42.0-alt1
- 3.42.0

* Tue May 16 2023 Yuri N. Sedunov <aris@altlinux.org> 3.40.0-alt2
- updated to 3.40.0-21-g5447968
- fixed dependencies

* Fri Jul 29 2022 Yuri N. Sedunov <aris@altlinux.org> 3.40.0-alt1
- 3.40.0

* Thu Sep 10 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Thu Aug 06 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.3-alt1
- 3.36.3

* Sat Jul 04 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.2-alt1
- 3.36.2

* Sat Apr 25 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Mon Mar 09 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Wed Feb 12 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.4-alt1
- 3.34.4
- updated dependencies
- fixed License tag

* Thu Jan 02 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.3-alt1
- 3.34.3

* Tue Nov 26 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2

* Mon Oct 07 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Sat Sep 07 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Thu Jun 20 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.3-alt1
- 3.32.3

* Sat May 25 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Sun Apr 07 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Fri Mar 29 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Fri Sep 30 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.14.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Paul Wolneykien <manowar@altlinux.org> 3.14.0-alt1
- Fresh up to v3.14.0 with the help of cronbuild and update-source-functions.

* Mon Apr 14 2014 Paul Wolneykien <manowar@altlinux.org> 3.12.0-alt1
- Fresh up to v3.12.0 with the help of cronbuild and update-source-functions.

* Wed Mar 12 2014 Paul Wolneykien <manowar@altlinux.org> 3.8.2-alt2
- Update the sources via script. Skip unstable branches.

* Tue May 14 2013 Paul Wolneykien <manowar@altlinux.org> 3.8.2-alt1
- new version 3.8.2

* Wed Apr 10 2013 Paul Wolneykien <manowar@altlinux.ru> 3.8.0-alt1
- Build with Python 3.
- New version 3.8.0.

* Sat Nov 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt2
- Clean spec

* Fri Nov 23 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt1
- Version 3.6.2 (ALT #28019)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.12.1-alt5.1
- Rebuild with Python-2.7

* Wed Oct 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt5
- updated watch file, updated future BuildRequires: for 3.2.x version

* Wed Oct 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt4
- added future BuildRequires: for 3.2.x version

* Tue Oct 11 2011 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt3
- find_lang finds gnome_helpdir, no need to package it explicitly

* Mon Oct 10 2011 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt2
- use find_lang, updated desktop file categories

* Sun Oct 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt1
- intermediate update to 1.12.1. added watch file.

* Sun Oct 10 2010 Michael Pozhidaev <msp@altlinux.ru> 1.11.1-alt1
- New version 1.11.1 (closes: #23423)

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.3-alt1
- Version 1.9.3

* Thu Mar 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt3
- Extracted python module into separate package

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2.1
- Rebuilt with python 2.6

* Wed Oct 15 2008 Michael Pozhidaev <msp@altlinux.ru> 1.4.0-alt2
- Fixed gconf schema installation

* Sun Sep 28 2008 Michael Pozhidaev <msp@altlinux.ru> 1.4.0-alt1
- ALT Linux package

* Thu Apr 12 2007 Peter Parente <parente@cs.unc.edu>
- Added gconf schema install, uninstall, and files

* Mon Apr 02 2007 Peter Parente <parente@cs.unc.edu>
- Added without-pyreqs flag to avoid checking for modules at rpmbuild time
- Added locales to files section

* Wed Feb 22 2007 Peter Parente <parente@cs.unc.edu>
- First release
