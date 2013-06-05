%define ver_major 3.6
%define api_ver 3.0
%def_disable static
%def_enable smartcard
%def_enable systemd
%def_enable ibus

%define _libexecdir %_prefix/libexec

Name: cinnamon-media-keys-helper
Version: %ver_major.4
Release: alt2

Summary: A media keys handler based on gnome-settings-daemon-3.6
License: GPLv2+
Group: Graphical desktop/GNOME

Url: svn://svn.archlinux.org/community/gnome-settings-daemon-compat
Source0: gnome-settings-daemon-%version.tar
Source1: %name.desktop
Patch: gnome-settings-daemon-%version-%release.patch

# From configure.ac
%define glib2_ver 2.29.14
%define gtk_ver 3.3.18
%define gio_ver 2.29.14
%define gnome_desktop_ver 3.5.3
%define notify_ver 0.7.3
%define pulse_ver 0.9.15
%define gsds_ver 3.3.0
%define colord_ver 0.1.9
%define dconf_ver 0.8
%define upower_ver 0.9.1
%define systemd_ver 40
%define wacom_ver 0.6
%define ibus_ver 1.4.99

Requires: dconf >= %dconf_ver
Requires: colord >= %colord_ver
%{?_enable_ibus:Requires:ibus >= %ibus_ver}

# From configure.ac
BuildPreReq: glib2-devel >= %glib2_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libgio-devel >= %gio_ver
BuildPreReq: libgnome-desktop3-devel >= %gnome_desktop_ver
BuildPreReq: libnotify-devel >= %notify_ver
BuildPreReq: gsettings-desktop-schemas-devel >= %gsds_ver
BuildPreReq: libpulseaudio-devel >= %pulse_ver libcanberra-gtk3-devel
BuildRequires: libdbus-devel libpolkit1-devel
%{?_enable_smartcard:BuildRequires: libnss-devel}
%{?_enable_systemd:BuildRequires: systemd-devel >= %systemd_ver libsystemd-login-devel}
%{?_enable_ibus:BuildRequires: libibus-devel >= %ibus_ver}
BuildRequires: libxkbfile-devel
BuildRequires: rpm-build-gnome intltool docbook-style-xsl xsltproc
BuildRequires: gcc-c++ libcups-devel libgudev-devel libXi-devel libXext-devel libXfixes-devel
BuildRequires: libXrandr-devel xorg-inputproto-devel libICE-devel libSM-devel
BuildRequires: libupower-devel >= %upower_ver
BuildRequires: libcolord-devel >= %colord_ver liblcms2-devel
BuildRequires: libwacom-devel >= %wacom_ver xorg-drv-wacom-devel libXtst-devel

%description
cinnamon-media-keys-helper is media keys handler based on gnome-settings-daemon 3.6. 
Purpose of package is to provide for Cinnamon functionality dropped in Gnome 3.8 


%prep
%setup -q -n gnome-settings-daemon-%version
%patch0 -p1

%build
%autoreconf
%configure \
	%{subst_enable static} \
	%{?_disable_smartcard:--disable-smartcard-support} \
	%{subst_enable systemd} \
	%{subst_enable ibus} \
	--disable-schemas-compile

%make -C plugins/common
%make -C plugins/media-keys

%install
%make_install -C plugins/media-keys DESTDIR=%buildroot install
mv %buildroot/%_libexecdir/gnome-fallback-media-keys-helper %buildroot/%_libexecdir/%name
mkdir -p %buildroot/%_datadir/applications/
cp %SOURCE1 %buildroot/%_datadir/applications/

%files 
%_libexecdir/%name
%exclude %_sysconfdir/xdg/autostart/gnome-fallback-media-keys-helper.desktop
%_datadir/applications/%name.desktop

%changelog
* Wed Jun 5 2013 Vladimir Didenko <cow@altlinux.org> 3.6.4-alt2
- Don't display desktop file

* Tue May 14 2013 Vladimir Didenko <cow@altlinux.org> 3.6.4-alt1
- Initial build for Sisyphus
