%define nm_version 1.1.90
%define nm_applet_version 1.1.90
%define nm_applet_name NetworkManager-applet-gtk
#define git_date %nil
%define git_date .git20180722

%def_without libnm_glib

%define _unpackaged_files_terminate_build 1

Name: NetworkManager-iodine
Version: 1.2.1
Release: alt1%git_date
License: %gpl2plus
Group: System/Configuration/Networking
Summary: NetworkManager VPN plugin for iodine
Url: https://honk.sigxcpu.org/piki/projects/network-manager-iodine/
# https://gitlab.gnome.org/GNOME/network-manager-iodine.git
Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: intltool
BuildRequires: libnm-devel >= %nm_version
BuildRequires: libnma-devel >= %nm_applet_version
%if_with libnm_glib
BuildRequires: NetworkManager-devel >= %nm_version
BuildRequires: libnm-glib-vpn-devel >= %nm_version
BuildRequires: libnm-gtk-devel >= %nm_applet_version
%endif
BuildRequires: libgtk+3-devel
BuildRequires: libsecret-devel

Requires: NetworkManager-daemon   >= %nm_version
Requires: iodine-client

%description
%name is a network manager VPN plugin that allows you
to tunnel your connection through a DNS tunnel. This can be useful if
internet access is firewalled but DNS traffic is still allowed.

%package gtk
License: %gpl2plus
Summary: Applications for use %name with %nm_applet_name
Group: Graphical desktop/GNOME
Requires: %nm_applet_name >= %nm_applet_version
Requires: NetworkManager-iodine = %version-%release

%description gtk
This package contains applications for use with
NetworkManager panel applet.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--libexecdir=%_libexecdir/NetworkManager \
	--localstatedir=%_var \
%if_without libnm_glib
	--without-libnm-glib \
%endif
	--enable-more-warnings=yes
%make_build

%install
%makeinstall_std
%find_lang %name

%files
%doc NEWS AUTHORS
%_libexecdir/NetworkManager/nm-iodine-service
%config %_sysconfdir/dbus-1/system.d/nm-iodine-service.conf
%if_with libnm_glib
%config %_sysconfdir/NetworkManager/VPN/nm-iodine-service.name
%endif
%config %_libexecdir/NetworkManager/VPN/nm-iodine-service.name

%files gtk -f %name.lang
%if_with libnm_glib
%_libdir/NetworkManager/libnm-iodine-properties.so*
%endif
%_libexecdir/NetworkManager/nm-iodine-auth-dialog
%_datadir/gnome-vpn-properties/*
%_libdir/NetworkManager/libnm-vpn-plugin-iodine.so
%_datadir/appdata/*.xml

%exclude %_libdir/NetworkManager/*.la

%changelog
* Tue Sep 18 2018 Mikhail Efremov <sem@altlinux.org> 1.2.1-alt1.git20180722
- Temporary don't treat warnings as errors.
- Upstream git snapshot.

* Wed Aug 01 2018 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt2
- Disable libnm-glib-* support.
- Fix build without libnm-glib-*.

* Thu Apr 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Thu Apr 07 2016 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1
- Initial build.

