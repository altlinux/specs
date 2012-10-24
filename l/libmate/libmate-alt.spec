# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize /usr/bin/mateconftool-2 libpopt-devel pkgconfig(audiofile) pkgconfig(esound) pkgconfig(gio-2.0)
# END SourceDeps(oneline)
Requires: design-graphics
%define _libexecdir %_prefix/libexec
#%global po_package libmate-2.0

Summary: 		MATE base library
Name:    		libmate
Version: 		1.4.0
Release: 		alt4_1.1
URL:     		http://http://mate-desktop.org
Source0: 		http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
Source1: 		desktop_mate_peripherals_monitor.schemas
Source2:		fedora-mate-default.xml
License: 		LGPLv2+
Group:   		System/Libraries

Requires(pre): 	utempter
Requires(post): mate-conf
Requires(pre): 	mate-conf
Requires(preun): mate-conf

BuildRequires: 	zlib-devel
BuildRequires: 	glib2-devel
BuildRequires:  libmatecomponent-devel
BuildRequires:  mate-conf-devel
BuildRequires:  mate-vfs-devel
BuildRequires:  libxml2-devel
BuildRequires:  mate-corba-devel
BuildRequires:  libxslt-devel
BuildRequires:  libcanberra-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  gettext
BuildRequires:  popt-devel
BuildRequires:  mate-common
BuildRequires:  gtk-doc
BuildRequires:  libdbus-glib-devel
BuildRequires:  libselinux-devel
BuildRequires:  libssl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libavahi-glib-devel

Patch0: libmate_default_background_path.patch

# make sure to update gnome-desktop requires when changing below patch
Patch1: default-mate-background.patch

# https://bugzilla.gnome.org/show_bug.cgi?id=606436
Patch2: libmate-2.11.1-scoreloc.patch

Patch3: libgnome-2.7.2-default-cursor.patch
Patch4: libmate-default-browser.patch
Patch6: libgnome-2.19.1-default-settings.patch
Patch7: libgnome-2.22.0-default-sound-effects.patch

# backport from upstream svn
Patch8: im-setting.patch

Patch9: libgnome-2.24.1-default-noblink.patch
Patch33: libgnome-2.22.0-alt-default_gtk_theme.patch
Patch34: libgnome-alt-settings.patch


%description
MATE is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libmate package includes
non-GUI-related libraries that are needed to run MATE. The libmateui
package contains X11-dependent MATE library features.


%package devel
Summary: Libraries and headers for libmate
Group: Development/C
Requires: %{name} = %{version}-%{release}

%description devel
You should install the libmate-devel package if you would like to
compile MATE applications. You do not need to install libmate-devel
if you just want to use the MATE desktop environment.

%prep
%setup -q
%patch0 -p1 -b .libmate_default_background
#patch1 -p1 -b .default-mate-background
%patch2 -p1 -b .scoreloc
%patch3 -p1 -b .default-cursor
%patch4 -p1 -b .default-browser
#ALT#patch6 -p1 -b .default-settings
%patch7 -p1 -b .default-sound-effects
%patch8 -p1 -b .im-setting
%patch9 -p1 -b .default-noblink
NOCONFIGURE=1 ./autogen.sh
%patch33 -p1
%patch34 -p1

%build

%configure \
	--disable-static          \
	--disable-esd

make %{?_smp_mflags} 

%install
export MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
unset MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/mateconf/schemas/
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/mate-background-properties/mate-default.xml

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

for serverfile in $RPM_BUILD_ROOT%{_libdir}/matecomponent/servers/*.server; do
    sed -i -e 's|location *= *"/usr/lib\(64\)*/|location="/usr/$LIB/|' $serverfile
done

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/skel/.mate

%find_lang libmate

%post
export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
	mateconftool-2 --makefile-install-rule \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_accessibility_keyboard.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_accessibility_startup.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_applications_at_mobility.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_applications_at_visual.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_applications_browser.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_applications_office.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_applications_terminal.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_applications_window_manager.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_background.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_file_views.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_interface.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_lockdown.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_peripherals_keyboard.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_peripherals_monitor.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_peripherals_mouse.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_sound.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_thumbnail_cache.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_thumbnailers.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_typing_break.schemas \
	> /dev/null || :

%pre
if [ "$1" -gt 1 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_accessibility_keyboard.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_accessibility_startup.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_applications_at_mobility.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_applications_at_visual.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_applications_browser.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_applications_office.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_applications_terminal.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_applications_window_manager.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_background.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_file_views.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_interface.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_lockdown.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_peripherals_keyboard.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_peripherals_monitor.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_peripherals_mouse.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_sound.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_thumbnail_cache.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_thumbnailers.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_typing_break.schemas \
	> /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_accessibility_keyboard.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_accessibility_startup.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_applications_at_mobility.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_applications_at_visual.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_applications_browser.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_applications_office.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_applications_terminal.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_applications_window_manager.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_background.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_file_views.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_interface.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_lockdown.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_peripherals_keyboard.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_peripherals_monitor.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_peripherals_mouse.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_sound.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_thumbnail_cache.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_thumbnailers.schemas \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_typing_break.schemas \
	> /dev/null || :
fi

%files -f libmate.lang
%doc AUTHORS COPYING.LIB NEWS README
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_libdir}/matecomponent/monikers/*
%{_libdir}/matecomponent/servers/*
%{_mandir}/man7/*
%{_sysconfdir}/mateconf/schemas/*.schemas
%{_sysconfdir}/sound
%{_sysconfdir}/skel/.mate
%{_datadir}/mate-background-properties/mate-default.xml

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
# as per guidelines own this instead Requires:gtk-doc 
%{_datadir}/gtk-doc


%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt4_1.1
- Build for Sisyphus

* Mon Oct 15 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt4_1
- adapted alt patches

* Tue Aug 14 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt3_1
- drop Fedora icon theme patch (6)

* Wed Aug 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- use altlinux background

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

