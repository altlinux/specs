%define _name geoclue
%define gitdate 20090310
%define git_version 3a31d26
%define tarfile %_name-%version-%gitdate.tar.gz
#%define snapshot %{gitdate}git%git_version
%define snapshot %nil

# Tarfile created using git
# git clone git://anongit.freedesktop.org/geoclue
# git archive --format=tar --prefix=geoclue-0.11.1.1/ %git_version | gzip > ~/RPM/SOURCES/geoclue-0.11.1.1-20090310.tar.gz

Name: lib%_name
Version: 0.12.0
Release: alt5%snapshot

Summary: A modular geoinformation service
Group: System/Libraries
License: LGPLv2
Url: http://geoclue.freedesktop.org/

Source: http://folks.o-hand.com/jku/geoclue-releases/%_name-%version.tar.gz
#Source: %tarfile
# from upstream
Patch: %_name-0.12.0-nm-0.9.patch
Patch1: %_name-unused-var.patch
Patch2: %_name-0.12.0-g_thread_init.patch

BuildRequires: libdbus-glib-devel
BuildRequires: glib2-devel
BuildRequires: libxml2-devel
BuildRequires: libGConf2-devel
BuildRequires: libgtk+2-devel
BuildRequires: NetworkManager-glib-devel
BuildRequires: libgypsy-devel
BuildRequires: libgps-devel >= 2.91
# for skyhook provider
BuildRequires: libsoup-gnome-devel
BuildRequires: gtk-doc

%description
Geoclue is a modular geoinformation service built on top of the D-Bus
messaging system. The goal of the Geoclue project is to make creating
location-aware applications as simple as possible.

%package devel
Summary: Development package for geoclue
Group: Development/C
Requires: %name = %version-%release

%description devel
Files for development with geoclue.

%package devel-doc
Summary: Developer documentation for geoclue
Group: Development/C
Conflicts: %name < %version
BuildArch: noarch

%description devel-doc
Developer documentation for geoclue

%package -n %_name-gui
Summary: Testing gui for geoclue
Group: Development/C
Requires: %name = %version-%release

%description -n %_name-gui
Testing gui for geoclue

%package -n %_name-gpsd
Summary: gpsd provider for geoclue
Group: Monitoring
Requires: %name = %version-%release
Requires: gpsd

%description -n %_name-gpsd
A gpsd provider for geoclue

%package -n %_name-gypsy
Summary: gypsy provider for geoclue
Group: Monitoring
Requires: %name = %version-%release
Requires: gypsy-daemon

%description -n %_name-gypsy
A gypsy provider for geoclue

%prep
%setup -q -n %_name-%version
%patch -p1
%patch1 -p1
%patch2 -p1

%build
%autoreconf
%configure --disable-static --enable-gtk-doc
# SMP-incompatible build
%make

%install
make install DESTDIR=%buildroot
# Install the test gui as it seems the test isn't installed any more
mkdir %buildroot%_bindir
cp test/.libs/geoclue-test-gui %buildroot%_bindir/

%files
%dir %_datadir/geoclue-providers
%_libdir/libgeoclue.so.0
%_libdir/libgeoclue.so.0.0.0
%_datadir/dbus-1/services/org.freedesktop.Geoclue.Master.service
%_datadir/dbus-1/services/org.freedesktop.Geoclue.Providers.Example.service
%_datadir/dbus-1/services/org.freedesktop.Geoclue.Providers.Geonames.service
%_datadir/dbus-1/services/org.freedesktop.Geoclue.Providers.Hostip.service
%_datadir/dbus-1/services/org.freedesktop.Geoclue.Providers.Localnet.service
%_datadir/dbus-1/services/org.freedesktop.Geoclue.Providers.Manual.service
%_datadir/dbus-1/services/org.freedesktop.Geoclue.Providers.Plazes.service
%_datadir/dbus-1/services/org.freedesktop.Geoclue.Providers.Yahoo.service
%_datadir/dbus-1/services/org.freedesktop.Geoclue.Providers.Gsmloc.service
%_datadir/dbus-1/services/org.freedesktop.Geoclue.Providers.Nominatim.service
%_datadir/dbus-1/services/org.freedesktop.Geoclue.Providers.Skyhook.service
%_datadir/geoclue-providers/geoclue-example.provider
%_datadir/geoclue-providers/geoclue-geonames.provider
%_datadir/geoclue-providers/geoclue-hostip.provider
%_datadir/geoclue-providers/geoclue-localnet.provider
%_datadir/geoclue-providers/geoclue-manual.provider
%_datadir/geoclue-providers/geoclue-plazes.provider
%_datadir/geoclue-providers/geoclue-yahoo.provider
%_datadir/geoclue-providers/geoclue-gsmloc.provider
%_datadir/geoclue-providers/geoclue-nominatim.provider
%_datadir/geoclue-providers/geoclue-skyhook.provider
%_libexecdir/geoclue-example
%_libexecdir/geoclue-geonames
%_libexecdir/geoclue-hostip
%_libexecdir/geoclue-localnet
%_libexecdir/geoclue-manual
%_libexecdir/geoclue-master
%_libexecdir/geoclue-plazes
%_libexecdir/geoclue-yahoo
%_libexecdir/geoclue-gsmloc
%_libexecdir/geoclue-nominatim
%_libexecdir/geoclue-skyhook
%doc AUTHORS README

