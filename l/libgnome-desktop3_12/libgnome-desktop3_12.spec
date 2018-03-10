%def_disable snapshot

%define _libexecdir %_prefix/libexec
%define _name gnome-desktop
%define ver_major 3.26
%define api_ver 3.0
%define sover 12
%define gnome_distributor "%vendor"
%define gnome_date "%(date "+%%B %%e %%Y"), Moscow"
%def_disable static
%def_disable gtk_doc
%def_enable introspection
%def_disable installed_tests
%def_enable udev

Name: lib%{_name}3_%sover
Version: %ver_major.2
Release: alt2

Summary: Library with common API for various GNOME 3 modules
License: %gpl2plus, %fdl
Group: Graphical desktop/GNOME
Url: http://www.gnome.org

%if_disabled snapshot
Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

Obsoletes: %_name
Provides: %_name = %version-%release

BuildPreReq: rpm-build-licenses rpm-build-gnome

# From configure.ac
BuildPreReq: gnome-common >= 2.8.0
BuildPreReq: intltool >= 0.40.6 yelp-tools gtk-doc
BuildPreReq: libgdk-pixbuf-devel >= 2.36.5
BuildPreReq: libgtk+3-devel >= 3.3.6
BuildPreReq: libgio-devel >= 2.53.0
BuildPreReq: gsettings-desktop-schemas-devel >= 3.5.91
BuildRequires: iso-codes-devel
BuildRequires: xkeyboard-config-devel
BuildRequires: libudev-devel
BuildRequires: libseccomp-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel gsettings-desktop-schemas-gir-devel}

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System.  GNOME is similar in purpose and scope
to CDE and KDE, but GNOME is based completely on free software. The

GNOME Desktop provides the core libraries for the gnome desktop.

%prep
%setup -n %_name-%version
[ ! -d m4 ] && mkdir m4

%build
%autoreconf
%configure \
    %{subst_enable static} \
    %{?_enable_gtk_doc:--enable-gtk-doc} \
    --with-gnome-distributor=%gnome_distributor \
    %{?_enable_installed_tests:--enable-installed-tests} \
    %{subst_enable udev}
%make_build

%install
%makeinstall_std

%find_lang --with-gnome --output=%_name.lang %_name-%api_ver fdl gpl lgpl

%files
%_libdir/*.so.*


%changelog
* Fri Mar 16 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt2
- compat library

* Tue Oct 31 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Sun Oct 29 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt2
- lib%%name requires bubblewrap

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Sat Sep 16 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt2
- updated to 3.26.0-1-g22b89aa (fixed BGO #787072)

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Wed Sep 06 2017 Yuri N. Sedunov <aris@altlinux.org> 3.25.92-alt1
- 3.25.92

* Mon May 08 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Sun Apr 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Mon Nov 07 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Mon Oct 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Tue Nov 10 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Tue Oct 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Thu Apr 30 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Wed Nov 26 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt2
- updated to 3.14_2b563b26 (fixed BGO #740289)

* Wed Nov 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Wed Apr 16 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Wed Nov 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt2
- fixed reqs

* Fri Nov 22 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Wed Sep 04 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.4-alt1
- 3.8.4

* Sun Jun 09 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt2
- fixed pnp.ids path

* Sat Jun 08 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Wed Mar 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0.1-alt1
- 3.8.0.1

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Wed Oct 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0.1-alt1
- 3.6.0.1

* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Sun Oct 16 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Wed Oct 05 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt2
- fixed https://bugzilla.gnome.org/show_bug.cgi?id=660482

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Wed Aug 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.5-alt1
- 3.1.5

* Fri May 27 2011 Alexey Shabalin <shaba@altlinux.ru> 3.0.2-alt2
- add empty package gnome-desktop3 with Provides/Obsoletes gnome-desktop
- update find_lang

* Tue May 24 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Wed May 11 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt2
- requires hwdatabase with pnp.ids, not pci.ids (shaba@)

* Tue Apr 05 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Wed Dec 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.91.3-alt1
- first build for Sisyphus

