# TODO:
# move Tao and semweb to separate package?

%def_disable static
# %add_findprov_lib_path %_libdir/f-spot
%define ver_major 0.8

Name: f-spot
Version: %ver_major.2
Release: alt2

Summary: F-Spot Photo Manager
License: GPLv2+
Group: Graphics

Url: http://f-spot.org
Source: http://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar
Source2: hyena.tar
Patch0: %name-%version-%release.patch

PreReq: librarian desktop-file-utils
BuildPreReq: desktop-file-utils

BuildRequires: docbook-dtds intltool gcc-c++ gnome-doc-utils-xslt libexif-devel libcairo-devel libunique-devel
BuildRequires: libflickr-sharp-devel libglitz-sharp-devel libgnome-desktop-sharp-devel libgnome-keyring-sharp-devel
BuildRequires: libgnomeui-devel libgoogle-sharp-devel libgtk-sharp2-devel libjpeg-devel liblcms-devel libmono-devel
BuildRequires: mono-addins-devel mono-devel mono-mcs mono-nunit-devel ndesk-dbus-glib-devel libtag-sharp-devel

# Not detected by buildreq:
BuildRequires: libsqlite3-devel libgnome-sharp-devel gnome-doc-utils
# need for gio-sharp
BuildPreReq: libgtk-sharp2-devel >= 2.12.1
BuildPreReq: libgio-devel libgio-sharp-devel

# Needed to properly detect run-time Mono dependencies:
BuildRequires: rpm-build-mono
BuildRequires: /proc

%description
F-Spot is a full-featured personal photo management application for the
GNOME desktop.

%package devel
Summary: Develpment files for f-spot
Group: Development/Other
Requires: %name = %version-%release

%description devel
Development files for f-spot

%prep
%setup
%__tar -xf %SOURCE2 -C lib/Hyena
%patch0 -p1

%build
NOCONFIGURE=1 ./autogen.sh
#intltoolize --force
#%autoreconf
%configure 			\
	%{subst_enable static}	\
	--disable-scrollkeeper	\
	--disable-schemas-install
	
# Parallel make unsafe :(
%make

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%make_install DESTDIR=%buildroot install
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL
%find_lang --with-gnome %name

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %name
fi

%files -f %name.lang
%config %_sysconfdir/gconf/schemas/%name.schemas
%_bindir/*
%_libdir/f-spot
%_desktopdir/f-spot*
%_iconsdir/hicolor/*/apps/*
%_datadir/f-spot
%_prefix/libexec/gnome-screensaver/f-spot-screensaver
%_datadir/applications/screensavers/*
%exclude %_libdir/f-spot/*.la

%files devel
%_pkgconfigdir/*

%changelog
* Mon Feb 20 2012 Alexey Shabalin <shaba@altlinux.ru> 0.8.2-alt2
- fix build with gtk-sharp/master

* Thu Mar 10 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Fri Oct 15 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Mon May 17 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Wed Nov 11 2009 Alexey Shabalin <shaba@altlinux.ru> 0.6.1.5-alt1
- 0.6.1.5

* Sat Oct 31 2009 Alexey Shabalin <shaba@altlinux.ru> 0.6.1.4-alt1
- 0.6.1.4

* Thu Oct 22 2009 Alexey Shabalin <shaba@altlinux.ru> 0.6.1.3-alt1
- 0.6.1.3 + branch FSPOT_0_6_0_STABLE(20091018)

* Fri Oct 16 2009 Alexey Shabalin <shaba@altlinux.ru> 0.6.1.2-alt2
- update dll map for libgphoto2

* Fri Oct 09 2009 Alexey Shabalin <shaba@altlinux.ru> 0.6.1.2-alt1
- 0.6.1.2

* Sun Sep 06 2009 Alexey Shabalin <shaba@altlinux.ru> 0.6.1.1-alt1
- 0.6.1.1

* Fri Aug 14 2009 Alexey Shabalin <shaba@altlinux.ru> 0.6.0.0-alt1
- 0.6.0.0
- move patches to git
- move pkgconfig files to devel package

* Fri Jul 10 2009 Alexey Shabalin <shaba@altlinux.ru> 0.5.0.3-alt6
- update buildreq

* Thu Apr 23 2009 Alexey Shabalin <shaba@altlinux.ru> 0.5.0.3-alt5
- rebuild with new nunit from mono-2.4

* Tue Feb 24 2009 Alexey Shabalin <shaba@altlinux.ru> 0.5.0.3-alt4
- fix Gnome bugs #551803,#556395

* Tue Dec 02 2008 Alexey Shabalin <shaba@altlinux.ru> 0.5.0.3-alt3
- rebuild with new libflickr-sharp
- removed obsolete post scripts

* Fri Nov 14 2008 Alexey Shabalin <shaba@altlinux.ru> 0.5.0.3-alt2
- don't requires debugers

* Wed Oct 22 2008 Alexey Shabalin <shaba@altlinux.ru> 0.5.0.3-alt1
- 0.5.0.3

* Tue Aug 12 2008 Alexey Shabalin <shaba@altlinux.ru> 0.4.4-alt1
- 0.4.4
- package files for gnome-screensaver

* Tue May 06 2008 Alexey Shabalin <shaba@altlinux.ru> 0.4.3.1-alt1
- 0.4.3.1
- i know, what export to picasa don't work
- update patches for build system libs
- build with local libgphoto2-sharp
- add patch from debian for optional use beagle

* Tue Apr 22 2008 Alexey Shabalin <shaba@altlinux.ru> 0.4.2-alt2
- rebuild with new libgpoto
- fix build with gtkhtml-sharp
- add patch from svn/branch-0.4.2-stable
- add mime type in desktop file

* Fri Mar 07 2008 Victor Forsyuk <force@altlinux.org> 0.4.2-alt1
- 0.4.2

* Thu Jan 31 2008 Alexey Shabalin <shaba@altlinux.ru> 0.4.1-alt2
- rewrite patch3(use system libs) with autotools syntax		

* Thu Jan 17 2008 Alexey Shabalin <shaba@altlinux.ru> 0.4.1-alt1
- 0.4.1
- build with system libs (patch3):
  + Mono.Addins
  + NDesk.DBus and NDesk.DBus.GLib
  + FlickrNet
  + google-sharp
  + gnome-keyring-sharp
  + glitz-sharp
  + libgphoto2-sharp
- update patch for linking (patch0)
- import debian patches (patch10-patch17):

* Wed Oct 17 2007 Victor Forsyuk <force@altlinux.org> 0.3.5-alt2
- Fix FTBFS in current build environment.

* Fri Apr 06 2007 Victor Forsyuk <force@altlinux.org> 0.3.5-alt1
- 0.3.5

* Wed Feb 07 2007 Victor Forsyuk <force@altlinux.org> 0.3.2-alt2
- Fixed Provides issue properly.

* Mon Feb 05 2007 Victor Forsyuk <force@altlinux.org> 0.3.2-alt1
- 0.3.2
- Fix ALT#9704.

* Thu Nov 30 2006 Victor Forsyuk <force@altlinux.org> 0.3.0-alt1
- 0.3.0
- Build with rpm-build-mono.

* Thu Oct 19 2006 Victor Forsyuk <force@altlinux.org> 0.2.2-alt1
- 0.2.2

* Mon May 29 2006 Victor Forsyuk <force@altlinux.ru> 0.1.11-alt1
- Initial build.
