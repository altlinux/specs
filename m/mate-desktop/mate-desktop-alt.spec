# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize pkgconfig(gdk-pixbuf-2.0) pkgconfig(gio-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(unique-3.0) pkgconfig(x11) pkgconfig(xrandr) python-devel
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define po_package mate-desktop-2.0

Summary: 	Shared code among gnome-panel, gnome-session, nautilus, etc
Name: 		mate-desktop
Version: 	1.4.1
Release: 	alt1_5.1
URL: 		http://pub.mate-desktop.org
Source0: 	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

License: 	GPLv2+ and LGPLv2+
Group: 		System/Libraries

Requires: 	altlinux-freedesktop-menu-common
Requires: 	python-module-pycairo
Requires: 	pygtk2

BuildRequires: mate-common
BuildRequires: gtk2-devel
BuildRequires: glib2-devel
BuildRequires: mate-conf-devel
BuildRequires: libstartup-notification-devel
BuildRequires: mate-doc-utils
BuildRequires: gtk-doc
BuildRequires: intltool
BuildRequires: libunique-devel
#only for bad mate-common from fedora
BuildRequires:  libtool


# Upstream fixes
Patch0: 0001-bgo-629168-Don-t-read-past-the-end-of-a-string-mate.patch
Patch1: 0001-Fix-possible-double-free-when-destroying-private-win.patch
Patch2: mate-desktop_remove_mate-bg-crossfade.patch

%description
The mate-desktop package contains an internal library
(libmatedesktop) used to implement some portions of the MATE
desktop, and also some data files and other shared components of the
MATE user environment.

%package devel
Summary: Libraries and headers for libmate-desktop
License: LGPLv2+
Group: Development/C
Requires: mate-desktop = %{version}-%{release}

%description devel
Libraries and header files for the MATE-internal private library
libmatedesktop.

%prep
%setup -q
%patch0 -p1 -b .pnp
%patch1 -p1 -b .double-free
%patch2 -p1 -b .mate-desktop_remove_mate-bg-crossfade
NOCONFIGURE=1 ./autogen.sh

%build

%configure \
	--disable-libtool-lock	\
	--disable-scrollkeeper    \
	--disable-static          \
	--with-pnp-ids-path="/usr/share/hwdata/pnp.ids" \
	--enable-unique \
	--enable-gtk-doc

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# stuff we don't want
rm -rf $RPM_BUILD_ROOT/var/scrollkeeper


mkdir $RPM_BUILD_ROOT%{_datadir}/omf/mate
mv -f $RPM_BUILD_ROOT%{_datadir}/omf/fdl $RPM_BUILD_ROOT%{_datadir}/omf/mate
mv -f $RPM_BUILD_ROOT%{_datadir}/omf/gpl $RPM_BUILD_ROOT%{_datadir}/omf/mate
mv -f $RPM_BUILD_ROOT%{_datadir}/omf/lgpl $RPM_BUILD_ROOT%{_datadir}/omf/mate

%find_lang %{po_package} --all-name

mkdir -p %buildroot%{_datadir}/mate-about


%files -f %{po_package}.lang
%doc AUTHORS COPYING COPYING.LIB NEWS README
%{_datadir}/applications/mate-about.desktop
%doc %{_mandir}/man*/*
# GPL
%{_bindir}/mate-about
# LGPL
%{_libdir}/lib*.so.*
%{_datadir}/mate/help/*/*/*.xml
%{_datadir}/omf/mate/*
%{_datadir}/mate-about/mate-version.xml

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%doc %{_datadir}/gtk-doc


%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.1-alt1_5.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt1_5
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_4
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

