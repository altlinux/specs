# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gio-querymodules /usr/bin/glib-genmarshal /usr/bin/gtkdocize gcc-c++ libldap-devel pkgconfig(dbus-1) pkgconfig(gio-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define libxml2_version 2.4.12
%define mate_corba_version 1.1.0
%define glib2_version 2.25.9
%define dbus_version 1.0.1
%define dbus_glib_version 0.74

Summary: 	A process-transparent configuration system
Name: 		mate-conf
Version:	1.4.0
Release: 	alt3_1.1
License:	LGPLv2+
Group: 		System/Base
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
Source1: 	macros.mateconf
URL: 		http://pub.mate-desktop.org

BuildRequires: libxml2-devel >= %{libxml2_version}
BuildRequires: libxslt-devel
BuildRequires: mate-corba-devel >= %{mate_corba_version}
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: gtk-doc >= 0.9
BuildRequires: gettext
BuildRequires: openldap-devel
BuildRequires: intltool
BuildRequires: libpolkit-devel >= 0.92
BuildRequires: libdbus-glib-devel >= 0.8
BuildRequires: gobject-introspection-devel >= 0.6.7
BuildRequires: autoconf automake libtool
BuildRequires: mate-common
BuildRequires: gtk2-devel
Requires: dbus
# for patch0
Requires: /usr/bin/killall
Conflicts: mate-conf-dbus

Patch0: GConf-2.18.0.1-reload.patch
Requires: rpm-macros-%{name} = %{version}-%{release}
# http://bugzilla.gnome.org/show_bug.cgi?id=568845

%description
mate-conf is a process-transparent configuration database API used to
store user preferences. It has pluggable backends and features to
support workgroup administration.

%package devel
Summary: Headers and libraries for mate-conf development
Group: Development/C
Requires: mate-conf = %{version}-%{release}
# we install a pc file
# we install an automake macro
Requires: automake

%description devel
mate-conf development package. Contains files needed for doing
development using mate-conf.

%package gtk
Summary: Graphical mate-conf utilities
Group: System/Base
Requires: mate-conf = %{version}-%{release}

%description gtk
The mate-conf-gtk package contains graphical mate-conf utilities
which require GTK+.


%package -n rpm-macros-%{name}
Summary: Set of RPM macros for packaging %name-based applications
Group: Development/Other
# uncomment if macroses are platform-neutral
#BuildArch: noarch
# helps old apt to resolve file conflict at dist-upgrade (thanks to Stanislav Ievlev)
Conflicts: mate-conf <= 1.4.0-alt1_1

%description -n rpm-macros-%{name}
Set of RPM macros for packaging %name-based applications for ALT Linux.
Install this package if you want to create RPM packages that use %name.

%prep
%setup -q -n mate-conf-%{version}
%patch0 -p1 -b .reload
NOCONFIGURE=1 ./autogen.sh

%build
%configure \
	--disable-static \
	--with-openldap \
	--enable-defaults-service \
	--enable-gtk \
	--enable-gsettings-backend=yes \
	--enable-introspection \
	--enable-gtk-doc

# drop unneeded direct library deps with --as-needed
# libtool doesn't make this easy, so we do it the hard way
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' -e 's/    if test "$export_dynamic" = yes && test -n "$export_dynamic_flag_spec"; then/      func_append compile_command " -Wl,-O1,--as-needed"\n      func_append finalize_command " -Wl,-O1,--as-needed"\n\0/' libtool

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/mateconf/schemas
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/mateconf/mateconf.xml.system
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rpm/
mkdir -p $RPM_BUILD_ROOT%{_var}/lib/rpm-state/mateconf
mkdir -p $RPM_BUILD_ROOT%{_datadir}/MateConf/matesettings

install -p -m 644 -D %{SOURCE1} $RPM_BUILD_ROOT%{_rpmmacrosdir}/mateconf
sed -i -e 's,%%{_localstatedir}/lib,%%{_var}/lib,g' $RPM_BUILD_ROOT%{_rpmmacrosdir}/mateconf

%find_lang %{name}

%post
if [ $1 -gt 1 ]; then
    if ! fgrep -q mateconf.xml.system %{_sysconfdir}/mateconf/2/path; then
        sed -i -e 's@xml:readwrite:$(HOME)/.mateconf@&\n\n# Location for system-wide settings.\nxml:readonly:/etc/mateconf/mateconf.xml.system@' %{_sysconfdir}/mateconf/2/path
    fi
fi

%files -f %{name}.lang
%doc COPYING NEWS README backends/README.evoldap
%config(noreplace) %{_sysconfdir}/mateconf/2/path
%config(noreplace) %{_sysconfdir}/mateconf/2/evoldap.conf
%dir %{_sysconfdir}/mateconf
%dir %{_sysconfdir}/mateconf/2
%dir %{_sysconfdir}/mateconf/mateconf.xml.defaults
%dir %{_sysconfdir}/mateconf/mateconf.xml.mandatory
%dir %{_sysconfdir}/mateconf/mateconf.xml.system
%dir %{_sysconfdir}/mateconf/schemas
%{_bindir}/mateconf-merge-tree
%{_bindir}/mateconftool-2
%{_libexecdir}/mateconfd-2
%{_libdir}/*.so.*
%{_libdir}/MateConf/2/*.so
%dir %{_datadir}/sgml
%{_datadir}/sgml/mateconf
%{_datadir}/MateConf
%{_mandir}/man1/*
%dir %{_libdir}/MateConf
%dir %{_libdir}/MateConf/2
%{_sysconfdir}/dbus-1/system.d/org.mate.MateConf.Defaults.conf
%{_libexecdir}/mateconf-defaults-mechanism
%{_datadir}/polkit-1/actions/org.mate.mateconf.defaults.policy
%{_datadir}/dbus-1/system-services/org.mate.MateConf.Defaults.service
%{_datadir}/dbus-1/services/org.mate.MateConf.service
%dir %{_var}/lib/rpm-state/
%{_var}/lib/rpm-state/mateconf/
%{_libdir}/girepository-1.0
%{_libdir}/MateConf/2/libmateconfbackend-evoldap.la
%{_libdir}/MateConf/2/libmateconfbackend-oldxml.la
%{_libdir}/MateConf/2/libmateconfbackend-xml.la
#%_rpmmacrosdir/mateconf
%{_sysconfdir}/xdg/autostart/mateconf-gsettings-data-convert.desktop
%{_bindir}/mateconf-gsettings-data-convert
%{_bindir}/mateconf-gsettings-schema-convert
%{_libdir}/gio/modules/libgsettingsmateconfbackend.la
%{_libdir}/gio/modules/libgsettingsmateconfbackend.so
%exclude %_rpmmacrosdir/*


%files gtk
%{_libexecdir}/mateconf-sanity-check-2

%files devel
%{_libdir}/*.so
%{_includedir}/mateconf
%{_datadir}/aclocal/*.m4
%{_datadir}/gtk-doc/html/mateconf
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0

%files -n rpm-macros-%{name}
%_rpmmacrosdir/*


%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt3_1.1
- Build for Sisyphus

* Sun Oct 14 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt3_1
- fixed localstatedir in macros

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- added rpm-macros-mate-conf

* Wed Aug 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- converted by srpmconvert script

