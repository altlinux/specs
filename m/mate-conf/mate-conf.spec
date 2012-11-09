# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gio-querymodules /usr/bin/glib-genmarshal /usr/bin/gtkdocize gcc-c++ libldap-devel pkgconfig(dbus-1) pkgconfig(gio-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0)
# END SourceDeps(oneline)
Group: System/Base
%define _libexecdir %_prefix/libexec
# fedora __isa_bits tmp hack
%ifarch x86_64
%define __isa_bits 64
%else
%define __isa_bits 32
%endif
Name:	        mate-conf	
Version:	1.4.0
Release:	alt3_21
Summary:	MATE Desktop configuration tool
License:	GPLv2+	
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

# Copy schemas from old package for later uninstall on upgrade.
# Macro to remove schemas.  Not meant to be used publically.
# Remove schemas unconditionally.
# Remove schemas on package removal (not upgrade).
Source1:	macros.mateconf

BuildRequires:	desktop-file-utils
BuildRequires:  libpolkit-devel
BuildRequires:  libglade2-devel
BuildRequires:  libdbus-glib-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  mate-corba-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk-doc
BuildRequires:  openldap-devel
BuildRequires:  gtk2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  mate-common
BuildRequires:  mate-doc-utils
BuildRequires:  libcairo-gobject-devel

Requires:	dbus

# for patch0
Requires: /usr/bin/killall
# I removed this once, and it got re-added, please document why -- rex
Conflicts: mate-conf-dbus

Patch0: mate-conf-1.4.0-reload.patch
Source44: import.info
Requires: rpm-macros-%{name} = %{version}-%{release}
# http://bugzilla.gnome.org/show_bug.cgi?id=568845

%description
MATE Desktop configuration tool

%package devel
Group: Development/C
Summary:	Development files for mate-conf
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for mate-conf

%package gtk
Summary: Graphical mate-conf utilities
Group: System/Base
Requires: %{name}%{?_isa} = %{version}-%{release}

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

make %{?_smp_mflags} V=1


%install
make install DESTDIR=%{buildroot}

# prep macros.mateconf
mkdir -p %{buildroot}%{_sysconfdir}/mateconf/schemas
mkdir -p %{buildroot}%{_sysconfdir}/mateconf/mateconf.xml.system
mkdir -p %{buildroot}%{_sysconfdir}/rpm/
mkdir -p %{buildroot}%{_var}/lib/rpm-state/mateconf
mkdir -p %{buildroot}%{_datadir}/MateConf/gsettings

install -p -m 644 -D %{SOURCE1} $RPM_BUILD_ROOT%{_rpmmacrosdir}/mateconf

# unpackaged files
find %{buildroot} -name '*.la' -exec rm -rf {} ';'

%find_lang %{name}
sed -i -e 's,%%{_localstatedir}/lib,%%{_var}/lib,g' %{buildroot}%{_rpmmacrosdir}/mateconf


%post
gio-querymodules-%{__isa_bits} %{_libdir}/gio/modules || :
if [ $1 -gt 1 ]; then
    if ! fgrep -q mateconf.xml.system %{_sysconfdir}/mateconf/2/path; then
        sed -i -e 's@xml:readwrite:$(HOME)/.mateconf@&\n\n# Location for system-wide settings.\nxml:readonly:/etc/mateconf/mateconf.xml.system@' %{_sysconfdir}/mateconf/2/path
    fi
fi

%postun
gio-querymodules-%{__isa_bits} %{_libdir}/gio/modules || :

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_sysconfdir}/mateconf/
%{_var}/lib/rpm-state/mateconf/
#%{_rpmmacrosdir}/mateconf
%{_sysconfdir}/xdg/autostart/mateconf-gsettings-data-convert.desktop
%{_mandir}/man1/*
%{_bindir}/mateconf-gsettings-data-convert
%{_bindir}/mateconf-gsettings-schema-convert
%{_bindir}/mateconf-merge-tree
%{_bindir}/mateconftool-2
%{_sysconfdir}/dbus-1/system.d/org.mate.MateConf.Defaults.conf
%{_datadir}/sgml/mateconf/
%{_libexecdir}/mateconf-defaults-mechanism
%{_libexecdir}/mateconfd-2
%{_libdir}/libmateconf-2.so.4*
%{_libdir}/MateConf/
%{_libdir}/gio/modules/libgsettingsmateconfbackend.so
%{_libdir}/girepository-1.0/MateConf-2.0.typelib
%{_datadir}/dbus-1/services/org.mate.MateConf.service
%{_datadir}/dbus-1/system-services/org.mate.MateConf.Defaults.service
%{_datadir}/polkit-1/actions/org.mate.mateconf.defaults.policy
%{_datadir}/MateConf/

%files gtk
%{_libexecdir}/mateconf-sanity-check-2

%files devel
%{_datadir}/gtk-doc/html/mateconf/
%{_libdir}/libmateconf-2.so
%{_includedir}/mateconf/
%{_datadir}/gir-1.0/MateConf-2.0.gir
%{_datadir}/aclocal/mateconf-2.m4
%{_libdir}/pkgconfig/mateconf-2.0.pc


%files -n rpm-macros-%{name}
%_rpmmacrosdir/*

%changelog
* Fri Nov 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt3_21
- new fc release

* Thu Nov 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt3_20
- use F19 import base

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