%files devel
%_includedir/geoclue
%_libdir/libgeoclue.so
%_libdir/pkgconfig/geoclue.pc

%files devel-doc
%_datadir/gtk-doc/html/geoclue/

%files -n %_name-gui
%_bindir/geoclue-test-gui

%files -n %_name-gpsd
%_libexecdir/geoclue-gpsd
%_datadir/geoclue-providers/geoclue-gpsd.provider
%_datadir/dbus-1/services/org.freedesktop.Geoclue.Providers.Gpsd.service

%files -n %_name-gypsy
%_libexecdir/geoclue-gypsy
%_datadir/geoclue-providers/geoclue-gypsy.provider
%_datadir/dbus-1/services/org.freedesktop.Geoclue.Providers.Gypsy.service

%changelog
* Thu May 31 2012 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt5
- fixed build with gcc-4.6 and glib-2.32
- built lost skyhook provider

* Thu Mar 24 2011 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt4
- built against nm-0.9

* Fri Mar 11 2011 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt3
- rebuild for debuginfo

* Thu Nov 11 2010 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt2
- rebuild for soname set-versions

* Wed Jun 09 2010 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Mon Sep 14 2009 Yuri N. Sedunov <aris@altlinux.org> 0.11.1.1-alt1.20090310git3a31d26
- adapted for Sisyphus

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1.1-0.8.20090310git3a31d26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Peter Robinson <pbrobinson@gmail.com> 0.11.1.1-0.7.%{gitdate}git%git_version
- Move develop documentation to its own noarch package to fix RHBZ 513488

* Sat Jun 20 2009 Bastien Nocera <bnocera@redhat.com> 0.11.1.1-0.6.%{gitdate}git%git_version
- Add developer documentation

* Fri Jun 19 2009 Bastien Nocera <bnocera@redhat.com> 0.11.1.1-0.4
- Fix geoclue-test-gui (#506921)

* Thu Apr 09 2009 Peter Robinson <pbrobinson@gmail.com> 0.11.1.1-0.3
- Fix install of test gui

* Sun Mar 29 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.11.1.1-0.2
- Rebuild for new gpsd

* Tue Mar 10 2009 Peter Robinson <pbrobinson@gmail.com> 0.11.1.1-0.1
- Move to a git snapshot until we finally get a new stable release

* Wed Mar 4 2009 Peter Robinson <pbrobinson@gmail.com> 0.11.1-15
- Move docs to noarch, a few spec file cleanups

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 22 2008 Peter Robinson <pbrobinson@gmail.com> 0.11.1-13
- Fix summary

* Thu Jul 31 2008 Peter Robinson <pbrobinson@gmail.com> 0.11.1-12
- Once more for fun

* Thu Jul 31 2008 Peter Robinson <pbrobinson@gmail.com> 0.11.1-11
- Increment build number to allow for clean F-8 and F-9 to F-10 upgrade

* Wed Jul 2 2008 Peter Robinson <pbrobinson@gmail.com> 0.11.1-6
- Fixed spec file so gpsd and gypsy are actually properly in a subpackage

* Sun May 18 2008 Peter Robinson <pbrobinson@gmail.com> 0.11.1-5
- Added gypsy and gpsd providers to build as sub packages

* Mon Apr 28 2008 Peter Robinson <pbrobinson@gmail.com> 0.11.1-4
- Moved api documentation to -devel

* Sat Apr 26 2008 Peter Robinson <pbrobinson@gmail.com> 0.11.1-3
- Cleanup requires and group for test gui

* Sat Apr 26 2008 Peter Robinson <pbrobinson@gmail.com> 0.11.1-2
- Some spec file cleanups

* Fri Apr 25 2008 Peter Robinson <pbrobinson@gmail.com> 0.11.1-1
- Initial package
