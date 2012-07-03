%define _name gypsy

Name: lib%_name
Version: 0.8
Release: alt4

Summary: A library for Gypsy
Group: System/Libraries
# See LICENSE file for details
License: LGPLv2 and GPLv2
Url: http://gypsy.freedesktop.org/
Source: http://gypsy.freedesktop.org/gypsy-releases/%_name-%version.tar.gz
Patch: gypsy-0.8-unusedvar.patch

BuildRequires: libbluez-devel
BuildRequires: libdbus-devel
BuildRequires: libdbus-glib-devel
BuildRequires: glib2-devel
BuildRequires: gtk-doc
BuildRequires: libxslt

%description
Gypsy is a GPS multiplexing daemon which allows multiple clients to
access GPS data from multiple GPS sources concurrently. This package
provides shared library needed Gypsy to work.

This package provides shared library needed for Gypsy to work.

%package devel
Summary: Development package for gypsy
Group: Development/C
Requires: %name = %version-%release

%description devel
Header files for development with gypsy.

%package devel-doc
Summary: Documentation files for %name
Group: Development/C
Requires: %name = %version-%release
BuildArch: noarch

%description devel-doc
This package contains developer documentation for %name.

%package -n %_name-daemon
Group: Monitoring
Summary: A GPS multiplexing daemon
Requires: %name = %version-%release
Requires: dbus-tools-gui

%description -n %_name-daemon
Gypsy is a GPS multiplexing daemon which allows multiple clients to
access GPS data from multiple GPS sources concurrently.

%prep
%setup -q -n %_name-%version
%patch -p1

%build
%configure --disable-static
%make_build

%install
make install DESTDIR=%buildroot

%files
%_libdir/libgypsy.so.0
%_libdir/libgypsy.so.0.0.0
%doc AUTHORS COPYING COPYING.lib LICENSE

%files -n %_name-daemon
%_libexecdir/gypsy-daemon
%_sysconfdir/dbus-1/system.d/Gypsy.conf
%_datadir/dbus-1/system-services/org.freedesktop.Gypsy.service

%files devel
%_libdir/pkgconfig/gypsy.pc
%_includedir/gypsy
%_libdir/libgypsy.so

%files devel-doc
%_datadir/gtk-doc/html/gypsy

%changelog
* Thu May 31 2012 Yuri N. Sedunov <aris@altlinux.org> 0.8-alt4
- fixed build with gcc-4.6

* Fri Mar 11 2011 Yuri N. Sedunov <aris@altlinux.org> 0.8-alt3
- rebuild for debuginfo

* Sat Dec 11 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8-alt2
- updated buildreqs

* Wed Nov 10 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8-alt1
- 0.8

* Mon Sep 14 2009 Yuri N. Sedunov <aris@altlinux.org> 0.7-alt1
- adapted for Sisyphus
- new daemon package

* Thu Aug 06 2009 Bastien Nocera <bnocera@redhat.com> 0.7-1
- Update to 0.7

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 19 2009 Bastien Nocera <bnocera@redhat.com> 0.6-9
- Gypsy is supposed to run as a system service, as root

* Wed Mar  4 2009 Peter Robinson <pbrobinson@gmail.com> 0.6-8
- Move docs to noarch, some spec file updates

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Peter Robinson <pbrobinson@gmail.com> 0.6-6
- Add gtk-doc build req

* Sat Nov 22 2008 Peter Robinson <pbrobinson@gmail.com> 0.6-5
- Rebuild

* Thu Sep 11 2008 - Bastien Nocera <bnocera@redhat.com> 0.6-4
- Rebuild

* Mon May 15 2008 Peter Robinson <pbrobinson@gmail.com> 0.6-3
- Further spec file cleanups

* Mon Apr 28 2008 Peter Robinson <pbrobinson@gmail.com> 0.6-2
- Some spec file cleanups

* Sat Apr 26 2008 Peter Robinson <pbrobinson@gmail.com> 0.6-1
- Initial package
