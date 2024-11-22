%def_with gtk4

%ifarch %e2k
%define more_warnings no
%else
%define more_warnings error
%endif

Name:           NetworkManager-libreswan
Version:        1.2.24
Release:        alt1

Group:          Networking/Other
Summary:        Libreswan VPN client plugin for NetworkManager

License:        GPL-2.0+
URL:            https://gitlab.gnome.org/GNOME/NetworkManager-libreswan
Source0:        %{name}-%{version}.tar

BuildRequires:  glib2-devel
BuildRequires:  intltool
BuildRequires:  libgio-devel
BuildRequires:  libnl-devel
BuildRequires:  libsecret-devel
BuildRequires:  libnma-devel
BuildRequires: libgtk+3-devel
%{?_with_gtk4:BuildRequires: libgtk4-devel >= 4.6.3 libnma-gtk4-devel}

%description
Libreswan VPN client plugin for NetworkManager

Support for configuring IKEv1 based IPsec virtual private network connections.
Compatible with Libreswan and Cisco IPsec VPN servers.

%package gtk-common
License: GPL-2.0+
Summary: Common part of %name GTK support
Group: Graphical desktop/GNOME
Requires: %name = %EVR

%description gtk-common
This package contains common part for %name GTK support.

%package gtk3
License: GPL-2.0+
Summary: Files for GTK3 applications to use %name
Group: Graphical desktop/GNOME
Requires: %name-gtk-common = %EVR

%description gtk3
This package contains files for GTK3 applications to use %name.

%if_with gtk4
%package gtk4
License: GPL-2.0+
Summary: Files for GTK4 applications to use %name
Group: Graphical desktop/GNOME
Requires: %name-gtk-common = %EVR

%description gtk4
This package contains files for GTK4 applications to use %name.
%endif

%prep
%setup

%build
%autoreconf
%configure \
	--disable-static \
	%{subst_with gtk4} \
	--enable-more-warnings=%more_warnings
%make_build

%install
%makeinstall_std
%find_lang %name

%files
%_libexecdir/nm-libreswan-service
%_libexecdir/nm-libreswan-service-helper
%_libdir/NetworkManager/libnm-vpn-plugin-libreswan.so
%config(noreplace) %_sysconfdir/dbus-1/system.d/nm-libreswan-service.conf
%config(noreplace) %_libexecdir/NetworkManager/VPN/nm-libreswan-service.name
%_man5dir/nm-settings-libreswan.5.xz

%files gtk-common -f %name.lang
%_libexecdir/nm-libreswan-auth-dialog
%_datadir/metainfo/*.xml

%files gtk3
%_libdir/NetworkManager/libnm-vpn-plugin-libreswan-editor.so

%if_with gtk4
%files gtk4
%_libdir/NetworkManager/libnm-gtk4-vpn-plugin-libreswan-editor.so
%endif

%exclude %_libdir/NetworkManager/*.la

%changelog
* Tue Nov 19 2024 Andrey Cherepanov <cas@altlinux.org> 1.2.24-alt1
- Initial build for Sisyphus (thanks Anton Meleshnikov <alton@altlinux.org>).
