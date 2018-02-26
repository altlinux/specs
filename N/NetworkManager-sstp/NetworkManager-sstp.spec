%define nm_version 0.9.4.0
%define nm_applet_version 0.9.4.0
%define ppp_version 2.4.5
%define gtkver 3

Name: NetworkManager-sstp
Version: 0.9.4.0
Release: alt1
License: %gpl2plus
Group: System/Configuration/Networking
Summary:  NetworkManager VPN plugin for SSTP

Url: http://www.gnome.org/projects/NetworkManager/

Source: %name-%version.tar
Requires: NetworkManager >= %nm_version
Requires: sstp-client
Requires: ppp = %ppp_version

BuildRequires(pre): rpm-build-licenses
BuildRequires: ppp-devel sstp-client-devel
BuildRequires: NetworkManager-devel >= %nm_version
BuildRequires: NetworkManager-glib-devel >= %nm_version
BuildRequires: libgtk+%gtkver-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: libdbus-glib-devel >= 0.74
BuildRequires: intltool gettext

%description
This package contains software for integrating the sstp VPN software
with NetworkManager and the GNOME desktop

%package gnome
License: %gpl2plus
Summary: GNOME applications for %name
Group: Graphical desktop/GNOME
Requires: shared-mime-info >= 0.16
Requires: gnome-keyring
Requires: NetworkManager-gnome >= %nm_applet_version
Requires: NetworkManager-sstp = %version-%release

%description gnome
This package contains GNOME applications for use with
NetworkManager panel applet.

%prep
%setup

%build
%autoreconf
%configure \
    --disable-static \
    --libexecdir=%_libexecdir/NetworkManager \
    --localstatedir=%_var \
    --with-pppd-plugin-dir=%_libdir/pppd/%ppp_version \
    --with-gtkver=%gtkver

%make_build

%install
%makeinstall_std
%find_lang %name

%post
if /sbin/service messagebus status &>/dev/null; then
 dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig &>/dev/null ||:
else
 echo "WARNING: %name requires running messagebus service." >&2
fi

%files
%doc AUTHORS ChangeLog COPYING
%config(noreplace) %_sysconfdir/dbus-1/system.d/nm-sstp-service.conf
%config(noreplace) %_sysconfdir/NetworkManager/VPN/nm-sstp-service.name
%_libexecdir/NetworkManager/nm-sstp-service
%_libdir/pppd/%ppp_version/*.so

%files gnome -f %name.lang
%_libdir/NetworkManager/lib*.so*
%_libexecdir/NetworkManager/nm-sstp-auth-dialog
%_datadir/gnome-vpn-properties/sstp

%exclude %_libdir/NetworkManager/lib*.la

%changelog
* Mon May 21 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.4.0-alt1
- initial build

